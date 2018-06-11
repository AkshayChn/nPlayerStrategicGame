"""
strongly dominant strateges and equilibrium
weakly dominant strateges and equilibrium
very weakly dominant strateges and equilibrium
all pure strategy nash equilibrium
"""

import input as ip
import gen as gen

def runAllTests():
    ##ip.buildUserTable_test()
    ##gen.stratGen_test()
    for i in gen.Sminusi(3, 3, 2, 1):
        print i
        
def isStronglyDominant(dict, k_players, k_actions, player, action):
    iSD_flag = True
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
            if not (util_from_action[i] > util_from_otherStrat[i]):
                iSD_flag = False
                #print "yay"
                #print util_from_action[i] - util_from_otherStrat[i]
    return iSD_flag       

def findStronglyDominantStrat(dict, k_players, k_actions, player):#ret 0 if none exists
    strat = 0
    for i in range(1, k_actions+1):
        if(isStronglyDominant(dict, k_players, k_actions, player, i)):
            strat = i
    return strat
    
def findStronglyDominantEquilibrium(dict, k_players, k_actions):#ret 0 if none exists
    dominantStratOfPlayers = []
    for i in range(1, k_players+1):
        dominantStratOfPlayers.append(findStronglyDominantStrat(dict, k_players, k_actions, i))
    print "The strongly dominant strategies are as follows"
    print "Player" + "\t" + "Strategy"
    
    for i in range(len(dominantStratOfPlayers)):
        print str(i+1) + "\t" + str(dominantStratOfPlayers[i])
        
    if 0 in dominantStratOfPlayers:
        print "No Strongly Dominant Strategy Equilibrium Exists"
    else:
        print "The strongly dominant strategy equilibrium is: "
        print str(dominantStratOfPlayers)
        
if __name__ == "__main__":
    dict = {}
    game = "./games/random-game-test-simple"
    game = "./games/strongdom"
    #game = "./zero-sum-game-test-simple"
    ip.buildUserTable(dict, game)
    ##print dict
    player  = 2
    findStronglyDominantEquilibrium(dict, 2, 2)


