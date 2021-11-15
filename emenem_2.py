from math import isnan
import random


#Je gaat nu doorbouwen op de eerdere taak (F1.6.01.L1 - I'm nutty and I know it! - Bag of M&M's als een List).

#Maak een nieuw functie die een Dictionary datatype (zak met M&M’s) aanmaakt en vult met kleuren
#De functie heeft 1 parameter → een int met het aantal kleuren (M&M’s) die aan de zak worden toegevoegd
#De functie voegt willekeurige een kleur (M&M) toe aan de zak. De beschikbare kleuren staan in de List aangemaakt in punt 1 uit de vorige taak.
#De functie geeft de Dictionary (zak met M&M’s) terug als return value
#Let op: Elke kleur komt maar 1x voor als key in de dictionary. De value is een nummer van de hoeveelheid M&M’s van de betreffende kleur die zich in de zak bevinden! Voorbeeld:

#mnmDictionaryBag = {

 # ”rood” : 2,
  #”geel” : 5,
  #”bruin” : 10
#}

#Dus als je een M&M gaat toevoegen aan de zak, zal je functie eerst moeten controleren of deze kleur al eerder is toegevoegd! Is dit niet het geval, dan zal je dus een nieuwe key met de kleur van de M&M moeten toevoegen aan de zak.

#Het programma gebruikt dezelfde input uit de vorige taak hoeveel kleuren (M&M’s) er aan de zak toegevoegd moeten worden
#Het programma print ook de de inhoud uit van de Dictionary zak met M&M’s
 
kleuren_mm = ["oranje","blauw","groen","bruin"]
inhoud_zak_mm = []





def vraag_mm():
    random.shuffle(kleuren_mm)
    vraag_aantal_mm = int(input("hoeveel mm wilt u "))
    vraag_kleuren = input("hoeveel kleuren wilt u ")
    for i in range (vraag_aantal_mm):
        inhoud_zak_mm.append(kleuren_mm[random.randint(0,int(vraag_kleuren)-1)])
    print(" ")    
    print("hier onder ziet u de inhoud van zakje m&m ")
    print(" ")    
    index_zak_mm(inhoud_zak_mm,kleuren_mm)      
    


def index_zak_mm(inhoud_zak_mm,kleuren_mm):

    for x in range (0,4):
        aantal = inhoud_zak_mm.count(kleuren_mm[x])
        if aantal > 0 : 
            print(kleuren_mm[x] + " = " + str(aantal))
    
    




vraag_mm()


  
    

  






