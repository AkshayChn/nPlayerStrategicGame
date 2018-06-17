import strong
import weak
import very_weak
import purenash
import maxmin
import minmax
import sys

def runAll(game):
    strong.strongDom(game)
    print ""
    weak.weakDom(game)
    print ""
    very_weak.veryWeakDom(game)
    print ""
    purenash.PSNE(game)
    print ""
    maxmin.maxmin(game)
    print ""
    minmax.minmax(game)
    print ""

def usage():
    print "Usage: python main.py <gamut_game_filename>"
    print "This program only accepts gamut games in the simple-output format"

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        usage()
    else:
        game = sys.argv[1]
        runAll(game)
    

