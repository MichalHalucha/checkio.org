class Warrior(object):
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0

class Knight(Warrior):
    def __init__(self):
        self.health = 50
        self.attack = 7

    @property
    def is_alive(self):
        return self.health > 0

class Army(object):
    def __init__(self):
        self.soldiers = []

    def add_units(self,soldierToAdd,soldierToAdd_amount):
        if soldierToAdd == Warrior:
            for soldierToAdd_i in range(soldierToAdd_amount):
                self.soldiers.append(Warrior())
        elif soldierToAdd == Knight:
            for soldierToAdd_i in range(soldierToAdd_amount):
                self.soldiers.append(Knight())

    def __len__(self):
        return len(self.soldiers)

class Battle(object):
    def __init__(object):
        pass

    def fight(self,army1,army2):
        assert type(army1) == Army
        assert type(army2) == Army

        while len(army1)>0 and len(army2)>0:
            is_soldier1_won = fight(army1.soldiers[0],army2.soldiers[0])
            if is_soldier1_won:
                army2.soldiers.pop(0)
            else:
                army1.soldiers.pop(0)

        if len(army1)>0:
            return True
        else:
            return False

def fight(soldier1,soldier2):
    assert type(soldier1) in {Warrior,Knight}
    assert type(soldier2) in {Warrior,Knight}

    warriorNextToAttack = 'soldier1'

    roundIndex = 0

    while True:
        roundIndex += 1
        if warriorNextToAttack == 'soldier1':
            damageDealt = soldier1.attack
            soldier2.health -= damageDealt
            warriorNextToAttack = 'soldier2'
            if not soldier2.is_alive:return True
        else:
            damageDealt = soldier2.attack
            soldier1.health -= damageDealt
            warriorNextToAttack = 'soldier1'
            if not soldier1.is_alive: return False

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
