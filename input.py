def buildUserTable(emptyTable, filename):
    """
    Reads the file and writes the payoffs to a dictionary
    """
    rF = open(filename, "r")
    for line in rF:
        if not line.startswith("#"):
            (key, val) = line.strip('\n').replace('[','').replace(']','').strip(' ').lstrip(' ').split(" :	")
            util_string = val.strip(' ').split(' ')
            util_float = list(map(lambda x: float(x), util_string))
            emptyTable[key] =  util_float

def findNumPlayers(filename):
    """
    Returns the total number of players
    """
    rF = open(filename, "r")
    for line in rF:
        if line.startswith("# Players:"):
            (key, val) = line.split(":	")
            #print key + "***" + val
            return int(val)

def findActionsVect(filename):
    """
    Returns a vector of the number of strategies of each player
    """
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

