import Node

StoryRoot = Node.Node('''
To start things off, are you in a:
1 - Forest
2 - Beach
''')

Forest = Node.Node('''
Forest
''')

Beach = Node.Node('''
Beach
''')


StoryRoot.add_child(Forest)
StoryRoot.add_child(Beach)
StoryRoot.TellAStory