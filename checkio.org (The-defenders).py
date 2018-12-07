class Warrior(object):
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property # it does probably does call the __init__()
    def is_alive(self):
        return self.health > 0

class Defender(Warrior):
    def __init__(self):
        self.health = 60
        self.attack = 3
        self.defense = 2


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
        elif soldierToAdd == Defender:
            for soldierToAdd_i in range(soldierToAdd_amount):
                self.soldiers.append(Defender())

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
    assert type(soldier1) in {Warrior,Knight,Defender}
    assert type(soldier2) in {Warrior,Knight,Defender}


    warriorNextToAttack = 'soldier1'

    roundIndex = 0

    while True:
        roundIndex += 1
        if warriorNextToAttack == 'soldier1':
            damageDealt = soldier1.attack
            try:

                if max(soldier1.attack - soldier2.defense, 0) > 0:
                    soldier2.health -= damageDealt - soldier2.defense
                else:
                    print("NIE MA")

            except:
                soldier2.health -= damageDealt
            warriorNextToAttack = 'soldier2'
            if not soldier2.is_alive:return True
        else:
            damageDealt = soldier2.attack
            try:
                if max(soldier2.attack - soldier1.defense, 0) > 0:
                    soldier1.health -= damageDealt - soldier1.defense
                else:
                    print("NIE MA")
            except:
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
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
