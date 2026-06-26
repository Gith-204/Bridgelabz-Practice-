#Stack
# class stack:
#     def __init__(self):
#         self.stack = []
    
#     def isEmpty(self):
#         return len(self.stack) == 0 
    
#     def push(self, item):
#         self.stack.append(item)

#     def pop(self):
#         if self.isEmpty(): 
#             return "Stack is empty"
#         else:
#             return self.stack.pop()
    
#     def size(self):
#         return len(self.stack) 

# s = stack() 
# s.push(10)
# s.push(20)
# s.push(30)
# s.push(40)
# s.push(50) 
# print("Stack size:", s.size())
# print("Popped:", s.pop())
# print("Stack size after pop:", s.size())
# print("Is empty:", s.isEmpty()) 

#Queue 
# class queue:
#     def __init__(self):
#         self.queue = [] 

#     def isEmpty(self):
#         return len(self.queue) == 0
    
#     def enqueue(self, item):
#         self.queue.append(item)
    
#     def dequeue(self):
#         if self.isEmpty():
#             return "Queue is empty"
#         else:
#             return self.queue.pop(0) 
    
#     def size(self):
#         return len(self.queue) 

# q = queue()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)
# q.enqueue(50) 
# print("Queue size:", q.size())
# print("Dequeued:", q.dequeue())
# print("Queue size after dequeue:", q.size())
# print("Is empty:", q.isEmpty()) 

# Linked List
# class node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None 

# head = node(10)
# second = node(20)
# third = node(30)  
# fourth = node(40) 
# fifth = node(50)     

# head.next = second
# second.next = third
# third.next = fourth 
# fourth.next = fifth 

# temp = head
# while temp:
#     print(temp.data, end = " --> ") 
#     temp = temp.next
# print("None") 

# # Singly linked list
# class node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None 

# class singlyLinkedList: 
#     def __init__(self):
#         self.head = None
    
#     def append(self, data):
#         new_node = node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node 
    
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end = " --> ")
#             temp = temp.next
#         print("None") 

# sll = singlyLinkedList() 
# sll.append(10)
# sll.append(20)
# sll.append(30)
# sll.append(40)
# sll.append(50)
# sll.display() 

# Doubly linked list 
# class node:
#     def __init__(self, data):
#         self.data = data 
#         self.next = None  
#         self.prev = None 

# class doublylinkedlist:
#     def __init__(self):
#         self.head = None  
    
#     def insert(self, data): 
#         new_node = node(data) 
#         if not self.head:
#             self.head = new_node 
#             return
        
#         temp = self.head
#         while temp.next:
#             temp = temp.next 
#         temp.next = new_node 
#         new_node.prev = temp   

#     def delete(self, key):
#         temp = self.head
#         while temp:
#             if temp.data == key:
#                 if temp.prev:
#                     temp.prev.next = temp.next
#                 else:
#                     self.head = temp.next 
#                 if temp.next:
#                     temp.next.prev = temp.prev 
#                 return
#             temp = temp.next  
    
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" <-> ")
#             temp = temp.next
#         print("None")

# dll = doublylinkedlist() 
# dll.insert(10)
# dll.insert(20)
# dll.insert(30) 
# dll.display()
# dll.delete(20)
# dll.display() 

# Circular linked list 
# class node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None   
    
# class circularLinkedList: 
#     def __init__(self):  
#         self.head = None
    
#     def insert(self, data):
#         new_node = node(data)
#         if not self.head:
#             self.head = new_node
#             new_node.next = self.head 
#             return
        
#         temp = self.head
#         while temp.next != self.head:
#             temp = temp.next 
#         temp.next = new_node
#         new_node.next = self.head 

#     def display(self):
#         if not self.head:
#             print("List is empty")
#             return
        
#         temp = self.head
#         while True:
#             print(temp.data, end=" --> ") 
#             temp = temp.next 
#             if temp == self.head:
#                 break 
#         print("None") 

# C1 = circularLinkedList()
# C1.insert(10) 
# C1.insert(20)
# C1.insert(30)
# C1.insert(40)
# C1.insert(50)
# C1.insert(60) 
# C1.display()

#Trees
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# root = Node(10)
# root.left = Node(20)
# root.right = Node(30)
# root.left.left = Node(40)
# root.left.right = Node(50) 
# root.right.left = Node(60)
# root.right.right = Node(70)

# print(root.data)
# print(root.left.data)
# print(root.right.data) 
# print(root.left.left.data)
# print(root.left.right.data) 
# print(root.right.left.data)
# print(root.right.right.data) 

#Preorder traversal
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None 
    
# def preorder(root):
#     if root:
#         print(root.data, end = " ")
#         preorder(root.left)
#         preorder(root.right) 

# root = Node(10)
# root.left = Node(20)
# root.right = Node(30)
# root.left.left = Node(40)
# root.left.right = Node(50) 
# preorder(root)   

#Inorder traversal
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None 
    
# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.data, end = " ")
#         inorder(root.right) 

# root = Node(10)
# root.left = Node(20)
# root.right = Node(30)
# root.left.left = Node(40)
# root.left.right = Node(50) 
# inorder(root) 

#Postorder traversal
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None 
    
# def postorder(root):
#     if root:
#         postorder(root.left)
#         postorder(root.right) 
#         print(root.data, end = " ") 

# root = Node(10)
# root.left = Node(20)
# root.right = Node(30)
# root.left.left = Node(40)
# root.left.right = Node(50) 
# postorder(root) 


#Level order traversal
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None 
    
# def levelOrder(root):
#     if not root:
#         return 
#     queue = [root]
#     while queue:
#         current = queue.pop(0)
#         print(current.data, end = " ")
#         if current.left:
#             queue.append(current.left)
#         if current.right:
#             queue.append(current.right) 

# root = Node(10)
# root.left = Node(20)
# root.right = Node(30)
# root.left.left = Node(40)
# root.left.right = Node(50) 


#Binary Search Tree 
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# def insert(root, value): 

#     if root is None:
#         return Node(value)

#     if value < root.data:
#         root.left = insert(root.left, value)

#     else:
#         root.right = insert(root.right, value)

#     return root

# def search(root, key):

#     if root is None:
#         return False

#     if root.data == key:
#         return True

#     elif key < root.data:
#         return search(root.left, key)

#     else:
#         return search(root.right, key)


# root = None

# values = [50,30,70,20,40,60,80]

# for value in values:
#     root = insert(root, value)

# print(search(root, 60))
# print(search(root, 100)) 


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# def insert(root, value):

#     if root is None:
#         return Node(value)

#     if value < root.data:
#         root.left = insert(root.left, value)

#     else:
#         root.right = insert(root.right, value)

#     return root

# def inorder(root):

#     if root:
#         inorder(root.left)

#         print(root.data, end=" ")

#         inorder(root.right)

# def find_min(root):

#     while root.left:
#         root = root.left

#     return root

# def delete(root, key):

#     # Tree empty
#     if root is None:
#         return root

#     # Move left
#     if key < root.data:
#         root.left = delete(root.left, key)

#     # Move right
#     elif key > root.data:
#         root.right = delete(root.right, key)

#     # Node found
#     else:

#         # Case 1 & 2
#         if root.left is None:
#             return root.right

#         elif root.right is None:
#             return root.left

#         # Case 3
#         temp = find_min(root.right)

#         root.data = temp.data

#         root.right = delete(root.right, temp.data)

#     return root

# root = None

# values = [50,30,70,20,40,60,80]

# for value in values:
#     root = insert(root, value)

# print("Before deletion:")
# inorder(root)

# root = delete(root, 50)

# print("\nAfter deletion:")
# inorder(root) 



#Graphs
# class Graph:
#     def __init__(self):
#         self.graph = {}

#     def add_edge(self, u, v):
#         if u not in self.graph:
#             self.graph[u] = []
#         if v not in self.graph:
#             self.graph[v] = []
#         self.graph[u].append(v)
#         self.graph[v].append(u)

#     def display(self):
#         for vertex in self.graph:   
#             print(f"{vertex}: {self.graph[vertex]}")

# g = Graph() 
# g.add_edge(1, 2)
# g.add_edge(1, 3)
# g.add_edge(2, 4)
# g.add_edge(3, 4)
# g.add_edge(4, 5)
# g.display()

#BFS
# from collections import deque
# graph = {'A': ['B', 'C'],
#          'B': ['D', 'E'],
#          'C': ['F'],
#          'D': [],
#          'E': ['F'],
#          'F': []
#          }

# def bfs(graph, start):
#     visited = set() 
#     queue = deque([start])
#     visited.add(start)
#     while queue:
#         node = queue.popleft()
#         print(node, end=" ")
#         for neighbor in graph[node]:
#             if neighbor not in visited:  
#                 visited.add(neighbor)
#                 queue.append(neighbor) 

# bfs(graph, 'A')
# bfs(graph, 'B')
# bfs(graph, 'C')
# bfs(graph, 'D')
# bfs(graph, 'E')
# bfs(graph, 'F') 

#DFS
# graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': ['F'], 'F': []}

# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     print(start, end=" ")
#     for neighbor in graph[start]:
#         if neighbor not in visited:
#             dfs(graph, neighbor, visited)

# dfs(graph, 'A')
# dfs(graph, 'B')
# dfs(graph, 'C')
# dfs(graph, 'D')
# dfs(graph, 'E')
# dfs(graph, 'F') 

#Search algorithms
#Linear search
# def linear_search(arr, key):
#     for i in range(len(arr)):
#         if arr[i] == key:
#             return i
#     return -1

# arr = [10,20,30,40,50] 
# key = 30
# result = linear_search(arr, key)
# print(f"Element found at index: {result}") 

#Binary Search
# def binary_search(arr, key):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2 
#         if arr[mid] == key:
#             return mid
#         elif arr[mid] < key:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# arr = [10,20,30,40,50]  
# key = 30  
# result = binary_search(arr, key)
# print(f"Element found at index: {result}") 