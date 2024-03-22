import random

class GameList:
    def __init__(self, games=None, filename=None):
        if games:
            self.games = games
        elif filename:
            self.games = self.load_games_from_file(filename)
        else:
            self.games = ["game 1", "game 2", "game 3", "game 4", "game 5"]

    def load_games_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                games = [line.strip() for line in f.readlines()]
            return games
        except FileNotFoundError:
            print("File not found.")
            return []

    def remove_game(self, game):
        if game in self.games:
            self.games.remove(game)
            return True
        else:
            return False

    def pull_random_games(self, num_to_pull=5):
        if num_to_pull > len(self.games):
            num_to_pull = len(self.games)
        random_games = random.sample(self.games, num_to_pull)
        return random_games

    def add_game(self, game):
        self.games.append(game)

    def display_games(self, filename=None):
        if filename:
            with open(filename, 'w') as f:
                f.write("Current Games:\n")
                for game in self.games:
                    f.write(game + "\n")
            print(f"Games list saved to {filename}")
        else:
            print("Current Games:")
            for index, game in enumerate(self.games, start=1):
              print(f"{index}. {game}")


if __name__ == "__main__":
    filename = input("Enter the filename to load the games list from (leave empty to start with an empty list): ")
    games_list = GameList(filename=filename)

    while True:
        print("\n1. Pull Random Games")
        print("2. Add a Game")
        print("3. Remove a Game")
        print("4. Display Games")
        print("5. Save Games List To a File")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            pulled_games = games_list.pull_random_games()
            print("Pulled games:")
            for index, game in enumerate(pulled_games):
                print(f"{index+1}. {game}")
            game_to_remove = input("Enter the number of the game you want to remove (0 to cancel): ")
            if game_to_remove.isdigit():
                game_index = int(game_to_remove) - 1
                if 0 <= game_index < len(pulled_games):
                    game_to_remove = pulled_games[game_index]
                    if games_list.remove_game(game_to_remove):
                        print(f"{game_to_remove} removed successfully.")
                    else:
                        print(f"{game_to_remove} not found in the list.")
                elif game_index == -1:
                    print("Operation cancelled.")
                else:
                    print("Invalid game number.")
            else:
                print("Invalid input.")
        elif choice == "2":
            new_game = input("Enter the name of the game to add: ")
            games_list.add_game(new_game)
            print("Game added successfully.")
        elif choice == "3":
            game_to_remove = input("Enter the name of the game you want to remove: ")
            if games_list.remove_game(game_to_remove):
                print(f"{game_to_remove} removed successfully.")
            else:
                print(f"{game_to_remove} not found in the list.")
        elif choice == "4":
            games_list.display_games()
        elif choice == "5":
            filename = input("Enter the filename to save the games list: ")
            games_list.display_games(filename)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
