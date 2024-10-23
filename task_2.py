class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)
    
    def find_maximum(self):
        """
        Знаходить найбільше значення в дереві.
        Повертає None, якщо дерево порожнє.
        """
        if not self.root:
            return None
        
        return self._find_maximum_recursive(self.root)
    
    def _find_maximum_recursive(self, node):
        current = node
        while current.right:
            current = current.right
        return current.key
    
    def find_minimum(self):
        """
        Знаходить найменше значення в дереві.
        Повертає None, якщо дерево порожнє.
        """
        if not self.root:
            return None
        
        return self._find_minimum_recursive(self.root)
    
    def _find_minimum_recursive(self, node):
        # У бінарному дереві пошуку найменше значення 
        # завжди знаходиться в крайньому лівому вузлі
        current = node
        while current.left:
            current = current.left
        return current.key

# Приклад використання:
def test_binary_search_tree():
    bst = BinarySearchTree()
    
    # Додаємо елементи
    values = [15, 10, 20, 8, 12, 17, 25]
    for value in values:
        bst.insert(value)
    
    # Знаходимо максимальне та мінімальне значення
    min_value = bst.find_minimum()
    print(f"Мінімальне значення у дереві: {min_value}")   # Виведе: 8

if __name__ == "__main__":
    test_binary_search_tree()