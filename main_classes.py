## Classe que representa o resultado da batalha
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
        self.armies = 0

    def update(self, winner_name):
        if self.player_name == winner_name:
            print(f"Parabéns, {self.player_name}, você venceu a batalha!")
        else:
            print(f"{self.player_name}, você perdeu a batalha. O vencedor é: {winner_name}")

    def add_armies(self, num_armies, target_player=None):
        if target_player is None or target_player == self.player_name:
            self.armies += num_armies
            print(f"{num_armies} exércitos adicionados ao território de {self.player_name}. Total de exércitos agora: {self.armies}")
        else:
            print(f"Operação negada: Você não pode colocar exércitos no território de outro jogador.")

# Exemplo de uso
if __name__ == "__main__":
    battle_result = BattleResult()

    player1 = Player("Alice")
    player2 = Player("Bob")

    battle_result.add_observer(player1)
    battle_result.add_observer(player2)

    battle_result.set_winner("Alice")

    player1.add_armies(5)  # Adicionando 5 exércitos ao território de Alice
    player2.add_armies(3)  # Tentando adicionar 3 exércitos ao território de Bob (será negado)
    player2.add_armies(3, target_player="Alice")  # Tentando adicionar 3 exércitos ao território de Alice (será permitido)
