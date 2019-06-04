import constants

# clean the data
player_list = []
for player in constants.PLAYERS:
    height = int(player['height'][0:2])
    guardians = player['guardians'].split(" and ")
    experience = True if player['experience'] == 'YES' else False
    player_list.append({'name': player['name'], 'guardians': guardians, 'experience': experience,
                        'height': height})


def make_teams(player_pool):
    # Count the number of experienced players
    experienced = 0
    vet_pool = []
    rookie_pool = []
    team_1 = []
    team_2 = []
    team_3 = []
    for player_in_pool in player_pool:
        if player_in_pool['experience']:
            experienced += 1
            vet_pool.append(player_in_pool)
        else:
            rookie_pool.append(player_in_pool)

    vets_per_team = int(experienced/3)
    print(vets_per_team)
    while len(vet_pool) > 0:
        team_1.extend(vet_pool[0:vets_per_team])
        del vet_pool[0:vets_per_team]
        team_2.extend(vet_pool[0:vets_per_team])
        del vet_pool[0:vets_per_team]
        team_3.extend(vet_pool[0:vets_per_team])
        del vet_pool[0:vets_per_team]

    while len(rookie_pool) > 0:
        team_1.extend(rookie_pool[0:1])
        del rookie_pool[0:1]
        team_2.extend(rookie_pool[0:1])
        del rookie_pool[0:1]
        team_3.extend(rookie_pool[0:1])
        del rookie_pool[0:1]

    return team_1, team_2, team_3


def show_menu():
    print("BASKETBALL TEAM STATS TOOL\n")
    print("Here are your choices:\n")
    print("1) Display Team Stats\n")
    print("2) Quit\n\n")
    show = True
    while show:
        choice = input("Enter an option >")
        if choice == "2":
            show = False
        elif choice == "1":
            team_choice = show_teams()


def show_teams():
    print("1) Panthers")
    print("2) Bandits")
    print("3) Warriors")
    option = int(input("Enter an option >"))
    print_team(option)


def print_team(team_number):
    teams_array = make_teams(player_list)
    team_list = ['Panthers', 'Bandits', 'Warriors']
    player_string = ""
    for player_here in teams_array[team_number-1]:
        player_string += player_here['name']+", "
    print("Team: {} Stats\n".format(team_list[team_number-1]))
    print("--------------------")
    print("Total players: {}\n".format(len(teams_array[team_number-1])))
    print("Player list:")
    print(player_string)


if __name__ == '__main__':
    show_menu()

