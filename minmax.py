import input as ip
import gen as gen

def stratsOfPlayerAgainstSminusi(sminusi, k_players, k_action_vect, player):
    #for a given sminusi find the best response
    assert (player <= k_players), "Invalid player p>K_p"
    strats = []
    for i in range(1, k_action_vect[player - 1]+1):
        strats.append(i)
    sminusi.insert(player-1, 0)
    for i in strats:
        sminusi[player-1] = i
        j = "  ".join(str(e) for e in sminusi)
        yield j

      

def bestResponse(dict, k_players, k_action_vect, player, sminusi):
    strats = []
    for i in stratsOfPlayerAgainstSminusi(sminusi, k_players, k_action_vect, player):
        strats.append(i)
    best = strats[0]
    best_strat = 0
    
    for i in range(len(strats)):
        if((dict[strats[i]][player - 1])>= dict[best][player - 1]):
            best = strats[i]
            best_strat = i+1
    ret = []
    ret.append(best)
    
    retStrat = []
    retStrat.append(best_strat)
    
    for i in range(len(strats)):
        if((dict[strats[i]][player - 1]) == dict[best][player - 1]):
            if (strats[i] != best):
                ret.append(strats[i])
                retStrat.append(i+1)
    return ret

def findMaxForAllSminusi(dict, k_players, k_action_vect, player):
    Sminusi = []
    ac_vec = list(k_action_vect)
    ac_vec.pop(player - 1)
    for i in gen.stratGenVect_list(k_players - 1, ac_vec):
        Sminusi.append(i) #set of all other strategies
    #print Sminusi
    
    bestResponses = []
    for i in Sminusi:
        bestResponses.extend(bestResponse(dict, k_players, k_action_vect, player, i))
        
    maxValues = []
    for i in bestResponses:
        maxValues.append(dict[i][player - 1])
    
    #finding minmax value
    min = maxValues[0]
    minmax_strat_index = 0
    
    for i in range(len(maxValues)):
        if(maxValues[i] <= min):
            min = maxValues[i]
            minmax_strat_index = i
    
    minmax_value = min
    minmax_indices = []
    minmax_indices.append(minmax_strat_index)
    for i in range(len(maxValues)):
        if(maxValues[i] == min):
            if(i != minmax_strat_index):
                minmax_indices.append(i)
    
    minmaxStrats = []
    for i in minmax_indices:
        minmaxStrats.append(bestResponses[i])
    minmaxList = []
    for i in minmaxStrats:
        li = (map(int, i.split('  ')))
        li.pop(player -1)
        j = "  ".join(str(e) for e in li)
        minmaxList.append(j)
    minmaxList = list(set(minmaxList)) #remove duplicates
    print str(player) + " \t " + str(minmax_value) + " \t\t " + str(minmaxList)

def findMinmaxForAllPlayers(dict, k_players, k_action_vect):
    print "*******************************************************"
    print "Minmax values and Minmax Strategy profiles against players are as follows:"
    print "Player \t Minmax Value \t Strategy profile s-i"
    for i in range(1, k_players +1):
        findMaxForAllSminusi(dict, k_players, k_action_vect, i)

def minmax(filename):
    dict = {}
    game = filename
    ip.buildUserTable(dict, game)
    k_players = ip.findNumPlayers(game)
    k_action_vect = ip.findActionsVect(game)
    findMinmaxForAllPlayers(dict, k_players, k_action_vect)

