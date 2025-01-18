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
        
            
    def play(self):
        position = self.n
        player = 1
        moves = []

        print(f"Gracz 1 rozpoczyna grę z {self.n} elementami na stosie, w jednym ruchu możliwe jest wyciągniecię s elementów,\
        gdzie s należy do S = {self.s}")

        while position > 0:
            print(f"Liczba elementów na stosie: {position}, ruch gracza {player}.")
            val = int(input("Wybierz ile elementów zabrać:"))
            if val > position or val not in self.s:
                print("Nieprawidłowy ruch! Spróbuj ponownie.")
                continue

            moves.append((player, position, val))
            position -= val
            player = 3 - player

        winner = 3 - player
        print(f"Gracz {winner} wygrywa!")

        print("Analiza ruchów:")

        for move in moves:
            p, pos, mv = move
            new_pos = pos - mv
            optimal = "OPTYMALNY" if self.grundy[new_pos] == 0 else "NIEOPTYMALNY"
            print(f"Gracz {p} przeszedł z {pos} do {new_pos} ({optimal})")
        print(self.grundy)


