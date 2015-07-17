# This is a sample set of 12 cards that should have at least two solutions
dealtCardAttribute=[
    ['purple','1','unfilled','squiggle'],
    ['purple','2','stripes','squiggle'],
    ['green','1','stripes','squiggle'],
    ['red','2','filled','oval'],
    ['red','2','stripes','oval'],
    ['purple','1','stripes','squiggle'],
    ['purple','2','unfilled','oval'],
    ['green','3','filled','squiggle'],
    ['green','2','filled','squiggle'],
    ['purple','3','unfilled','diamond'],
    ['green','3','unfilled','diamond'],
    ['red','3','filled','diamond']
    ]
    
nDealtCards=12

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
