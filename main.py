import os
from game.game import Game

def main():
    #Read input text files from test directory
    for inputfile in os.listdir("tests/"):
        if not inputfile.endswith("txt"):
            continue
        path = os.path.join("tests", inputfile)
        print ("Input file:", inputfile)
        with open(path) as inhandle:
            commands = [line.upper().strip() for line in inhandle.readlines()]
            #Create game object
            curr_game = Game()
            #Pass commands into game
            curr_game.process_commands(commands)

if __name__ == "__main__":
    main()
    