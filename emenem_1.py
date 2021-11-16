import random

# je gaat nu zelf aan de slag met Collections! In deze opdracht ga je een programma schrijven waarmee je een zak met M&M’s kan vullen.

# Maak een List waar de volgende kleuren in zitten: oranje, blauw, groen, bruin
# Maak een functie die een List datatype (zak met M&M’s) aanmaakt en vult met kleuren
# De functie heeft 1 parameter → een int met het aantal M&M’s (die een random kleur krijgen) en die dan aan de zak worden toegevoegd
# De functie voegt willekeurige een kleur (M&M) toe aan de zak. De beschikbare kleuren staan in de List aangemaakt in punt 1
# De functie geeft de List (zak met M&M’s) terug als return value
# Het programma vraagt met een input hoeveel kleuren (M&M’s) er aan de zak toegevoegd moeten worden
# Het programma print als laatste de inhoud uit van de zak met M&M’s
 

#  te_raden_getal =(random.randint(1,1000)) 

 

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
    print(inhoud_zak_mm)      


vraag_mm()


  
    

  






