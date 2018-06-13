import strong
import weak
import very_weak
import purenash
import maxmin
import minmax

if __name__ == "__main__":
    game = "./games/random-game-test-simple"
    #game = "./games/weakdom"
    strong.strongDom(game)
    weak.weakDom(game)
    very_weak.veryWeakDom(game)
    maxmin.maxmin(game)
    minmax.minmax(game)
