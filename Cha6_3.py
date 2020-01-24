''' Palindrome Integer '''
def reverse(number):
  reversed_number = ""
  for num in range(len(number) - 1, -1, -1):
    reversed_number += number[num]
  return reversed_number

def isPalindrome(number):
  if number == reverse(number):
    return "Integer is Palindrome"
  else:
    return "Integer is not Palindrome"


def main():
  number = str(input("Enter a number: "))
  print(format(number) + " " + isPalindrome(number))
main()

