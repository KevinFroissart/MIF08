from typing import Dict, Set
from TP04.Operands import Operand
from TP04.Instruction3A import Instruction, regset_to_string
from TP05.CFG import Block
import copy


class LivenessDataFlow:

    def __init__(self, function, debug=False):
        self._function = function
        self._debug = debug
        # Live Operands at input and output of blocks
        self._blockin: Dict[Block, Set[Operand]] = {}
        self._blockout: Dict[Block, Set[Operand]] = {}
        # Live Operands at outputs of instructions
        self._liveout: Dict[Instruction, Set[Operand]] = {}

    def run(self):
        self.set_gen_kill()
        if self._debug:
            self.print_gen_kill()

        self.run_dataflow_analysis()
        if self._debug:
            self.print_map_in_out()

        self.fill_liveout()

    def set_gen_kill(self):
        """Set the _gen and _kill field for each block in the function."""
        for blk in self._function.get_blocks():
            blk.set_gen_kill()

    def run_dataflow_analysis(self):
        """Run the dataflow liveness analysis, i.e. compute self._blockin and
        self._blockout based on the ._kill and ._gen fields of individual
        instructions."""
        if self._debug:
            print("Dataflow Analysis")
        countit = 0
        # initialisation of all blockout,blockin sets, and def = kill
        for blk in self._function.get_blocks():
            self._blockin[blk] = set()
            self._blockout[blk] = set()
        stable = False
        while not stable:
            # Iterate until fixpoint :
            # make calls to self._function.dataflow_one_step
            countit = countit + 1
            saveoldout = copy.copy(self._blockout)
            saveoldin = copy.copy(self._blockin)  # structure copy
            self.dataflow_one_step()
            stable = True
            for blk in self._function.get_blocks():
                # sets are growing.
                # print (self._blockout[i])
                if (self._blockout[blk] > saveoldout[blk] or
                        self._blockin[blk] > saveoldin[blk]):
                    stable = False
        if self._debug:
            print("finished in " + str(countit) + " iterations")
        # print(self._blockin)
        # print(self._blockout)

    def dataflow_one_step(self):
        """Run one iteration of the dataflow analysis. This function is meant
        to be run iteratively until fixpoint."""
        for blk in self._function.get_blocks():
            self._blockout[blk] = set()
            for child in blk._out:
                self._blockout[blk] = self._blockout[blk] | self._blockin[child]

            self._blockin[blk] = (self._blockout[blk] - blk._kill) | blk._gen

    def fill_liveout(self):
        """Propagate the information from blockout/blockin inside the block
        to get liveset instruction by instructions."""
        for blk in self._function.get_blocks():
            liveset = self._blockout[blk]
            for instr in reversed(blk.get_instructions()):
                self._liveout[instr] = liveset
                liveset = (liveset - set(instr.defined())) | set(instr.used())

    def print_gen_kill(self):  # pragma: no cover
        print("Dataflow Analysis, Initialisation")
        i = 0
        for blk in self._function.get_blocks():
            blk.print_gen_kill(i)
            i += 1

    def print_map_in_out(self):  # pragma: no cover
        """Print in/out sets, useful for debug!"""
        print("In: {" +
              ", ".join(str(x._label) + ": "
                        + regset_to_string(self._blockin[x])
                        for x in self._blockin.keys()) +
              "}")
        print("Out: {" +
              ", ".join(str(x._label) + ": "
                        + regset_to_string(self._blockout[x])
                        for x in self._blockout.keys()) +
              "}")
