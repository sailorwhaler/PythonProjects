import random, RaceFeatures

def multiRoll(times, num):
    totalRolls = []
    for i in range(0, times):
        if num <= 120:
            rolls = [random.randint(1, num)]
            for roll in rolls:
                totalRolls.append(roll)
        else:
            print('Please pick a number between 2 and 120.') 
    return totalRolls


class Character:

    def whichRace(self):
        self.allRaces = ['Human', 'Elf', 'Half-Elf', 'Halfling', 'Tiefling', 'Dragonborn', 'Half-Orc', 'Dwarf', 'Gnome',
        'Orc of Exandria', 'Leonin', 'Satyr', 'Aarakocra', 'Genasi', 'Goliath', 'Aasimar', 'Bugbear', 'Firbolg', 'Goblin',
        'Hobgoblin', 'Kenku', 'Kobold', 'Lizardfolk', 'Orc', 'Tabaxi', 'Triton', 'Yuan-ti Pureblood', 'Feral Tiefling', 
        'Tortle', 'Changeling', 'Kalashtar', 'Orc of Eberron', 'Shifter', 'Warforged', 'Gith', 'Centaur', 'Loxodon', 'Minotaur',
        'Simic Hybrid', 'Vedalken', 'Verdan', 'Locathah', 'Grung']
        self.randomRace = random.choice(self.allRaces)
        return self.randomRace

    def whichClass(self):
        self.allClasses = ['Barbarian', 'Bard', 'Warlock', 'Paladin', 'Cleric', 'Ranger', 'Fighter', 'Druid', 'Monk', 'Rogue', 'Sorcerer', 'Wizard', 'Artificer', 'Blood Hunter']
        self.randomClass = random.choice(self.allClasses)
        return self.randomClass

    def abilityScores(self):
        self.abilities = {'Strength': 0, 'Dexterity': 0, 'Constitution': 0, 'Intelligence': 0, 'Wisdom': 0, 'Charisma':0}
        self.newAbilities = {}
        for ability, score  in self.abilities.items():
            self.result = multiRoll(4, 6)
            self.result.sort()
            highestScores = self.result[-3:]
            totalScore = sum(highestScores)
            #return totalScore
            self.abilities.update({ability:totalScore})
            print(f"Your {ability} score is " + str(totalScore))
    
        
    def modifier(self):
        self.abilityScores()
        self.mods = {}
        for ability, score in self.abilities.items():
            scoreSubTen = score - 10
            mod = scoreSubTen / 2 
            remainder = scoreSubTen % 2
            if remainder != 0:
                mod = int(mod - .5)
            else:
                mod = int(mod)
            print(f"The modifier for your {ability} score is {mod}")
            self.mods.update({ability:mod})

    def hitPoints(self):
        HP = self.mods['Constitution'] + 10
        print(f"You should start with {HP} hit points.")

    @property
    def characterSheet(self):
        RaceFeatures.RacialFeatures.match(self)
        self.whichRace()
        #print(f"You should play a(n) {self.randomRace} {self.randomClass}")
        self.modifier()
        self.hitPoints()



newChar = Character()

newChar.characterSheet

