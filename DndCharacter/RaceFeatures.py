import random
featureList = {}


#class Stats: 
 #   {strength: 0,
  #  dex: 0,
   # con: 0,
    #intel: 0,
    #wis: 0,
    #char: 0,
    #}

class RacialFeatures:

    def Human(self):
        raceName = 'Human'
        RaceBonus = {'str': 1, 'dex': 1, 'con': 1, 'int': 1, 'wis': 1, 'char': 1}
        featureList.update(RaceBonus)
        return featureList

feat = RacialFeatures()
print(feat.Human())
print(featureList)