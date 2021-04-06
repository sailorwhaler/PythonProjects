import random
featureList = []

raceName = ['Human', 'Elf', 'Half-Elf', 'Halfling', 'Tiefling', 'Dragonborn', 'Half-Orc', 'Dwarf', 'Gnome',
        'Orc of Exandria', 'Leonin', 'Satyr', 'Aarakocra', 'Genasi', 'Goliath', 'Aasimar', 'Bugbear', 'Firbolg', 'Goblin',
        'Hobgoblin', 'Kenku', 'Kobold', 'Lizardfolk', 'Orc', 'Tabaxi', 'Triton', 'Yuan-ti Pureblood', 'Feral Tiefling', 
        'Tortle', 'Changeling', 'Kalashtar', 'Orc of Eberron', 'Shifter', 'Warforged', 'Gith', 'Centaur', 'Loxodon', 'Minotaur',
        'Simic Hybrid', 'Vedalken', 'Verdan', 'Locathah', 'Grung']
        
Bonuses = ['Str: 1 dex: 1 con: 1 int: 1 wis: 1 char: 1', 'Str: 0 dex: 2 con: 0 int: 0 wis: 0 char: 0', 'Str: 0 dex: 0 con: 0 int: 0 wis: 0 char: 2 and 1 to any other 2 abilities', 'Str: 0 dex: 2 con: 0 int: 0 wis: 0 char: 0', 
        'Str: 0 dex: 0 con: 0 int: 1 wis: 0 char: 2', 'Str: 2 dex: 0 con: 0 int: 0 wis: 0 char: 1', 'Str: 2 dex: 0 con: 1 int: 0 wis: 0 char: 0', 'Str: 0 dex: 0 con: 2 int: 0 wis: 0 char: 0', 'Str: 0 dex: 0 con: 0 int: 2 wis: 0 char: 0',
        'Str: 2 dex: 0 con: 1 int: 0 wis: 0 char: 0', 'Str: 1 dex: 0 con: 2 int: 0 wis: 0 char: 0', 'Str: 0 dex: 1 con: 0 int: 0 wis: 0 char: 2', 'Str: 0 dex: 2 con: 0 int: 0 wis: 1 char: 0', 'Str: 0 dex: 0 con: 2 int: 0 wis: 0 char: 0', 
        'Str: 2 dex: 0 con: 1 int: 0 wis: 0 char: 0', 'Str: 0 dex: 0 con: 0 int: 0 wis: 0 char: 2', 'Str: 2 dex: 1 con: 0 int: 0 wis: 0 char: 0', 'Str: 1 dex: 0 con: 0 int: 0 wis: 2 char: 0', 'Str: 0 dex: 2 con: 1 int: 0 wis: 0 char: 0', 
        'Str: 0 dex: 0 con: 2 int: 1 wis: 0 char: 0', 'Str: 0 dex: 2 con: 0 int: 0 wis: 1 char: 0', 'Str: 0 dex: 2 con: 0 int: 0 wis: 0 char: 0', 'Str: 0 dex: 0 con: 2 int: 0 wis: 1 char: 0', 'Str: 2 dex: 0 con: 1 int: 0 wis: 0 char: 0', 
        'Str: 0 dex: 2 con: 0 int: 0 wis: 0 char: 1', 'Str: 1 dex: 0 con: 1 int: 0 wis: 0 char:1', 'Str:0 dex:0 con:0 int:1 wis:0 char:2', 'Str:0 dex:2 con:0 int:1 wis:0 char:0', 'Str:2 dex:0 con:0 int:0 wis:1 char:0', 
        'Str: 0 dex: 0 con: 0 int: 0 wis: 0 char: 2 and 1 to any other ability', 'Str: 0 dex: 0 con: 0 int: 0 wis: 2 char: 1', 'Str: 2 dex: 0 con: 1 int: 0 wis: 0 char: 0', 'Str: 0 dex: 0 con: 0 int: 0 wis: 0 char: 0', 
        'Str: 0 dex:0 con:2 int:0 wis:0 char:0 and 1 to any other ability', 'Str: 0 dex: 0 con: 0 int: 1 wis: 0 char: 0', 'Str: 2 dex: 0 con: 0 int: 0 wis: 1 char: 0', 'Str: 0 dex: 0 con: 2 int: 0 wis: 1 char: 0', 
        'Str: 2 dex: 0 con: 1 int: 0 wis: 0 char: 0', 'Str: 0 dex: 0 con: 2 int: 0 wis: 0 char:0 and 1 to any other ability', 'Str: 0 dex: 0 con: 0 int: 2 wis: 1 char: 0', 'Str: 0 dex: 0 con: 1 int: 0 wis: 0 char: 2', 
        'Str: 2 dex: 1 con: 0 int: 0 wis: 0 char: 0', 'Str: 0 dex: 2 con: 1 int: 0 wis: 0 char: 0']

HasDarkvision = ['Elf', 'Half-Elf', 'Tiefling', 'Half-Orc', 'Dwarf', 'Gnome', 'Orc of Exandria', 'Leonin', 'Aasimar', 'Bugbear', 'Goblin'
        'Hobgoblin', 'Kobold', 'Orc', 'Tabaxi', 'Yuan-Ti Pureblood', 'Feral Tiefling', 'Orc of Eberron', 'Shifter', 'Simic Hybrid']

class RacialFeatures:

    #A function that pulls from tuples to create a list of races and bonus ability scores which is then randomized.
    def attributes(self):
        while len(raceName) > 0 and len(Bonuses) > 0 :
            race = raceName.pop(-1)
            bonus = Bonuses.pop(-1)
            if race == 'Grung' or race == 'Dwarf' or race == 'Gnome' or race == 'Aarakocra':
                speed = 25
            elif race == 'Centaur':
                speed = 40
            else:
                speed = 30
            featureList.append(f'You should play a(n) {race}. You will add {bonus} to your ability scores. Your movement speed will be {speed}.')
        self.choice = random.choice(featureList)
        print(self.choice)

    def darkvision(self):
       pass
    
feat = RacialFeatures()
feat.darkvision()
