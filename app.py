from flask import Flask, jsonify
from test import trees

app = Flask(__name__)


# visualizes trees in a way that the flask app can print
def to_dict(self):
    return {"name": self.name, "age": self.age}
def get_trees():
    tree_list = [tree.to_dict() for tree in trees]
    return jsonify(tree_list)

# http://127.0.0.1:5000/ (homepage)
@app.route('/')
def hello_world():
    return get_trees()

if __name__ == '__main__':
   app.run(debug=True)

