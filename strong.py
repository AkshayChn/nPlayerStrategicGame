import input as ip
import gen as gen

def isStronglyDominantVect(dict, k_players, k_action_vect, player, action):
    iSD_flag = True
    dominatedStrategies = []
    for i in range(1, k_action_vect[player - 1] + 1):
        dominatedStrategies.append(i)
    dominatedStrategies.remove(action)
    
    for otherStrat in dominatedStrategies:
        util_from_action = []
        util_from_otherStrat = []
        for i in gen.Sminusi_withVect(k_players, k_action_vect, player, action):
            util_from_action.append((dict[i][player - 1]))
        for i in gen.Sminusi_withVect(k_players, k_action_vect, player, otherStrat):
            util_from_otherStrat.append((dict[i][player - 1]))
        for i in range(len(util_from_action)):
            if not (util_from_action[i] > util_from_otherStrat[i]):
                iSD_flag = False
    
    return iSD_flag
  
    
def findStronglyDominantStratVect(dict, k_players, k_action_vect, player):#ret 0 if none exists
    assert (player <= k_players), "Player Unknown, p>k_p"
    strat = 0
    for i in range(1, k_action_vect[player - 1]+1):
        if(isStronglyDominantVect(dict, k_players, k_action_vect, player, i)):
            strat = i
    return strat
    

def findStronglyDominantEquilibriumVect(dict, k_players, k_action_vect):#ret 0 if none exists
    dominantStratOfPlayers = []
    for i in range(1, k_players+1):
        dominantStratOfPlayers.append(findStronglyDominantStratVect(dict, k_players, k_action_vect, i))
    print "\nThe strongly dominant strategies are as follows"
    print "Player" + "\t" + "Strategy"
    
    for i in range(len(dominantStratOfPlayers)):
        print str(i+1) + "\t" + str(dominantStratOfPlayers[i])
        
    if 0 in dominantStratOfPlayers:
        print "No Strongly Dominant Strategy Equilibrium Exists"
    else:
        print "The strongly dominant strategy equilibrium is: "
        print str(dominantStratOfPlayers)

def strongDom(filename):
    dict = {}
    game = filename
    ip.buildUserTable(dict, game)
    k_players = ip.findNumPlayers(game)
    k_action_vect = ip.findActionsVect(game)
    findStronglyDominantEquilibriumVect(dict, k_players, k_action_vect)

