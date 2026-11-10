class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    current.next = list1 if list1 else list2

    return dummy.next


def create_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def display_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


list1 = create_list([1, 2, 4])
list2 = create_list([1, 3, 4])
display_list(merge_two_lists(list1, list2))

list3 = create_list([])
list4 = create_list([0])
display_list(merge_two_lists(list3, list4))

list5 = create_list([])
list6 = create_list([])
display_list(merge_two_lists(list5, list6))