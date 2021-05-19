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
        CharTxt.insert(tk.END, f'\n Maybe a {self.randomClass}?')

    def abilityScores(self):
        self.abilities = {'Strength': 0, 'Dexterity': 0, 'Constitution': 0, 'Intelligence': 0, 'Wisdom': 0, 'Charisma':0}
        self.newAbilities = {}
        for ability, score  in self.abilities.items():
            self.result = multiRoll(4, 6)
            self.result.sort()
            highestScores = self.result[-3:]
            totalScore = sum(highestScores)
            self.abilities.update({ability:totalScore})
            CharTxt.insert(tk.END, f"\n Your {ability} score is " + str(totalScore)+". ")
    
        
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
            CharTxt.insert(tk.END, f"\n The modifier for your {ability} score is {mod}. ")
            self.mods.update({ability:mod})

    def hitPoints(self):
        HP = self.mods['Constitution'] + 10
        CharTxt.insert(tk.END, f"\n You should start with {HP} hit points.")

    @property
    def characterSheet(self):
        CharTxt.insert('1.0', f'{RaceFeatures.RacialFeatures.attributes(self)}')
        self.whichClass()
        self.modifier()
        self.hitPoints()
      
def ReRoll(event):
    newChar = Character()
    newChar.characterSheet

def Clear(event):
    CharTxt.delete('1.0', tk.END)

window = tk.Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.title('Who\'s my Character?')

lblFr = tk.Frame(master=window)
lblFr.grid(row=0, column=1, sticky='w')

TxtFr = tk.Frame(window)
TxtFr.grid(row=0, column=1, sticky='e')

lblRace = tk.Label(lblFr, text="")
lblRace.grid(row=0, column=1)

#lblClass = tk.Label(lblFr, text='Class:')
#lblClass.grid(row=1, column=1)
CharTxt = tk.Text(TxtFr)
CharTxt.grid(row=1, column=1)

#lblStats = tk.Label(lblFr, text='Stats:')
#lblStats.grid(row=2, column=1)
#ClassTxt = tk.Entry(EntFr)
#EntTxt.grid(row=2, column=1)

#lblScores = tk.Label(lblFr, text='Scores:' )
#lblScores.grid(row=3, column=1)
#ScoresEnt = tk.Entry(EntFr)
#ScoresEnt.grid(row=3, column=1)

#lblHP = tk.Label(lblFr, text='Hit Points:' )
#lblHP.grid(row=4, column=1)
#HPEnt = tk.Entry(EntFr)
#HPEnt.grid(row=4, column=1)

rollBtn = tk.Button(window, text='Roll me a character')
rollBtn.bind('<Button>',  Clear)
rollBtn.bind('<ButtonRelease>', ReRoll)
rollBtn.grid(row=0, column=0, sticky='nsew')



window.mainloop()
