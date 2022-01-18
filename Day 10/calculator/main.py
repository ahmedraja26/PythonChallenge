#Calculator 

#add
def add(n1, n2):
  """Adds 2 numbers"""
  return n1 + n2

def multiply(n1, n2):
  """Multiply 2 numbers"""
  return n1 * n2

def divide(n1, n2):
  """divide 2 numbers"""
  return n1 / n2

def sub(n1, n2):
  """subtract 2 numbers"""
  return n1 - n2

operations = {
  "+":add,
  "-":sub,
  "/":divide,
  "*":multiply,
}

from art import logo
def calculator():
  print (logo)
  num1 = float(input("Please enter your first number: "))
  for key in operations:
    print(key)
  operation_symbol = input("Pick an operation from the line above: ")
  num2 = float(input("Please enter your second number: "))

  function = operations[operation_symbol]
  answer = function(num1, num2)
  print(f"{num1} {operation_symbol} {num2} = {answer}")

  chain = True
  check = input(f"Type y to continue calculating with {answer} or type n to exit")
  if check == "n":
    chain = False

  while chain == True:
    for key in operations:
      print(key)
    operation_symbol = input("Pick another operation from the line above: ")
    num3 = float(input("Please enter the next number: "))
    function = operations[operation_symbol]
    second_answer = function(answer,num3)

    print(f"{num1} {operation_symbol} {num2} = {second_answer}")
    check = input(f"Type y to continue calculating with {answer} or type n to exit")
    if check == "n":
      chain = False
      calculator()

calculator()