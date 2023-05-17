
# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, the_damage):
        self.health -= the_damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, the_damage):
        self.health -= the_damage
        if self.health > 0:
            return f"{self.name} has received {the_damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, the_damage):
        self.health -= the_damage
        if self.health > 0:
            return f"A Saxon has received {the_damage} points of damage"
        else:
            return "A Saxon has died in combat"

# War


class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        from random import sample
        saxon_def = sample(self.saxonArmy, 1)[0]
        viking_atk = sample(self.vikingArmy, 1)[0]
        saxon_def.receiveDamage(viking_atk.strength)
        if saxon_def.health <= 0:
            self.saxonArmy.remove(saxon_def)
            return f"A Saxon has died in combat"
        return f"A Saxon has received {viking_atk.strength} points of damage"

    def saxonAttack(self):
        from random import sample
        saxon_atk = sample(self.saxonArmy, 1)[0]
        viking_def = sample(self.vikingArmy, 1)[0]
        viking_def.receiveDamage(saxon_atk.strength)
        if viking_def.health <= 0:
            self.vikingArmy.remove(viking_def)
        return f"{viking_def.name} has received {saxon_atk.strength} points of damage"

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0:
            return "Vikings and Saxons are still in the thick of battle."
