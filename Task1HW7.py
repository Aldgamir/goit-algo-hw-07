import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def plot_tree(node, x, y, spacing=1000):
    if node is not None:
        plt.scatter(x, y)
        plt.text(x, y, str(node.value), verticalalignment='center', horizontalalignment='center')
        if node.left is not None:
            plt.plot([x, x - spacing], [y, y - spacing])
            plot_tree(node.left, x - spacing, y - spacing, spacing / 2)
        if node.right is not None:
            plt.plot([x, x + spacing], [y, y - spacing])
            plot_tree(node.right, x + spacing, y - spacing, spacing / 2)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)
    
    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)
        # Ignore if value is equal to node.value
    
    # Знахожимо максимальне значення
    def find_max(self):
        if self.root is None:
            return None
        current_node = self.root
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.value
    
    # Знаходимо мінімальне значення
    def find_min(self):
        if self.root is None:
            return None
        current_node = self.root
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
    # Знаходимо суму всіх значень
    def tree_sum(self):
        return self._tree_sum_recursive(self.root)

    def _tree_sum_recursive(self, node):
        if node is None:
            return 0
        return node.value + self._tree_sum_recursive(node.left) + self._tree_sum_recursive(node.right)


# Задаємо значення для візулізації графіка
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

plot_tree(root, 0, 0)
plt.show()


# Довільно задані значення
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Максимальне значення в дереві:", bst.find_max())

print("Мінімальне значення в дереві:", bst.find_min())

print("Сума всіх значень в дереві:", bst.tree_sum())

