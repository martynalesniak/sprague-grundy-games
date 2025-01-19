from sprague_grundy_game import SpragueGrundyGame

class GameRunner:
    def __init__(self, S, game_type, n):
        self.game = SpragueGrundyGame(S, game_type, n)
    
    def start_game(self):
        self.game.play()


if __name__ == "__main__":
    S = {3,5,6}
    n = 10
    game_type = "subtraction"  
    game = GameRunner(S, game_type, n)
    game.start_game()
