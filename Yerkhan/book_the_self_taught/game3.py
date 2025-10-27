from random import shuffle

class Card:
    suits = ["пикей", "червей", "бубей", "треф"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]

    def __init__(self, v, s):
        """suit и value - целые числа"""
        self.value = v
        self.suit = s 

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
        return False

    def __gt__(self, c2): 
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
        return False

    def __repr__(self):
        v = self.values[self.value] + " " + self.suits[self.suit]
        return v 


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name 


class Game:
    def __init__(self):
        name1 = input("Введите имя игрока 1: ")
        name2 = input("Введите имя игрока 2: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def print_round_winner(self, winner):
        print(f"{winner} забирает карты!")

    def draw(self, p1n, p1c, p2n, p2c):
        print(f"{p1n} кладёт {p1c}, а {p2n} кладёт {p2c}")

    def play_game(self):
        cards = self.deck.cards
        print("Поехали!")
        while len(cards) >= 2:
            response = input("Нажмите X для выхода, любую другую клавишу — чтобы сыграть раунд: ").strip().upper()
            if response == 'X':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)

            if p1c > p2c:
                self.p1.wins += 1
                self.print_round_winner(self.p1.name)
            else:
                self.p2.wins += 1
                self.print_round_winner(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print(f"\nИгра окончена. Победитель: {win}")

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p2.wins > p1.wins:
            return p2.name
        return "Ничья!"


# запуск игры
if __name__ == "__main__":
    game = Game()
    game.play_game()
