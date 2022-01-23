from art import logo
from game_data import data
from art import vs
import random



def options():
  choice = random.choice(data)
  return choice

def generateOutputForPerson(comparePerson, person):
  print(f"Compare {person}: {comparePerson['name']}, a {comparePerson['description']}, from {comparePerson['country']}")

def checkmorefollowers(followersA, followersB):
  if (followersA > followersB):
    return "A"
  else:
    return "B"

def increaseScore(score):
  score += 1
  return score
  



def game():
  print(logo)
  score = 0
  gameisOn = True
  compareA = ''

  while gameisOn == True:
    compareB = options()
    if (compareA == ''):
      compareA = options()
    generateOutputForPerson(compareA,"A")
    print(vs)
    generateOutputForPerson(compareB,"B")
    choice = input("Who has more followers? Type 'A' or 'B': ")
    moreFollowers = checkmorefollowers(compareA['follower_count'],compareB['follower_count'])
    if choice == moreFollowers:
      score = increaseScore(score)
      print(f"You're right! Current score: {score}")
      compareA = compareB
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      gameisOn = False
      return()




game()