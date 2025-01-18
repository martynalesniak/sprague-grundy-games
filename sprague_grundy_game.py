class SpragueGrundyGame:
    def __init__(self, S, game_type, n):
        self.s = S #set
        self.game_type = game_type
        if game_type == "allbut":
            self.s = set(range(n+1)) - S
        else:
            self.s = S
        self.n = n 
        self.grundy = [0]*(n+1)
        self.calculate_grundy()

    # najmniejsza liczba ktora nie wystepuje w zbiorze
    def mex(self, position):
        reachable = set()
        for el in self.s:
            if (position - el) >= 0:
                reachable.add(self.grundy[position-el])
        mex_value = 0
        while mex_value in reachable:
            mex_value += 1
        return mex_value

    def calculate_grundy(self):
        for position in range(len(self.grundy)):
            self.grundy[position] = self.mex(position)
        
            
