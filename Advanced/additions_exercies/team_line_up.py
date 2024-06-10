def team_lineup(*args):
    players_countries = {}

    for data in args:
        player_name = data[0]
        country = data[1]
        if country not in players_countries:
            players_countries[country] = []
        players_countries[country].append(player_name)

    result = ''

    sorted_dict = sorted(players_countries.items(), key=lambda x: (-len(x[1]), x[0]))

    for tuple_ in sorted_dict:
        result += f"{tuple_[0]}:\n"
        sorted_players = (tuple_[1])
        for player in sorted_players:
            result += f"  -{player}\n"

    return result


print(team_lineup(
      ("Harry Kane", "England"),
      ("Manuel Neuer", "Germany"),
      ("Raheem Sterling", "England"),
      ("Toni Kroos", "Germany"),
      ("Cristiano Ronaldo", "Portugal"),
      ("Thomas Muller", "Germany"),
      ("Toni Kroos", "Germany"),))

# print(team_lineup(
#     ("Harry Kane", "England"),
#     ("Manuel Neuer", "Germany"),
#     ("Raheem Sterling", "England"),
#     ("Toni Kroos", "Germany"),
#     ("Cristiano Ronaldo", "Portugal"),
#     ("Thomas Muller", "Germany")))

# from unittest import TestCase, main
#
#
# class Test(TestCase):
#     def test_example_input(self):
#         result = team_lineup(
#             ("Harry Kane", "England"),
#             ("Manuel Neuer", "Germany"),
#             ("Raheem Sterling", "England"),
#             ("Toni Kroos", "Germany"),
#             ("Cristiano Ronaldo", "Portugal"),
#             ("Thomas Muller", "Germany")
#         )
#         expected = """Germany:
#   -Manuel Neuer
#   -Toni Kroos
#   -Thomas Muller
# England:
#   -Harry Kane
#   -Raheem Sterling
# Portugal:
#   -Cristiano Ronaldo"""
#
#         self.assertEqual(result.strip(), expected)
#
#
# if __name__ == '__main__':
#     main()