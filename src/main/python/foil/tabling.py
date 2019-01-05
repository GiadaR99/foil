import copy
from typing import List
from typing import Tuple


class Tabling:
    def __init__(self, f):
        self.f = f
        self.cache = {}

    def __call__(self, *args):
        key = ()
        for arg in args:
            if type(arg) is list:
                key = (*key, tuple(arg))
            elif type(arg) is dict:
                key = (*key, tuple((k, v) for k, v in arg.items()))
            else:
                key = (*key, arg)

        return copy.deepcopy(self.cache.setdefault(key, self.f(*args)))


@Tabling
def get_examples(
        world: List['Literal'],
        constants: List['Value'],
        target: 'Literal',
        examples: List['Example'],
) -> Tuple[List['Assignment'], List['Assignment']]:
    from foil.exploration import get_assignments
    from foil.exploration import get_closure

    pos, neg = get_assignments(examples)
    pos, neg = get_closure(world, constants, target, pos, neg)

    return pos, neg


@Tabling
def get_masks(target: 'Literal', background: List['Clause']) -> List['Mask']:
    from foil.exploration import get_masks

    return get_masks([*[l for c in background for l in c.literals], target])


@Tabling
def get_variables(target: 'Literal', body: List['Literal']) -> List['Variable']:
    from foil.exploration import get_variables

    return get_variables([target, *body])