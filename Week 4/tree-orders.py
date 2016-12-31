# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    current = 0
    stack = []
    while True:
      if current != -1:
        stack.append(current)
        current = self.left[current]
      elif stack:
        current = stack.pop()
        self.result.append(self.key[current])
        current = self.right[current]
      else:
        break
    return self.result

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    current = 0
    stack = []
    while True:
      if current != -1:
        self.result.append(self.key[current])
        stack.append(current)
        current = self.left[current]
      elif stack:
        current = stack.pop()
        current = self.right[current]
      else:
        break
    return self.result

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    stack1 = [0]
    stack2 = []
    while stack1:
      current = stack1.pop()
      stack2.append(self.key[current])

      left = self.left[current]
      right = self.right[current]

      if left != -1:
        stack1.append(left)
      if right != -1:
        stack1.append(right)

      self.result = reversed(stack2)

    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
