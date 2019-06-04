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

    vets_per_team = int(experienced / 3)
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


def get_more_stats(team_list):
    vet_total = 0
    rookie_total = 0
    av_height = 0
    guardian_list = ""

    pass


def show_menu():
    print("BASKETBALL TEAM STATS TOOL\n")
    print("-" * 20)
    show = True
    while show:
        print("Here are your choices:\n")
        print("1) Display Team Stats\n")
        print("2) Quit\n\n")
        choice = input("Enter an option >")
        if choice == "2":
            print("Exiting. Thanks for playing")
            show = False
        elif choice == "1":
            print("Choose a team:")
            team_choice = show_teams()
        else:
            print("Exiting. Thanks for playing")


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
    for player_here in teams_array[team_number - 1]:
        player_string += player_here['name'] + ", "
    print("Team: {} Stats\n".format(team_list[team_number - 1]))
    print("-"*20)
    print("Total players: {}".format(len(teams_array[team_number - 1])))
    print("Player list:")
    print(player_string)
    print("-" * 20)


if __name__ == '__main__':
    show_menu()
