from sprague_grundy_game import SpragueGrundyGame

class Main:
    def __init__(self, S, game_type, n):
        self.game = SpragueGrundyGame(S, game_type, n)
    
    def start_game(self):
        self.game.play()


if __name__ == "__main__":
    S = {3}
    n = 10
    game_type = "subtraction"  
    main_game = Main(S, game_type, n)
    main_game.start_game()
