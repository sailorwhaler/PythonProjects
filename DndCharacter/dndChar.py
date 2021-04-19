import random, RaceFeatures
import tkinter as tk

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

    def whichClass(self):
        self.allClasses = ['Barbarian', 'Bard', 'Warlock', 'Paladin', 'Cleric', 'Ranger', 'Fighter', 'Druid', 'Monk', 'Rogue', 'Sorcerer', 'Wizard', 'Artificer', 'Blood Hunter']
        self.randomClass = random.choice(self.allClasses)
        ClassEnt.insert('0', f'Maybe a {self.randomClass}?')

    def abilityScores(self):
        self.abilities = {'Strength': 0, 'Dexterity': 0, 'Constitution': 0, 'Intelligence': 0, 'Wisdom': 0, 'Charisma':0}
        self.newAbilities = {}
        for ability, score  in self.abilities.items():
            self.result = multiRoll(4, 6)
            self.result.sort()
            highestScores = self.result[-3:]
            totalScore = sum(highestScores)
            self.abilities.update({ability:totalScore})
            EntStats.insert('0', f"Your {ability} score is " + str(totalScore)+". ")
    
        
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
            ScoresEnt.insert('0', f"The modifier for your {ability} score is {mod}. ")
            self.mods.update({ability:mod})

    def hitPoints(self):
        HP = self.mods['Constitution'] + 10
        HPEnt.insert('0', f"You should start with {HP} hit points.")

    @property
    def characterSheet(self):
        RaceEnt.insert('0', f'{RaceFeatures.RacialFeatures.attributes(self)}')
        self.whichClass()
        self.modifier()
        self.hitPoints()
      
def ReRoll(event):
    newChar = Character()
    newChar.characterSheet

def Clear(event):
    RaceEnt.delete('0', tk.END)
    ClassEnt.delete('0', tk.END)
    EntStats.delete('0', tk.END)
    ScoresEnt.delete('0', tk.END)
    HPEnt.delete('0', tk.END)

window = tk.Tk()
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(6, minsize=500, weight=1)
lblFr = tk.Frame(window, bg='red')


lblRace = tk.Label(window, text='Race:')
lblRace.grid(row=0, column=1, sticky='n')
RaceEnt = tk.Entry()
RaceEnt.grid(row=0, column=1,)

lblClass = tk.Label(window, text='Class:')
lblClass.grid(row=0, column=2, sticky='se')
ClassEnt = tk.Entry()
ClassEnt.grid(row=0, column=2)

lblStats = tk.Label(window, text='Stats:')
lblStats.grid(row=0, column=3, sticky='se')
EntStats = tk.Entry()
EntStats.grid(row=0, column=3)

lblScores = tk.Label(window, text='Scores:' )
lblScores.grid(row=0, column=4, sticky='se')
ScoresEnt = tk.Entry()
ScoresEnt.grid(row=0, column=4)

lblHP = tk.Label(window, text='Hit Points:' )
lblHP.grid(row=0, column=5, sticky='w')
HPEnt = tk.Entry()
HPEnt.grid(row=0, column=5)

rollBtn = tk.Button(window, text='Roll me a character')
#againbtn = tk.Button(window, text='Reroll!!')
#againbtn.bind('<Button-2>', Clear)
#againbtn.grid(row=0, column=1, sticky='nsew')
rollBtn.bind('<Button-1>', Clear)
rollBtn.bind('<ButtonRelease>', ReRoll)
rollBtn.grid(row=0, column=0, sticky='nsew')



window.mainloop()
