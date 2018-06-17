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

def markBestResponse(dict, marker_dict, k_players, k_action_vect, player):
    Sminusi = []
    ac_vec = list(k_action_vect)
    ac_vec.pop(player - 1)
    for i in gen.stratGenVect_list(k_players - 1, ac_vec):
        Sminusi.append(i) #set of all other strategies
    bestResponses = []
    for i in Sminusi:
        bestResponses.extend(bestResponse(dict, k_players, k_action_vect, player, i))
    for i in bestResponses:
        marker_dict[i] = marker_dict[i] + 1

def markAllBestResponses(dict, marker_dict, k_players, k_action_vect):
    for i in range(k_players):
        markBestResponse(dict, marker_dict, k_players, k_action_vect, i+1)

def findPSNE(marker_dict, k_players, k_action_vect):
    psne = []
    for i in gen.stratGenVect(k_players, k_action_vect):
        if(marker_dict[i] == k_players):
            psne.append(i)
    print "****************"
    if psne:
        print "The following strategy profiles are PSNE"
        for i in psne:
            print i
    else:
        print "No PSNE found"

def makeEmptyMarkerDict(marker_dict, k_players, k_action_vect):
    keys = 0
    for i in gen.stratGenVect(k_players, k_action_vect):
        marker_dict[i] = keys

def PSNE(filename):
    dict = {}
    ip.buildUserTable(dict, filename)
    k_players = ip.findNumPlayers(filename)
    k_action_vect = ip.findActionsVect(filename)
    marker_dict = {}
    makeEmptyMarkerDict(marker_dict, k_players, k_action_vect)
    markAllBestResponses(dict, marker_dict, k_players, k_action_vect)
    findPSNE(marker_dict, k_players, k_action_vect)

