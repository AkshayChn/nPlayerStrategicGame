
def stratGen(k_players, k_actions):
    pl = []
    for i in range(1, k_actions+1):
        pl.append(i)
    import itertools
    for i in itertools.product(pl, repeat=k_players):
        j = "  ".join(map(str, i))
        yield j

def stratGen_list(k_players, k_actions):
    pl = []
    for i in range(1, k_actions + 1):
        pl.append(i)
    import itertools
    for i in itertools.product(pl, repeat=k_players):
        j = list(i)
        yield j

def stratGenVect(k_players, action_vect):
    pl = []
    for i in range(k_players):
        ac = []
        for j in range(action_vect[i]):
            ac.append(j + 1)
            #print "j\n"
        pl.append(ac)
    print "action_vect is:" + str(action_vect)
    print "pl is :" + str(pl)
    import itertools
    for i in itertools.product(*pl):
        j = "  ".join(map(str, i))
        yield j
        #print j
      
def stratGenVect_list(k_players, action_vect):
    pl = []
    for i in range(k_players):
        #print i
        ac = []
        for j in range(action_vect[i]):
            ac.append(j + 1)
            #print "j\n"
        pl.append(ac)
    #print "action_vect is:" + str(action_vect)
    #print "actions are :" + str(pl)
    import itertools
    for i in itertools.product(*pl):
        j = list(i)
        yield j
        #print j

def Sminusi(k_players, k_actions, player, action):
    assert (action <= k_actions), "Unknown Aciton, a > k_a" + str(action) + " " + str(k_actions)
    for i in stratGen_list(k_players - 1, k_actions):
        i.insert(player-1, action)
        j = "  ".join(str(e) for e in i)
        yield j
        
def Sminusi_withVect(k_players, action_vect, player, action):
    assert (action <= action_vect[player - 1]), "Unknown Action, a>k_a in Sminusi: " + str(action) + " > " + str(action_vect[player - 1])
    
    lis = list(action_vect)
    
    lis.pop(player - 1)
    playerRemoved_action_vect = lis
    #print "action_vect  " + str(playerRemoved_action_vect) + " *******"
    for i in stratGenVect_list(k_players - 1, playerRemoved_action_vect):
        i.insert(player-1, action)
        j = "  ".join(str(e) for e in i)
        yield j
        #print j


