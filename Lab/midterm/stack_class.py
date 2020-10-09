class Stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[-1]

  def isEmpty(self):
    return self.items == []

  def size(self):
    return len(self.items)

  class queue:
    def __init__(self, list = None):
      if self.list == None:
        self._queue = []
      else:
        self._queue = list
      self._dequeue = []

    def dequeue(self, item):
      self._dequeue.append(item)
    
    def push(self, item):
      self._queue.append(item)

    def pop(self):
      return self._queue.pop(0)

    def peek(self):
      return self._queue[-1]

    def isEmpty(self):
      return self._queue == []

    def size(self):
      return len(self._queue)
    
    def show_dequeue(self):
      return self._dequeue

    def show_queue(self):
      return self._queue