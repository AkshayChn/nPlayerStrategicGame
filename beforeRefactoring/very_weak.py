"""
strongly dominant strateges and equilibrium
weakly dominant strateges and equilibrium
very weakly dominant strateges and equilibrium
all pure strategy nash equilibrium
"""

import input as ip
import gen as gen


def isListEmpty(inList):
    ##https://stackoverflow.com/a/1605679
    if isinstance(inList, list): # Is a list
        return all( map(isListEmpty, inList) )
    return False


def isVeryWeaklyDominant(dict, k_players, k_actions, player, action):
    iWD_flag = True
    dominatedStrategies = []
    for i in range(1, k_actions+1):
        dominatedStrategies.append(i)
    dominatedStrategies.remove(action)
    #print "yay"
    #print dominatedStrategies
    for otherStrat in dominatedStrategies:
        #action > otherStrat for all sminusi
        util_from_action = []
        util_from_otherStrat = []
        for i in gen.Sminusi(k_players, k_actions, player, action):
            util_from_action.append((dict[i][player - 1]))
        for i in gen.Sminusi(k_players, k_actions, player, otherStrat):
            util_from_otherStrat.append((dict[i][player - 1]))
        #print util_from_action
        #print util_from_otherStrat
        for i in range(len(util_from_action)):
            if not (util_from_action[i] >= util_from_otherStrat[i]):
                iWD_flag = False
                #print "yay"
                #print util_from_action[i] - util_from_otherStrat[i]
    return iWD_flag 



def findVeryWeaklyDominantStrat(dict, k_players, k_actions, player):#ret 0 if none exists
    strat = []
    for i in range(1, k_actions+1):
        if(isVeryWeaklyDominant(dict, k_players, k_actions, player, i)):
            strat.append(i)
    return strat
    


def findVeryWeaklyDominantEquilibria(dict, k_players, k_actions):#ret 0 if none exists
    dominantStratOfPlayers = []
    for i in range(1, k_players+1):
        dominantStratOfPlayers.append(findVeryWeaklyDominantStrat(dict, k_players, k_actions, i))
    #print dominantStratOfPlayers
    print "***************************************"
    print "Very weakly dominant strategy of the players"
    print "Player" + "\t" + "Strategies"
    for i in range(len(dominantStratOfPlayers)):
        print str(i+1) + "\t" + str(dominantStratOfPlayers[i])
    
    if (isListEmpty(dominantStratOfPlayers)):
        print "No very weakly dominant strategy equilibrium exists"
        return 0
    import itertools
    print "The following are very weakly dominant strategy equilibria"
    for i in itertools.product(*dominantStratOfPlayers):
        print list(i)

def veryWeakDom(filename):
    dict = {}
    game = filename
    ip.buildUserTable(dict, game)
    k_players = ip.findNumPlayers(game)
    k_actions = ip.findNumActions(game)
    findVeryWeaklyDominantEquilibria(dict, k_players, k_actions)
    
           
if __name__ == "__main__":
    dict = {}
    game = "./games/random-game-test-simple"
    #game = "./games/strongdom"
    game = "./games/weakdom"
    #game = "./zero-sum-game-test-simple"
    ip.buildUserTable(dict, game)
    ##print dict
    player  = 2
    #print isVeryWeaklyDominant(dict, 2, 2, 1, 1)
    #print isVeryWeaklyDominant(dict, 2, 2, 2, 2)
    #print findVeryWeaklyDominantStrat(dict, 2,2,1)
    #print findVeryWeaklyDominantStrat(dict, 2,2,2)
    findVeryWeaklyDominantEquilibria(dict, 2,2)

