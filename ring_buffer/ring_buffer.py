class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.ls = []
        self.iter = 0
        self.iters = []

    def append(self, item):
        if len(self.ls) < self.capacity:
            self.ls.append(item)
            self.iter += 1
            self.iters.append(self.iter)

        else:
            m = min(self.iters)
            for num, i in enumerate(self.iters):
                if i == m:
                    self.ls[num] = item
                    self.iter += 1
                    self.iters[num] = self.iter
    
    def get(self):
        return self.ls