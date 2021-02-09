## Just a simple class to practice working with inheritance 

class QueueError(Exception):  # Choose base class for the new exception.
    #
    #  Write code here
    #
    pass

class Queue:
    def __init__(self):
        #
        # Write code here
        #
        self.queue = []

    def put(self, elem):
        #
        # Write code here
        #
        self.queue.append(elem)

    def get(self):
        #
        # Write code here
        #
        return self.queue.pop(0)

class SuperQueue(Queue):
    #
    # Write new code here.
    #

    def isempty(self):
        if len(self.queue) > 0:
            return False
        else:
            return True



que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
        
  
