# ================================[-dictionary-]========================================
game_boven = {
    "enen" : 0,
    "tween" :0,
    "drieen" : 0,
    "vieren" : 0,
    "vijven" : 0,
    "zessen" : 0
}
naam_speelveld = {}

speler1_score_blok={
    "naam": "geen",
    "game1": {
        "enen" : 0,
        "tweeen" : 0,
        "drieen" : 0,
        "vieren" : 0,
        "vijven" : 0, 
        "zessen" : 0 
        },
    "game2": {
        "enen" : 0,
        "tweeen" : 0,
        "drieen" : 0,
        "vieren" : 0,
        "vijven" : 0, 
        "zessen" : 0 
        }
    
}

# =================================[-list-]==============================================
speler = []

# ================================[-speler aanmaak-]=====================================
def speler_aanmaak():
    vraag_hoeveel_spelers = input("met hoeveel personen wilt u spelen ? : ")
    for i in range(0,int(vraag_hoeveel_spelers)):
        speler_naam = input("naam van speler " + str(i + 1) + " ")
        speler.append(speler_naam)
        



# =================================[-score vel aanmaak-]===================================
def score_vel_aanmaak(): 
    for sp in (speler):
        for x in range(1,7):
            global naam_speelveld
            naam_speelveld = sp + "game" + str(x)
            naam_speelveld = game_boven.copy()
        
       
def print_score_blok():
    for sp in (speler):
        for x in range(1,7):
            naam_speelveld = sp + "game" + str(x)
            naam_speelveld = game_boven.copy()
            print(sp + "game" + str(x))
            print(naam_speelveld)
                   

def wijzig_score():
    for sp in (speler):
        naam_speelveld= sp + "game1"
        dict[naam_speelveld].update({"enen" : 2 })
    print_score_blok()


speler_aanmaak()
score_vel_aanmaak()
print_score_blok()
wijzig_score()

#car.update({"color": "White"})
