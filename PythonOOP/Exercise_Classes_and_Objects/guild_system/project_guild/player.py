class Player:
    DEFAULT_GUILD = "Unaffiliated"

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = self.DEFAULT_GUILD

    def add_skill(self, skills_name, mana):
        if skills_name not in self.skills:
            self.skills[skills_name] = mana
            return f"Skill {skills_name} added to the collection of the player {self.name}"

        return f"Skill already added"

    def player_info(self):
        skills_string = "\n".join(f"==={name} - {mp}" for name, mp in self.skills.items())
        return f"Name: {self.name}\n" \
               f"Guild: {self.guild}\n" \
               f"HP: {self.hp}\n" \
               f"MP: {self.mp}\n" \
               f"{skills_string}"

