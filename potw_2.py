from random import random

# Picking a random move out of several moves

def floor(n) :
    return int(n-(n%1))

def move(out) :
    num = len(out)
    rand = floor((random()*num))

    if rand == num :
        rand -= 1

    return out[rand]

# Getting possible moves from a specific position
# x = x co-ordinate
# y = y co-ordinate
# k = Number of moves in straight line prior to deviating
# n = Number of squares on each side of board

def play(x,y,k,n) :           

    out = []

    if n+1>x+k>0 and n+1>y+1>0 :
        out.append([x+k,y+1])
    if n+1>x-k>0 and n+1>y+1>0 :
        out.append([x-k,y+1])
    if n+1>x+k>0 and n+1>y-1>0 :
        out.append([x+k,y-1])
    if n+1>x-k>0 and n+1>y-1>0 :
        out.append([x-k,y-1])
    if n+1>x+1>0 and n+1>y+k>0 :
        out.append([x+1,y+k])
    if n+1>x-1>0 and n+1>y+k>0 :
        out.append([x-1,y+k])
    if n+1>x+1>0 and n+1>y-k>0 :
        out.append([x+1,y-k])
    if n+1>x-1>0 and n+1>y-k>0 :
        out.append([x-1,y-k])
    
    return out

x = 1  # Initial coordinates of knight
y = 1
moves_lst_2 = []

for i in range(0,10**5) :  #Running 10^5 simulations
    moves = 0
    condition = False

    while condition == False :
        out = play(x,y,2,8)
        final = move(out)

        x = final[0]
        y = final[1]

        moves += 1

        if x == 1 and y == 1 :
            condition = True
        
    moves_lst_2.append(moves)

moves_total_2 = 0

for el in moves_lst_2 :
    moves_total_2 += el

print("Expected Moves(2.5 moves)=",moves_total_2/10**5)

x = 1
y = 1
moves_lst_3 = []

for i in range(0,10**5) :
    moves = 0
    condition = False

    while condition == False :
        out = play(x,y,3,8)
        final = move(out)

        x = final[0]
        y = final[1]

        moves += 1

        if x == 1 and y == 1 :
            condition = True
        
    moves_lst_3.append(moves)

moves_total_3 = 0

for el in moves_lst_3 :
    moves_total_3 += el

print("Expected Moves(3.5 moves)=",moves_total_3/10**5)
