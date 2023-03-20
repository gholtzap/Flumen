from flask import Flask, jsonify, render_template, request, redirect, url_for
from test import trees, create_event_app, add_child_app

app = Flask(__name__)

with open('text_data.txt', 'w') as f:
    f.write('')
    
# visualizes trees in a way that the flask app can print
def to_dict(self):
    return {"name": self.name, "age": self.age}

def get_trees():
    
    tree_list = [tree.to_dict() for tree in trees]
    return jsonify(tree_list)

@app.route('/submit_text', methods=['POST'])
def submit_text():
    text = request.form['textfield']
    create_event_app(text)
    return "Event successfully submitted!"

@app.route('/submit_child', methods=['POST'])
def submit_child():
    nameChild = request.form['nameChild']
    indexParent = int(request.form['indexParent'])
    add_child_app(nameChild, indexParent)
    return "Child successfully submitted!"

@app.route('/')
def index():
    x = get_trees().json
    return render_template('index.html', output=x)

if __name__ == '__main__':
    app.run(debug=True)
