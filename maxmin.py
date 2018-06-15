import input as ip
import gen as gen

def findMinForAction(dict, k_players, k_action_vect, player, action):
    strats = []
    for i in gen.Sminusi_withVect(k_players, k_action_vect, player, action):
        #print i
        strats.append(i)
    #print strats
    min = strats[0]
    #min_strat = 0
    min_val = dict[min][player - 1]
    for i in range(len(strats)):
        if((dict[strats[i]][player - 1]) <= dict[min][player - 1]):
            min = strats[i]
            min_val = (dict[strats[i]][player - 1])
            #min_strat = i+1
    ##found best strategy
    ##next find if anything else is as good, you don't need this as the strat gets marked if its max anyways
    return min_val #list of strategies which have min payoff


def findMaxOfMins(dict, k_players, k_action_vect, player):
    actions = []
    for i in range(1, k_action_vect[player - 1] + 1):
        actions.append(i)
    minValues = []
    for i in actions:
        minValues.append(findMinForAction(dict, k_players, k_action_vect, player, i))
    #print minValues
    
    max = minValues[0]
    maxmin_strat = 1
    for i in range(len(minValues)):
        if(minValues[i] >= max):
            max = minValues[i]
            maxmin_strat = i + 1
    #print max
    #print maxmin_strat
    retStrats = []
    retStrats.append(maxmin_strat)
    for i in range(len(minValues)):
        if(minValues[i] == max):
            if (i != maxmin_strat - 1):
                retStrats.append(i+1)
    #print "**************************"
    print str(player) + " \t " + str(max) + " \t\t " + str(retStrats)
    #print "Her maxmin strategies are: " + str(retStrats)
    #print retStrats
    
def findAllMaxmins(dict, k_players, k_action_vect):
    print "***************************"
    print "Maxmin values and Maxmin Strategies of players are as follows:"
    print "Player \t Maxmin Value \t Maxmin Strategies"
    for i in range(1, k_players + 1):
        findMaxOfMins(dict, k_players, k_action_vect, i)

def maxmin(filename):
    dict = {}
    game = filename
    ip.buildUserTable(dict, game)
    k_players = ip.findNumPlayers(game)
    k_action_vect = ip.findActionsVect(game)
    findAllMaxmins(dict, k_players, k_action_vect)    

def good_test():
    game = "./games/random-game-test-simple"
    #game = "./games/32-game"
    #game = "./games/zero-sum-game2"
    #game = "./games/veryweakdom"
    #game = "./games/weakdom"
    
    maxmin(game)
good_test()

def bad_test():             
    #PSNE("./games/weakdom")
    #psne_test()
    dict = {}
    game = "./games/random-game-test-simple"
    #game = "./games/zero-sum-game2"
    #game = "./games/veryweakdom"
    #game = "./games/weakdom"
    #game = "./zero-sum-game-test-simple"
    ip.buildUserTable(dict, game)
    ##print dict
    k_players = ip.findNumPlayers(game)
    #print k_players
    k_actions = ip.findNumActions(game)
    findMinForAction(dict, k_players, k_actions, 1, 2)    
    #findMaxOfMins(dict, k_players, k_actions, 1)
    findAllMaxmins(dict, k_players, k_actions)

