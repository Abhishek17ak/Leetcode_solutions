#Create a node wirh key and value with next and prev pointers
class Node:
    def __init__ (self,key,val):
        self.key,self.val = key,val
        self.prev=self.next=None# initially set them to null(none)

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache ={}#initilize a hash set

        #dummy nodes to show most recent and least recent
        self.left,self.right = Node(0,0),Node(0,0)
        self.left.next,self.right.prev = self.right,self.left
       #we will add our nodes between these
       #left will point to lease used and right to most used        

    #helper functions to add and remove from our doubly linked list
    #remove node from list
    def remove(self,node):
        prev,nxt=node.prev,node.next
        prev.next,nxt.prev=nxt,prev

    #insert node at right
    def insert(self,node):
        prev,nxt=self.right.prev,self.right
        prev.next=nxt.prev=node
        node.next,node.prev=nxt,prev    

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            #we remove and insert again to its at right most position
            #this sginifies its most recently used and pointed by right pointer
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])#if key is already present
        self.cache[key]=Node(key,value)#insert in our hash map
        self.insert(self.cache[key])#insert in our doubly linked list

        #remove least used element if capacity exceeds
        if len(self.cache)>self.cap:
            lru=self.left.next
            self.remove(lru)#remove from linked list
            del self.cache[lru.key]#remove from hash map
        
