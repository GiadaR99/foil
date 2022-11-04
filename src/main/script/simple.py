import datetime

from src.main.python.foil.learning import foil
from src.main.python.foil.learning import get_closure
from src.main.python.foil.learning import get_constants
from src.main.python.foil.learning import get_masks
from src.main.python.foil.models import Clause
from src.main.python.foil.models import Example
from src.main.python.foil.models import Literal
from src.main.python.foil.models import Program


class Measure:
    def __init__(self):
        self.elapsed = None

    def __enter__(self):
        self.elapsed = datetime.datetime.now()

    def __exit__(self, ty, val, tb):
        print('\nElapsed time: %s sec.\n' % (datetime.datetime.now() - self.elapsed))


if __name__ == '__main__':
    target = Literal.parse('path(X,Y)')
    examples = [
        Example({'X': 0, 'Y': 1}), Example({'X': 0, 'Y': 2}), Example({'X': 0, 'Y': 3}),
        Example({'X': 0, 'Y': 4}), Example({'X': 0, 'Y': 5}), Example({'X': 0, 'Y': 6}),
        Example({'X': 0, 'Y': 8}), Example({'X': 1, 'Y': 2}), Example({'X': 3, 'Y': 2}),
        Example({'X': 3, 'Y': 4}), Example({'X': 3, 'Y': 5}), Example({'X': 3, 'Y': 6}),
        Example({'X': 3, 'Y': 8}), Example({'X': 4, 'Y': 5}), Example({'X': 4, 'Y': 6}),
        Example({'X': 4, 'Y': 8}), Example({'X': 6, 'Y': 8}), Example({'X': 7, 'Y': 6}),
        Example({'X': 7, 'Y': 8}),
    ]
    background = [
        Clause.parse('edge(0,1).'), Clause.parse('edge(0,3).'), Clause.parse('edge(1,2).'),
        Clause.parse('edge(3,2).'), Clause.parse('edge(3,4).'), Clause.parse('edge(4,5).'),
        Clause.parse('edge(4,6).'), Clause.parse('edge(6,8).'), Clause.parse('edge(7,6).'),
        Clause.parse('edge(7,8).'),
    ]

    for i in range(10):
        with Measure():
            print()
            constants = get_constants([target, *{l for c in background for l in c.literals}])
            print()
            world = Program(background).ground()
            print()
            positives, negatives = get_closure(target, constants, world, examples)
            print()
            masks = get_masks([target, *{l for c in background for l in c.literals}])
            print()
            for clause in foil(target, background, masks, constants, positives, negatives):
                print(clause)
