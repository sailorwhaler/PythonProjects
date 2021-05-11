class Node:
    def __init__(self, piece):
        self.piece = piece
        self.choices = []

    def add_child(self, node):
        self.choices.append(node)

    @property
    def TellAStory(self):
        story_node = self
        
        print(story_node.piece)

        while len(story_node.piece) > 0:
            choice = input('Enter 1 or 2 to continue the story: ')
            
            if choice not in ['1', '2']:
                print('Please enter a valid option, either 1 or 2: ')
            else:
                chosen_index = int(choice)
                chosen_index -= 1
                chosen_child = story_node.choices[chosen_index]
                print(chosen_child.piece)
                story_node = chosen_child

