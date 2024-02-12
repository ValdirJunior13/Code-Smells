# Classe que representa o resultado da batalha
class BattleResult:
    def __init__(self):
        self.observers = []
        self.winner_name = None

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print(f"Erro: Observador '{observer}' não encontrado na lista.")

    def notify_observers(self, winner_name):
        for observer in self.observers:
            observer.update(winner_name)

    def set_winner(self, winner_name):
        self.winner_name = winner_name
        self.notify_observers(winner_name)

# Classe que representa um jogador
class Player:
    def __init__(self, player_name):
        self.player_name = player_name

    def update(self, winner_name):
        if self.player_name == winner_name:
            print(f"Parabéns, {self.player_name}, você venceu a batalha!")
        else:
            print(f"{self.player_name}, você perdeu a batalha. O vencedor é: {winner_name}")

# Implementação das Interfaces (não é mais necessário)
# from abc import ABC, abstractmethod
#
# class Observer(ABC):
#     @abstractmethod
#     def update(self, winner_name):
#         pass

# Implementação das Classes
# A classe Subject não é mais necessária, pois não estamos usando a interface Subject.

# Exemplo de uso
if __name__ == "__main__":
    battle_result = BattleResult()

    player1 = Player("Alice")
    player2 = Player("Bob")

    battle_result.add_observer(player1)
    battle_result.add_observer(player2)

    battle_result.set_winner("Alice")
