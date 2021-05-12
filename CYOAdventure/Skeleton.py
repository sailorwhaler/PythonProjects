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

forestA2 = Node('''
    'Nope, not gonna get eaten today' you think and sprint further down the trail. The noise slowly disappears behind you.
    However, the vegetation now seems enourmous. You think you can barely make out a clearing up ahead.
    Do you:
    1 - Keep moving towards it
    2 - Look at the trees
''')

forestA1a = Node('''
    Stepping forward, the lizard makes that horrendous sound again. Something that small should not make a noise that fearsome.
    But it looks amicable enough and it definitely isn't big enough to eat you. It makes a motion as if it wants you to follow it.
    Do you?
    1 - Yes
    2 - No
''')



Beach = Node('''

''')


StoryRoot.add_child(forest)
StoryRoot.add_child(Beach)

forest.add_child(forestA)
forest.add_child(ForestBEnd)

forestA.add_child(forestA1)
forestA.add_child(forestA2)

forestA1.add_child(forestA1a)
forestA1.add_child(forestA2)
StoryRoot.TellAStory