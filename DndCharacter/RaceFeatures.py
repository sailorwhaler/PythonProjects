import random
featureList = []


raceName = ('Human', 'Elf', 'Half-Elf', 'Halfling', 'Tiefling', 'Dragonborn', 'Half-Orc', 'Dwarf', 'Gnome')
RaceBonus = ({'str': 1, 'dex': 1, 'con': 1, 'int': 1, 'wis': 1, 'char': 1}, {'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'char': 0}, {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'char': 2}, {'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'char': 0},
{'str': 0, 'dex': 0, 'con': 0, 'int': 1, 'wis': 0, 'char': 2}, {'str': 2, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'char': 1}, {'str': 2, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'char': 0}, {'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 0, 'char': 0}, 
{'str': 0, 'dex': 0, 'con': 0, 'int': 2, 'wis': 0, 'char': 0})

class RacialFeatures:

    def match(self):
        #Add Humans with ability modifiers for that race
        race = 'Human'
        bonus = 'str: 1, dex: 1, con: 1, int: 1, wis: 1, char: 1'
        featureList.append(f'You should play a {race}. You will add {bonus} to your ability scores.')

        #Add Elfs with ability modifiers for that race
        race = "Elf"
        bonus = 'str: 0, dex: 2, con: 0, int: 0, wis: 0, char: 0'
        featureList.append(f'You should play an {race}. You will add {bonus} to your ability scores.')

        #Add Half-elfs with ability modifiers for that race
        race = 'Half Elf'
        bonus = 'str: 0, dex: 0, con: 0, int: 0, wis: 0, char: 2'
        featureList.append(f'You should play a {race}. You will add {bonus} to your ability scores, and 1 to any other 2 ability scores.')

        #Add Halflings with ability modifiers for that race
        race = "Halfling"
        bonus = 'str: 0, dex: 2, con: 0, int: 0, wis: 0, char: 0'
        featureList.append(f'You should play a {race}. You will add {bonus} to your ability scores.')

        #Add Tieflings with ability modifiers for that race
        race = "Tiefling"
        bonus = 'str: 0, dex: 0, con: 0, int: 1, wis: 0, char: 2'
        featureList.append(f'You should play a {race}. You will add {bonus} to your ability scores.')

        #Add Dragonborn with ability modifiers for that race
        race = "Dragonborn"
        bonus = 'str: 2, dex: 0, con: 0, int: 0, wis: 0, char: 1'
        featureList.append(f'You should play a {race}. You will add {bonus} to your ability scores.')

        #Add Half-orcs with ability modifiers for that race
        race = 'Half Orc'
        bonus = 'str: 2, dex: 0, con: 1, int: 0, wis: 0, char: 0'
        featureList.append(f'You should play a {race}. You will add {bonus} to your ability scores.')

        #Add Dwarves with ability modifiers for that race
        race = 'Dwarf'
        bonus = 'str: 0, dex: 0, con: 2, int: 0, wis: 0, char: 0'
        featureList.append(f'You should play a {race}. You will add {bonus} to your ability scores.')

        #Add Gnomes with ability modifiers for that race
        race = "Gnome"
        bonus = 'str: 0, dex: 0, con: 0, int: 2, wis: 0, char: 0'
        featureList.append(f'You should play a {race}. You will add {bonus} to your ability scores.')
        print(random.choice(featureList))
