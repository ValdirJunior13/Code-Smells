# Definição das Interfaces
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, winner_name):
        pass

class Subject(ABC):
    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self, winner_name):
        pass

# Implementação das Classes
class BattleResult(Subject):
    def __init__(self):
        self.observers = []
        self.winner_name = None

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, winner_name):
        for observer in self.observers:
            observer.update(winner_name)

    def set_winner(self, winner_name):
        self.winner_name = winner_name
        self.notify_observers(winner_name)

class Player(Observer):
    def __init__(self, player_name):
        self.player_name = player_name

    def update(self, winner_name):
        if self.player_name == winner_name:
            print(f"Parabéns, {self.player_name}! Você venceu a batalha!")
        else:
            print(f"{self.player_name}, você perdeu a batalha. O vencedor é: {winner_name}")

# Teste do Padrão Observer
if __name__ == "__main__":
    # Criar o resultado da batalha (Subject)
    battle_result = BattleResult()

    # Criar jogadores (Observers)
    player1 = Player("Jogador 1")
    player2 = Player("Jogador 2")

    # Adicionar jogadores como observadores do resultado da batalha
    battle_result.add_observer(player1)
    battle_result.add_observer(player2)

    # Simular uma batalha e definir o vencedor
    battle_result.set_winner("Jogador 1")