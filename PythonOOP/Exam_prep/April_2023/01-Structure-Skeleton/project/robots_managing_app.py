from typing import List

from project import BaseRobot
from project import FemaleRobot
from project import MaleRobot
from project import BaseService
from project import MainService
from project import SecondaryService


class RobotsManagingApp:

    CALCULATED_PRICE = 0

    VALID_ROBOTS = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot
    }

    VALID_SERVICES = {
        "MainService": MainService,
        "SecondaryService": SecondaryService
    }

    ERROR_MSG_TYPE_SERVICE = "Invalid service type!"
    ERROR_MSG_TYPE_ROBOT = "Invalid robot type!"
    ERROR_MSG_CAPACITY = "Not enough capacity for this robot!"
    ERROR_MSG_NO_ROBOT = "No such robot in this service!"

    def __init__(self):
        self.robots_list: List[BaseRobot] = []
        self.service_list: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICES.keys():
            raise Exception("Invalid service type!")

        current_service = self.VALID_SERVICES[service_type](name)
        self.service_list.append(current_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOTS.keys():
            raise Exception("Invalid robot type!")

        current_robot = self.VALID_ROBOTS[robot_type](name, kind, price)
        self.robots_list.append(current_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        current_robot_to_add = [r for r in self.robots_list if r.name == robot_name][0]
        current_service_for_robot = [s for s in self.service_list if s.name == service_name][0]

        if current_service_for_robot.capacity < len(current_service_for_robot.list_with_services):
            raise Exception("Not enough capacity for this robot!")

        if current_robot_to_add.__class__.__name__ == "FemaleRobot" \
                and current_service_for_robot.__class__.__name__ == "SecondaryService":
            current_service_for_robot.list_with_services.append(current_robot_to_add)

            return f"Successfully added {robot_name} to {service_name}."

        elif current_robot_to_add.__class__.__name__ == "MaleRobot" \
                and current_service_for_robot.__class__.__name__ == "MainService":
            current_service_for_robot.list_with_services.append(current_robot_to_add)
            return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):

        try:
            current_robot_to_add = [r for r in self.robots_list if r.name == robot_name][0]
            current_service_for_robot = [s for s in self.service_list if s.name == service_name][0]

            if current_robot_to_add.__class__.__name__ == "FemaleRobot" \
                    and current_service_for_robot.__class__.__name__ == "SecondaryService":
                current_service_for_robot.list_with_services.remove(current_robot_to_add)

                return f"Successfully removed {robot_name} from {service_name}."

            elif current_robot_to_add.__class__.__name__ == "MaleRobot" \
                    and current_service_for_robot.__class__.__name__ == "MainService":
                current_service_for_robot.list_with_services.remove(current_robot_to_add)

                return f"Successfully removed {robot_name} from {service_name}."

        except IndexError:
            return "No such robot in this service!"

    def feed_all_robots_from_service(self, service_name: str):
        service = next((service for service in self.service_list if service.name == service_name), None)

        if not service:
            raise Exception("Service not found!")

        count = 0
        for robot in service.list_with_services:
            robot.eating()
            count += 1

        return f"Robots fed: {count}."

    def service_price(self, service_name: str):
        service = next((service for service in self.service_list if service.name == service_name), None)
        total_price = sum(robot.price for robot in service.list_with_services)
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        return '\n'.join(str(service.details()) for service in self.service_list)

