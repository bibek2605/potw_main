# We have 15 games so we can assign each scenario a binary number having 15 bits
# 1 represents an upset
# 0 represents a normal result

def prob(x,y) :     # x is winner
    return y/(x+y)

def make_case(n) :
    a = str(bin(n))[2:]

    result = []

    for el in a :
        result.append(int(el))
    
    result.reverse()

    for i in range(0,15-len(result)) :
        result.append(0)
    
    result.reverse()

    return result

def play(array,team) :
    strong = []
    weak = []

    for i in range(0,len(array)) :
        strong.append(min(team[2*i],team[2*i+1]))
        weak.append(max(team[2*i],team[2*i+1]))

    result = 1
    team = []

    for i in range(0,len(array)) :
        if array[i] == 0 :    #No upset
            result *= prob(strong[i],weak[i])
            team.append(strong[i])
        
        else :      #Upset
            result *= prob(weak[i],strong[i])
            team.append(weak[i])

    return [result,team]
    
# n = number of stages
# team = list of teams

def tournament(team) :
    upsets = 0

    for i in range(0,2**15) :
        cases = make_case(i)

        qf = play(cases[0:8],team)
        prbl_qf = qf[0]
        team_qf = qf[1]

        sf = play(cases[8:12],team_qf)
        prbl_sf = sf[0]
        team_sf = sf[1]

        f = play(cases[12:14],team_sf)
        prbl_f = f[0]
        team_f = f[1]

        if cases[-1] == 0 :    #no upset
            prbl_w = prob(min(team_f),max(team_f))
    
        else :  # upset
            prbl_w = prob(max(team_f),min(team_f))
    
        prbl = prbl_qf*prbl_sf*prbl_f*prbl_w
        upsets += prbl*sum(cases)
    
    return upsets

def swap(team,i,j) :
    team[i] += team[j]
    team[j] = team[i] - team[j]
    team[i] = team[i] - team[j]

    result = tournament(team)

    team[i] += team[j]
    team[j] = team[i] - team[j]
    team[i] = team[i] - team[j]

    return result

# match 1   1 v 16
# match 2   8 v 9
# match 3   5 v 12
# match 4   4 v 13
# match 5   6 v 11
# match 6   3 v 14
# match 7   7 v 10
# match 8   2 v 15

team = [1,16,8,9,5,12,4,13,6,11,3,14,7,10,2,15]

upsets = []
change = []

for i in range(0,16) :
    for j in range(i+1,16) :
        upsets.append(swap(team,i,j))
        change.append([team[i],team[j]])

max_upset = max(upsets)
i = upsets.index(max_upset)

print("If ",change[i][0]," and ",change[i][1]," change places then upsets are ",max_upset)
