#! /usr/bin/env python3

import os
import sys
import pytest
import glob
import subprocess
import re
from test_expect_pragma import (
    TestExpectPragmas, cat, testinfo,
    env_bool_variable, env_str_variable
    )

"""
Usage:
    python3 test_codegen.py
(or make tests)
"""

"""
MIF08 and CAP, 2019
Unit test infrastructure for testing code generation:
1) compare the actual output to the expected one (in comments)
2) compare the actual output to the one obtained by simulation
3) for different allocation algorithms
"""

DISABLE_TYPECHECK = False
TYPECHECK_ONLY = False
ENABLE_SSA = False
SSA_OPTIMS = False
env_bool_variable('ENABLE_SSA', globals())
env_bool_variable('SSA_OPTIMS', globals())

HERE = os.path.dirname(os.path.realpath(__file__))
if HERE == os.path.realpath('.'):
    HERE = '.'
TEST_DIR = HERE
IMPLEM_DIR = HERE
MINIC_COMPILE = os.path.join(IMPLEM_DIR, 'MiniCC.py')

ALL_FILES = glob.glob(os.path.join(TEST_DIR, 'TP04/tests/**/[a-zA-Z]*.c'), recursive=True)

ALLOC_FILES = glob.glob(os.path.join(HERE, 'TP05/tests/**/*.c'), recursive=True)

ASM = 'riscv64-unknown-elf-gcc'
SIMU = 'spike'

SKIP_NOT_IMPLEMENTED = False
if 'SKIP_NOT_IMPLEMENTED' in os.environ:
    SKIP_NOT_IMPLEMENTED = True

if 'TEST_FILES' in os.environ:
    ALL_FILES = glob.glob(os.environ['TEST_FILES'], recursive=True)

MINIC_EVAL = os.path.join(
HERE, '..', '..', 'TP03', 'MiniC-type-interpret', 'Main.py')

# if 'COMPIL_MINIC_EVAL' in os.environ:
#     MINIC_EVAL = os.environ['COMPIL_MINIC_EVAL']
# else:
#     MINIC_EVAL = os.path.join(
#         HERE, '..', '..', 'TP03', 'MiniC-type-interpret', 'Main.py')

# Avoid duplicates
ALL_IN_MEM_FILES = list(set(ALL_FILES) | set(ALLOC_FILES))
ALL_IN_MEM_FILES.sort()
ALL_FILES = list(set(ALL_FILES))
ALL_FILES.sort()

if 'TEST_FILES' in os.environ:
    ALLOC_FILES = ALL_FILES
    ALL_IN_MEM_FILES = ALL_FILES


class TestCodeGen(TestExpectPragmas):
    # Not in test_expect_pragma to get assertion rewritting
    def assert_equal(self, actual, expected):
        if TYPECHECK_ONLY and expected.exitcode == 0:
            # Compiler does not fail => no output expected
            assert actual.output == "", \
                "Compiler unexpectedly generated some output with --disable-codegen"
            assert actual.exitcode == 0, \
                "Compiler unexpectedly failed with --disable-codegen"
            return
        if DISABLE_TYPECHECK and expected.exitcode != 0:
            # Test should fail at typecheck, and we don't do
            # typechecking => nothing to check.
            pytest.skip("Test that doesn't typecheck with --disable-typecheck")
        if expected.output is not None and actual.output is not None:
            assert actual.output == expected.output, \
                "Output of the program is incorrect."
        assert actual.exitcode == expected.exitcode, \
            "Exit code of the compiler is incorrect"
        assert actual.execcode == expected.execcode, \
            "Exit code of the execution (spike) is incorrect"

    def naive_alloc(self, file, info):
        return self.compile_and_simulate(file, info, reg_alloc='naive')

    def all_in_mem(self, file, info):
        return self.compile_and_simulate(file, info, reg_alloc='all_in_mem')

    def smart_alloc(self, file, info):
        return self.compile_and_simulate(file, info, reg_alloc='smart')

    def run_with_gcc(self, file, info):
        return self.compile_and_simulate(file, info, reg_alloc='gcc', use_gcc=True)

    def compile_with_gcc(self, file, output_name):
        print("Compiling with GCC...")
        result = self.run_command(
            [ASM, '-S', '-I./',
             '--output=' + output_name,
             '-Werror',
             '-Wno-div-by-zero',  # We need to accept 1/0 at compile-time
             file])
        print(result.output)
        print("Compiling with GCC... DONE")
        return result

    def compile_with_ours(self, file, output_name, reg_alloc):
        print("Compiling ...")
        self.remove(output_name)
        alloc_opt = '--reg-alloc=' + reg_alloc
        out_opt = '--output=' + output_name
        cmd = [sys.executable, MINIC_COMPILE,
               alloc_opt, out_opt]
        if ENABLE_SSA:
            cmd += ['--ssa']
        if SSA_OPTIMS:
            cmd += ['--ssa-optim']
        if DISABLE_TYPECHECK:
            cmd += ['--disable-typecheck']
        if TYPECHECK_ONLY:
            cmd += ['--disable-codegen']
        cmd += [file]
        result = self.run_command(cmd)
        print(' '.join(cmd))
        print("Exited with status:", result.exitcode)
        print(result.output)
        if result.exitcode == 4:
            if "AllocationError" in result.output:
                if reg_alloc == 'naive':
                    pytest.skip("Too big for the naive allocator")
                elif reg_alloc == 'all_in_mem':
                    pytest.skip("Too big for the all in memory allocator")
                else:
                    raise Exception("AllocationError should only happen "
                                    "for reg_alloc='naive' or reg_alloc='all_in_mem'")
            elif ("NotImplementedError" in result.output and
                  SKIP_NOT_IMPLEMENTED):
                pytest.skip("Feature not implemented in this compiler")
        if result.exitcode != 0:
            # May either be a failing test or a test with expected
            # compilation failure (bad type, ...). Let the caller
            # do the assertion and decide:
            return result
        if not TYPECHECK_ONLY:
            assert(os.path.isfile(output_name))
        print("Compiling ... OK")
        return result

    def link_and_run(self, output_name, exec_name, info):
        self.remove(exec_name)
        cmd = [
            ASM, output_name, 'TP04/libprint.s',
            '-o', exec_name
        ] + info.linkargs
        print(info)
        print("Assembling and linking " + output_name + ": " + ' '.join(cmd))
        try:
            subprocess.check_output(cmd, timeout=60, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            print("Assembling failed:\n")
            print(e.output.decode())
            print("Assembler code below:\n")
            cat(output_name)
            pytest.fail()
        assert(os.path.isfile(exec_name))
        sys.stdout.write("Assembling and linking ... OK\n")
        try:
            result = self.run_command(
                [SIMU,
                 '-m100',  # Limit memory usage to 100MB, more than enough and
                           # avoids crashing on a VM with <= 2GB RAM for example.
                 'pk',
                 exec_name],
                scope="runtime")
            output = re.sub(r'bbl loader\r?\n', '', result.output)
            return testinfo(execcode=result.execcode,
                            exitcode=result.exitcode,
                            output=output,
                            linkargs=[],
                            skip_test_expected=False)
        except subprocess.TimeoutExpired:
            pytest.fail("Timeout executing program. Infinite loop in generated code?")

    def compile_and_simulate(self, file, info, reg_alloc, use_gcc=False):
        basename, _ = os.path.splitext(file)
        output_name = basename + '-' + reg_alloc + '.s'
        if use_gcc:
            result = self.compile_with_gcc(file, output_name)
            if result.exitcode != 0:
                # We don't consider the exact exitcode, and ignore the
                # output (our error messages may be different from
                # GCC's)
                return result._replace(exitcode=1,
                                       output=None)
        else:
            result = self.compile_with_ours(file, output_name, reg_alloc)
        if (TYPECHECK_ONLY or
                reg_alloc == 'none' or
                info.exitcode != 0 or result.exitcode != 0):
            # Either the result is meaningless, or we already failed
            # and don't need to go any further:
            return result
        # Only executable code past this point.
        exec_name = basename + '.riscv'
        return self.link_and_run(output_name, exec_name, info)

    @pytest.mark.parametrize('filename', ALL_FILES)
    def test_expect(self, filename):
        """Test the EXPECTED annotations in test files by launching the
        program with GCC."""
        expect = self.get_expect(filename)
        if expect.skip_test_expected:
            pytest.skip("Skipping test because it contains SKIP TEST EXPECTED")
        if expect.exitcode != 0:
            # GCC is more permissive than us, so trying to compile an
            # incorrect program would bring us no information (it may
            # compile, or fail with a different message...)
            pytest.skip("Not testing the expected value for tests expecting exitcode!=0")
        gcc_result = self.run_with_gcc(filename, expect)
        self.assert_equal(gcc_result, expect)

    @pytest.mark.parametrize('filename', ALL_FILES)
    def test_naive_alloc(self, filename):
        expect = self.get_expect(filename)
        naive = self.naive_alloc(filename, expect)
        self.assert_equal(naive, expect)

    @pytest.mark.parametrize('filename', ALL_IN_MEM_FILES)
    def test_alloc_mem(self, filename):
        expect = self.get_expect(filename)
        actual = self.all_in_mem(filename, expect)
        self.assert_equal(actual, expect)

    @pytest.mark.parametrize('filename', ALLOC_FILES)
    def test_smart_alloc(self, filename):
        """Generate code with smart allocation."""
        expect = self.get_expect(filename)
        actual = self.smart_alloc(filename, expect)
        self.assert_equal(actual, expect)


if __name__ == '__main__':
    pytest.main(sys.argv)
