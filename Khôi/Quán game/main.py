from game_cafe import GameCafe
from manager import Manager

if __name__ == "__main__":
    cafe = GameCafe()
    manager = Manager(cafe)
    manager.menu()
