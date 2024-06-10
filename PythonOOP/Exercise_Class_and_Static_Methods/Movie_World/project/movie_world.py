from typing import List

from project import Customer
from project import DVD


class MovieWorld:

    def __init__(self, name):
        self.name = name
        self.customers_list: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers_list) < self.customer_capacity():
            self.customers_list.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = next(filter(lambda c: c.id == customer_id, self.customers_list))
        dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return f"DVD is already rented"




        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = next(filter(lambda c: c.id == customer_id, self.customers_list))
        dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))

        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False

        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        return "\n".join([
            *[str(c) for c in self.customers_list],
            *[str(d) for d in self.dvds],
        ])