import PySimpleGUI as sg

#getting the 5 star card exp 

# Add some color
# to the window
sg.theme('SandyBeach')	

# Very basic window.
# Return values using
# automatic-numbered keys
layout = [
	[sg.Text('Please enter the 5 star class exp card')],
    [sg.Text('Character Class', size =(15, 1)), sg.InputText()],
	[sg.Text('Saber', size =(15, 1)), sg.InputText()],
    [sg.Text('Archer', size =(15, 1)), sg.InputText()],
    [sg.Text('Lancer', size =(15, 1)), sg.InputText()],
    [sg.Text('Rider', size =(15, 1)), sg.InputText()],
    [sg.Text('Caster', size =(15, 1)), sg.InputText()],
    [sg.Text('Assassin', size =(15, 1)), sg.InputText()],
    [sg.Text('Berserker', size =(15, 1)), sg.InputText()],
    [sg.Text('All', size =(15, 1)), sg.InputText()],
	[sg.Submit(), sg.Cancel()]
]

window = sg.Window('FGO EXP calculator', layout)
event, values = window.read()
window.close()

# The input data looks like a simple list
# when automatic numbered
character = values[0]
Saber = int(values[1])
Archer = int(values[2])
Lancer = int(values[3])
Rider = int(values[4])
Caster = int(values[5])
Assassin = int(values[6])
Berserker = int(values[7])
All = int(values[8])

if character == "Saber" or character == "saber":
    Saber = Saber*97200
    Archer = Archer * 81000
    Lancer = Lancer * 81000
    Rider = Rider * 81000
    Caster = Caster * 81000
    Assassin = Assassin * 81000
    Berserker = Berserker * 81000
    All = All * 97200
    total = Saber+Archer+Lancer+Rider+Caster+Assassin+Berserker+All  
if character == "Archer" or character == "archer":
    Saber = Saber*81000
    Archer = Archer * 97200
    Lancer = Lancer * 81000
    Rider = Rider * 81000
    Caster = Caster * 81000
    Assassin = Assassin * 81000
    Berserker = Berserker * 81000
    All = All * 97200
    total = Saber+Archer+Lancer+Rider+Caster+Assassin+Berserker+All  
if character == "Lancer" or character == "lancer":
    Saber = Saber*81000
    Archer = Archer * 81000
    Lancer = Lancer * 97200
    Rider = Rider * 81000
    Caster = Caster * 81000
    Assassin = Assassin * 81000
    Berserker = Berserker * 81000
    All = All * 97200
    total = Saber+Archer+Lancer+Rider+Caster+Assassin+Berserker+All   
if character == "Rider" or character == "rider":
    Saber = Saber*81000
    Archer = Archer * 81000
    Lancer = Lancer * 81000
    Rider = Rider * 97200
    Caster = Caster * 81000
    Assassin = Assassin * 81000
    Berserker = Berserker * 81000
    All = All * 97200
    total = Saber+Archer+Lancer+Rider+Caster+Assassin+Berserker+All   
if character == "Caster" or character == "caster":
    Saber = Saber*81000
    Archer = Archer * 81000
    Lancer = Lancer * 81000
    Rider = Rider * 81000
    Caster = Caster * 97200
    Assassin = Assassin * 81000
    Berserker = Berserker * 81000
    All = All * 97200
    total = Saber+Archer+Lancer+Rider+Caster+Assassin+Berserker+All   
if character == "Assassin" or character == "assassin":
    Saber = Saber*81000
    Archer = Archer * 81000
    Lancer = Lancer * 81000
    Rider = Rider * 81000
    Caster = Caster * 81000
    Assassin = Assassin * 97200
    Berserker = Berserker * 81000
    All = All * 97200
    total = Saber+Archer+Lancer+Rider+Caster+Assassin+Berserker+All   
if character == "Berserker" or character == "berserker":
    Saber = Saber*81000
    Archer = Archer * 81000
    Lancer = Lancer * 81000
    Rider = Rider * 81000
    Caster = Caster * 81000
    Assassin = Assassin * 81000
    Berserker = Berserker * 97200
    All = All * 97200
    total = Saber+Archer+Lancer+Rider+Caster+Assassin+Berserker+All   
if character == "All" or character == "all":
    Saber = Saber*81000
    Archer = Archer * 81000
    Lancer = Lancer * 81000
    Rider = Rider * 81000
    Caster = Caster * 81000
    Assassin = Assassin * 81000
    Berserker = Berserker * 81000
    All = All * 97200
    total = Saber+Archer+Lancer+Rider+Caster+Assassin+Berserker+All   
    
print(total)

#getting the 4 star card exp 

# Add some color
# to the window
sg.theme('SandyBeach')	

# Very basic window.
# Return values using
# automatic-numbered keys
layout = [
	[sg.Text('Please enter the 4 star class exp card')],
	[sg.Text('Saber', size =(15, 1)), sg.InputText()],
    [sg.Text('Archer', size =(15, 1)), sg.InputText()],
    [sg.Text('Lancer', size =(15, 1)), sg.InputText()],
    [sg.Text('Rider', size =(15, 1)), sg.InputText()],
    [sg.Text('Caster', size =(15, 1)), sg.InputText()],
    [sg.Text('Assassin', size =(15, 1)), sg.InputText()],
    [sg.Text('Berserker', size =(15, 1)), sg.InputText()],
    [sg.Text('All', size =(15, 1)), sg.InputText()],
	[sg.Submit(), sg.Cancel()]
]

window = sg.Window('FGO EXP calculator', layout)
event, values1 = window.read()
window.close()


Saber4 = int(values1[0])
Archer4 = int(values1[1])
Lancer4 = int(values1[2])
Rider4 = int(values1[3])
Caster4 = int(values1[4])
Assassin4 = int(values1[5])
Berserker4 = int(values1[6])
All4 = int(values1[7])

if character == "Saber" or character == "saber":
    Saber4 = Saber4 *32400
    Archer4 = Archer4 * 27000
    Lancer4 = Lancer4 * 27000
    Rider4 = Rider4 * 27000
    Caster4 = Caster4 * 27000
    Assassin4 = Assassin4 * 27000
    Berserker4 = Berserker4 * 27000
    All4 = All4 * 32400
    total2 = Saber4+Archer4+Lancer4+Rider4+Caster4+Assassin4+Berserker4+All4  
if character == "Archer" or character == "archer":
    Saber4 = Saber4 *27000
    Archer4 = Archer4 * 32400
    Lancer4 = Lancer4 * 27000
    Rider4 = Rider4 * 27000
    Caster4 = Caster4 * 27000
    Assassin4 = Assassin4 * 27000
    Berserker4 = Berserker4 * 27000
    All4 = All4 * 32400
    total2 = Saber4+Archer4+Lancer4+Rider4+Caster4+Assassin4+Berserker4+All4   
if character == "Lancer" or character == "lancer":
    Saber4 = Saber4 *27000
    Archer4 = Archer4 * 27000
    Lancer4 = Lancer4 * 32400
    Rider4 = Rider4 * 27000
    Caster4 = Caster4 * 27000
    Assassin4 = Assassin4 * 27000
    Berserker4 = Berserker4 * 27000
    All4 = All4 * 32400
    total2 = Saber4+Archer4+Lancer4+Rider4+Caster4+Assassin4+Berserker4+All4    
if character == "Rider" or character == "rider":
    Saber4 = Saber4 *27000
    Archer4 = Archer4 * 27000
    Lancer4 = Lancer4 * 27000
    Rider4 = Rider4 * 32400
    Caster4 = Caster4 * 27000
    Assassin4 = Assassin4 * 27000
    Berserker4 = Berserker4 * 27000
    All4 = All4 * 32400
    total2 = Saber4+Archer4+Lancer4+Rider4+Caster4+Assassin4+Berserker4+All4     
if character == "Caster" or character == "caster":
    Saber4 = Saber4 *27000
    Archer4 = Archer4 * 27000
    Lancer4 = Lancer4 * 27000
    Rider4 = Rider4 * 27000
    Caster4 = Caster4 * 32400
    Assassin4 = Assassin4 * 27000
    Berserker4 = Berserker4 * 27000
    All4 = All4 * 32400
    total2 = Saber4+Archer4+Lancer4+Rider4+Caster4+Assassin4+Berserker4+All4    
if character == "Assassin" or character == "assassin":
    Saber4 = Saber4 *27000
    Archer4 = Archer4 * 27000
    Lancer4 = Lancer4 * 27000
    Rider4 = Rider4 * 27000
    Caster4 = Caster4 * 27000
    Assassin4 = Assassin4 * 32400
    Berserker4 = Berserker4 * 27000
    All4 = All4 * 32400
    total2 = Saber4+Archer4+Lancer4+Rider4+Caster4+Assassin4+Berserker4+All4   
if character == "Berserker" or character == "berserker":
    Saber4 = Saber4 *27000
    Archer4 = Archer4 * 27000
    Lancer4 = Lancer4 * 27000
    Rider4 = Rider4 * 27000
    Caster4 = Caster4 * 27000
    Assassin4 = Assassin4 * 27000
    Berserker4 = Berserker4 * 32400
    All4 = All4 * 32400
    total2 = Saber4+Archer4+Lancer4+Rider4+Caster4+Assassin4+Berserker4+All4  
if character == "All" or character == "all":
    Saber4 = Saber4 *27000
    Archer4 = Archer4 * 27000
    Lancer4 = Lancer4 * 27000
    Rider4 = Rider4 * 27000
    Caster4 = Caster4 * 27000
    Assassin4 = Assassin4 * 27000
    Berserker4 = Berserker4 * 27000
    All4 = All4 * 32400
    total2 = Saber4+Archer4+Lancer4+Rider4+Caster4+Assassin4+Berserker4+All4  
    
print(total2)

#getting the 3 star card exp 

# Add some color
# to the window
sg.theme('SandyBeach')	

# Very basic window.
# Return values using
# automatic-numbered keys
layout = [
	[sg.Text('Please enter the 3 star class exp card')],
	[sg.Text('Saber', size =(15, 1)), sg.InputText()],
    [sg.Text('Archer', size =(15, 1)), sg.InputText()],
    [sg.Text('Lancer', size =(15, 1)), sg.InputText()],
    [sg.Text('Rider', size =(15, 1)), sg.InputText()],
    [sg.Text('Caster', size =(15, 1)), sg.InputText()],
    [sg.Text('Assassin', size =(15, 1)), sg.InputText()],
    [sg.Text('Berserker', size =(15, 1)), sg.InputText()],
    [sg.Text('All', size =(15, 1)), sg.InputText()],
	[sg.Submit(), sg.Cancel()]
]

window = sg.Window('FGO EXP calculator', layout)
event, values2 = window.read()
window.close()


Saber3 = int(values2[0])
Archer3 = int(values2[1])
Lancer3 = int(values2[2])
Rider3 = int(values2[3])
Caster3 = int(values2[4])
Assassin3 = int(values2[5])
Berserker3 = int(values2[6])
All3 = int(values2[7])

if character == "Saber" or character == "saber":
    Saber3 = Saber3 *10800
    Archer3 = Archer3 * 9000
    Lancer3 = Lancer3 * 9000
    Rider3 = Rider3 * 9000
    Caster3 = Caster3 * 9000
    Assassin3 = Assassin3 * 9000
    Berserker3 = Berserker3 * 9000
    All3 = All3 * 10800
    total3 = Saber3+Archer3+Lancer3+Rider3+Caster3+Assassin3+Berserker3+All3  
if character == "Archer" or character == "archer":
    Saber3 = Saber3 *9000
    Archer3 = Archer3 * 10800
    Lancer3 = Lancer3 * 9000
    Rider3 = Rider3 * 9000
    Caster3 = Caster3 * 9000
    Assassin3 = Assassin3 * 9000
    Berserker3 = Berserker3 * 9000
    All3 = All3 * 10800
    total3 = Saber3+Archer3+Lancer3+Rider3+Caster3+Assassin3+Berserker3+All3 
if character == "Lancer" or character == "lancer":
    Saber3 = Saber3 *9000
    Archer3 = Archer3 * 9000
    Lancer3 = Lancer3 * 10800
    Rider3 = Rider3 * 9000
    Caster3 = Caster3 * 9000
    Assassin3 = Assassin3 * 9000
    Berserker3 = Berserker3 * 9000
    All3 = All3 * 10800
    total3 = Saber3+Archer3+Lancer3+Rider3+Caster3+Assassin3+Berserker3+All3    
if character == "Rider" or character == "rider":
    Saber3 = Saber3 *9000
    Archer3 = Archer3 * 9000
    Lancer3 = Lancer3 * 9000
    Rider3 = Rider3 * 10800
    Caster3 = Caster3 * 9000
    Assassin3 = Assassin3 * 9000
    Berserker3 = Berserker3 * 9000
    All3 = All3 * 10800
    total3 = Saber3+Archer3+Lancer3+Rider3+Caster3+Assassin3+Berserker3+All3     
if character == "Caster" or character == "caster":
    Saber3 = Saber3 *9000
    Archer3 = Archer3 * 9000
    Lancer3 = Lancer3 * 9000
    Rider3 = Rider3 * 9000
    Caster3 = Caster3 * 10800
    Assassin3 = Assassin3 * 9000
    Berserker3 = Berserker3 * 9000
    All3 = All3 * 10800
    total3 = Saber3+Archer3+Lancer3+Rider3+Caster3+Assassin3+Berserker3+All3   
if character == "Assassin" or character == "assassin":
    Saber3 = Saber3 *9000
    Archer3 = Archer3 * 9000
    Lancer3 = Lancer3 * 9000
    Rider3 = Rider3 * 9000
    Caster3 = Caster3 * 9000
    Assassin3 = Assassin3 * 10800
    Berserker3 = Berserker3 * 9000
    All3 = All3 * 10800
    total3 = Saber3+Archer3+Lancer3+Rider3+Caster3+Assassin3+Berserker3+All3    
if character == "Berserker" or character == "berserker":
    Saber3 = Saber3 *9000
    Archer3 = Archer3 * 9000
    Lancer3 = Lancer3 * 9000
    Rider3 = Rider3 * 9000
    Caster3 = Caster3 * 9000
    Assassin3 = Assassin3 * 10800
    Berserker3 = Berserker3 * 9000
    All3 = All3 * 10800
    total3 = Saber3+Archer3+Lancer3+Rider3+Caster3+Assassin3+Berserker3+All3  
if character == "All" or character == "all":
    Saber3 = Saber3 *9000
    Archer3 = Archer3 * 9000
    Lancer3 = Lancer3 * 9000
    Rider3 = Rider3 * 9000
    Caster3 = Caster3 * 9000
    Assassin3 = Assassin3 * 9000
    Berserker3 = Berserker3 * 10800
    All3 = All3 * 10800
    total3 = Saber3+Archer3+Lancer3+Rider3+Caster3+Assassin3+Berserker3+All3 
    
print(total3)

#print the values for the amount of exp and how much exp is needed left to get different lvls
#amount needed for lvl 100
print("Total exp gained from cards is")
print(total+total2+total3)

print("amount needed to get servant lvl 100")
finaltotal100 = 20311500-(total+total2+total3)
if finaltotal100<=0:
    finaltotal100 = 0
    
print(finaltotal100)

lvl = 20311500-(total+total2+total3)
lvl = lvl/81000

if lvl<0:
    lvl = 0

print("amount of 5 star exp cards needed left")
print("\n"+lvl)


#amount for lvl 120

print("amount needed to get servant lvl 120")
finaltotal120 = 426541500-(total+total2+total3)
if finaltotal120<=0:
    finaltotal120 = 0
print(finaltotal120)

lvl120 = 426541500-(total+total2+total3)
lvl120 = lvl120/81000

print("amount of 5 star exp cards needed left")
print("\n"+lvl120)