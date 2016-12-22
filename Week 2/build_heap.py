# python3
import math

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    '''for i in range(len(self._data)):
      for j in range(i + 1, len(self._data)):
        if self._data[i] > self._data[j]:
          self._swaps.append((i, j))
          self._data[i], self._data[j] = self._data[j], self._data[i]'''
    start = math.floor(len(self._data) / 2)
    for i in range(start, -1, -1):
      self.siftDown(i)

  def siftDown(self, i):
        minIndex = i
        l = self.leftChild(i)
        if l <= len(self._data) - 1 and self._data[l] < self._data[minIndex]:
          minIndex = l
        r = self.rightChild(i)
        if r <= len(self._data) - 1 and self._data[r] < self._data[minIndex]:
          minIndex = r
        if i != minIndex:
          self._swaps.append((i,minIndex))
          self._data[i], self._data[minIndex] = self._data[minIndex], self._data[i]
          self.siftDown(minIndex)



  def leftChild(self, i):
    return 2 * i + 1

  def rightChild(self, i):
    return 2 * i + 2

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
