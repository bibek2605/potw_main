gukesh = [[90,4,3,2,1],[0,91,4,3,2],[0,0,93,4,3],[0,0,0,95,5],[0,0,0,0,100]] #table for gukesh
ding = [[100,0,0,0,0],[8,92,0,0,0],[3,7,90,0,0],[2,3,7,88,0],[1,3,4,6,86]] # table for ding

#payer = the player who's move is now
#gukesh = the transfer probabilities for gukesh
#ding = the transfer probabilities for ding
#case_1 = list for current probabilities of each scenario

def play(player,gukesh,ding,case_1) :

    result = [] #creating the list to return from the function

    if player == "gukesh" :
        for n in range(1,6) :  # for current scenarios
            a = 0              # for scenarios after the move
            b = 0              # some kind of iteration variable
            # adding up probabilities to get the final value of a
            for el in case_1 :
                a += el*gukesh[b][n-1]
                b += 1
            result.append(a/100)   # appending the final probability and dividing by 100 to get it in percent

    if player == "ding" :
        for n in range(1,6) :
            a = 0
            b = 0
            for el in case_1 :
                a += el*ding[b][n-1]
                b += 1
            result.append(a/100)
    
    return result

case = [[0,0,100,0,0]] # intial case

# 10 moves each

for i in range(0,10) :
    case.append(play("gukesh",gukesh,ding,case[-1]))
    case.append(play("ding",gukesh,ding,case[-1]))

case_final = case[-1]

# Final state probability

gukesh_final = case_final[0]*0.9 + case_final[1]*0.7
draw_final = case_final[0]*0.1 + case_final[1]*0.3 + case_final[2] + case_final[3]*0.4 + case_final[4]*0.2
ding_final = case_final[3]*0.6 + case_final[4]*0.8

# final output

print("The Probabilities after 10 moves are :")
print("Gukesh :",gukesh_final,"%")
print("Draw   :",draw_final,"%")
print("Ding   :",ding_final,"%")
