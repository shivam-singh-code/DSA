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


    def contain(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
   
    def __r_contains(self, current_node, value):
        if current_node.value == None:
            return False
       
        if value == current_node.value:
            return True
       
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
       
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
       


    def r_contains(self, value):
        return self.__r_contains(self.root, value)
   
    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)
   
    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node


my_bst = BinarySearchTree()
# my_bst.insert(47)
# my_bst.insert(21)
# my_bst.insert(76)
# my_bst.insert(18)
# my_bst.insert(27)
# my_bst.insert(52)
# my_bst.insert(82)


# print("BST contains 27:")
# print(my_bst.contain(27))


# print("BST contains 17:")
# print(my_bst.contain(17))


my_bst.r_insert(2)
my_bst.r_insert(1)
my_bst.r_insert(3)


print("--Printing result value now")
print('Root: value', my_bst.root.value)
print('Root left: ', my_bst.root.left.value)
print('Root right: ', my_bst.root.right.value)

