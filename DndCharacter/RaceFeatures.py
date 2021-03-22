import random
featureList = {}


raceName = ('Human', 'Elf', 'Half-Elf', 'Halfling', 'Tiefling', 'Dragonborn', 'Half-Orc', 'Dwarf', 'Gnome')
RaceBonus = ({'str': 1, 'dex': 1, 'con': 1, 'int': 1, 'wis': 1, 'char': 1}, {'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'char': 0}, {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'char': 2}, {'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'char': 0},
{'str': 0, 'dex': 0, 'con': 0, 'int': 1, 'wis': 0, 'char': 2}, {'str': 2, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'char': 1}, {'str': 2, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'char': 0}, {'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 0, 'char': 0}, 
{'str': 0, 'dex': 0, 'con': 0, 'int': 2, 'wis': 0, 'char': 0})

class RacialFeatures:
        
    def match(self):
        raceName = ['Human', 'Elf', 'Half-Elf', 'Halfling', 'Tiefling', 'Dragonborn', 'Half-Orc', 'Dwarf', 'Gnome']
        RaceBonus = [{'str': 1, 'dex': 1, 'con': 1, 'int': 1, 'wis': 1, 'char': 1}, {'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'char': 0}, {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'char': 2}, {'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'char': 0},
        {'str': 0, 'dex': 0, 'con': 0, 'int': 1, 'wis': 0, 'char': 2}, {'str': 2, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'char': 1}, {'str': 2, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'char': 0}, {'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 0, 'char': 0}, 
        {'str': 0, 'dex': 0, 'con': 0, 'int': 2, 'wis': 0, 'char': 0}]
        i = 0
        for name in raceName:
            match = [raceName[i], RaceBonus[i]]
            i += 1
            return match
        print(random.choice(match))

    def Human(self):
        raceName = 'Human'
        RaceBonus.update({'str': 1, 'dex': 1, 'con': 1, 'int': 1, 'wis': 1, 'char': 1})
        featureList.update(RaceBonus)
        return f'You should play a {raceName}. You will add {RaceBonus} to your ability scores.'

    def Elf(self):
        raceName = "Elf"
        RaceBonus.update({'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'char': 0})
        featureList.update(RaceBonus)
        return f'You should play an {raceName}. You will add {RaceBonus} to your ability scores.'

    def HalfElf(self):
        raceName = 'Half Elf'
        RaceBonus.update({'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'char': 2})
        featureList.update(RaceBonus)
        return f'You should play a {raceName}. You will add {RaceBonus} to your ability scores, and 1 to any other 2 ability scores.'

    def Halfling(self):
        raceName = "Halfling"
        RaceBonus.update({'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'char': 0})
        featureList.update(RaceBonus)
        return f'You should play a {raceName}. You will add {RaceBonus} to your ability scores.'

    def Tiefling(self):
        raceName = "Tiefling"
        RaceBonus.update({'str': 0, 'dex': 0, 'con': 0, 'int': 1, 'wis': 0, 'char': 2})
        featureList.update(RaceBonus)
        return f'You should play a {raceName}. You will add {RaceBonus} to your ability scores.'

    def Dragonborn(self):
        raceName = "Dragonborn"
        RaceBonus.update({'str': 2, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'char': 1})
        featureList.update(RaceBonus)
        return f'You should play a {raceName}. You will add {RaceBonus} to your ability scores.'

    def HalfOrc(self):
        raceName = 'Half Orc'
        RaceBonus.update({'str': 2, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'char': 0})
        featureList.update(RaceBonus)
        return f'You should play a {raceName}. You will add {RaceBonus} to your ability scores.'

    def Dwarf(self):
        raceName = 'Dwarf'
        RaceBonus.update({'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 0, 'char': 0})
        featureList.update(RaceBonus)
        return f'You should play a {raceName}. You will add {RaceBonus} to your ability scores.'

    def Gnome(self):
        raceName = "Gnome"
        RaceBonus.update({'str': 0, 'dex': 0, 'con': 0, 'int': 2, 'wis': 0, 'char': 0})
        featureList.update(RaceBonus)
        return f'You should play a {raceName}. You will add {RaceBonus} to your ability scores.'


#Tuples of Races and Ability bonuses matched to race. Could randomize race and pull bonus based on key??
#races = ('Human', 'Elf', 'Half-Elf', 'Halfling', 'Tiefling', 'Dragonborn', 'Half-Orc', 'Dwarf', 'Gnome')
#Bonuses = ({'str': 1, 'dex': 1, 'con': 1, 'int': 1, 'wis': 1, 'char': 1}, {'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'char': 0}, {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'char': 2}, {'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'char': 0},
#{'str': 0, 'dex': 0, 'con': 0, 'int': 1, 'wis': 0, 'char': 2}, {'str': 2, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'char': 1}, {'str': 2, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'char': 0}, {'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 0, 'char': 0}, 
#{'str': 0, 'dex': 0, 'con': 0, 'int': 2, 'wis': 0, 'char': 0})


feat = RacialFeatures()
#print(feat.Human())
#print(featureList)
print(feat.match())