from treelib import Node, Tree

# https://treelib.readthedocs.io/en/latest/

# big boys
trees = []

def count_child_nodes(tree, parent_id):
    child_count = 0
    for node_id in tree.nodes:
        node = tree.get_node(node_id)
        if node.predecessor(tree.identifier) == parent_id:
            child_count += 1
    return child_count

def create_event(value):
    tree = Tree()
    tree.create_node(value,len(trees))
    trees.append(tree)
    return tree

def add_child(value, p):
    x = count_child_nodes(trees[p], p)
    trees[p].create_node(value, 100+x, parent=p)
    
def delete_parent(value):
  trees.pop(value)

def delete_child(value, id):
    trees[value].remove_node(id+100)

# reads text from text_data.py and stores it as a variable
# TO DO : use this text to call the add event function
#       end goal: the user can type text into the site's form and the tree changes based on what they type
def read_text_from_file(file_path):
    with open(file_path, 'r') as f:
        text_data = f.read()
    return text_data




file_path = 'text_data.txt'
text_data = read_text_from_file(file_path)


def create_event_app(value):
    create_event(value)
    
# Now you can use the `text_data` variable in your program as needed
print(text_data)

# driver 

#create_event(text_data) # ID of this event is 0

#create_event("Get CA return offer") 
#create_event("made to be del   eted haha")
#create_event("Calculate salary")

#add_child("Buy parking at Fulton garage",0)
#add_child("Cancel OLIV lease",0)
#add_child("See if I have to file taxes", 2)

#delete_child(0,1)

for tree in trees:
    print(trees.index(tree), end=" ")
    print(tree, end="")
 