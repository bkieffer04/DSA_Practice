class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = None


class practice:
    def createList():
        head = Node(2)
        head.next = Node(15)
        head.next.next = Node(3)
        head.next.next.next = Node(47)
        head.next.next.next.next = Node(72)
        head.next.next.next.next.next = Node(52)
        head.next.next.next.next.next.next = Node(235)
        head.next.next.next.next.next.next.next  = Node(144)

        return head
    

    def onlyPositives(head):
        result = None  # Initialize the result linked list
        result_tail = None  # Keep track of the tail of the result linked list

        while head is not None:
            if head.val % 2 == 0:
                # Create a new node with the same value
                new_node = Node(head.val)

                if result is None:
                    # If result is empty, set the new node as the head of the result
                    result = new_node
                    result_tail = new_node
                else:
                    # Otherwise, append the new node to the result linked list
                    result_tail.next = new_node
                    result_tail = new_node

            head = head.next

        return result
    
    def reverseList(head):
        # 3, 8, 19, 24, 91, 31
        #31, 91, 24, 19, 8, 3

        # 3 -> None
        # 8 -> 3 -> None
        # 19 -> 8 -> 3 -> None
        # 24 -> 19 -> 8 -> 3 -> None
        # 91 -> 24 -> 19 -> 8 -> 3 -> None
        # 31 -> 91 -> 24 -> 19 -> 8 -> 3 -> None

        result = None
        while(head != None):
            if result is None:
                curr = Node(head.val)
                result = Node(curr.val, curr.next)
            else: 
                curr = Node(head.val)
                curr.next = result
                result = curr
            head = head.next
        
        return result
    
    def twoPtr(head):
        # slow = 2  fast = 3 => != 75
        # slow = 15 fast = 3 => != 75
        # slow = 3  fast = 72 => == 75

        slow = head
        fast = slow.next.next
        while fast.next or fast.next.next:
            if slow.val == fast.val:
                fast = fast.next.next or fast.next
            #if slow.val + fast.val == target:
                #return True
            slow = slow.next

        return False
    
    def findTargetWithTwoVals(head, target):
        # target = 75
        # 2, 15, 3, 47, 72, 52, 235, 144
        seen_values = set()

        while head is not None:
            complement = target - head.val

            if complement in seen_values:
                # Found a pair whose sum is equal to the target
                return True

            seen_values.add(head.val)
            head = head.next

        # No pair found
        return False

    def leastToGreatest(head):
        # 2, 15, 3, 47, 72, 52, 235, 144
        # ^
        #        ^
        # 2, 3, 15, 47, 72, 52, 235, 144
        #    ^
        #        ^
        #            ^
        #                    ^
        # 2, 3, 15, 47, 52, 72, 235, 144
        #                    ^
        #                             ^
        # 2, 3, 15, 47, 52, 72, 144, 235
        temp = head
        result = temp
        curr = temp
        while curr.next != None:
            if curr.val > curr.next.val:
                temp = curr.val
                curr.val = curr.next.val
                curr.next.val = temp
            else:
                curr = curr.next

        return result 


    