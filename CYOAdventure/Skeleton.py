from Node import Node

StoryRoot = Node('''
To start things off, are you at a:
    1 - Forest
    2 - Beach
''')

ForestAEnd = Node('''
    You open the door and see nobody inside. 'I could live here' you think stepping inside.
    There's everything you need already and you could make a little garden in the back. 
    Finally away from everyone else.
    
    THE END
''')

ForestBEnd = Node('''
    Deciding instead that it's better to return home. You don't want to be outside when sun sets.
    You manage to follow the path back to the station and make it safely to your bed.

    THE END
''')

forest = Node('''
    You find yourself at the start of a forest path, do you:
    1 - Follow it
    2 - Turn around
''')

forestA = Node('''
    You've been down this particular trail before but something seems different this time. 
    The wildlife is more lively than usual, and there are sounds you swear you've never heard before.
    One decidedly unusual sound rings out, do you:
    1 - Stop to see what made it
    2 - Run further down the path
''')

forestA1 = Node('''
    You pause and look around for the source of the sound. On a nearby rock, there's a brightly colored
    lizard. You've never seen this type of animal before. It licks one eye and stares at you; it looks friendly.
    Do you:
    1 - Approach it
    2 - Ignore it and follow the path
''')

forestA1a = Node('''
    Stepping forward, the lizard makes that horrendous sound again. Something that small should not make a noise that fearsome.
    But it looks amicable enough and it definitely isn't big enough to eat you. It makes a motion as if it wants you to follow it.
    Do you?
    1 - Yes
    2 - No
''')

forestAa1 = Node('''
    You take a step towards the tiny creature and it starts moving away. Deciding to go along with it, you urge it ahead.
    Soon you're standing in front of a small cabin, the lizard on the wall underneath a small window. It looks well taken care of.
    Do you try to open the door?
    1 - Yes
    2 - No
''')

forestA2 = Node('''
    'Nope, not gonna get eaten today' you think and sprint further down the trail. The noise slowly disappears behind you.
    However, the vegetation now seems enourmous. You think you can barely make out a clearing up ahead.
    Do you:
    1 - Keep moving towards it
    2 - Look at the trees
''')

forestA2a = Node('''
    You carefully plot your course through the gigantic roots, making sure to not trip. There is absolutely a clearing ahead.
    Rounding the last massive tree you see a tiny cabin. Isolated but it looks well maintained, do you:
    1 - Approach the door and open it
    2 - Turn around and leave
''')

forestA2b = Node('''
    These things are HUGE!! Easily big enough that someone could live in one. You start picking your way through them one by one, running
    a hand over the trunks until you're engulfed by not only them but equally huge ferns. You need to find the trail again. Do you turn:
    1 - Left
    2 - Right 
''')

forestA2b1 = Node('''
    'Yup this is definitely the right way' you think as the ferns recede, leaving only the massive trees. Pretty soon you're back where you 
    started. Sure that there's a clearing ahead. Will curiosity get the better of you?
    1 - Yes, approach the clearing
    2 - Nah, better to leave
''')

forestA2b2 = Node('''
    'Okay this isn't right' you think as the trees get bigger and the ferns start to canopy your body. 
    Soon it's dark out and the noises are getting louder. Rustling starts to creep up on you. Soon it's 
    closer than you expect. 

    THE END
''')

Beach = Node('''
    
''')

BeachEndA = Node('''

''')

BeachEndB = Node('''

''')


StoryRoot.add_child(forest)
StoryRoot.add_child(Beach)

forest.add_child(forestA)
forest.add_child(ForestBEnd)

forestA.add_child(forestA1)
forestA.add_child(forestA2)

forestA1.add_child(forestA1a)
forestA1.add_child(forestA2)

forestA1a.add_child(forestAa1)
forestA1a.add_child(ForestBEnd)
forestAa1.add_child(ForestAEnd)
forestAa1.add_child(ForestBEnd)

forestA2.add_child(forestA2a)
forestA2.add_child(forestA2b)
forestA2a.add_child(ForestAEnd)
forestA2a.add_child(ForestBEnd)
forestA2b.add_child(forestA2b1)
forestA2b.add_child(forestA2b2)

forestA2b1.add_child(forestA2a)
forestA2b1.add_child(ForestBEnd)

Beach.add_child()
Beach.add_child()


StoryRoot.TellAStory