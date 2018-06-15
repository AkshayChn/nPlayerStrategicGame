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

if __name__ == "__main__":
    #print "This is the name of the script: ", sys.argv[0]
    #print "Number of arguments: ", len(sys.argv)
    #print "The arguments are: " , str(sys.argv)
    
    if(len(sys.argv) != 2):
        usage()
    else:
        game = sys.argv[1]
        #game = "./games/random-game-test-simple"
        #game = "./games/strongdom"
        #game = "./games/zero-sum-game2"
        #game = "./games/nppd"
        
        runAll(game)
    

