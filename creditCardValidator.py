# number = "4388576018402626"
number = "4388576018410707"
summation = 0
for num in range(len(number)-2, -1, -2):

  ''' Double every second digit from right to left. '''
  product = int(number[num]) * 2

  ''' If doubling of a digit results in a two-digit number,
   add up the two digits to get a single-digit number. '''
  if len(str(product)) == 2:
    each_num = [int(nums) for nums in str(product)]
    product = sum(each_num)

  ''' Add all single digit number '''
  summation += product

''' Add all digits in the odd places from right to left in the card number '''
summer = 0
for odd in range(len(number)-1, -1, -2):
  summer += int(number[odd])

''' Sum the results from summation and summer'''
summertosom = summation + summer

'''  '''
if summertosom % 10 == 0:
  print("Card is valid")
else:
  print("Card isn't valid")


