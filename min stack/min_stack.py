class MinStack:
    min=float('inf')
    def __init__(self):
        self.min=float('inf')
        self.stack = []
    def push(self,x):
        if x<=self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)
    def pop(self):
      t = self.stack[-1]
      self.stack.pop()
      if self.min == t:
         self.min = self.stack[-1]
         self.stack.pop()
    def top(self):
      return self.stack[-1]
    def getMin(self):
      return self.min
    def __str__(self):
        return "Node({})".format(self.value)
 
  
   

   
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
