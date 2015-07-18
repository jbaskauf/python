# cardInCombination[[card0,card1,card2],[0,1,3],[0,1,4],... ]

def generateCombinations(n):
    allCombinations=[]
    firstCard=0
    while firstCard<n-2:
        secondCard=firstCard+1
        while secondCard<n-1:
            thirdCard=secondCard+1
            while thirdCard<n:
                combination=[firstCard,secondCard,thirdCard]
                allCombinations.append(combination)
                thirdCard=thirdCard+1
            secondCard=secondCard+1
        firstCard=firstCard+1
    return allCombinations

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

def checkAttributeSuccess(attribute,combination,cards):
    attributeSame=checkCombinationAttributeForSame(attribute,combination,cards)
    attributeDifferent=checkCombinationAttributeForDifferent(attribute,combination,cards)
    if attributeSame | attributeDifferent:
        return True
    else: return False
    
def checkCombination(combination,cards):
    attribute=0
    success=True
    while attribute<4:
        if not checkAttributeSuccess(attribute,combination,cards):
            success=False
        attribute=attribute+1
    return success
        
# Here is the start of the main script
nDealtCards=12 #this should come from user input

# This is a sample set of 12 cards that should have at least two solutions
# This should also come from user input
dealtCardAttribute=[
    ['1','purple','unfilled','squiggle'],
    ['2','purple','stripes','squiggle'],
    ['1','green','stripes','squiggle'],
    ['2','red','filled','oval'],
    ['2','red','stripes','oval'],
    ['1','purple','stripes','squiggle'],
    ['2','purple','unfilled','oval'],
    ['3','green','filled','squiggle'],
    ['2','green','filled','squiggle'],
    ['3','purple','unfilled','diamond'],
    ['3','green','unfilled','diamond'],
    ['3','red','filled','diamond']
    ]
    

allCombinations=generateCombinations(nDealtCards)
nCombinations=len(allCombinations)
setIndices=[]
combinationIndex=0
while combinationIndex<nCombinations:
    combination=allCombinations[combinationIndex]
    if checkCombination(combination,dealtCardAttribute):
        setIndices.append(combination)
    combinationIndex=combinationIndex+1
    
