import random
import time
import sys
import os
row1 = [0,0,0,0,0,0,0] #all of the rows
row2 = [0,0,0,0,0,0,0]
row3 = [0,0,0,0,0,0,0]
row4 = [0,0,0,0,0,0,0]
row5 = [0,0,0,0,0,0,0]
row6 = [0,0,0,0,0,0,0]
rows = [row1,row2,row3,row4,row5,row6]
player1vertwin=0
player2vertwin=0
player1horiwin=0
player2horiwin=0
#clearing command to clear the system after a message is sent
def clear():
  input()
  if os.name == 'nt':
        _ = os.system('cls')
  else:
      _ = os.system('clear')
#clearing command for after a
def clear2():
  if name == 'nt':
        _ = system('cls')
  else:
      _ = system('clear')
#writing command for instructions or text reponses
def typer(write):
  for i in write:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.1)
def gbprint(): #prints the gameboard
  for x in range(0,5):
    rowsC = rows[x]
    for y in range(0,7):
      if rowsC[y]==0:
        rowsC[y]="░" 
      elif rowsC[y]==1:
        rowsC[y]="•" 
      elif rowsC[y]==2:
        rowsC[y]="█"
    print(rowsC)
def check4win():
  player1vertwin=0 # these variables determine if the player has won
  player2vertwin=0
  player1horiwin=0
  player2horiwin=0
  for y in range(0,5):
    for x in range(0,7):
      rows2=rows[y]
      if rows2[x] == 1:
        player1horiwin += 1
        player2horiwin = 0
      elif rows2[x] == 2:
        player2horiwin += 1
        player1horiwin = 0
  for y in range(0,7):
    for x in range(0,5):
      rows2=rows[y]
      if rows2[x] == 1:
        player1vertwin += 1
        player2vertwin = 0
      elif rows2[x] == 2:
        player2vertwin += 1
        player1vertwin = 0
def place(z,y): #z is playernumber, y is column
  for x in range (0,6):
    rowsA=rows[x]
    rowsB=rows[x-1]
    while rowsA[y]==0:
      rowsA[y-1] = z
      rowsB[y-1] = 0
  time.sleep(0.2)
  gbprint()
  
typer("This Is The Tutorial. \nPress the Enter/Return Key To Go To The Next Message \n")
clear()
place(1,3)
typer("Hello Human with a Brain! \nWelcome To Circles And Squares. \nThe goal of the game is simple: \n ")
