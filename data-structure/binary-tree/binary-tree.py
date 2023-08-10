# binary Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# insert node
def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if root.data == data:
            return root
        elif root.data < data:
            root.right = insert(root.right, data)
        else:
            root.left = insert(root.left, data)
    return root

# find node
def find(root, data):
    if root is None:
        return False
    elif root.data == data:
        return True
    elif root.data < data:
        return find(root.right, data)
    else:
        return find(root.left, data)
    
# find min node
def findMin(root):
    if root is None:
        return None
    elif root.left is None:
        return root
    else:
        return findMin(root.left)
    
# find max node
def findMax(root):
    if root is None:
        return None
    elif root.right is None:
        return root
    else:
        return findMax(root.right)
    
# find height of tree
def height(root):
    if root is None:
        return -1
    else:
        return max(height(root.left), height(root.right)) + 1
    
# level order traversal
def levelOrder(root):
    if root is None:
        return
    else:
        queue = []
        queue.append(root)
        while len(queue) != 0:
            node = queue.pop(0)
            print(node.data, end=" ")
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

# pre order traversal
def preOrder(root):
    if root is None:
        return
    else:
        print(root.data, end=" ")
        preOrder(root.left)
        preOrder(root.right)

# in order traversal
def inOrder(root):
    if root is None:
        return
    else:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)

# post order traversal
def postOrder(root):
    if root is None:
        return
    else:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=" ")

# delete node
def delete(root, data):
    if root is None:
        return root
    elif root.data < data:
        root.right = delete(root.right, data)
    elif root.data > data:
        root.left = delete(root.left, data)
    else:
        # case 1: no child
        if root.left is None and root.right is None:
            root = None
        # case 2: one child
        elif root.left is None:
            root = root.right
        elif root.right is None:
            root = root.left
        # case 3: two child
        else:
            temp = findMin(root.right)
            root.data = temp.data
            root.right = delete(root.right, temp.data)
    return root

# delete tree
def deleteTree(root):
    if root is None:
        return
    else:
        deleteTree(root.left)
        deleteTree(root.right)
        root = None

# check if two trees are identical
def isIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is not None and root2 is not None:
        return (root1.data == root2.data and isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right))
    else:
        return False
    
# check if two trees are mirror
def isMirror(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is not None and root2 is not None:
        return (root1.data == root2.data and isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left))
    else:
        return False
    

# check if tree is symmetric
def isSymmetric(root):
    if root is None:
        return True
    else:
        return isMirror(root.left, root.right)
    
# check if tree is balanced
def isBalanced(root):
    if root is None:
        return True
    else:
        return (isBalanced(root.left) and isBalanced(root.right) and abs(height(root.left) - height(root.right)) <= 1)
    

# check if tree is BST
def isBST(root):
    if root is None:
        return True
    else:
        if root.left is not None and findMax(root.left).data > root.data:
            return False
        if root.right is not None and findMin(root.right).data < root.data:
            return False
        if not isBST(root.left) or not isBST(root.right):
            return False
        return True
    

# find LCA of two nodes
def findLCA(root, node1, node2):
    if root is None:
        return None
    elif root.data == node1 or root.data == node2:
        return root
    else:
        left = findLCA(root.left, node1, node2)
        right = findLCA(root.right, node1, node2)
        if left is not None and right is not None:
            return root
        elif left is not None:
            return left
        else:
            return right
        
# find distance between two nodes
def findDistance(root, node1, node2):
    lca = findLCA(root, node1, node2)
    return height(lca.left) + height(lca.right) + 1

# find diameter of tree
def findDiameter(root):
    if root is None:
        return 0
    else:
        leftHeight = height(root.left)
        rightHeight = height(root.right)
        leftDiameter = findDiameter(root.left)
        rightDiameter = findDiameter(root.right)
        return max(leftHeight + rightHeight + 1, max(leftDiameter, rightDiameter))
    

# find diameter of tree in O(n)
def findDiameterOptimized(root):
    if root is None:
        return 0, 0
    else:
        leftHeight, leftDiameter = findDiameterOptimized(root.left)
        rightHeight, rightDiameter = findDiameterOptimized(root.right)
        return max(leftHeight, rightHeight) + 1, max(leftHeight + rightHeight + 1, max(leftDiameter, rightDiameter))
    

# find max sum path
def findMaxSumPath(root):
    if root is None:
        return 0
    else:
        leftSum = findMaxSumPath(root.left)
        rightSum = findMaxSumPath(root.right)
        return max(max(leftSum, rightSum) + root.data, root.data)
    

# find max sum path in tree
def findMaxSumPathInTree(root):
    if root is None:
        return 0, 0
    else:
        leftSum, leftMaxSum = findMaxSumPathInTree(root.left)
        rightSum, rightMaxSum = findMaxSumPathInTree(root.right)
        return max(leftSum, rightSum) + root.data, max(leftSum + rightSum + root.data, max(leftMaxSum, rightMaxSum))