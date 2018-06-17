import itertools

def stratGenVect(k_players, action_vect):
    """
    Generates all strategy profiles of k_players given their strategy sets.
    Returns a string
    """
    pl = []
    for i in range(k_players):
        ac = []
        for j in range(action_vect[i]):
            ac.append(j + 1)
        pl.append(ac)
    for i in itertools.product(*pl):
        j = "  ".join(map(str, i))
        yield j
      
def stratGenVect_list(k_players, action_vect):
    """
    Generates all strategy profiles of k_players given their strategy sets.
    Returns a list of ints
    """
    pl = []
    for i in range(k_players):
        ac = []
        for j in range(action_vect[i]):
            ac.append(j + 1)
        pl.append(ac)
    for i in itertools.product(*pl):
        j = list(i)
        yield j


def Sminusi_withVect(k_players, action_vect, player, action):
    """
    Generates all strategy profiles of k_players agains't the given action of the given player.
    Returns a string
    """
    assert (action <= action_vect[player - 1]), "Unknown Action, a>k_a in Sminusi: " + str(action) + " > " + str(action_vect[player - 1])
    
    lis = list(action_vect)
    lis.pop(player - 1)
    playerRemoved_action_vect = lis
    for i in stratGenVect_list(k_players - 1, playerRemoved_action_vect):
        i.insert(player-1, action)
        j = "  ".join(str(e) for e in i)
        yield j

