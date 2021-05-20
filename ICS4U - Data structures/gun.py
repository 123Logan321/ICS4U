class Gun:
    '''
    The object consists of all the available guns and their corresponding stats.

    Attributes
    ----------
    name : string
        The name of the gun
    
    cost : int
        The cost of the gun

    damage : int
        The damage of the gun
    '''
    def __init__(self, name, cost, damage):
        '''
        Constructor to build a gun

        Paramaters
        ----------
        name : string
            The name of the gun
        
        cost : int
            The cost of the gun

        damage : int
            The damage of the gun
        '''
        self.name = name
        self.cost = cost
        self.damage = damage
    
    def __str__(self):
        '''
        Returns the object's name when called
        '''
        return self.name