from project import BaseRobot


class FemaleRobot(BaseRobot):

    INITIAL_WEIGHT = 7

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, self.INITIAL_WEIGHT)

    def eating(self):
        self.weight += 1
