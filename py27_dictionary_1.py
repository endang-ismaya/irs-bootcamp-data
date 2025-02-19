from pprint import pprint
from prj_database_2 import rogers_team, voda_team, sw_team


# pprint(rogers_team)
# print(voda_team)
# print(sw_team)
def show_info(person: dict) -> None:
    first_name = person["first_name"]
    last_name = person["last_name"]
    team_name = person["team"]
    division_name = person.get("divisi")
    print(
        f"{first_name.title()} {last_name.title()} termasuk dalam team: {team_name} di divisi: {division_name}"
    )


def show_info_loop(person: dict) -> None:
    for k, v in person.items():
        print(f"Key: {k}, Value: {v}")


irs_team = []
irs_team.extend(rogers_team)
irs_team.extend(voda_team)
irs_team.extend(sw_team)

for person in irs_team:
    show_info_loop(person)
