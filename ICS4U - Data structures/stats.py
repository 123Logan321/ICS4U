from gun import Gun
from ability import Ability
class Stats:
    '''
    This is the basic stats of the agent that the player chose

    Attributes
    ----------
    health : int
        The amount of health that the player has with a upper limit of 150 and a lower limit of 0

    gun : list
        A list of guns that the player has in his/her inventory

    alive : boolean
        Indicates whether the player is alive in game or dead in game 

    name : string
        The name of the character that the player chose

    money : int
        The amount of money that the player has

    ability: list
        A list of abilities that are available for the player to use

    Methods
    -------
    shoot(gun : str, Guns : list, target:str) : str
        Attempt to shoot the opponent

    useAbility(ability : str, abilities : list, target:string) : str
        Attempt to use an ability to hit the opponent

    buyAbility(ability : str, availableAbilities : list, charge : int) : None
        Purchasing an ability

    buyGun(Gun : str, Guns : list) : None
        Purchasing a gun
    '''

    def __init__(self, health, gun, alive, name, money, ability):
        '''
        Constructor to build a player's stats in Valorant

        Parameters
        ----------
        health : int
            The amount of health that the player has with a upper limit of 150 and a lower limit of 0

        gun : list
            A list of guns that the player has in his/her inventory

        alive : boolean
            Indicates whether the player is alive in game or dead in game 

        name : string
            The name of the character that the player chose

        money : int
            The amount of money that the player has

        ability: list
            A list of abilities that are available for the player to use
        '''
    
        self.health = health
        self.gun = gun
        self.alive = alive
        self.name = name
        self.money = money
        self.ability = ability
    
    def shoot(self, gun : str, Guns : list, target : str) -> str:
        '''
        returns the shot that the player shoots and whether it connected or not

        Parameters
        ----------
        gun : str
            The gun that the player will be using when shooting the
            opponent

        Guns : list
            The list of all the guns that are in the game

        target : str
            The target will be the opponent's character's name.
            The opponent could not be alive, then the shot will always miss.

        Returns
        -------
        str
            Messages to indicate the result from the shot, whether the
            target was already dead, or the shot connect and if it was a shot that
            killed the target, then it is counted as a final blow.
            Also checks if the player has this gun.
        '''
        d = 0
        if target.health == 0: 
            return ('Target is already dead')
        
        if gun in self.gun:
            for i in Guns:
                if str(gun) == str(i):
                    d = int(i.damage)

        target.health -= d
        if target.health <= 0:
            target.alive = False
            target.health = 0
            return ('Final blow connected')
        else:
            return ('Shot connected')
    
    def useAbility(self, ability : str, abilities : list, target : str) -> str:
        '''
        returns the target that the player uses an ability on and if it connects or not

        Parameters
        ----------
        ability : str
            The ability that the player decides to use

        abilities : list
            The list of all abilities that are in the game

        target : str
            The target will be the opponent's character's name.
            The opponent could not be alive, then the ability will not cast.
        
        Returns
        -------
        str
            Messages to indicate the result from the usage of the ability, whether the
            target was already dead, or the ability connected and if the ability
            killed the target, then it is counted as a final blow.
            Also checks if the player has this ability.
        '''
        d = 0
        if target.health == 0: 
            return ('Target is already dead')
        
        if ability in self.ability:
            for i in abilities:
                if str(ability) == str(i):
                    d = int(i.damage)

            for i in range(len(self.ability) - 1):
                if ability == str(self.ability[i]) and int(self.ability[i + 1]) > 0:
                    target.health -= d
                    self.ability[i + 1] = str(int(self.ability[i + 1]) - 1)
               
                    if int(self.ability[i + 1]) == 0:
                        del self.ability[i]
                        del self.ability[i]
                        break
        else:
            return("Player does not have this ability purchased")

        if target.health <= 0:
            target.alive = False
            target.health = 0
            return ('Final blow connected')
        else:
            return ('Ability connected')

    def buyAbility(self, ability : str, availableAbilities : list, charge : int) -> None:
        '''
        returns the ability that the player buys

        Parameters
        ----------
        ability : str
            The ability that the player decides to buy
        
        availableAbilities : list
            The list of all abilities that are in the game

        charges : int
            The ultimate abilities that the player can buy from

        Returns
        -------
        None
        '''
        c = 0
        m = 0
        cb = 0
        for i in availableAbilities:
            if str(ability) == str(i):
                cb = int(i.cost)
                c = int(i.cost) * int(charge)
                m = int(i.charges)
        
        if c > self.money:
            print("Player does not have sufficient funds")
            return None
        
        else:
            if ability in self.ability:
                for i in range(len(self.ability)):
                    if str(ability) == self.ability[i] and (int(self.ability[i + 1]) + charge) <= m:
                        self.ability[i + 1] = str(int(self.ability[i + 1]) + charge)
                        self.money -= c
                        return None
                    elif str(ability) == self.ability[i] and (int(self.ability[i + 1]) + charge) > m:
                        print('Ability can not hold this many charges')
                        self.ability[i + 1] = str(m)
                        self.money -= (m - int(self.ability[i + 1])) * cb
                        return None
            else:
                if charge > m:
                    print('Ability can not hold this many charges')
                    self.ability.append(ability)
                    self.ability.append(str(m))
                    self.money -= m*cb
                    return None

                else:
                    self.ability.append(str(ability))
                    self.ability.append(str(charge))
                    self.money -= c
                    return None


    def buyGun(self, Gun : str, Guns : list) -> None:
        '''
        returns the gun that the player buys

        Parameters
        ----------
        Gun : str
            The gun that the player decides to buy
        
        Guns : list
            The list of all the guns that are in the game

        Returns
        -------
        None
        '''
        c = 0
        for i in Guns:
            if str(i.name) == str(Gun):
                c = i.cost

        if c > self.money:
            print("Player does not have sufficient funds")
            return None
        else:
            if Gun in self.gun:
                print("Player already has this gun")
                return None
            else:
                self.money -= int(c)
                self.gun.append(str(Gun))
                return None

    def buyUltAbility(self, ability : str, ultAbilities : list) -> None:
        '''
        returns the ability that the player buys

        Parameters
        ----------
        ability : str
            The ability that the player decides to buy
        
        ultAbilities : list
            The ultimate abilities that the player can buy from

        Returns
        -------
        None
        '''
        c = 0
        for i in ultAbilities:
            if str(ability) == str(i):
                c = i.cost

        if c > self.money:
            print("Player does not have sufficient funds")
            return None

        else:
            if ability in self.ability:
                print("Player already has this ultimate")
                return None
            else:
                self.money -= int(c)
                self.ability.append(str(ability))
                self.ability.append(str('1'))
                return None

    def upAmplify(self, ability : str, ultAbility : list , multiplier : int, target : str) -> None:
        '''
        Allows a player to increase its ultimate abilitie's damage at the cost of its fortune

        Parameters
        ----------
        ability : str
            The ability to be permanetly amplified

        ultAbility : list
            The list of all the ultimate abilities in the game

        multiplier : int
            The additional multiplier that will be added

        target : str
            The target of the amplified ability

        Returns
        -------
        None
        '''
        f = open("D:\\🐧\\Coding stuff\\Python files\\ICS4U\\ultimateAbilityInput.txt",'r')
        f_data = f.readlines()
        f.close()
        data = []
        for i in f_data:
            data.append(i[:-1])
        c = 0
        for i in ultAbility:
            if str(i) == ability:
                c = int(int(i.cost) * multiplier)
        
        if c > self.money:
            print("Player does not have enough funds")
            return None
        
        else:
            self.money -= c
            for i in ultAbility:
                if str(i) == ability:
                    for i in range(len(data)):
                        if data[i] == ability:
                            data[i + 4] = str(int(data[i + 4]) + multiplier)
                            d = int(data[i+2] * int(*data[i+4]))
                    break
            f = open("D:\\🐧\\Coding stuff\\Python files\\ICS4U\\ultimateAbilityInput.txt",'w')
            for i in range(len(data)):
                f.write(data[i]+'\n')
            f.close()
            if target.health == 0: 
                return None

            for i in range(len(self.ability) - 1):
                if ability == str(self.ability[i]) and int(self.ability[i + 1]) > 0:
                    target.health -= d
                    self.ability[i + 1] = str(int(self.ability[i + 1]) - 1)
                
                    if int(self.ability[i + 1]) == 0:
                        del self.ability[i]
                        del self.ability[i]
                        break

        if target.health <= 0:
            target.alive = False
            target.health = 0

    def __lt__(self, other):
        '''
        Sorts all of the given objects by the name.
        '''
        return self.name < other.name