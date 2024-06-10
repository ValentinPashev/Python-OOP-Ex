from project import BaseService


class MainService(BaseService):

    INITIAL_CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_CAPACITY)

    def details(self):
        result = ''

        if self.list_with_services:
            result += f"{self.name} Main Service:\n" + \
                      f"Robots: {' '.join(str(x.name) for x in self.list_with_services)}"

        else:
            result += f"{self.name} Main Service:\n" + \
                      f"Robots: none"

        return result
