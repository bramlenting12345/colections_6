#listOne met daarin de getallen: 1,2,3,4,5,6,7,8,9,10
#listTwo met daarin de getallen: 2,4,6,8,10,12,14,16,18,20
# som maken met allen boolen - + * / met de nummers van de de 2 listen 
uitslag = 0


list_one =[1,2,3,4,5,6,7,8,9,10]                # list 1 
list_two =[2,4,6,8,10,12,14,26,18,20]           # list 2 

#================================================================================================
def som_plus(list_one,list_two):
    for i in range(len(list_one)):
        
        antwoord = list_one[i] + list_two[i]
        print(str(list_one[i]) + " + " + str(list_two[i] ) + " = " + str(antwoord))


som_plus(list_one,list_two)
print(" ")
#==================================================================================================
print(" ")

def som_min(list_one,list_two):
    for i in range(len(list_one)):
        
        antwoord = list_one[i] - list_two[i]
        print(str(list_one[i]) + " - " + str(list_two[i] ) + " = " + str(antwoord))


som_min(list_one,list_two)
print("")
#=====================================================================================================
print(" ")

def som_delen(list_one,list_two):
    for i in range(len(list_one)):
        
        antwoord = list_one[i] / list_two[i]
        print(str(list_one[i]) + " / " + str(list_two[i] ) + " = " + str(antwoord))


som_delen(list_one,list_two)
print(" ")
#======================================================================================================
print(" ")

def som_keer(list_one,list_two):
    for i in range(len(list_one)):
        
        antwoord = list_one[i] * list_two[i]
        print(str(list_one[i]) + " * " + str(list_two[i] ) + " = " + str(antwoord))


som_keer(list_one,list_two)
#======================================================================================================