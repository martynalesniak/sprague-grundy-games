from sprague_grundy_game import SpragueGrundyGame
from periodicity_analysis import PeriodicityAnalysis

class GameAnalysis:
    def __init__(self, S, n):
        self.S = S
        self.n = n

    def analyze_game(self, game_type):
        game = SpragueGrundyGame(self.S, game_type, self.n)
        analysis = PeriodicityAnalysis(game)
        preperiod, period = analysis.find_period()
        arithmetic_preperiod, arithmetic_period, saltus = analysis.find_arithmetic_period()

        print(f"Analiza okresowości dla gry {game_type.upper()} dla której S = {self.S} i n = {self.n}")
        print(f"Okres: {period} i preokres: {preperiod}")
        print(f"Okres arytmetyczny: {arithmetic_period} i jego saltus: {saltus}")
    
if __name__ == '__main__':
    S = {1,2,3,5,6,7,9,10,11,13}
    n = 14
    game_analysis = GameAnalysis(S, n)

    #SUBTRACTION
    game_analysis.analyze_game("subtraction")

    # #ALLBUT
    game_analysis.analyze_game("allbut")