#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
terms = 0
while terms<=0:
  terms= int(input("How many terms of the Fibonacci sequence do you want"))
  if terms<=0:
      print("Please enter a positive integer")

a=0
b=1
for i in range (terms):
  print (a, end" ")
  a, b = b, a+b

  
