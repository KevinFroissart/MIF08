from typing import List, Tuple, Set, Any
from TP04.Operands import Operand, Temporary, S, Register, GP_REGS, FP
from TP04.Instruction3A import Instru3A
from TP04.SimpleAllocations import Allocator
from .LibGraphes import Graph, DiGraph  # For Graph coloring utility functions
from Errors import MiniCInternalError


def replace_smart(old_i):
    """Replace Temporary operands with the corresponding allocated
    physical register OR memory location."""
    before = []
    after = []
    ins, old_args = old_i.unfold()
    args = []
    numreg = 1
    # TODO (lab5): compute before,after,args. This is similar to what
    # TODO (lab5): replace_mem and replace_reg from TP04 do.

    first_arg = old_args[0]
    if isinstance(first_arg, Temporary) and first_arg.get_alloced_loc() in GP_REGS:
        if old_i.is_read_only()  :
            before.append(Instru3A("ld", S[numreg], first_arg.get_alloced_loc()))
        if not old_i.is_read_only():
            after.append(Instru3A("sd", S[numreg], first_arg.get_alloced_loc()))
        first_arg = S[numreg]
    elif isinstance(first_arg, Temporary):
        arg = first_arg.get_alloced_loc()
    numreg += 1
    args.append(first_arg)

    for arg in old_args[1:]:
        if isinstance(arg, Temporary) and arg.get_alloced_loc() in GP_REGS:
            before.append(Instru3A("ld", S[numreg], arg.get_alloced_loc()))
            arg = S[numreg]
            numreg += 1
        elif isinstance(arg, Temporary):
            arg = first_arg.get_alloced_loc()
        args.append(arg)

    # and now return the new list!
    i = Instru3A(ins, args=args)  # change argument list into args
    return before + [i] + after


class SmartAllocator(Allocator):

    _igraph: Graph  # interference graph

    def __init__(self, function, basename, liveness,
                 debug=False, debug_graphs=False, *args):
        self._liveness = liveness
        self._basename = basename
        self._debug = debug
        self._debug_graphs = debug_graphs
        super().__init__(function, *args)

    def prepare(self):
        """Perform all steps related to smart register allocation:

        - Dataflow analysis to compute liveness range of each
          temporary.

        - Interference graph construction

        - Graph coloring

        - Substitution of temporaries by actual locations in the
          3-address code.
        """
        # prints the CFG as a dot file
        if self._debug_graphs:
            self._function_code.print_dot(self._basename + ".dot", view=True)
            print("CFG generated in " + self._basename + ".dot.pdf")
        # TODO (lab5): Move the raise statement below down as you progress
        # TODO (lab5): in the lab. It must be removed from the final version.
        # raise NotImplementedError("run: stopping here for now")

        # liveness analysis
        self._liveness.run()

        # conflict graph
        self.build_interference_graph()

        if self._debug_graphs:
            print("printing the conflict graph")
            self._igraph.print_dot(self._basename + "_conflicts.dot")

        # Smart Alloc via graph coloring
        self.smart_alloc(self._basename + "_colored.dot")

    def rewriteCode(self, listcode):
        # Finally, modify the code to replace temporaries with
        # regs/memory locations
        self._function_code.iter_instructions(replace_smart)

    def interfere(self, t1, t2):
        """Interfere function: True if t1 and t2 are in conflit anywhere in
        the function."""
        for _, set in self._liveness._liveout.items() :
            if t1 in set and t2 in set:
                return True
        return False

    def build_interference_graph(self):
        """Build the interference graph. Nodes of the graph are temporaries,
        and an edge exists between temporaries iff they are in conflict (i.e.
        iff self.interfere(t1, t2)."""
        self._igraph = Graph()
        t = self._function_code._pool._all_temps
        for v in t:
            # print("add vertex "+str(v))
            self._igraph.add_vertex(v)
        tpairs = [(p1, p2) for p1 in t for p2 in t]
        # print(tpairs)
        for (t1, t2) in tpairs:
            if t1 == t2:
                continue  # A temporary cannot conflict with itself
            if self.interfere(t1, t2):
                # print("add edge "+str(t1)+" - "+str(t2))
                self._igraph.add_edge((t1, t2))

    def smart_alloc(self, outputname):
        """Allocate all temporaries with graph coloring
        also prints the colored graph if debug.

        Precondition: the interference graph (_igraph) must have been
        initialized.
        """
        if not self._igraph:
            raise MiniCInternalError("hum, the interference graph seems to be empty")
        # Temporary -> Operand (register or offset) dictionary,
        # specifying where a given Temporary should be allocated:
        alloc_dict = {}
        # TODO (lab5): color the graph and get back the coloring (see
        # Graph.color() in LibGraphes.py). Then, construct a dictionary Temporary ->
        # Register or Offset. Our version is less than 15 lines
        # including debug log. You can get all temporaries in
        # self._function_code._pool._all_temps.
        coloringreg = self._igraph.color()
        for reg in self._function_code._pool._all_temps:
            if coloringreg[reg] >= len(GP_REGS):
                alloc_dict[reg] = self._function_code.new_offset(FP)
            else:
                alloc_dict[reg] = GP_REGS[len(GP_REGS) - 1 - coloringreg[reg]]
        print(alloc_dict)
        self._function_code._pool.set_temp_allocation(alloc_dict)
        self._function_code._stacksize = self._function_code.get_offset()
        if self._debug_graphs:
            print("printing the colored conflict graph")
            self._igraph.print_dot(outputname, coloringreg)


def generate_smart_move(dest: Operand, src: Operand) -> List[Instru3A]:
    """Generate a list of move, store and load instructions, depending if the
    operands are registers or memory locations"""
    instr = []
    return instr


def sequentialize_moves(tmp: Register,
                        parallel_moves: Set[Tuple[Any, Any]]) -> List[Tuple[Any, Any]]:
    """Take a set of parallel moves represented as (destination, source) pairs,
    and return a list of sequential moves which respect the cycles.
    Use the specified tmp for cycles.
    Returns a list of (destination, source) pairs"""
    move_graph = DiGraph()
    for dest, src in parallel_moves:
        move_graph.add_edge((src, dest))
    moves = []
    # First iteratively remove all the edges without successors.
    vars_without_successor = {src
                              for src, dests in move_graph.neighbourhoods()
                              if len(dests) == 0}
    while vars_without_successor:
        var = vars_without_successor.pop()
        for src, dests in move_graph.neighbourhoods():
            if var in dests:
                moves.append((var, src))
                dests.remove(var)
                if len(dests) == 0:
                    vars_without_successor.add(src)
        move_graph.delete_vertex(var)
    # Then handle the cycles.
    cycles = move_graph.connex_components()
    for cycle in cycles:
        if len(cycle) == 1:
            v = cycle.pop()
            moves.append((v, v))
        else:
            previous = tmp
            for v in reversed(cycle):
                moves.append((previous, v))
                previous = v
            moves.append((previous, tmp))
    return moves
