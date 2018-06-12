import input as ip
import gen as gen

def stratsOfPlayerAgainstSminusi(sminusi, k_players, k_actions, player):
    #for a given sminusi find the best response
    assert (player <= k_players), "Invalid player p>K_p"
    strats = []
    for i in range(1, k_actions+1):
        strats.append(i)
    #print "****"
    #print sminusi
    sminusi.insert(player-1, 0)
    for i in strats:
        sminusi[player-1] = i
        j = "  ".join(str(e) for e in sminusi)
        yield j
        
def strats_test():
    for i in stratsOfPlayerAgainstSminusi([2,3],3, 3, 3):
        print i
    
def bestResponse(dict, k_players, k_actions, player, sminusi):
    strats = []
    for i in stratsOfPlayerAgainstSminusi(sminusi, k_players, k_actions, player):
        #print i
        strats.append(i)
    #print strats
    best = strats[0]
    best_strat = 0
    
    for i in range(len(strats)):
        if((dict[strats[i]][player - 1])>= dict[best][player - 1]):
            best = strats[i]
            best_strat = i+1
    ##found best strategy
    ##next find if anything else is as good
    ret = []
    ret.append(best)
    
    retStrat = []
    retStrat.append(best_strat)
    
    for i in range(len(strats)):
        if((dict[strats[i]][player - 1]) == dict[best][player - 1]):
            if (strats[i] != best):
                ret.append(strats[i])
                retStrat.append(i+1)
    
    #print ret
    #print retStrat
    return ret

def markBestResponse(dict, marker_dict, k_players, k_actions, player):
    #Sminusi = [[1,2],[2,3],[3,1]] #set of all other strategies
    Sminusi = []
    for i in gen.stratGen_list(k_players -1, k_actions):
        Sminusi.append(i) #set of all other strategies
    print Sminusi
    bestResponses = []
    for i in Sminusi:
        bestResponses.extend(bestResponse(dict, k_players, k_actions, player, i))
    print "bestResponsesare:"
    #print bestResponses
    for i in bestResponses:
        print i
        print marker_dict[i]
        marker_dict[i] = marker_dict[i] + 1

def markAllBesrResponses(dict, marker_dict, k_players, k_actions):
    for i in range(k_players):
        markBestResponse(dict, marker_dict, k_players, k_actions, i+1)
            

def makeEmptyMarkerDict(marker_dict, k_players, k_actions):
    keys = 0
    for i in gen.stratGen(k_players, k_actions):
        marker_dict[i] = keys

dict = {}
game = "./games/random-game-test-simple"
#game = "./games/strongdom"
#game = "./games/veryweakdom"
#game = "./games/weakdom"
#game = "./zero-sum-game-test-simple"
ip.buildUserTable(dict, game)
##print dict
k_players = ip.findNumPlayers(game)
#print k_players
k_actions = ip.findNumActions(game)
marker_dict = {}
makeEmptyMarkerDict(marker_dict, 3 ,3 )   
print "markerdict is"
print marker_dict      
markBestResponse(dict, marker_dict, k_players, k_actions, 1)
print "markerdict is"
print marker_dict
