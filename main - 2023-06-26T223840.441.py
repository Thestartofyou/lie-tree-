from anytree import Node, RenderTree

truths = Node("Truths")
lies = Node("Lies")
root = Node("Statements", children=[truths, lies])

while True:
    statement = input("Enter a statement (or 'q' to quit): ")

    if statement.lower() == 'q':
        break

    is_true = input("Is the statement true? (y/n): ")

    node = Node(statement, parent=truths if is_true.lower() == 'y' else lies)

print("\nTree Diagram:")
for pre, _, node in RenderTree(root):
    print(f"{pre}{node.name}")

total_statements = len(truths.children) + len(lies.children)
total_truths = len(truths.children)
percentage_success = (total_truths / total_statements) * 100

print(f"\nPercentage of Success: {percentage_success:.2f}%")

