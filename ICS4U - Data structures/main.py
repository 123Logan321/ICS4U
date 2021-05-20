from stats import Stats
from gun import Gun
from ability import Ability
from ability import ultimateAbility

gunfile_input = open("D:\🐧\Coding stuff\Python files\ICS4U\gunInput.txt",'r')
gunfile_data = gunfile_input.readlines()
gunfile_input.close()

abilityfile_input = open("D:\\🐧\\Coding stuff\\Python files\\ICS4U\\abilityInput.txt",'r')
abilityfile_data = abilityfile_input.readlines()
abilityfile_input.close()

ultimateAbilityfile_input = open("D:\\🐧\\Coding stuff\\Python files\\ICS4U\\ultimateAbilityInput.txt",'r')
ultimateAbilityfile_data = ultimateAbilityfile_input.readlines()
ultimateAbilityfile_input.close()

characterfile_input = open("D:\🐧\Coding stuff\Python files\ICS4U\characterInput.txt",'r')
characterfile_data = characterfile_input.readlines()
characterfile_input.close()

characterfile2_input = open("D:\🐧\Coding stuff\Python files\ICS4U\characterInput2.txt",'r')
characterfile2_data = characterfile2_input.readlines()
characterfile2_input.close()

characterfile3_input = open("D:\🐧\Coding stuff\Python files\ICS4U\characterInput3.txt",'r')
characterfile3_data = characterfile3_input.readlines()
characterfile3_input.close()

x = 0
guns = []
for i in gunfile_data:
    if x == 0:
        n = (i[:-1])
    elif x == 1:
        c = (i[:-1])
    else:
        d = (i[:-1])
    x += 1
    if x == 3:
        x = 0
        guns.append(Gun(str(n), int(c), int(d)))

x = 0
abilities = []
for i in abilityfile_data:
    if x == 0:
        n = (i[:-1])
    elif x == 1:
        c = (i[:-1])
    elif x == 2:
        d = (i[:-1])
    elif x == 3:
        g = (i[:-1])
        abilities.append(Ability(str(n), int(c), int(d), int(g)))
    x += 1 
    if x == 4:
        x = 0

x = 0
ultimateAbilities = []   
for i in ultimateAbilityfile_data:
    if x == 0:
        n = (i[:-1])
    elif x == 1:
        c = (i[:-1])
    elif x == 2:
        d = (i[:-1])
    elif x == 3:
        g = (i[:-1])
    elif x == 4:
        a = (i[:-1])
        ultimateAbilities.append(ultimateAbility(str(n), int(c), int(d),int(g),int(a)))
    x += 1 
    if x == 5:
        x = 0

x = 0
for y in characterfile_data:
    if x == 0:
        h = (y[:-1])
    elif x == 1:
        g = [(y[:-1])]
        g = [i for item in g for i in item.split(',')]
    elif x == 2:
        if (y[:-1]) == "Alive":
            a = True
        else:
            a = False
    elif x == 3:
        n = (y[:-1])
    elif x == 4:
        o = (y[:-1])
    elif x == 5:
        b = [(y[:-1])]
        b = [i for item in b for i in item.split(',')]
        player1 = Stats(int(h), g, a, str(n), int(o), b)
        x = 0
    x += 1

x = 0
for y in characterfile2_data:
    if x == 0:
        h = (y[:-1])
    elif x == 1:
        g = [(y[:-1])]
        g = [i for item in g for i in item.split(',')]
    elif x == 2:
        if (y[:-1]) == "Alive":
            a = True
        else:
            a = False
    elif x == 3:
        n = (y[:-1])
    elif x == 4:
        o = (y[:-1])
    elif x == 5:
        b = [(y[:-1])]
        b = [i for item in b for i in item.split(',')]
        player2 = Stats(int(h), g, a, str(n), int(o), b)
        x = 0
    x += 1

x = 0
for y in characterfile3_data:
    if x == 0:
        h = (y[:-1])
    elif x == 1:
        g = [(y[:-1])]
        g = [i for item in g for i in item.split(',')]
    elif x == 2:
        if (y[:-1]) == "Alive":
            a = True
        else:
            a = False
    elif x == 3:
        n = (y[:-1])
    elif x == 4:
        o = (y[:-1])
    elif x == 5:
        b = [(y[:-1])]
        b = [i for item in b for i in item.split(',')]
        player3 = Stats(int(h), g, a, str(n), int(o), b)
        x = 0
    x += 1

'''
player1.buyGun('Vandal',guns)
print(player1.shoot('Operator',guns,player2))
'''
'''
player1.buyUltAbility('BladeStorm',ultimateAbilities)
player1.useAbility('ShowStopper',ultimateAbilities,player3)
'''
'''
player1.useAbility('ShowStopper',ultimateAbilities,player2)
player1.buyUltAbility('ShowStopper',ultimateAbilities)
player1.upAmplify('ShowStopper',ultimateAbilities,3,player3)
player1.buyUltAbility('ShowStopper',ultimateAbilities)
print(player1.money)
player1.upAmplify('ShowStopper',ultimateAbilities,3,player3)
'''
'''
player1.buyAbility('BlastPack',abilities,2)
'''

file_output = open("D:\🐧\Coding stuff\Python files\ICS4U\export.txt",'w')
p_sort = [player1,player2,player3]
p_sort.sort()
file_output.write("================================================================================\n")
for i in p_sort:
    x = str('Character Name:'+ i.name+"\n")
    file_output.write(x)  
    x = str('Character Health:'+ str(i.health) + "\n")
    file_output.write(x)
    x = str('Character Money:'+ str(i.money)+"\n")
    file_output.write(x)
    x = str('Character is Alive:'+ str(i.alive)+"\n")
    file_output.write(x)
    x = str('Guns:'+ str(i.gun)+"\n")
    file_output.write(x)
    x = str('Abilities:' + str(i.ability)+ "\n")
    file_output.write(x)
    file_output.write("================================================================================\n")

