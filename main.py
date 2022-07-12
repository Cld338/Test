from random import *
import time
first_gen = []
first_A=0
first_a=0
f_AA = 0
f_Aa = 0
f_aa = 0
for k in range(200):
    for i in range(8):
        first_gen.append("AA") 
        first_gen.append("AA") #AA 320개
        f_AA += 2
        first_A+=4
        first_gen.append("Aa") #Aa 160개
        f_Aa += 1
        first_A+=1
        first_a+=1
    first_gen.append("aa") #aa 20개
    f_aa += 1
    first_a+=2

def get_next_gen(gen):
    Next_gen = []
    A = 0
    a = 0
    for i in range(2):
        shuffle(gen)
        for k in range(0,len(gen),2):
            r1 = randint(0,1)
            r2 = randint(0,1)
            Next_gen.append("".join(sorted(gen[k][r1]+gen[k+1][r2])))

            if gen[k][r1] == "A":A+=1
            else:a+=1

            if gen[k][r2] == "A":A+=1
            else:a+=1
    AA = Next_gen.count("AA")
    Aa = Next_gen.count("Aa")
    aa = Next_gen.count("aa")
    return Next_gen,A,a,AA,Aa,aa


second_gen,sec_A,sec_a,AA,Aa,aa = get_next_gen(first_gen)
print("__________1세대__________\n")
print(f"A : {first_A}개\na : {first_a}개\n")
print(f"AA : {f_AA}개\nAa : {f_Aa}개\naa : {f_aa}개")
print("_______________________")
print("\n")
print("__________2세대__________\n")
print(f"A : {sec_A}개\na : {sec_a}개\n")
print(f"AA : {AA}개\nAa : {Aa}개\naa : {aa}개")
print("_______________________")
n=2
while True:
    print("\n")
    print(f"__________{n}세대__________\n")
    print(f"A : {sec_A}개\na : {sec_a}개\n")
    print(f"AA : {AA}개\nAa : {Aa}개\naa : {aa}개")
    print("_______________________")
    time.sleep(0.3)
    second_gen,sec_A,sec_a,AA,Aa,aa = get_next_gen(second_gen)
    n += 1