#IMPORTing LIBRARIES_________________________________________________________________end((
from random import *
#IMPORTing LIBRARIES_______________________________________________________________start((


#FUNCTIONS______________________________________________________________________start((
def help() :
    print("enter (rock, paper, scissors) to make the game countinue \nenter (result) to see your score, pc_score, tie rounds \nenter (refresh) to refresh the results(your score, pc score, tie mathces) \nenter (exit) to exit")

def rock_f() :
    global rock
    global scissors
    global paper
    global u_rps_n

    #make a value which the value which the value wich PC choosed is going to is goint to be subtracted with that
    u_rps_n = 10
    #if the user, had not choosed the rock more than 3 times, add 1 to the rock
    if rock != 3 :
        rock += 1

    #if the scissors and paper were not 0, subtract them by themselves
    if scissors >= 0 and paper >= 0 :
        scissors -= scissors
        paper -= paper

def scissors_f() :
    global rock
    global scissors
    global paper
    global u_rps_n

    #make a value which the value which the value wich PC choosed is going to is goint to be subtracted with that
    u_rps_n = 9
    #if the user, had not choosed the scissors more than 3 times, add 1 to the scissors
    if scissors != 3 :
        scissors += 1

    #if the rock and paper were not 0, subtract them by themselves
    if rock >= 0 and paper >= 0 :
        rock -= rock
        paper -= paper

def paper_f() :
    global rock
    global scissors
    global paper
    global u_rps_n

    #make a value which the value which the value wich PC choosed is going to is goint to be subtracted with that
    u_rps_n = 1
    #if the user, had not choosed the paper more than 3 times, add 1 to the paper
    if paper != 3 :
        paper += 1

    #if the rock and scissors were not 0, subtract them by themselves
    if rock >= 0 and scissors >= 0:
        rock -= rock
        scissors -= scissors

def w_result() :
    global u_win
    global pc_win
    global tie

    #print the number of (user's win matches) (pc's win matches) (tie matches)
    print(f"you : {u_win} \npc : {pc_win} \nties : {tie}")

def g_result_find(result):
    #(result) is a number that had made with the subtraction of "p_rps"(a number which pc choosed when it choosed one of(rock, paper, scissors)) and "u_rps_n"(a number which user had choosed when it choosed one of(rock, paper, scissors)) (each one of(rock, paper, scissors) has a number)
    
    global u_win
    global pc_win
    global tie

    if result == 1 :
        print("scissros, you won!")
        u_win += 1

    elif result == -1 :
        print("rock, I won!")
        pc_win += 1

    elif result == -9 :
        print("rock, you won!")
        u_win += 1

    elif result == -8 :
        print("scissors, I won!")
        pc_win += 1

    elif result == 9 :
        print("paper, I won!")
        pc_win += 1

    elif result == 8 :
        print("paper, you won!")
        u_win += 1

    else :
        print(f"{u_rps}, tie!")
        tie += 1

def p_rps_find() :
    #pc choosing one of (rock, paper, scissors)
    #at the first check to see if the user had not choosed rock or paper or scissors for a lot of times, if user had, pc will choose somthing which it can win the user, so the user won't cheat

    #if the user had choosed the rock for 3 times or more, pc must choose paper(-1)
    if rock == 3 :
        p_rps = -1

    #if the user had choosed the paper for 3 times or more, pc must choose scissors(-9)
    elif paper == 3 :
        p_rps = -9

    #if the user had choosed the scissors for 3 times or more, pc must choose rock(-10)
    elif scissors == 3 :
        p_rps = -10

    #if the user had not choosed anything 3 times or more, pc must choose somthing random
    else :
        while True :
            #choose a random number between 1, 10 and substract it with (the choosed number * 2)
            p_rps = randint(1, 10)
            p_rps -= p_rps*2
            #if the p_rps(the choosed number) was not (-10 or -9 or -1) choose a number again
            if p_rps == -10 or p_rps == -9 or p_rps == -1 :
                return p_rps

    return p_rps

def refresh() :
    global pc_win
    global u_win
    global tie
    global rock
    global paper
    global scissors

    pc_win = 0
    u_win = 0
    tie = 0
    rock = 0
    paper = 0
    scissors = 0

def error() :
    print("\nplease enter one of (rock, paper, scissors, result, help, refresh, exit)\n")
#FUNCTIONS________________________________________________________________________end((


#MAIN___________________________________________________________________________start((
pc_win = 0
u_win = 0
tie = 0
rock = 0
paper = 0
scissors = 0
u_rps_n = 0

print("let we play rock paper scissors! \n")

while True :
    u_rps = (input("enter one of (rock, paper, scissors) enter (help) for more informations: ")).lower()
    print()

    if u_rps == "help" :
        help()

    elif u_rps == "rock" :
        rock_f()

    elif u_rps == "scissors" :
        scissors_f()

    elif u_rps == "paper" :
        paper_f()

    elif u_rps == "result" :
        w_result()

    elif u_rps == "exit" :
        w_result()
        exit()

    elif u_rps == "refresh" :
        refresh()

    #if the user had entered somthing which is not known, print an error
    else :
        error()
        #turn the u_rps to (help) so the pc will not choose r,p,s(rock, paper, scissors)
        u_rps = "help"

    #if the user had choosed (result, help or refresh), pc will not choose r,p,s
    if u_rps != "result" and u_rps != "help" and u_rps != "refresh" :
        #choose a r,p,s for the pc
        p_rps = p_rps_find()

        #subtract the number of the r,p,s which pc had choosed with the number of the r,p,s which user had choosed
        result = p_rps + u_rps_n
        #after the subtractions, find the winner
        g_result_find(result)
        print()
#MAIN_____________________________________________________________________________end((