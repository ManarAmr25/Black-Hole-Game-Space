from models.guest import Guest
from queue import PriorityQueue


class Tournament:
    def __init__(self):
        self.game = None
        self.players = None
        self.players_queue = None
        self.current_match = None

    @staticmethod
    def build_tournament(game, players):  # game : string, game name | players : list of strings, players names
        """Build a tournament with the given parameters. returns none if there are invalid parameters."""
        is_successful = True
        tournament = Tournament()
        is_successful = is_successful and tournament.set_game(game)  # TODO:
        is_successful = is_successful and tournament.set_players(players)
        return tournament if is_successful else None

    def get_player(self, player_id):
        if isinstance(player_id, int) and -1 < player_id < len(self.players):
            return self.players[player_id]
        return None

    def set_game(self, game):
        self.game = game
        return True

    def get_game(self):
        return self.game

    def set_players(self, names):
        if not isinstance(names, list):
            return False
        colors = ['green', 'red', 'yellow', 'blue']
        players = []
        for i, name in enumerate(names):
            if not isinstance(name, str):
                return False
            guest_player = Guest.build_guest(name)
            player_obj = {'player': guest_player, 'state': True, 'wins': 0, 'color': colors[i], 'id': i}
            players.append(player_obj)

        self.players = players
        self.players_queue = PriorityQueue()
        print('init queue in tournament')
        for x in range(len(self.players)):
            print(x, (0, x))
            self.players_queue.put((0, x))
        print(self.players_queue)
        # self.players_queue = [x for x in range(len(self.players))]
        return True

    def next_match(self):
        print('get next match in tournament')
        if self.players_queue.qsize() > 1:
            p1, p2 = self.players_queue.get()[1], self.players_queue.get()[1]
            self.current_match = (p1, p2)
            print(self.current_match)
            return p1, p2
        return None

    def get_match(self):
        return self.current_match

    def push_winner(self, player_id):
        print("push_winner in tournament", player_id)
        if isinstance(player_id, int) and -1 < player_id < len(self.players):
            self.players[player_id]['wins'] += 1
            self.players[player_id]['state'] = True
            self.players_queue.put((self.players[player_id]['wins'], player_id))
            print(self.players_queue)

    def push_tie(self, p1_id, p2_id):
        print("push_tie in tournament", p1_id, p2_id)
        if isinstance(p1_id, int) and -1 < p1_id < len(self.players) \
                and isinstance(p2_id, int) and -1 < p2_id < len(self.players):
            self.players_queue.put((self.players[p1_id]['wins'], p1_id))
            self.players_queue.put((self.players[p2_id]['wins'], p2_id))
            self.players[p1_id]['state'] = True
            self.players[p2_id]['state'] = True
            print(self.players_queue)

    def get_winner(self):
        if self.players_queue is not None and self.players is not None and self.players_queue.qsize() == 1:
            player_id = self.players_queue.get()[1]
            return self.players[player_id]
        return None
