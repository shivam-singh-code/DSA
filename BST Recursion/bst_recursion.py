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
   
    def __delete_node(self, current_node, value):
        if current_node == None:
            return
       
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node
   
    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value


    def delete_node(self, value):
        self.__delete_node(self.root, value)


# my_bst = BinarySearchTree()
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


# my_bst.r_insert(2)
# my_bst.r_insert(1)
# my_bst.r_insert(3)


# print("--Printing result value now")
# print('Root: value', my_bst.root.value)
# print('Root left: ', my_bst.root.left)
# print('Root right: ', my_bst.root.right)


# print(my_bst.min_value(my_bst.root))
# print(my_bst.min_value(my_bst.root.right))
       
my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)


"""
       2
      / \
     1   3
"""


print("root:", my_tree.root.value)
print("root.left =", my_tree.root.left.value)
print("root.right =", my_tree.root.right.value)




my_tree.delete_node(2)


"""
       3
      / \
     1   None
"""




print("\nroot:", my_tree.root.value)
print("root.left =", my_tree.root.left.value)
print("root.right =", my_tree.root.right)






"""
    EXPECTED OUTPUT:
    ----------------
    root: 2
    root.left = 1
    root.right = 3


    root: 3
    root.left = 1
    root.right = None


"""