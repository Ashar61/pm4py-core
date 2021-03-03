from collections import Counter


def playout(*args, **kwargs):
    """
    Performs the playout of the provided model,
    i.e., gets a set of traces from the model

    Parameters
    ---------------
    args
        Model
    kwargs
        Parameters of the playout

    Returns
    --------------
    log
        Simulated event log
    """
    if len(args) == 3:
        from pm4py.objects.petri.petrinet import PetriNet
        if type(args[0]) is PetriNet:
            from pm4py.simulation.playout import simulator
            return simulator.apply(args[0], args[1], final_marking=args[2], **kwargs)
        elif type(args[0]) is dict or type(args[0]) is Counter:
            from pm4py.objects.dfg.utils import dfg_playout
            return dfg_playout.apply(args[0], args[1], args[2], **kwargs)
    elif len(args) == 1:
        from pm4py.objects.process_tree.process_tree import ProcessTree
        if type(args[0]) is ProcessTree:
            from pm4py.simulation.tree_playout import algorithm
            return algorithm.apply(args[0], **kwargs)
    raise Exception("unsupported model for playout")