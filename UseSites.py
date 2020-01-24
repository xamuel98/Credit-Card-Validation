''' Selection Sort '''

nums = [5,8,9,1,3,2]
for i in range(len(nums)):
  _min = i
  for j in range(i + 1, len(nums)):
    if (nums[j] < nums[_min]):
      _min = j
  nums[i], nums[_min] = nums[_min], nums[i]

for i in range(len(nums)):
  print(nums[i], end=" ")
print()

''' Insertion Sort '''
for j in range(1, len(nums)):
  key = nums[j]
  i = j - 1
  while i > 0 and nums[i] > key:
    nums[i + 1] = nums[i]
    i -= 1
  nums[i + 1] = key

for i in range(len(nums)):
  print(nums[i], end=" ")








