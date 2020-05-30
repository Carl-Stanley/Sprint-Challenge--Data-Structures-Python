# Binary Search tree 
class Binary_st:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    # Insert 
    def insert(self, value):
        def find_insert(current_node, value):
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = Binary_st(value)
                    return
                else:
                    return find_insert(current_node.left, value)
            else:
                if current_node.right is None:
                    current_node.right = Binary_st(value)
                    return
                else:
                    return find_insert(current_node.right, value)

        find_insert(self, value)
    # Check for a value in the tree, if none return false 
    def contains(self, target):
        def search(current_node, target):
            if current_node.value == target:
                return True
            if target < current_node.value:
                if current_node.left is not None:
                    return search(current_node.left, target)
            if target >= current_node.value:
                if current_node.right is not None:
                    return search(current_node.right, target)
            # If not then false. 
            return False
        
        return search(self, target)
     