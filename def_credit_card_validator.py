# Return the first k number of digits from number. If the
# number of digits in number is less than k, return number.
def getPrefix(number, k):
  if k > getSize(number):
    return number
  return number // 10 ** (getSize(number) - k)


# Return the number of digits in d
def getSize(d):
  size = 0
  while d >= 10**size:
    size += 1
  return size


# Return true if the digit d is a prefix for number
def prefixMatched(number, d):
  return getPrefix(number, getSize(d)) == d


# Return sum of odd place digits in number
def sumOfOddPlace(number):
  total = 0
  for i in range(getSize(number), 0, -2):
    total += getPrefix(number, i) % 10
  return total


# Return this number if it is a single digit, otherwise, return
# the sum of the two digits
def getDigit(number):
  if getSize(number) <= 1:
    return number
  else:
    return number // 10 + number % 10


# Get the result from Step 2
def sumOfDoubleEvenPlace(number):
  total = 0
  for i in range(1, getSize(number) + 1, 2):
    total += getDigit(2 * getPrefix(number, i) % 10)
  return total


# Return true if the card number is valid
def isValid(number):
  # Check length of number
  if not 13 <= getSize(number) <= 16:
    return False

  # Check prefix
  if not (prefixMatched(number, 4) or prefixMatched(number, 5) \
    or prefixMatched(number, 37) or prefixMatched(number, 6)):
    return False

#   Then performing the algorithm to see if it yields a number divisible by 10
  num1 = sumOfDoubleEvenPlace(number)
  num2 = sumOfOddPlace(number)
  return (num1 + num2) % 10 == 0



def main():
  # cc = eval(input("Enter a credit card number: "))

  cc = 4388576018402626
  print(getPrefix(cc,12))
  # if isValid(cc):
  #   print("That is a valid credit card number")
  # else:
  #   print("That is not a valid credit card number")

main()
