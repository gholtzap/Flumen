from treelib import Node, Tree

# https://treelib.readthedocs.io/en/latest/

# big boys
trees = []
child = 0

def count_child_nodes(tree, parent_id):
    child_count = 0
    for node_id in tree.nodes:
        node = tree.get_node(node_id)
        if node.bpointer == parent_id:
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

# driver 



create_event("Get CA return offer") # ID of this event is 0
create_event("made to be deleted haha")
create_event("Calculate salary")

add_child("Buy parking at Fulton garage",0)
add_child("Cancel OLIV lease",0)
add_child("See if I have to file taxes", 2)

delete_child(0,1)


#delete_child(2,"See if I have to file taxes")

for tree in trees:
    print(trees.index(tree), end=" ")
    print(tree, end="")
 