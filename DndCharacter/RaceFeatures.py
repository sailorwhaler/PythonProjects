import random
featureList = []
testList = []

raceName = ['Human', 'Elf', 'Half-Elf', 'Halfling', 'Tiefling', 'Dragonborn', 'Half-Orc', 'Dwarf', 'Gnome',
        'Orc of Exandria', 'Leonin', 'Satyr', 'Aarakocra', 'Genasi', 'Goliath', 'Aasimar', 'Bugbear', 'Firbolg', 'Goblin',
        'Hobgoblin', 'Kenku', 'Kobold', 'Lizardfolk', 'Orc', 'Tabaxi', 'Triton', 'Yuan-ti Pureblood', 'Feral Tiefling', 
        'Tortle', 'Changeling', 'Kalashtar', 'Orc of Eberron', 'Shifter', 'Warforged', 'Gith', 'Centaur', 'Loxodon', 'Minotaur',
        'Simic Hybrid', 'Vedalken', 'Verdan', 'Locathah', 'Grung']
        
RaceBonus = [{'str': 1, 'dex': 1, 'con': 1, 'int': 1, 'wis': 1, 'char': 1}, {'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'char': 0}, {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'char': 2}, {'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'char': 0},
{'str': 0, 'dex': 0, 'con': 0, 'int': 1, 'wis': 0, 'char': 2}, {'str': 2, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'char': 1}, {'str': 2, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'char': 0}, {'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 0, 'char': 0}, 
{'str': 0, 'dex': 0, 'con': 0, 'int': 2, 'wis': 0, 'char': 0}, {'str': 2, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'char': 0}, {'str': 1, 'dex': 0, 'con': 2, 'int': 0, 'wis': 0, 'char': 0}, {'str': 0, 'dex': 1, 'con': 0, 'int': 0, 'wis': 0, 'char': 2}, 
{'str':0 , 'dex': 2, 'con': 0, 'int': 0, 'wis': 1, 'char': 0}, {'str': 2, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'char': 0}, {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'char': 2}, {'str': 2, 'dex': 1, 'con': 0, 'int': 0, 'wis': 0, 'char': 0},
{'str': 1, 'dex': 0, 'con': 0, 'int': 0, 'wis': 2, 'char': 0}, {'str': 0, 'dex': 2, 'con': 1, 'int': 0, 'wis': 0, 'char': 0}, {'str': 0, 'dex': 0, 'con': 2, 'int': 1, 'wis': 0, 'char': 0}, {'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 1, 'char': 0}, 
{'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'char': 0}, {'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 1, 'char': 0}, {'str': 2, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'char': 0}, {'str': 0, 'dex': 2, 'con': 0, 'int': 0, 'wis': 0, 'char': 1}, 
{'str': 1, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'char': 1}, {'str': 1, 'dex': 0, 'con': 0, 'int': 1, 'wis': 0, 'char': 2}, {'str': 0, 'dex': 2, 'con': 0, 'int': 1, 'wis': 0, 'char': 0}, {'str': 2, 'dex': 0, 'con': 0, 'int': 0, 'wis': 1, 'char': 0}, 
{'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'char': 2}, {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 2, 'char': 1}, {'str': 2, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'char': 0}, {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'char': 0}, 
{'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 0, 'char': 0}, {'str': 0, 'dex': 0, 'con': 0, 'int': 1, 'wis': 0, 'char': 0},{'str': 2, 'dex': 0, 'con': 0, 'int': 0, 'wis': 1, 'char': 0}, {'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 1, 'char': 0}, 
{'str': 2, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'char': 0}, {'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 0, 'char': 0}, {'str': 0, 'dex': 0, 'con': 0, 'int': 2, 'wis': 1, 'char': 0}, {'str': 0, 'dex': 0, 'con': 1, 'int': 0, 'wis': 0, 'char': 2}, 
{'str': 2, 'dex': 1, 'con': 0, 'int': 0, 'wis': 0, 'char': 0}, {'str': 0, 'dex': 2, 'con': 1, 'int': 0, 'wis': 0, 'char': 0}]

class RacialFeatures:

    #A function that creates a string containing race and bonuses for that race to a list: featureList and then prints a random string from said list. 
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

    #A function that pulls from tuples to create a list of races and bonus ability scores which is then randomized.
    def test(self):
        while len(raceName) > 0 and len(RaceBonus) > 0 :
            #testList.append(raceName.pop(-1))
            #testList.append(RaceBonus.pop(-1))
            race = raceName.pop(-1)
            bonus = RaceBonus.pop(-1)
            testList.append(f'You should play a {race}. You will add {bonus} to your ability scores.')
        print(random.choice(testList))
