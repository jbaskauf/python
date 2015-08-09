# cardInCombination[[card0,card1,card2],[0,1,3],[0,1,4],... ]

import tkinter
from tkinter import *
from tkinter import ttk
import pdb

# will be a list of which each item is a dealt card
# each dealt card is itself a list of the values of the four attributes of that card
dealtCardAttribute=[]

# a list of values of the four attributes of the card being generated from the attribute buttons
newCard=["","","",""]

# creates a list of 15 empty combinations of cards
counter=0
while counter<15:
    dealtCardAttribute.append(list(newCard))
    counter=counter+1

# this generates all possible combinations of 3 cards
# returns a list of three-card combinations (where cards are represented by position numbers based on the order in which they were dealt)
def generateCombinations(n):
    allCombinations=[]
    firstCard=0
    while firstCard<n-2:
        if dealtCardAttribute[firstCard]!=["","","",""]:
            secondCard=firstCard+1
            while secondCard<n-1:
                if dealtCardAttribute[secondCard]!=["","","",""]:
                    thirdCard=secondCard+1
                    while thirdCard<n:
                        if dealtCardAttribute[thirdCard]!=["","","",""]:
                            combination=[firstCard,secondCard,thirdCard]
                            allCombinations.append(combination)
                        thirdCard=thirdCard+1
                secondCard=secondCard+1
        firstCard=firstCard+1
    return allCombinations

# checks one combination of cards to see if a particular attribute of the cards in the combination is the same for all three
def checkCombinationAttributeForSame(attribute,combination,cards):
    firstCardIndex=combination[0]
    secondCardIndex=combination[1]
    thirdCardIndex=combination[2]
    if cards[firstCardIndex][attribute]==cards[secondCardIndex][attribute]:
        if cards[firstCardIndex][attribute]==cards[thirdCardIndex][attribute]:
            test=True
        else:test=False
        return test
    else: test=False
    return test

# checks one combination of cards to see if a particular attribute is different
def checkCombinationAttributeForDifferent(attribute,combination,cards):
    firstCardIndex=combination[0]
    secondCardIndex=combination[1]
    thirdCardIndex=combination[2]
    if cards[firstCardIndex][attribute]!=cards[secondCardIndex][attribute]:
        if cards[firstCardIndex][attribute]!=cards[thirdCardIndex][attribute]:
            if cards[secondCardIndex][attribute]!=cards[thirdCardIndex][attribute]:
                test=True
            else: test=False
            return test
        else:test=False
        return test
    else: test=False
    return test

# determines if the instances of a given attribute within a combinaton are all different or all the same
def checkAttributeSuccess(attribute,combination,cards):
    attributeSame=checkCombinationAttributeForSame(attribute,combination,cards)
    attributeDifferent=checkCombinationAttributeForDifferent(attribute,combination,cards)
    if attributeSame | attributeDifferent:
        return True
    else: return False

# runs the same/different test for all four attributes for a given combination
# if True, the combination is a set
def checkCombination(combination,cards):
    attribute=0
    success=True
    while attribute<4:
        if not checkAttributeSuccess(attribute,combination,cards):
            success=False
        attribute=attribute+1
    return success

# the function called to handle clicking any of the number buttons - puts clicked attribute into newCard list
def defineNumber(string):
    newCard[0]=string
    number.set(string)

# the function called to handle clicking any of the color buttons - puts clicked attribute into newCard list
def defineColor(string):
    newCard[1]=string
    color.set(string)

# the function called to handle clicking any of the fill buttons - puts clicked attribute into newCard list
def defineFill(string):
    newCard[2]=string
    fill.set(string)

# the function called to handle clicking any of the shape buttons - puts clicked attribute into newCard list
def defineShape(string):
    newCard[3]=string
    shape.set(string)
    
# when the Add Card button is clicked, adds the new card (list) to the end of the list of dealt cards
# clears display values for the new card
# also puts the value of newCard into the text of a radiobutton
def changeCard(newCard,dealtCardAttribute):       
    dealtCardAttribute[buttonIndex.get()]=list(newCard)
    cardsOnTable[buttonIndex.get()].config(text=number.get()+" "+color.get()+" "+fill.get()+" "+shape.get())
    #cardsOnTable[buttonIndex.get()] refers to radiobutton number "buttonIndex"
    color.set("")
    shape.set("")
    fill.set("")
    number.set("")
    selected=findNextEmpty(buttonIndex)
    #cardsOnTable[3]                #we need to figure out how to make it select the next empty button

def deleteCard():       
    dealtCardAttribute[buttonIndex.get()]=["","","",""]
    cardsOnTable[buttonIndex.get()].config(text="no card")
    color.set("")
    shape.set("")
    fill.set("")
    number.set("")

# selects the next empty radiobutton
def findNextEmpty(currentButton):
    button=0
    while button<15:
        if dealtCardAttribute[button][0]=="":
            if dealtCardAttribute[button][1]=="":
                if dealtCardAttribute[button][2]=="":
                    if dealtCardAttribute[button][3]=="":
                        return button
        button=button+1
    return currentButton

# this checks for sets and stores the card combinations in the set index list
# steps through all generated combinations and checks whether each should be added to the list of sets
def findSets(dealtCardAttribute):
    allCombinations=generateCombinations(len(dealtCardAttribute))
    nCombinations=len(allCombinations)
    setIndices=[]
    combinationIndex=0
    while combinationIndex<nCombinations:
        combination=allCombinations[combinationIndex]
        if checkCombination(combination,dealtCardAttribute):
            setIndices.append(combination)
        combinationIndex=combinationIndex+1
    return setIndices

# the function called to handle clicking the "Are there sets?" button
def areThereSets(dealtCardAttribute):
    if len(findSets(dealtCardAttribute))==0:
        result="no"
    else: result="yes"
    answer.set(result)

# the function called to handle clicking the "How many sets?" button
def numberSets(dealtCardAttribute):
    result=len(findSets(dealtCardAttribute))
    answer.set(result)

# the function called to handle clicking the "What are the sets?" button
def displaySets(dealtCardAttribute):
    result=findSets(dealtCardAttribute)
    answer.set(result)
    
def buttonPress():
    print(buttonIndex.get())



#this is the main script

root = Tk()

# this sets up the characteristics of the window
root.title("Set Wizard")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# establishes grid of buttons and labels
number = StringVar()
ttk.Button(mainframe, text="1", command=lambda: defineNumber("1")).grid(column=3, row=3, sticky=W)
ttk.Button(mainframe, text="2", command=lambda: defineNumber("2")).grid(column=4, row=3, sticky=W)
ttk.Button(mainframe, text="3", command=lambda: defineNumber("3")).grid(column=5, row=3, sticky=W)
ttk.Label(mainframe, textvariable=number).grid(column=6, row=3, sticky=(W, E))

color = StringVar()
ttk.Button(mainframe, text="purple", command=lambda: defineColor("purple")).grid(column=3, row=4, sticky=W)
ttk.Button(mainframe, text="green", command=lambda: defineColor("green")).grid(column=4, row=4, sticky=W)
ttk.Button(mainframe, text="red", command=lambda: defineColor("red")).grid(column=5, row=4, sticky=W)
ttk.Label(mainframe, textvariable=color).grid(column=6, row=4, sticky=(W, E))

fill = StringVar()
ttk.Button(mainframe, text="unfilled", command=lambda: defineFill("unfilled")).grid(column=3, row=5, sticky=W)
ttk.Button(mainframe, text="striped", command=lambda: defineFill("striped")).grid(column=4, row=5, sticky=W)
ttk.Button(mainframe, text="filled", command=lambda: defineFill("filled")).grid(column=5, row=5, sticky=W)
ttk.Label(mainframe, textvariable=fill).grid(column=6, row=5, sticky=(W, E))

shape = StringVar()
ttk.Button(mainframe, text="squiggle", command=lambda: defineShape("squiggle")).grid(column=3, row=6, sticky=W)
ttk.Button(mainframe, text="oval", command=lambda: defineShape("oval")).grid(column=4, row=6, sticky=W)
ttk.Button(mainframe, text="diamond", command=lambda: defineShape("diamond")).grid(column=5, row=6, sticky=W)
ttk.Label(mainframe, textvariable=shape).grid(column=6, row=6, sticky=(W, E))

# this is the grid of test buttons
ttk.Button(mainframe, text="Change Card", command=lambda: changeCard(newCard, dealtCardAttribute)).grid(column=6, row=7, sticky=W)
ttk.Button(mainframe, text="Delete Card", command=lambda: deleteCard()).grid(column=7, row=7, sticky=W)


answer=StringVar()
ttk.Button(mainframe, text="Are there sets?", command=lambda: areThereSets(dealtCardAttribute)).grid(column=3, row=8, sticky=W)
ttk.Button(mainframe, text="How many sets?", command=lambda: numberSets(dealtCardAttribute)).grid(column=4, row=8, sticky=W)
ttk.Button(mainframe, text="What are the sets?", command=lambda: displaySets(dealtCardAttribute)).grid(column=5, row=8, sticky=W)

# this is the answer row
ttk.Label(mainframe, textvariable=answer).grid(column=3, row=9, sticky=(W,E))


# creates a table of radiobuttons
button=0
buttonIndex = IntVar()
cardsOnTable={}
for button in range (0,15): # for some reason final endpoint is not included in range but initial endpoint is
    cardsOnTable[button]=ttk.Radiobutton(mainframe, text="no card", variable=buttonIndex, value=button, command=lambda button=button: buttonPress())
    cardsOnTable[button].grid(column=button%3+3, row=int(button/3+11), sticky=W)



mainloop()
