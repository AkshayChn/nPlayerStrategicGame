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

def isVeryWeaklyDominantVect(dict, k_players, k_action_vect, player, action):
    assert (player <= k_players), "Unknown Player"
    assert (action <= k_action_vect[player - 1]), "unknown Action"
    iWD_flag = True
    dominatedStrategies = []
    for i in range(1, k_action_vect[player - 1] + 1):
        dominatedStrategies.append(i)
    dominatedStrategies.remove(action)
    
    for otherStrat in dominatedStrategies:
        #action > otherStrat for all sminusi
        util_from_action = []
        util_from_otherStrat = []
        for i in gen.Sminusi_withVect(k_players, k_action_vect, player, action):
            util_from_action.append((dict[i][player - 1]))
        for i in gen.Sminusi_withVect(k_players, k_action_vect, player, otherStrat):
            util_from_otherStrat.append((dict[i][player - 1]))
        
        for i in range(len(util_from_action)):
            if not (util_from_action[i] >= util_from_otherStrat[i]):
                iWD_flag = False
    return iWD_flag 

def findVeryWeaklyDominantStratVect(dict, k_players, k_action_vect, player):#ret 0 if none exists
    strat = []
    for i in range(1, k_action_vect[player - 1] + 1):
        if(isVeryWeaklyDominantVect(dict, k_players, k_action_vect, player, i)):
            strat.append(i)
    return strat
    

def findVeryWeaklyDominantEquilibriaVect(dict, k_players, k_action_vect):#ret 0 if none exists
    dominantStratOfPlayers = []
    for i in range(1, k_players+1):
        dominantStratOfPlayers.append(findVeryWeaklyDominantStratVect(dict, k_players, k_action_vect, i))
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
    k_action_vect = ip.findActionsVect(game)
    findVeryWeaklyDominantEquilibriaVect(dict, k_players, k_action_vect)

