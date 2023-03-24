from flask import Flask, jsonify, render_template, request, redirect, url_for
from tree_mod import trees, add_child, create_event_app


app = Flask(__name__)

with open('text_data.txt', 'w') as f:
    f.write('')
    
# visualizes trees in a way that the flask app can print
#def to_dict(self):
    #return {"name": self.name, "age": self.age}
    
def to_dict(tree):
    data = {}

    for node in tree.all_nodes_itr():
        if node.is_root():
            data[node.tag] = {"children": []}
        else:
            parent = tree.parent(node.identifier)
            if "children" not in data[parent.tag]:
                data[parent.tag]["children"] = []
            data[parent.tag]["children"].append(node.tag)

    return data

def get_trees():
    
    tree_list = [tree.to_dict() for tree in trees]
    return jsonify(tree_list)

# parses through JSON object and returns list of children/parents/etc
def vis_trees(json_object, return_type):
    full, parents, children = "","",""
    
    for item in json_object:
        for parent, child_data in item.items():
            full+=parent
            parents += parent
            #print("Parent name:",parent)
            
            for child in child_data['children']:
                full+=child
                children += child
                #print("Child name:", child)
    
    match return_type:
        case 1:
            return parents
        case 2:
            return children
        case 3: 
            return full
    return full

@app.route('/submit_text', methods=['POST'])
def submit_text():
    text = request.form['textfield']
    create_event_app(text)
    return "Event successfully submitted!"

@app.route('/submit_child', methods=['POST'])
def submit_child():
    nameChild = request.form['nameChild']
    indexParent = int(request.form['indexParent'])
    add_child(nameChild, indexParent)
    return "Child successfully submitted!"

@app.route('/')
def index():
    raw_json = get_trees().json
    # for the second param:
    # 1 = parents, 2 = children, 3 = full (both parents and children)
    full_tree = vis_trees(raw_json,3)
    parents = vis_trees(raw_json,1)
    children = vis_trees(raw_json,2)
    
    # sending the above variables to index.html
    return render_template('index.html', full_tree=full_tree, parents = parents, children = children)

if __name__ == '__main__':
    app.run(debug=True)