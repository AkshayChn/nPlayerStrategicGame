def test_3():
    dict = {}
    game = "./games/random-game-test-simple"
    #game = "./games/strongdom"
    #game = "./zero-sum-game-test-simple"
    ip.buildUserTable(dict, game)
    ##print dict
    player  = 2
    #print findStronglyDominantStrat(dict, 2, 2, 2)
    print findStronglyDominantEquilibrium(dict, 3, 3)

def test_2():
    dict = {}
    game = "./random-game-test-simple"
    game = "./strongdom"
    #game = "./zero-sum-game-test-simple"
    ip.buildUserTable(dict, game)
    ##print dict
    player  = 2
    print isStronglyDominant(dict, 2, 2, 1, 2)
    print isStronglyDominant(dict, 2, 2, 2, 2)

def test_1():
    for i in gen.Sminusi(3, 3, player, 1):
        print i + "  -> " + str(dict[i][player - 1])
    print "*******"
    for j in gen.Sminusi(3,3, 2, 2):
        print j + "  -> " + str(dict[j][player - 1])
    
    li1 = []
    li2 = []
    for i in gen.Sminusi(3, 3, player, 1):
        li1.append((dict[i][player - 1]))
    print "*******"
    for j in gen.Sminusi(3,3, 2, 2):
        li2.append((dict[j][player - 1]))
    
    for m in range(len(li1)):
        print li1[m] - li2[m]
       
