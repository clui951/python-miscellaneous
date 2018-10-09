# Enter your code here. Read input from STDIN. Print output to STDOUT


# rateLimiter = RateLimiter(10)
# assert rateLimiter.canSend(100, 3) == True #true
# assert rateLimiter.getRate(100) == 3
# assert rateLimiter.canSend(200, 4) == True # true
# assert rateLimiter.getRate(200) == 7
# assert rateLimiter.canSend(300, 9) == False # false
# assert rateLimiter.getRate(300) == 7
# assert rateLimiter.canSend(400, 1) == True # true
# assert rateLimiter.getRate(400) == 8
# assert rateLimiter.canSend(2000, 10) == True# true
# assert rateLimiter.getRate(2000) == 10

# /*class RateLimiter {
#    // Set maxRate in Bytes per second
#      RateLimiter(int maxBytes){   
#      }
#      // Returns true if sending bytes at time = timestamp (milliseconds) will not exceed the maxRate in last second
#      boolean canSend(long timestamp, int bytes) {            
#      }

#      // Returns the total Bytes sent out in the last second at time = timestamp (milliseconds)
#      long getRate(long timestamp) {
#      }
# }*/

class RateLimiter:
    def __init__(self, maxBytes):
        self.maxBytes = maxBytes
        self.requests = [] # (timestamp, bytes)
        self.requestBytes = 0 # total amount of bytes in request list
        
    def pruneProcess(self, timestamp):
        # part 1, prune request list until only contains last second of requests
        i = 0
        while i < len(self.requests):
            if self.requests[i][0] < (timestamp - 1000):
                # need to prune
                self.requestBytes -= self.requests[i][1]
                i += 1
            else:
                break;
        self.requests = self.requests[i:]
    

    def canSend(self, timestamp, bytes):
        self.pruneProcess(timestamp)
        
        # part 2, check if new request is allowed and add if so
        if bytes + self.requestBytes <= self.maxBytes:
            self.requests.append((timestamp, bytes))
            self.requestBytes += bytes
            return True
        else:
            return False
            
    def getRate(self, timestamp):
        self.pruneProcess(timestamp)
        # part 2, return the current counter of bytes, which should be pruned to 1 second already
        return self.requestBytes

rateLimiter = RateLimiter(10)
assert rateLimiter.canSend(100, 3) == True #true
assert rateLimiter.getRate(100) == 3
assert rateLimiter.canSend(200, 4) == True # true
assert rateLimiter.getRate(100) == 7
assert rateLimiter.canSend(300, 9) == False # false
assert rateLimiter.getRate(100) == 7
assert rateLimiter.canSend(400, 1) == True # true
assert rateLimiter.getRate(100) == 8
assert rateLimiter.canSend(2000, 10) == True# true
assert rateLimiter.getRate(100) == 10


# --- General Cases To Consider ---
# if no requests yet, and call request < maxBytes
# if no requests yet, and call request > maxBytes
# if requests exist, call request < / > maxBytes
# if requests exist and need to be pruned, call request < / > maxBytes

# downsides of design
#   centralized bottleneck across threads/machines
#   parallel locking issues
#   memory of computer to hold queue
#   maybe can loosen requirements, bucket the requests, fuzzy borders, (circular array of length bytesMax)

# O(# requests / second) ; O(n)

    