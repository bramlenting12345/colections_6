import os
import time

# Alle dagen van de week zijn: maandag, dinsdag, woensdag, donderdag, vrijdag, zaterdag, zondag.
# De werkdagen zijn: maandag, dinsdag, woensdag, donderdag, vrijdag.
# De weekenddagen zijn: zaterdag, zondag.
# Alle dagen van de week in omgekeerde volgorde zijn: zondag, zaterdag, vrijdag, donderdag, woensdag, dinsdag, maandag.
# De werkdagen in omgekeerde volgorde zijn: vrijdag, donderdag, woensdag, dinsdag, maandag.
# De weekenddagen in omgekeerde volgorde zijn: zondag, zaterdag.#

print("alle dagen van de week opdracht 1 ")
alle_dagen_week = ["maandag", "dinsdag", "woensdag","donderdag","vrijdag","zaterdag","zondag"]

for i in range(len(alle_dagen_week)):
  print(alle_dagen_week[i])
#=================================================================================================

print(" ")
print("alle werk dagen van de week ")
print(" ")
for i in range(0,5):
  print(alle_dagen_week[i])
#==================================================================================================

print(" ")
print("print weekend ")
print(" ")
for i in range(5,7):
  print(alle_dagen_week[i])
#===================================================================================================  

print("")
alle_dagen_week.reverse()                 # met reserve worden de cordinaten van de lijst om gekeerd 
print("alle werk dagen achterste voren")
print(" ")
for i in range (2,7):
  print(alle_dagen_week[i])  
#===================================================================================================

print(" ")
print("alle dagen van de week achterste voren ")
print(" ")
for i in range (0,7):
  print(alle_dagen_week[i])
#====================================================================================================

print(" ")
print("weekend achterste voren geprint ")
print(" ")
for i in range (0,3):
  print(alle_dagen_week[i])
#=====================================================================================================  


  
