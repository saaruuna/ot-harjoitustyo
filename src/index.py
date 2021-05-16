from initialize_database import initialize_database
from logic.game import Game

def main():
    initialize_database()

    game = Game()

    while game.running:
        game.curr_menu.display_menu()
        game.run()

if __name__ == "__main__":
    main()
