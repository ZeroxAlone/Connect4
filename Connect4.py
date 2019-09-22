# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:08:43 2019

@author: lisa_
"""
import numpy as np

def ThisPlayerChoosesColumn(ThisPlayer):
    print("Player ", ThisPlayer, "'s turn.")
    while True:
        ColumnNumber = int(input("Enter a valid column number: "))
        if ColumnNumberVaild(ColumnNumber) == True:
            break
    return ColumnNumber

def ColumnNumberVaild(ColumnNumber):
    Valid = False
    if 0 <= ColumnNumber <= 6:
        if Board[5, ColumnNumber] == "⚫":
            Valid = True
    return Valid

def FindNextFreePositionInColumn(ValidColumn):
    ThisRow = 0
    while Board[ThisRow, ValidColumn] != "⚫":
        ThisRow+=1
    return ThisRow

Board = np.array([["","","","","","",""],
                  ["","","","","","",""],
                  ["","","","","","",""],
                  ["","","","","","",""],
                  ["","","","","","",""],
                  ["","","","","","",""]])

#InitialiseBoard
for Row in range(6):
    for Column in range(7):
        Board[Row, Column] = "⚫"
        
#SetUpGame
ThisPlayer = "◯"
GameFinished = False

#OutputBoard
for Row in range(6):
    for Column in range(7):
        print(Board[Row, Column], "  ", end = '')
    print("\n")

Count = 0

while GameFinished == False:
    if Count % 2 == 0:
        ThisPlayer = "◯"
    if Count % 2 == 1:
        ThisPlayer = "⛒"
    #ThisPlayerMakesMove
    ValidColumn = ThisPlayerChoosesColumn(ThisPlayer)
    ValidRow = FindNextFreePositionInColumn(ValidColumn)
    Board[ValidRow, ValidColumn] = ThisPlayer
    
    #OutputBoard
    for Row in range(6):
        for Column in range(7):
            print(Board[Row, Column], "  ", end = '')
        print("\n")
    
    #CheckIfThisPlayerHasWon
    WinnerFound = False
        #CheckHorizontalLineInValidRow
    for i in range(4):
        if Board[ValidRow, i] == ThisPlayer and Board[ValidRow, i + 1] == ThisPlayer and Board[ValidRow, i + 2] == ThisPlayer and Board[ValidRow, i + 3] == ThisPlayer:
            WinnerFound = True
            
    if WinnerFound == False:
            #CheckVerticalLineInValidColumn
        if ValidRow == 3 or ValidRow == 4 or ValidRow == 5:
            if Board[ValidRow, ValidColumn] == ThisPlayer and Board[ValidRow - 1, ValidColumn] == ThisPlayer and Board[ValidRow - 2, ValidColumn] == ThisPlayer and Board[ValidRow - 3, ValidColumn] == ThisPlayer:
                WinnerFound = True
    if WinnerFound == False:
            #CheckLeftObliqueLineInValidColumn
        if ValidRow == 3 or ValidRow == 4 or ValidRow == 5:
            if Board[ValidRow, ValidColumn] == ThisPlayer and Board[ValidRow - 1, ValidColumn - 1] == ThisPlayer and Board[ValidRow - 2, ValidColumn - 2] == ThisPlayer and Board[ValidRow - 3, ValidColumn - 3] == ThisPlayer:
                WinnerFound = True
    if WinnerFound == False:
            #CheckRightObliqueLineInValidColumn
        if ValidRow == 3 or ValidRow == 4 or ValidRow == 5:
            if Board[ValidRow - 3, ValidColumn + 3] == ThisPlayer and Board[ValidRow - 2, ValidColumn + 2] == ThisPlayer and Board[ValidRow - 1, ValidColumn + 1] == ThisPlayer and Board[ValidRow, ValidColumn] == ThisPlayer:
                WinnerFound = True
    if WinnerFound == True:
        GameFinished = True
        print(ThisPlayer, " is the winner.")
    else:
            #CheckForFullBoard
        BlankFound = False
        ThisRow = 0
        while True:
            ThisColumn = 0
            ThisRow+=1
            while True:
                ThisColumn+=1
                if Board[ThisRow, ThisColumn] == "⚫":
                    BlankFound = True
                if ThisColumn == 6 or BlankFound == True:
                    break
            if ThisRow == 5 or BlankFound == True:
                break
        if BlankFound == False:
            print("It is a draw.")
            GameFinished = True
        Count+=1

    