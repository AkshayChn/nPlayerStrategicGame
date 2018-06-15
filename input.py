def buildUserTable(emptyTable, filename):
    rF = open(filename, "r")
    for line in rF:
        if not line.startswith("#"):
            (key, val) = line.strip('\n').replace('[','').replace(']','').strip(' ').lstrip(' ').split(" :	")
            util_string = val.strip(' ').split(' ')
            util_float = list(map(lambda x: float(x), util_string))
            emptyTable[key] =  util_float

def findNumPlayers(filename):
    rF = open(filename, "r")
    for line in rF:
        if line.startswith("# Players:"):
            (key, val) = line.split(":	")
            #print key + "***" + val
            return int(val)
        

            

def findActionsVect(filename):
    rF = open(filename, "r")
    for line in rF:
        if line.startswith("# Actions:"):
            (key, val) = line.split(":	")
            actions = "a"
            #print val
            val_list = []
            val_list = map(int, val.split(' '))
            #print val_list
            #print val_list[0] + 2
            #for i in line.split(" "):
             #   actions = i
            #return int(actions)
    return val_list
"""    
import gen
dict = {}
game = "./games/dominant"
game = "./games/random-game-test-simple"
game = "./games/32-game"
print game
k_players = findNumPlayers(game)
s = findActionsVect(game)
#gen.stratGenVect_list(k_players, s)
gen.Sminusi_withVect(k_players, s, 2,3)
"""

"""
**************************************************************************************
"""
    
def findNumActions(filename):
    rF = open(filename, "r")
    for line in rF:
        if line.startswith("# Actions:"):
            (key, val) = line.split(":	")
            actions = "a"
            for i in line.split(" "):
                actions = i
            return int(actions)
       
def buildUserTable_test():            
    dict = {}
    game = "./games/random-game-test-simple"
    #game = "./zero-sum-game-test-simple"
    buildUserTable(dict, game)

    dict['test'] = "test"
    print dict

    print dict['test']

def findPlayers_test():
    game = "./games/dominant"
    #print "player = " + str(findNumPlayers(game))
    print "actions =" 
    print "asdf " + str(findNumActions(game))
