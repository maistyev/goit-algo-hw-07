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
        if not self.root:
            return None
        return self._find_maximum_recursive(self.root)
    
    def _find_maximum_recursive(self, node):
        current = node
        while current.right:
            current = current.right
        return current.key
    
    def find_minimum(self):
        if not self.root:
            return None
        return self._find_minimum_recursive(self.root)
    
    def _find_minimum_recursive(self, node):
        current = node
        while current.left:
            current = current.left
        return current.key
    
    def sum_all_values(self):
        """
        Обчислює суму всіх значень у дереві.
        Повертає 0, якщо дерево порожнє.
        """
        if not self.root:
            return 0
        return self._sum_all_values_recursive(self.root)
    
    def _sum_all_values_recursive(self, node):
        """
        Рекурсивно обчислює суму значень у піддереві з коренем node
        """
        if not node:
            return 0
        
        # Сума = значення поточного вузла + сума лівого піддерева + сума правого піддерева
        return node.key + self._sum_all_values_recursive(node.left) + self._sum_all_values_recursive(node.right)
    
    def print_tree(self):
        """
        Виводить дерево в порядку інфіксного обходу (in-order traversal)
        """
        def inorder(node):
            if node:
                inorder(node.left)
                print(node.key, end=' ')
                inorder(node.right)
        
        print("Дерево (in-order):", end=' ')
        inorder(self.root)
        print()

def test_binary_search_tree():
    bst = BinarySearchTree()
    
    # Додаємо елементи
    values = [15, 10, 20, 8, 12, 17, 25]
    for value in values:
        bst.insert(value)
    
    # Виводимо дерево
    bst.print_tree()
    
    # Знаходимо суму всіх значень
    total_sum = bst.sum_all_values()
    print(f"Сума всіх значень у дереві: {total_sum}")

if __name__ == "__main__":
    test_binary_search_tree()