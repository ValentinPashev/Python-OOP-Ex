from typing import List
from project import BaseDiver
from project import FreeDiver
from project import ScubaDiver
from project import BaseFish
from project import DeepSeaFish
from project import PredatoryFish


class NauticalCatchChallengeApp:



    VALID_TYPES_OF_FISH = {
        "PredatoryFish": PredatoryFish,
        "DeepSeaFish": DeepSeaFish
    }

    VALID_TYPES_OF_DIVERS = {
        "FreeDiver": FreeDiver,
        "ScubaDiver": ScubaDiver
    }

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_TYPES_OF_DIVERS.keys():
            return f"{diver_type} is not allowed in our competition."

        try:
            diver = [d for d in self.divers if d.name == diver_name][0]
            return f"{diver.name} is already a participant."

        except IndexError:
            new_diver = self.VALID_TYPES_OF_DIVERS[diver_type](diver_name)
            self.divers.append(new_diver)
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_TYPES_OF_FISH:
            return f"{fish_type} is forbidden for chasing in our competition."

        try:
            fish = [f for f in self.fish_list if f.name == fish_name][0]
            return f"{fish.name} is already permitted."

        except IndexError:
            new_fish = self.VALID_TYPES_OF_FISH[fish_type](fish_name, points)
            self.fish_list.append(new_fish)
            return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):

        try:
            diver = [d for d in self.divers if d.name == diver_name][0]

        except IndexError:
            return f"{diver_name} is not registered for the competition."

        try:
            fish = [f for f in self.fish_list if f.name == fish_name][0]

        except IndexError:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            message = f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                message = f"{diver_name} hits a {fish.points}pt. {fish_name}."

            else:
                message = f"{diver_name} missed a good {fish_name}."

        else:
            diver.hit(fish)
            message = f"{diver_name} hits a {fish.points}pt. {fish_name}."

        if diver.oxygen_level == 0:
            diver.update_health_status()

        return message

    def health_recovery(self):
        divers_with_health_issue = [d for d in self.divers if d.has_health_issue]

        for diver in divers_with_health_issue:
            diver.has_health_issue = False
            diver.renew_oxy()
        return f"Divers recovered: {len(divers_with_health_issue)}"

    def diver_catch_report(self, diver_name: str):
        divers = [d for d in self.divers if d.name == diver_name][0]
        result = f"**{diver_name} Catch Report**\n"
        fish_details = "\n".join([fish.fish_details() for fish in divers.catch])
        result += fish_details
        return result

    def competition_statistics(self):
        healthy_divers = [d for d in self.divers if not d.has_health_issue]

        sorted_divers = sorted(healthy_divers, key= lambda d: (-d.competition_points, -len(d.catch), d.name))

        result = f"**Nautical Catch Challenge Statistics**\n"
        result += '\n'.join(str(d) for d in sorted_divers)

        return result
