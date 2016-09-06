# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def get_number(self, list_item):
        number_string = ''
        while True:
            number_string += str(list_item.val)

            if list_item.next is None:
                break
            else:
                list_item = list_item.next

        return int(number_string[::-1])

    def create_list_node(self, val, next):
        list_node = ListNode(val)
        list_node.next = next
        return list_node

    def create_linked_list(self, numbers):
        last_item = None
        first_item = None
        for number in numbers:
            last_item = self.create_list_node(number, last_item)
            if first_item is None:
                first_item = last_item
        return last_item

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_number = self.get_number(l1)
        l2_number = self.get_number(l2)

        summed_val = l1_number + l2_number
        int_list = [int(i) for i in list(str(summed_val))]

        return self.create_linked_list(int_list)


solution = Solution()
# 2 -> 4 -> 3
list1 = solution.create_linked_list([2, 4, 3])
# 5 -> 6 -> 4
list2 = solution.create_linked_list([5, 6, 4])


added = solution.addTwoNumbers(list1, list2)
print(str(added.val) + str(added.next.val) + str(added.next.next.val))

