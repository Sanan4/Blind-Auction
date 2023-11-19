import art
from replit import clear
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
bidders = True
bidding = {}

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for i in bidding_record:
    bid_amount = bidding_record[i]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = i
  print(f"The winner is {winner} with a bid of ${highest_bid}")
  
while bidders == True:
  name = input("What's your name?: ").lower()
  bid = int(input("What is your bid?: $").lower())
  bidding[name] = bid
  other_bidders = input("Are there any others who would like to bid? Type 'yes' or 'no'. \n").lower()
  if other_bidders == "yes":
    clear()
    bidders = True
  elif other_bidders == "no":
    bidders = False
    find_highest_bidder(bidding)
  else:
    print("Sorry I only accept 'yes' or 'no' ")
