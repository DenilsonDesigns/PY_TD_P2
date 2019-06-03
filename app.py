import constants

# print("Player name:", player['name'])
# clean the data
player_list = []
for player in constants.PLAYERS:
    height = int(player['height'][0:2])
    player_list.append({'name': player['name'], 'guardians': player['guardians'], 'experience': player['experience'],
                        'height': height})

print(player_list)


def make_teams(player_pool):
    pass


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
            if team_choice == "1":
                print("You chose Panthers!")
                show = False
            elif team_choice == "2":
                print("You chose Bandits!")
                show = False
            elif team_choice == "3":
                print("You chose Warriors!")
                show = False


def show_teams():
    print("1) Panthers")
    print("2) Bandits")
    print("3) Warriors")
    return input("Enter an option >")


if __name__ == '__main__':
    show_menu()
