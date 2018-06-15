
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
    for i in range(1, k_actions+1):
        pl.append(i)
    import itertools
    for i in itertools.product(pl, repeat=k_players):
        j = list(i)
        yield j
        
def stratGen_test():
    for i in stratGen(3, 3):
        print i


def Sminusi(k_players, k_actions, player, action):
    assert (action <= k_actions), "Unknown Aciton, a > k_a" + str(action) + " " + str(k_actions)
    for i in stratGen_list(k_players - 1, k_actions):
        i.insert(player-1, action)
        j = "  ".join(str(e) for e in i)
        yield j
def Sminusi_test():
    for i in Sminusi(3, 3, 2, 3):
        print i
