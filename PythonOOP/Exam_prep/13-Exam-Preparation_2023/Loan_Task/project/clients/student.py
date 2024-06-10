from project import BaseClient


class Student(BaseClient):

    def __init__(self, name: str, client_id: str, income):
        super().__init__(name, client_id, income, 2.0)

    def increase_clients_interest(self):
        self.interest += 1.0

