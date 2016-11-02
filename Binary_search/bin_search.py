class BinarySearch(list):

    def __init__(self,a,b):
        self.a = a
        self.b = b

        '''
        Generate  a list of numbers to the length of a
        '''
        for num in range(self.a):
            list.append(self, self.b)
            self.b += b

        self.length = self.a

    def search(self, number):
        '''
        Implements the binary search and return the index of the number
        and the count of iterations in a dictionary
        '''
        upper = (self.length - 1)
        lower = 0
        count = 0
        found = False
        '''
        Check if the number appears on the list and set the index to its lowest index
        and set found to true if not set found to false and index to -1
        '''
        try:
            index = self.index(number)
            found = True
        except ValueError:
            index = -1
            found = False
        while lower <= upper and found and number != self[upper]:
            mid = (lower + upper) //2
            mid_value = self[mid] # it gt the value that the mid index is holding
            if number > mid_value:
                lower = mid + 1
                count += 1
            elif number < mid_value:
                upper = mid - 1
                count += 1
            else:
                count += 1
                break
        return {'count': count, 'index': index}

list1 = BinarySearch(1000,10)
print(list1.search(880))
