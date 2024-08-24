class practice:
    #prints the even numbers
    def printOnlyEvens(val): 
        if(val % 2 == 0):
            print(val)
        else:
            print('Odd')
        if(val == 0):
            return val
        else:
            return practice.printOnlyEvens(val - 1)
    def onlyEvens(list, index):
        if(index == len(list)):
            return list
        if(list[index] % 2 != 0):
            list.remove(list[index])
        else: 
            index += 1
            
        return practice.onlyEvens(list, index)
    def findIndexOfVal(list, index, target):
        if(index == len(list)):
            return 0
        elif(list[index] == target):
            return index
        return practice.findIndexOfVal(list, index+1, target)
    
    #helper function for twoValsSumInSortedList
    def findSum(list, target, first, last):
        if(first == last):
            return False
        elif(list[first] + list[last] == target):
            return True
        if(list[first] + list[last] < target):
            return practice.findSum(list, target, first + 1, last)
        else:
            return practice.findSum(list, target, first, last - 1)
    def twoValsSumInSortedList(list, target):
        return practice.findSum(list, target, 0, len(list) - 1)
    
    #helper function for twoValsSumInUnsortedList
    def findSumUnsorted(list, target, first, next):
        if(first >= len(list) - 1):
            return False
        elif(next == len(list)):
            return practice.findSumUnsorted(list, target, first + 1, first + 2)
        elif(list[first] + list[next] == target):
            return True
        else:
            return practice.findSumUnsorted(list, target, first, next + 1)
        
    def twoValsSumInUnsortedList(list, target):
        if(len(list) > 2):
            return practice.findSumUnsorted(list, target, 0, 1)
        elif(list[0] + list[1] == target):
            return True
        return False
    
    #helper function for binarySearch
    def recursiveBS(list, target, first, last):
        if(first == last):
            return False
        elif(list[(last + first) // 2] == target):
            return True
        mid = (last + first) // 2
        if(list[mid] < target):
            return practice.recursiveBS(list, target, first + 1, last)
        else:
            return practice.recursiveBS(list, target, first, last - 1)
    def binarySearch(list, target):
        return practice.recursiveBS(list, target, 0, len(list))
    
    #helper function for generateParanthese
    def backtrack(n, leftCount, rightCount, output, result):
        # Base case where count of left and right braces is "n"
        if leftCount >= n and rightCount >= n:
            # Join the array elements into a string without any separators.
            outputStr = "".join(output)
            result.append(outputStr)

        # Case where we can still append left braces
        if leftCount < n:
            output.append("(")
            practice.backtrack(n, leftCount + 1, rightCount, output, result)
            output.pop()

        # Case where we append right braces if the current count of right braces is less than the count of left braces
        if rightCount < leftCount:
            output.append(")")
            practice.backtrack(n, leftCount, rightCount + 1, output, result)
            output.pop()
    def generateParanthese(n):
        result = []
        output = []
        practice.backtrack(n, 0, 0, output, result)
        return result

