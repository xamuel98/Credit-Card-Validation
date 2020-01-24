# moveZeros.py
class Solution:
  '''Create a function with parameters nums (the list to be passed) and another list
    list2 initially empty
  '''
  def moveZeros(self, nums, list2=[]):
    '''In order to eliminate the issue of list index out of range create a
    list object, passing the list - nums variable as an argument
    '''
    res_list = list(nums)
    # Loop through the list - nums
    for i in range(len(nums)):
      # If an element of the list - nums equals 0
      if nums[i] == 0:
        # Append the 0s the initially empty created list
        list2.append(nums[i])
        # Once the 0s are appended to the new list - list2, remove them the old list - res_list
        res_list.remove(nums[i])

    # Add the new list - list, to the old list
    res_list.extend(list2)

    # Return the updated list
    return res_list

def main():
  nums = [0,0,0,2,0,1,3,4,0,0]
  # print(Solution().moveZeros(nums))
main()


# maximum_product_of_three.py
class Solution:
  def maximum_product_of_three(self, lst):
    product_list = []
    for i in range(len(lst)):
      for j in range(i + 1, len(lst)):
        for k in range(j + 1, len(lst)):
          max_product = lst[i] * lst[j] * lst[k]
          product_list.append(max_product)

    _max = max(product_list)
    return _max

#   Minified Solution
  def maximum_product_of_threes(self, lst):
    product_list = [lst[i] * lst[j] * lst[k] for i in range(len(lst)) for j in range(i + 1, len(lst)) for k in
         range(j + 1, len(lst))]

    _max = max(product_list)
    return _max


def main():
  lst = [-4,-4,2,8]
  # print(Solution().maximum_product_of_three(lst))
main()


#Kth_largest_element_in_a_list.py
class Solution:
  def findKthLargest(self, nums, k):
    if k <= len(nums):
      nums.sort(reverse=False)
    else:
      raise ValueError("K has exceeded the length of the list")

    return nums[-k]

def main():
  # print(Solution().findKthLargest([1,23,12,9,30,2,50],3))
  main()


# Program that prints k largest elements in an array
class Solution:
  def kthLargestElement(self, nums, k):
    nums.sort(reverse=True)
    for i in range(k):
      print(nums[i], end = " ")


def main():
  # (Solution().kthLargestElement([1,23,12,9,30,2,50],3))
  main()



# Validate Parentheses
class Solution:
  def isValid(self, s):
    stack = []
    open_list = ["(","{","["]
    closed_list = [")","}","]"]

    for i in s:
      if i in open_list:
        stack.append(i)
      elif i in closed_list:
        position = closed_list.index(i)
        if ((len(stack) > 0) and (open_list[position] == stack[len(stack) - 1])):
          stack.pop()
        else:
          return False
    if len(stack) == 0:
      return True


# def main():
#   s = "({[)]"
#   print(Solution().isValid(s))
# main()

'''Improved Valid Parentheses Solution'''
class Solution:
  def isValid(self, s):
    stack, bracket_map = [], {"(":")","{":"}","[":"]"}

    for bracket in s:
      if bracket in bracket_map:
        stack.append(bracket_map[bracket])
      elif not stack or bracket != stack.pop():
        return False
    return not stack


# def main():
#   s = "()(){(())"
#   print(Solution().isValid(s))
# main()


# Two Sum.py
class Solution:
  def twoSum(self, list, k):
    for i in range(len(list)):
      for j in range(i + 1, len(list)):
        if (list[i] + list[j] == k):
          return True

    return False


# def main():
#   list = [4,7,1,-3,2]
#   k = 5
#   print(Solution().twoSum(list, k))
# main()



''' Find non-duplicate number '''
class Solution:
  def singleNumber(self, nums):
    for i in range(len(nums)):
      each_num_count = nums.count(nums[i])

      if each_num_count == 1:
        return nums[i]


def main():
  nums = [4, 3, 2, 4, 1, 3, 2]
  print(Solution().singleNumber(nums))
main()
