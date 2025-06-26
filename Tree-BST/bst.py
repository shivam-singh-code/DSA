class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None


    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
                   


my_bst = BinarySearchTree()
my_bst.insert(2)
my_bst.insert(1)
my_bst.insert(3)
print("BST root: ",my_bst.root.value)
print("BST left: ",my_bst.root.left.value)
print("BST right: ",my_bst.root.right.value)





