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
    You find yourself on a sandy beach, clear blue water stretches out before you. 
    Do you:
    1 - Explore the sand
    2 - Go towards the water
''')

beachA = Node('''
    The sun-soaked sand surrounding you seems inviting. It's just warm enough to not burn your feet. You begin
    walking along the beach, well above the tidal line, scanning ahead for anything interesting. Something glints ahead.
    Do you:
    1 - Go towards it
    2 - Ignore it and keep walking along the beach
''')

beachA1 = Node('''
    You approach the glimmering object and bend down to inspect it. Poking through the warm sand is the tip of a 
    small gem. You kneel down and start to poke around it. To your surprise it's not the only one, just the topmost one.
    Digging your fingers around the gem your eyes are met with more of it's kind and others. There's easily enough here
    to make life easy for you, do you:
    1 - Take as many as possible and leave
    2 - Take a few in your pockets and continue
''')

beachA1End = Node('''
    You shove as many gems as possible into your pockets. Heck you even find pockets you didn't know existed until this 
    moment! There is no way you're leaving this treasure behind! Soon you're laden down and heavy with precious stones.
    Content with your discovery, you begin the trek away from the water. Soon enough you'll find your way back home.

    THE END
''')

beachA1a = Node('''
    'Best to not be greedy' you think and take a few in your pockets, just enough to feel their weight there. There's 
    still plenty there for someone else to discover and enjoy. You keep walking further down the beach and soon discover
    an expanse filled with chairs. Nobody is around as far as you can tell, however there's laughter in the distance, do
    you:
    1 - Investigate the laughter
    2 - Sit in a chair and rest
''')

beachA2 = Node('''
    You figure it's probably just some toy that got dropped by a careless child and continue right on by without another glance.
    The sands seem to go on forever, the sun beating overhead. You finally reach an expanse filled with lounge chairs. You hear
    laughter off in the distance and see tiny cabanas. Do you: 
    1 - Go towards the cabanas
    2 - Settle into a chair
''')

beachA2End = Node('''
    The chairs look so comfortable, and you have been walking for quite some time now. You sit down in one and kick your feet up.
    You suddenly feel so heavy with the sun beating down on you. You feel your eyelids sliding over your eyes. The sounds of the 
    waves lapping the shoreline too inviting. Soon you're sleeping. Or so you think.

    You wake up comfortably in your bed at home. It was a dream all along. 'I really need a vacation' you think as you roll over
    to recapture that pleasant dream.

    THE END
''')

beachA2a = Node('''
    You realize you haven't seen anyone else in days, and the laughter sounds so inviting. Like a group of friends you haven't
    seen in ages. You head towards the sound with a smile on your face. Maybe there will be drinks at one of the cabanas. Sure
    enough when you reach one there's a group of people standing around a bar. One of them smiles at you and waves you over, a 
    drink in hand. What do you do?
    1 - Accept the drink and join the group
    2 - Shake your head and leave
''')

beachA2bEnd = Node('''
    You step up to the group and accept the drink offered. It smells crisp and everyone starts talking to you like they
    haven't seen you in ages. You feel like you've known these people for all of your life, you realize that you have
    actually! How funny to stumble upon them all in some scenic oceanside vista in the middle of nowhere. You take a 
    sip and catch up with your old friends as the sun begins to set in the distance.

    THE END
''')

beachA2b = Node('''
    'This is just too weird' you think as you shake your head, realizing that you don't recognize a single face in 
    the crowd of people. It would be better to just leave now. You turn around and start to follow the footprints
    you had left in the sand. Soon you're back where there are no footprints. 
''')


beachB = Node('''
    'There's never anything in the sand' you think and head towards the cool blue water. You reach the waves and let them lap 
    up to your toes. It's not incredibly cold but the sun is starting to get pretty warm on your back, what do you do?
    1 - Get in the water
    2 - Continue walking in the water
''')

beachB1 = Node('''
    The water is actually really refreshing; it's not too cold but not warm either. You start to swim out further from the shore.
    Soon you're up to your chest in the clear blue waves. You can see some of the oceanlife beneath you. Nothing seems too big or
    frightening. Do you:
    1 - Dive under
    2 - Keep swimming
''')

beachB1a = Node('''
    You take a deep breath in and hold it, pushing your way down under the ocean. You push your eyes open and take in your surroundings.
    Everything is so vibrant. Little fish dart around nearby, some close enough that you can feel them. You turn your whole body and pull
    your arms away from yourself, dragging them through the water. Soon your  near the bottom. It's odd, you don't feel like you need to 
    stop and break the surface for air. Do you:
    1 - Test the theory and let the air out
    2 - Resurface
''')

beachB1Endb = Node('''
    You slowly let all of the air out of your lungs and wait. And wait. There's no burn, no screaming pain from your chest begginging you
    to take another breath. 'That's odd' you think with a shrug. But the water is warm enough, and it's kind of pleasant to be able to 
    flit around without a care. You could stay down here, maybe make friends with the various aquatic life. That doesn't sound too bad right?
    You swim down further, farther from the shoreline, basking in your newfound ability. Yeah...this could be fun.

    THE END
''')

beachB1Enda = Node('''
    It took days to get your hair to sit right and you know if you get it wet it's only going to take even longer to fix with the 
    possible salt in it. You wade out farther from the shoreline instead. Soon you're surrounded by nothing but the clear surface of 
    the water, the waves becoming smaller and smaller the further you swim out. You can't see the shore anymore; can't tell which way to
    go if you wanted to get back. Hopefully a boat passes by or you'll be well and truly stranded here.

    THE END
''')

beachB1Endc = Node('''
    Even though it feels like you could stay underwater for ages the thought unnerves you and you propel yourself towards the surface as
    fast as you possibly can. You break through the crest of a wave. 'That was weird' you think, shaking your hair and wiping the water
    from your eyes. You think you can see the shoreline from here, you didn't go out too far after all. You start swimming back towards
    it, the sun setting behind the horizon. Maybe you'll come back to explore the sensation later. Maybe you'll just let it stay here
    underneath the waves.

    THE END
''')

beachB2 = Node('''
    You may be warm but you're not warm enough to get in the depths. 'No thank you, there could be anything out there' you think
    as you step along the edge of the water. You walk for what seems like forever, nothing really changing. Soon the sun begins to
    sink behind the horizon. Do you:
    1 - Turn around
    2 - Keep walking
''')

beachB2Enda = Node('''
    You decide it's best to leave with the sun setting. Chances are good that nothing is out here that could cause you harm, however
    you have no shelter and don't know how much the temperature will drop overnight. 'I'll come back when the sun is up' you think as 
    you turn around. You can find the place again easily enough.

    THE END
''')

beachB2a = Node('''
    'It can't get that cold out here at night' you think as you keep walking along the water. Soon the sun has completely set and the
    stars have made their appearances. There isn't much to see anymore, but the moon is huge above you lending its light to allow you 
    to continue your journey. You hear splashing next to you and look out to the sea. There in the waves is an odd shape, it looks almost
    like a person. Do you:
    1 - Call out to it
    2 - Turn around and leave
''')

beachB2Endb = Node('''
    'If it's a person, maybe they know where we are!' you think as you call out the figure. It waves at you and motions for you to come towards
    it. You pause for a minute. Why wouldn't it just move towards you. That water must be freezing cold by now. But your doubts are pushed aside 
    as the figure starts to approach. You can make out the familiar shape of another person - arms, torso, a smiling face - all by the moonlight.
    But something seems different. You find yourself slowly going into the water. It's much colder than you thought it would be. Soon you're being
    wrapped up by this other person. 'This isn't right' you think as you're pulled away from the shoreline with a strange forcefulness. 

    Soon the light from the moon isn't visible anymore. The things arms are tight around your body. Your lungs burn for air. There was a reason you
    were afraid of the water.

    THE END
''')

beachB2EndC = Node('''
    'Nope, that is bait' you think and turn around. The sun has set and NOTHING good can be out in the water right now. You haven't seen a single
    other person this whole time but now suddenly there's someone, something splashing around. You haven't managed to keep yourself alive this
    long without some caution. You hear the sound of it splashing more furiously than before as your footsteps take you farther and farther away
    from the water. 'Definitely made the right choice' you think as you soon find yourself back where you began. 'I'm going home'

    You plod your way over the sand. Just wanting to put more distance between yourself and that creature. You'll be back home soon.

    THE END
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

Beach.add_child(beachA)
Beach.add_child(beachB)

beachA.add_child(beachA1)
beachA.add_child(beachA2)

beachA1.add_child(beachA1End)
beachA1.add_child(beachA1a)

beachA1a.add_child(beachA2a)
beachA1a.add_child(beachA2End)

beachA2.add_child(beachA2a)
beachA2.add_child(beachA2End)

beachA2a.add_child(beachA2bEnd)
beachA2a.add_child(Beach)

beachB.add_child(beachB1)
beachB.add_child(beachB2)

beachB1.add_child(beachB1a)
beachB1.add_child(beachB1Enda)

beachB1a.add_child(beachB1Endb)
beachB1a.add_child(beachB1Endc)

beachB2.add_child(beachB2Enda)
beachB2.add_child(beachB2a)

beachB2a.add_child(beachB2Endb)
beachB2a.add_child(beachB2EndC)

StoryRoot.TellAStory