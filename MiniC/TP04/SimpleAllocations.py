from TP04.Operands import Temporary, S, GP_REGS, FP
from TP04.Instruction3A import Instru3A
from Errors import AllocationError


class Allocator():
    def __init__(self, function):
        self._function_code = function

    def prepare(self):  # pragma: no cover
        pass

    def rewriteCode(self, listcode):  # pragma: no cover
        pass


class NaiveAllocator(Allocator):
    def __init__(self, *args):
        super().__init__(*args)

    # Allocation functions
    def prepare(self):
        """ Allocate all temporaries to registers.
        Fail if there are too many temporaries."""
        regs = list(GP_REGS)  # Get a writable copy
        temp_allocation = dict()
        for tmp in self._function_code._pool._all_temps:
            try:
                reg = regs.pop()
            except IndexError:
                raise AllocationError(
                    "Too many temporaries ({}) for the naive allocation, sorry."
                    .format(len(self._function_code._pool._all_temps)))
            temp_allocation[tmp] = reg
        self._function_code._pool.set_temp_allocation(temp_allocation)

    def rewriteCode(self, listcode):
        # Finally, modify the code to replace temporaries with
        # regs/memory locations
        listcode.iter_instructions(replace_reg)


def replace_reg(old_i):
    """Replace Temporary operands with
    the corresponding allocated register."""
    ins, old_args = old_i.unfold()
    args = []
    for arg in old_args:
        if isinstance(arg, Temporary):
            arg = arg.get_alloced_loc()
        args.append(arg)
    return [Instru3A(ins, args=args)]


class AllInMemAllocator(Allocator):
    def __init__(self, *args):
        super().__init__(*args)

    def prepare(self):
        """Allocate all temporaries to memory. Hypothesis:
        - Expanded instructions can use  s2 and
        s3 (to store the values of temporaries before the actual
        instruction).
        """
        self._function_code._pool.set_temp_allocation(
            {temp: self._function_code.new_offset(FP)
             for temp in self._function_code._pool._all_temps})
        self._function_code._stacksize = self._function_code.get_offset()
        if self._function_code._stacksize > 234:
            raise AllocationError(
                    "Too many temporaries ({}) for the all in memory allocation, sorry."
                    .format(len(self._function_code._pool._all_temps)))

    def rewriteCode(self, listcode):
        # Finally, modify the code to replace temporaries with
        # regs/memory locations
        listcode.iter_instructions(replace_mem)


def replace_mem(old_i):
    """Replace Temporary operands with the corresponding allocated
    memory location. FP points to the stack."""
    before = []
    after = []
    ins, old_args = old_i.unfold()
    args = []
    numreg = 1

    # iterate over old_args, check which argument
    for arg in old_args :
        # is a temporary (e.g. isinstance(..., Temporary))
        if isinstance(arg, Temporary) :
            # and if so, generate ld/sd accordingly.
            before.append(Instru3A("ld", S[numreg], arg.get_alloced_loc()))
            after.append(Instru3A("sd", S[numreg], arg.get_alloced_loc()))
            # Replace the temporary with S[1], S[2] or S[3] physical registers.
            arg = S[numreg]
            numreg += 1
        args.append(arg)

    # (Exercise 7): compute before,after,args.
    # (Exercise 7): iterate over old_args, check which argument
    # (Exercise 7): is a temporary (e.g. isinstance(..., Temporary)),
    # (Exercise 7): and if so, generate ld/sd accordingly. Replace the
    # (Exercise 7): temporary with S[1], S[2] or S[3] physical registers.
    i = Instru3A(ins, args=args)
    return before + [i] + after
