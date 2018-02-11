# Egan Mthembu
# A program that displays Fibonacci numbers using people's names.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Mthembu"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)


WEEK1

# Egan Mthembu 24.01.2018
# A program that displays Fibonacci numbers.

def fib(n):
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i
x = 19
ans = fib(x)
print("Fibonacci number", x, "is", ans)

Re: Fibonacci exercise responses
by EGAN MTHEMBU - Wednesday, 24 January 2018, 11:12 PM
 
Egan : E + N = 19, Fibonacci Number = 4181

C:\Users\ppc\Desktop\Fibonacci>python fib3.py

Fibonacci number 19 is 4181
