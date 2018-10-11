"""

    CacheElements are put in a doubly linkedList implementation for easy tracking of LRU
        When recently used, move to tail of list
        Evict from head when capacity reached
        remove & append are constant time

    Use a key_node_map dict that maps from key to node (CacheElement) in the cache linkedList
        Allows constant time lookup

"""

class CacheElement:
    def __init__(self, key, element, prev, next):
        self.key = key
        self.element = element
        self.prev = prev
        self.next = next

    

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.length = 0

        self.head = None
        self.tail = None

        self.key_node_map = {}
        
        

    def remove(self, node):
        # check removing head node
        if node == self.head:
            self.head = node.next
        else:
            node.prev.next = node.next

        # check removing tail node
        if node == self.tail:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        self.length -= 1


    def append(self, node):
        # check if there is a tail node (non empty list)
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.tail = node
            self.head = node

        self.length += 1


    def evict_head(self):
        node_to_evict = self.head
        self.key_node_map.pop(node_to_evict.key)
        self.remove(node_to_evict)


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.key_node_map:
            node = self.key_node_map[key]
            self.remove(node)
            self.append(node)
            return node.element
        else:
            return -1

        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.key_node_map:
            node = self.key_node_map[key]
            node.element = value
            self.remove(node)
            self.append(node)
        else:
            node = CacheElement(key, value, None, None)
            self.key_node_map[key] = node

            # need to evict
            if self.length == self.capacity:
                self.evict_head()
            self.append(node)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

if __name__ == "__main__":
    print("=== LRUCache ===")

    cache = LRUCache(2)

    cache.put(1,1)
    cache.put(2,2)
    cache.get(1)        # returns 1
    cache.put(3,3)      # evicts key 2
    cache.get(2);       # returns -1 (not found)
    cache.put(4, 4);    # evicts key 1
    cache.get(1);       # returns -1 (not found)
    cache.get(3);       # returns 3
    cache.get(4);       # returns 4

    print("=== done! ===")