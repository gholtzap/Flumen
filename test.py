from treelib import Node, Tree

# https://treelib.readthedocs.io/en/latest/

# big boys
trees = []

# creates a parent node

def create_event(value):
    tree = Tree()
    tree.create_node(value,len(trees))
    trees.append(tree)
    return tree

# creates a child node
def add_child(value, p):
    trees[p].create_node(value, len(trees[p])+100, parent=p)

def delete_parent(value):
  trees.pop(value)
    

# driver 

create_event("Get CA return offer") # ID of this event is 0
create_event("made to be deleted haha")
create_event("Calculate salary")



add_child("Buy parking at Fulton garage",0)
add_child("Cancel OLIV lease",0)
add_child("See if I have to file taxes", 2)


#delete_parent(1)
#delete_parent(1)

for tree in trees:
    print(trees.index(tree), end=" ")
    print(tree, end="")
 