from typing import List

from project import Adult
from project import BaseClient
from project import Student
from project import BaseLoan
from project import MortgageLoan
from project import StudentLoan


class BankApp:
    NUMBER_OF_CLIENTS = 0
    NOT_GRANTED_LOANS = 0
    GRANTED_LOANS = 0
    NUMBER_OF_GRANTED_LOANS = 0
    SUM_OF_NOT_GRANTED_LOANS = 0

    TYPES_OF_LOANS = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan
    }

    TYPES_OF_CLIENTS = {
        "Student": Student,
        "Adult": Adult
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.TYPES_OF_LOANS.keys():
            raise Exception("Invalid loan type!")

        loan = eval(f"{loan_type}()")
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.TYPES_OF_CLIENTS.keys():
            raise Exception("Invalid client type!")

        if self.capacity == self.NUMBER_OF_CLIENTS:
            if client_type == "Student":
                self.SUM_OF_NOT_GRANTED_LOANS += 2000
            elif client_type == "Adult":
                self.SUM_OF_NOT_GRANTED_LOANS += 50000

            self.NOT_GRANTED_LOANS += 1
            return f"Not enough bank capacity."

        client = self.TYPES_OF_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(client)
        self.NUMBER_OF_CLIENTS += 1
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = [c for c in self.clients if c.client_id == client_id][0]

        if (client.__class__.__name__ == "Student" and loan_type == "StudentLoan") or\
                (client.__class__.__name__ == "Adult" and loan_type == "MortgageLoan"):

            loan = [x for x in self.loans if x.__class__.__name__ == loan_type][0]
            self.loans.remove(loan)
            client.client_loans.append(loan)

            if client.__class__.__name__ == "Student" and loan_type == "StudentLoan":
                self.GRANTED_LOANS += 2000
                self.NOT_GRANTED_LOANS += 1
            else:
                self.NOT_GRANTED_LOANS += 1
                self.GRANTED_LOANS += 50000

            return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

        else:
            self.NOT_GRANTED_LOANS += 1
            raise Exception("Inappropriate loan type!")

    def remove_client(self, client_id: str):
        try:
            client = next(filter(lambda c: c.client_id == client_id, self.clients))
        except StopIteration:
            raise Exception("No such client!")

        if len(client.client_loans) > 0:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        num_of_loans = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                num_of_loans += 1
                loan.increase_interest_rate()
        return f"Successfully changed {num_of_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        num_clients = 0
        for client in self.clients:
            if client.interest < min_rate:
                num_clients += 1
                client.increase_clients_interest()

        return f"Number of clients affected: {num_clients}."

    def get_statistics(self):
        sum_income = 0
        sum_loans = 0
        avg_rate = 0

        for c in self.clients:
            sum_income += c.income
            avg_rate += c.interest

        return f"Active Clients: {len(self.clients)}\n" + \
               f"Total Income: {sum_income:.2f}\n" + \
               f"Granted Loans: {self.NUMBER_OF_CLIENTS}, Total Sum: {self.GRANTED_LOANS:.2f}\n" + \
               f"Available Loans: {len(self.loans)}, Total Sum: {self.SUM_OF_NOT_GRANTED_LOANS:.2f}\n" + \
               f"Average Client Interest Rate: {avg_rate / len(self.clients):.2f}"
