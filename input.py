def buildUserTable(emptyTable, filename):
    rF = open(filename, "r")
    for line in rF:
        if not line.startswith("#"):
            (key, val) = line.strip('\n').replace('[','').replace(']','').strip(' ').lstrip(' ').split(" :	")
            util_string = val.strip(' ').split(' ')
            util_float = list(map(lambda x: float(x), util_string))
            emptyTable[key] =  util_float

def buildUserTable_test():            
    dict = {}
    game = "./random-game-test-simple"
    #game = "./zero-sum-game-test-simple"
    buildUserTable(dict, game)

    dict['test'] = "test"
    print dict

    print dict['test']

    

