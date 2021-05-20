class Ability:
    '''
    The object consists of all the available abilities and their corresponding stats.

    Attributes
    ----------
    name : string
        The name of the ability
    
    cost : int
        The cost of the ability

    damage : int
        The damage of the ability

    charges : int
        The number of charges that an ability could be held
    '''
    def __init__(self, name, cost, damage, charges):
        '''
        Constructor to build the ability

        Paramaters
        ----------
        name : string
            The name of the ability
        
        cost : int
            The cost of the ability

        damage : int
            The damage of the ability

        charges : int
        The number of charges that an ability could be held
        '''
        self.name = name
        self.cost = cost
        self.damage = damage
        self.charges = charges
        
    def __str__(self):
        '''
        Returns the object's name when called
        '''
        return self.name
    
class ultimateAbility(Ability):
    '''
    The object consists of all the available ultimate abilities and their corresponding stats.
    It is a sub class of Ability.

    Attributes
    ----------
    amplifier : int
        The x amount that the dmg will be increased by
    '''
    def __init__(self, name, cost, damage, charges, amplifier):
        '''
        Constructor to build the ability

        Paramaters
        ----------
        amplifier : int
            The x amount that the dmg will be increased by
        '''
        self.amplifier = amplifier
        super().__init__(name,cost,damage,charges)
    
    