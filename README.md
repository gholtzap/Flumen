## Flumen - Todo List with Conditional Events
Flumen is a Python Flask app for creating and managing a to-do list with conditional events, implemented with the use of tree data structures. You can add parents, children, and delete nodes as needed.

### Features
- Create a to-do event (parent node)<br>
- Add child events (child nodes) to existing parent nodes<br>
- Delete parent or child nodes<br>
- Visualize the to-do list as a tree structure<br>

### Usage
Flumen provides an interface for managing the to-do list:

- To create a new to-do event (parent node), enter the event's name in the "Create Event" field and click "Submit".<br>
- To add a child event (child node) to an existing parent node, enter the child's name and the parent's index in the "Add Child" section and click "Submit".<br>
- To delete a parent node, enter its index in the "Delete Event" section and click "Submit".<br>
- To delete a child node, enter its parent's index and its index in the "Delete Child" section and click "Submit".<br>
- Flumen will display the to-do list as a tree structure, showing parent nodes and their child nodes.
