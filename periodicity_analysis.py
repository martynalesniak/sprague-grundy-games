from sprague_grundy_game import SpragueGrundyGame

class PeriodicityAnalysis:
    def __init__(self, game):
        self.game = game

    def find_period(self):
        grundy_values = self.game.grundy
        n = len(grundy_values) - 1
        for start in range(n):
            for period in range(1, n - start - 2):
                is_periodic = True
                for i in range(n - start - period):
                    if grundy_values[start + i] != grundy_values[start + i + period]:
                        is_periodic = False
                        break
                if is_periodic:
                    return start, period
        return None, None


    def find_arithmetic_period(self):
        grundy_values = self.game.grundy
        n = len(grundy_values)
        
        for start in range(n):
            for period in range(1, n - start):
                is_arithmetic = True
                saltus = grundy_values[start + period] - grundy_values[start]
                for i in range(1, n - start - period):
                    if grundy_values[start + i + period] - grundy_values[start + i] != saltus:
                        is_arithmetic = False
                        break
                if is_arithmetic:
                    return start, period, saltus
        return None, None, None



