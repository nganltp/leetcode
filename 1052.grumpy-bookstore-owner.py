import numpy as np
def maxSatisfied(customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """

        grumpy = [1 if i==0 else 0 for i in grumpy]

        maximum_new = maximum = np.dot(customers[minutes:], grumpy[minutes:])+sum(customers[:minutes])
        
        for i in range(minutes, len(grumpy)):
            if grumpy[i] == 0:
                maximum_new += customers[i]
            if grumpy[i - minutes] == 0:
                maximum_new -= customers[i - minutes]
            maximum = max(maximum, maximum_new)
        return maximum

customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3

print(maxSatisfied(customers, grumpy, minutes))