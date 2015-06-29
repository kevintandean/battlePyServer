from django.shortcuts import render

# Create your views here
from battlePy.tournament import Tournament
# from battlePy.players.random_player import RandomPlayer
from battlePy.improved_random_player import ImprovedRandomPlayer
from battlePy.player import Player
from battlePy.config import (BOARD_WIDTH,
                    BOARD_HEIGHT)
from battlePy.ship import UP, RIGHT
from battlePy.random_player import RandomPlayer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import random
import pickle


def play(player1,player2):
    tournament = Tournament(player1, player2, 100)
    tournament.start()
    tournament.printStats()


# @require_http_methods(['POST',])
@csrf_exempt
def battle(request):
    print 'test'
    # pickled_player = request.POST.get('dumped')
    # player = pickle.loads(pickled_player)
    player = RandomPlayer()
    # player2 = pickle.loads(pickled_player)
    # print player
    code ="""
class ImprovedRandomPlayer2(Player):
    def initPlayer(self):
        self.name = 'ImprovedRandomPlayer'

    def newGame(self):
        self.shots = set()

    def placeShips(self):
        for ship in self.ships:
            isValid = False
            while not isValid:
                orientation = random.choice([UP, RIGHT])
                if orientation == UP:
                    location = (random.randint(0, BOARD_WIDTH - 1),
                                random.randint(0, BOARD_HEIGHT - 1 - ship.size))
                else:
                    location = (random.randint(0, BOARD_WIDTH - 1 - ship.size),
                                random.randint(0, BOARD_HEIGHT - 1))
                ship.placeShip(location, orientation)

                if self.isShipPlacedLegally(ship):
                    isValid = True

    def fireShot(self):
        shot = (random.randint(0, BOARD_WIDTH - 1),
                random.randint(0, BOARD_HEIGHT - 1))

        while shot in self.shots:
            shot = (random.randint(0, BOARD_WIDTH - 1),
                    random.randint(0, BOARD_HEIGHT - 1))
        self.shots.add(shot)
        return shot
    """
    exec code
    tournament = Tournament(ImprovedRandomPlayer2(),ImprovedRandomPlayer(),100)
    tournament.start()
    result = tournament.getStats()
    print result
    return JsonResponse(result)
