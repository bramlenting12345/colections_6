
#====================list===========================================
  
import random 


collors_mm = ["oranje","blauw","groen","bruin"]
totaal_mm_in_zak = []

#===================================================================

def vraag_mm():
    random.shuffle(collors_mm)
    vraag_kleuren_mm = input("hoeveel kleuren wilt u : ? ")
    vraag_aantal_mm = int(input("hoeveel m&m wilt u : ? "))

    for i in range (vraag_aantal_mm):
        totaal_mm_in_zak.append(collors_mm[random.randint(0,(int(vraag_kleuren_mm)-1))])

    print(" ")
    print("hier u inhoud van u zakje ")
    index_zakje()

#====================================================================

def index_zakje():
    for y in range(0,4):

        aantal = totaal_mm_in_zak.count(collors_mm[y])
        if aantal > 0:
            print(collors_mm[y] + " = " + str(aantal) + " m&m ")

#=====================================================================

vraag_mm()