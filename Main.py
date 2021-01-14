class App:
    def __init__(self):
        self.turn = 0
        self.grid = ["1","2","3","4","5","6","7","8","9"]
        self.symbol_1 = "x"
        self.symbol_2 = "o"
        self.player1 = input("Votre prenom ?")
        print("Vous vous appellez ", self.player1, " vous aurez le simbole", self.symbol_1, "\n")
        self.player2 = input("Votre prenom")
        print("Vous vous appellez ", self.player2, " vous aurez le simbole", self.symbol_2, "\n")
        self.pawn = self.symbol_1
        self.player = self.player1
        while True:
            self.show_grid()
            if self.turn == 9 and self.verification() == False:
                print("personne n'a gagné !")
                break
            if self.verification():
                print(self.player, "a gagné !!!!!!!!!!!!!")
                break
            if self.turn % 2 == 0:
                self.pawn = self.symbol_1
                self.player = self.player1
            else:
                self.pawn = self.symbol_2
                self.player = self.player2
            self.position = input(self.player+": Position")
            if self.position not in self.grid:
                continue

            self.set_pawn()
            self.turn += 1

    def set_pawn(self):
        self.grid[int(self.position)-1] = self.pawn

    def verification(self):
        H1=self.grid[0] == self.pawn and self.grid[1] == self.pawn and self.grid[2] == self.pawn
        H2=self.grid[3] == self.pawn and self.grid[4] == self.pawn and self.grid[5] == self.pawn
        H3=self.grid[6] == self.pawn and self.grid[7] == self.pawn and self.grid[8] == self.pawn
        V1=self.grid[0] == self.pawn and self.grid[3] == self.pawn and self.grid[6] == self.pawn
        V2=self.grid[1] == self.pawn and self.grid[4] == self.pawn and self.grid[7] == self.pawn
        V3=self.grid[2] == self.pawn and self.grid[5] == self.pawn and self.grid[8] == self.pawn
        D1=self.grid[0] == self.pawn and self.grid[4] == self.pawn and self.grid[8] == self.pawn
        D2=self.grid[2] == self.pawn and self.grid[4] == self.pawn and self.grid[6] == self.pawn
        return any([H1, H2, H3, V1, V2, V3, D1, D2])

    def show_grid(self):
        print("Voici la grille :", "".join(self.grid[0:3]), "".join(self.grid[3:6]), "".join(self.grid[6:9]), sep="\n")

App()
