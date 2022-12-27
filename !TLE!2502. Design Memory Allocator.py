class Allocator:

    def __init__(self, n: int):
        self.allocater=[None for x in range(n)]
        
    def allocate(self, size: int, mID: int) -> int:
        for i,x in enumerate(self.allocater):
            if x == None and i+size<=len(self.allocater):
                new=[x for x in self.allocater[i:i+size] if x != None]
                if len(new)==0 : 
                    self.allocater[i:i+size] = (mID for x in range(size))
                    return i
        return -1

    def free(self, mID: int) -> int:
        count=0
        for i,x in enumerate(self.allocater):
            if x == mID:
                self.allocater[i]=None
                count+=1
        return count
        

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)

if __name__ == '__main__':
    n=10
    obj = Allocator(n)
    print(obj.allocate(1,1))
    print(obj.allocater)

    print(obj.allocate(1,2))    
    print(obj.allocater)

    print(obj.allocate(1,3))
    print(obj.allocater)
    print(obj.free(2))
    print(obj.allocater)
    print(obj.allocate(3,4))
    print(obj.allocater)
    print(obj.allocate(1,1))
    print(obj.allocater)
    print(obj.allocate(1,1))
    print(obj.allocater)
    print(obj.free(1))
    print(obj.allocater)
    print(obj.allocate(10,2))
    print(obj.allocater)
    print(obj.free(7))
    print(obj.allocater) 
