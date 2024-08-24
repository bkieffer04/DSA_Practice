from practice import Node, practice

def linked_list_to_list(head):
    """Helper function to convert linked list to Python list for easy comparison."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def test_createList():
    head = practice.createList()
    result = linked_list_to_list(head)
    expected = [2, 15, 3, 47, 72, 52, 235, 144]
    assert result == expected

def test_onlyPositives():
    head = practice.createList()
    result = practice.onlyPositives(head)
    result = linked_list_to_list(result)
    expected = [2, 72, 52, 144]  # Assuming only even numbers are positives
    assert result == expected

def test_reverseList():
    head = practice.createList()
    result = practice.reverseList(head)
    result = linked_list_to_list(result)
    expected = [144, 235, 52, 72, 47, 3, 15, 2]
    assert result == expected

def test_findTargetWithTwoVals():
    head = practice.createList()
    assert practice.findTargetWithTwoVals(head, 379)  # 144 + 235
    assert not practice.findTargetWithTwoVals(head, 500)  # No such pair

def test_leastToGreatest():
    head = practice.createList()
    result = practice.leastToGreatest(head)
    result = linked_list_to_list(result)
    expected = [2, 3, 15, 47, 52, 72, 144, 235]
    assert result == expected
