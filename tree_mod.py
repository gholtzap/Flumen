from treelib import Tree

# https://treelib.readthedocs.io/en/latest/

trees = []

# #################################################################
# add

def count_child_nodes(tree, parent_id):
    child_count = 0
    for node_id in tree.nodes:
        node = tree.get_node(node_id)
        if node.predecessor(tree.identifier) == parent_id:
            child_count += 1
    return child_count

def count_parent_nodes():
    return len(trees)

def create_event(value):
    tree = Tree()
    tree.create_node(value,len(trees))
    trees.append(tree)
    return tree

def add_child(nameChild, indexParent):
    
    if(indexParent > count_parent_nodes):
        return "Parent Index does not exist"
        
    x = count_child_nodes(trees[indexParent], indexParent)
    trees[indexParent].create_node(nameChild, 100+x, parent=indexParent)
    
def create_event_app(value):
    create_event(value)
    
def add_child_app(value, index):
    add_child(value,int(index))

# #################################################################
# delete

def delete_parent(value):
  trees.pop(value)

def delete_child(value, id):
    trees[value].remove_node(id+100)

def read_text_from_file(file_path):
    with open(file_path, 'r') as f:
        text_data = f.read()
    return text_data

# #################################################################
# misc 
file_path = 'text_data.txt'
text_data = read_text_from_file(file_path)

    
for tree in trees:
    print(trees.index(tree), end=" ")
    print(tree, end="")