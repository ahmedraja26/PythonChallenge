from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print (logo)
bids = {}
EndAuction = False

while EndAuction == False:
  name = input("Enter You name: ")
  bid = input("Enter your bid: ")
  bids[name] = bid
  again = input("Is there another bidder: ")
  if (again == "no"):
    EndAuction = True

maxBid = 0
person = ""
for key in bids:
  bid = int(bids[key])
  if bid > maxBid:
    maxBid = bid
    person = key

print(f"The winnner is {person} with a bid of {bids[person]}")


  
