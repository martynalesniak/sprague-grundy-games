from sprague_grundy_game import SpragueGrundyGame

class PeriodicityAnalysis:
    def __init__(self, game):
        self.game = game

    def find_period(self):
        grundy_values = self.game.grundy
        n = len(grundy_values) - 1
        
        for period in range(1, n):
            is_periodic = True
            for i in range(n - period):
                if grundy_values[i] != grundy_values[i + period]:
                    is_periodic = False
                    break
            if is_periodic:
                return period
        return None 


    def find_arithmetic_period(self):
        grundy_values = self.game.grundy
        n = len(grundy_values) - 1
        
        for period in range(1, n):
            is_arithmetic = True
            difference = grundy_values[period] - grundy_values[0]
            for i in range(1, n - period):
                if grundy_values[i + period] - grundy_values[i] != difference:
                    is_arithmetic = False
                    break
            if is_arithmetic:
                return period, difference
        return None


    def find_preperiod(self):
        grundy_values = self.game.grundy
        n = len(grundy_values) - 1
        
        period = self.find_period()
        if period is None:
            return None  # Jeśli nie znaleziono okresu
        
        # Szukamy, gdzie zaczyna się powtarzający się okres
        preperiod_length = 0
        for i in range(n - period):
            if grundy_values[i] == grundy_values[i + period]:
                preperiod_length = i
                break
        
        return preperiod_length
if __name__=='__main__':
    S_subtraction = {1,2,3,4,5}  # Przykładowe S dla gry SUBTRACTION
    S_allbut = {1,2,3,4,5}  # Przykładowe S dla gry ALLBUT
    n = 20  # Liczba pozycji, które chcemy przeanalizować

    # Gra SUBTRACTION
    subtraction_game = SpragueGrundyGame(S_subtraction, "subtraction", n)
    subtraction_analysis = PeriodicityAnalysis(subtraction_game)
    subtraction_period = subtraction_analysis.find_period()
    subtraction_arithmetic_period = subtraction_analysis.find_arithmetic_period()
    subtraction_preperiod = subtraction_analysis.find_preperiod()

    print(f"Okres gry SUBTRACTION: {subtraction_period}")
    print(f"Okres arytmetyczny gry SUBTRACTION: {subtraction_arithmetic_period}")
    print(f"Preokres gry SUBTRACTION: {subtraction_preperiod}")

    # Gra ALLBUT
    allbut_game = SpragueGrundyGame(S_allbut, "allbut", n)
    allbut_analysis = PeriodicityAnalysis(allbut_game)
    allbut_period = allbut_analysis.find_period()
    allbut_arithmetic_period = allbut_analysis.find_arithmetic_period()
    allbut_preperiod = allbut_analysis.find_preperiod()

    print(f"Okres gry ALLBUT: {allbut_period}")
    print(f"Okres arytmetyczny gry ALLBUT: {allbut_arithmetic_period}")