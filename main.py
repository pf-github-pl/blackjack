from game import Game, GameOverCroupierException, GameOverPlayerException

if __name__ == '__main__':
    PLAY = True
    while PLAY:
        try:
            game = Game()
            game.play()
        except GameOverPlayerException as exception:
            print(exception)
        except GameOverCroupierException as exception:
            print(exception)
        PLAY = input('Chcesz grać dalej? [T/n] ').upper() != 'N'
