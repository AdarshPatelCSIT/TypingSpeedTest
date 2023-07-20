from time import *
import random as r

def mistake(partest , usertest):
    error=0
    for i in range(len(partest)):
        try :
            if partest[i] != usertest[i]:
                error = error + 1
        except :
                error = error + 1
    return error

def speed_time(time_s , time_e , user_input):
    time_delay = time_e - time_s
    time_r = round(time_delay,2)
    speed = len(user_input)/time_r 
    return round(speed)      
while True:
    ck= input("Ready to test: yes / no:")
    if ck == "yes":
        test=["hello i am aman verma","The quick brown fox jumps over the lazy dog" ,  "the most  famous pangram, but there are many others. ","Hello dude i am learning","My favorite may be the five boxing wizards jump quickly,which is four letters shorter.","Hello dude Do you know the strings in java stored in the heap memory","hello i am adarsh patel "]
        test1 = r.choice(test)
        print("            *****Typing Speed******")
        print()
        print(test1)
        print()
        print()
        time1 = time()
        testinput = input("Enter:")
        time2 = time()

        print('Speed : ', speed_time(time1,time2,testinput),"w/sec")
        print("Error : ",mistake(test1,testinput))
    elif ck =="no":
        print("Thank You!")
        break
    else:
        print("wrong input")
