const eventJson = [
    {
        "id": "1",
        "name": "Event 1",
        "children": []
    },
    {
        "id": "2",
        "name": "Event 2",
        "children": [
            {
                "id": "3",
                "name": "Event 3",
                "children": []
            }
        ]
    }
];

function processNode(node, container) {
    const li = document.createElement('li');
    li.textContent = node.name;
    container.appendChild(li);

    if (node.children.length > 0) {
        const ul = document.createElement('ul');
        container.appendChild(ul);

        node.children.forEach(child => {
            processNode(child, ul);
        });
    }
}

const eventList = document.getElementById('event-list');
eventJson.forEach(event => {
    processNode(event, eventList);
});
