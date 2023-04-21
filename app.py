from flask import Flask, jsonify, render_template, request
from tree_mod import trees, add_child, create_event_app, delete_parent, delete_child, count_child_nodes, count_parent_nodes

app = Flask(__name__)

with open('text_data.txt', 'w') as f:
    f.write('')


# visualizes trees in a way that the flask app can print
def to_dict(self):
    return {"name": self.name, "age": self.age}

def get_trees():
    tree_list = [tree.to_dict() for tree in trees]
    return jsonify(tree_list)

# parses through JSON object and returns list of children/parents/etc
def vis_trees(json_object, return_type):
    full, parents, children = "","",""
    
    print("json_object:", json_object) 
    
    for item in json_object:
        
        if isinstance(item, dict):
            parent = list(item.keys())[0]
            child_data = item[parent]
        elif isinstance(item, str):
            parent = item
            child_data = {}
        else:
            continue

        full += f"\n{parent}"
        parents += f"\n{parent}"

        if 'children' in child_data:
            for child in child_data['children']:
                full += f"\n\t{child}"
                children += f"\n{child}"
            
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
    
    childName = request.form['nameChild']
    parentIndex = request.form['indexParent']
    
    if childName == '' or parentIndex == '' or not parentIndex.isnumeric():
        return "Please provide valid input for both fields: (str) , (int)"
    elif (int(parentIndex) > count_parent_nodes()):
        return "Parent index does not exist"
    
    nameChild = request.form['nameChild']
    indexParent = int(request.form['indexParent'])
    add_child(nameChild, indexParent)
    return "Child successfully submitted!"

@app.route('/delete_parent', methods=['POST'])
def delete_event_route():
    
    if request.form['nameParent'] == '' or not request.form['nameParent'].isnumeric():
        return "Please provide valid input: (int)"
    
    index = int(request.form['nameParent'])
    delete_parent(index)
    return "Event successfully deleted!"

@app.route('/delete_child', methods=['POST'])
def delete_child_route():
    print("################################")
    print(request.form['indexParent'])
    print(request.form['indexParent'].isnumeric())
    
    print(request.form['indexChild'])
    print(request.form['indexChild'].isnumeric())
    
    if request.form['indexParent'] == '' or not request.form['indexParent'].isnumeric() or request.form['indexChild'] == '' or not request.form['indexChild'].isnumeric():
        return "Please provide valid input: (int) (int)"
    
    index_parent = int(request.form['indexParent'])
    index_child = int(request.form['indexChild'])
    delete_child(index_parent, index_child)
    return "Event successfully deleted!"

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