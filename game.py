"""
strongly dominant strateges and equilibrium
weakly dominant strateges and equilibrium
very weakly dominant strateges and equilibrium
all pure strategy nash equilibrium
"""

import input as ip
import gen as gen

def runAllTests():
    ##ip.buildUserTable_test()
    ##gen.stratGen_test()
    for i in gen.Sminusi(3, 3, 2, 1):
        print i
        
def isStronglyDominant(dict, k_players, k_actions, player, action):
    iSD_flag = True
    dominatedStrategies = []
    for i in range(1, k_actions+1):
        dominatedStrategies.append(i)
    dominatedStrategies.remove(action)
    #print "yay"
    #print dominatedStrategies
    for otherStrat in dominatedStrategies:
        #action > otherStrat for all sminusi
        util_from_action = []
        util_from_otherStrat = []
        for i in gen.Sminusi(k_players, k_actions, player, action):
            util_from_action.append((dict[i][player - 1]))
        for i in gen.Sminusi(k_players, k_actions, player, otherStrat):
            util_from_otherStrat.append((dict[i][player - 1]))
        print util_from_action
        print util_from_otherStrat
        for i in range(len(util_from_action)):
            if not (util_from_action[i] > util_from_otherStrat[i]):
                iSD_flag = False
                print "yay"
                print util_from_action[i] - util_from_otherStrat[i]
    return iSD_flag       

    

if __name__ == "__main__":
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
       
