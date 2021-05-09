import random
ran = random.randint(1, 9)
inp = int(input("Guess the number between 1 to 9 " ))
inp1 = 0
if(inp != ran):
     if(inp > ran):
          print("guess a lower number ")
          inp = int(input())
     elif(inp < ran):
          print("guess a higher number ")
          inp = int(input())
     else:
          print("Congratulations you won!")
          inp = int(input())