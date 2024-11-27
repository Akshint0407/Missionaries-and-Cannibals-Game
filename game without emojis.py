#The whole code::
#Initial Condition
boat_side = "Right"
missionaries_on_right = 3
cannibals_on_right = 3
missionaries_on_left = 0
cannibals_on_left = 0

print("Right Side")
print("M =", str(missionaries_on_left) , "C =", str(cannibals_on_left), "|---------B|", "M =", str(missionaries_on_right), "C =", str(cannibals_on_right))

while(True):
  #Boat on Right Side
  if boat_side == "Right":

    missionaries = int(input("Enter the no of Missionaries on Boat:"))
    cannibals = int(input("Enter the no of Cannibals on Boat:"))
    
    if (missionaries + cannibals)<0 or (missionaries + cannibals)>2:
        print("Invalid Move 1!!")
        continue
    else:
      if (missionaries_on_right < missionaries) or (cannibals_on_right < cannibals):
        print("Invalid Move 2!")
        continue
      
      else:
        cannibals_on_right -= cannibals
        missionaries_on_right -= missionaries

        cannibals_on_left += cannibals
        missionaries_on_left += missionaries

        print("M = ", str(missionaries_on_left), "C = ", str(cannibals_on_left), "|B----------|", " M = ", missionaries_on_right, " C = ", cannibals_on_right)
        boat_side = "Left"

#Boat on Left Side
  elif boat_side == "Left":
    missionaries = int(input("Enter the no of Missionaries on Boat:"))
    cannibals = int(input("Enter the Cannibals on Boat:"))

    if (missionaries + cannibals)<0 or (missionaries + cannibals)>2:
        print("Invalid Move 1!!")
        continue
    else:
      if (missionaries_on_left < missionaries) or (cannibals_on_left < cannibals):
        print("Invalid Move 2!")
        continue
      
      else:
        cannibals_on_left -= cannibals
        missionaries_on_left -= missionaries

        cannibals_on_right += cannibals
        missionaries_on_right += missionaries    

        print("M = ", str(missionaries_on_left), "C = ", str(cannibals_on_left), "|----------B|", " M = ", missionaries_on_right, " C = ", cannibals_on_right)
        boat_side = "Right"
        
 #Game Result
  #Losing Condition
  if ((missionaries_on_left < cannibals_on_left) and (missionaries_on_left > 0)) or ((missionaries_on_right < cannibals_on_right) and (missionaries_on_right > 0)):
    print("YOU LOSE SUCKER!")
    break
  #winning Condition
  if ((missionaries_on_left == 3) and (cannibals_on_left == 3)):
    print("YOU DID IT, YOU WON!!") #Final Condition
    break

print("GAME OVER!")
