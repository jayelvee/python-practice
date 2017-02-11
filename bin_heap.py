class BinHeap(object):
    def __init__(self):
        self.heaplist = [0]
        self.heapsize = 0
        
    def perc_up(self, i):
        while i//2 > 0:
            if self.heaplist[i] < self.heaplist[i//2]:
                tmp = self.heaplist[i//2]
                self.heaplist[i//2] = self.heaplist[i]
                self.heaplist[i] = tmp
            i = i//2

    def insert(self, val):
        self.heaplist.append(val)
        self.heapsize += 1
        self.perc_up(self.heapsize)
        
    def print_tree(self):
        for i in range(1, self.heapsize+1):
            print(self.heaplist[i], end=" ")
            
    def percDown(self,i):
        while (i * 2) <= self.heapsize:
            mc = self.minChild(i)
            if self.heaplist[i] > self.heaplist[mc]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[mc]
                self.heaplist[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.heapsize:
            return i * 2
        else:
            if self.heaplist[i*2] < self.heaplist[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.heapsize]
        self.heapsize = self.heapsize - 1
        self.heaplist.pop()
        self.percDown(1)
        return retval

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.heapsize = len(alist)
        self.heaplist = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
            
if __name__ == "__main__":
    h = BinHeap()
    h.buildHeap([2, 4, 6, 8, 10, 9, 7, 5, 3, 1])