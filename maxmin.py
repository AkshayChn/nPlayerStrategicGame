import input as ip
import gen as gen

def findMinForAction(dict, k_players, k_action_vect, player, action):
    strats = []
    for i in gen.Sminusi_withVect(k_players, k_action_vect, player, action):
        strats.append(i)
    min = strats[0]
    min_val = dict[min][player - 1]
    for i in range(len(strats)):
        if((dict[strats[i]][player - 1]) <= dict[min][player - 1]):
            min = strats[i]
            min_val = (dict[strats[i]][player - 1])
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
    
    max = minValues[0]
    maxmin_strat = 1
    for i in range(len(minValues)):
        if(minValues[i] >= max):
            max = minValues[i]
            maxmin_strat = i + 1
    
    retStrats = []
    retStrats.append(maxmin_strat)
    for i in range(len(minValues)):
        if(minValues[i] == max):
            if (i != maxmin_strat - 1):
                retStrats.append(i+1)
    print str(player) + " \t " + str(max) + " \t\t " + str(retStrats)
    

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


