from flask import Flask, jsonify, render_template
from test import trees, add_child

app = Flask(__name__)

# visualizes trees in a way that the flask app can print


def to_dict(self):
    return {"name": self.name, "age": self.age}


def get_trees():
    tree_list = [tree.to_dict() for tree in trees]
    return jsonify(tree_list)

# http://127.0.0.1:5000/ (homepage)


@app.route('/')
def index():
    x = get_trees().json
    return render_template('index.html', output=x)


if __name__ == '__main__':
    app.run(debug=True)
