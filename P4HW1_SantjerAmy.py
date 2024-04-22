#Amy Santjer
#03/27/2024
#P4HW1
#Grade Calculator / Lists with loops 

#Ask user to enter for number of scores they would like to enter
numOfScores = int(input('How many scores do you want to enter? '))
print("")

#Create a loop to collect the number of scores the user wants to enter.
scores = [] 
for scoreNum in range(numOfScores):
    score = float(input(f"Enter score #{scoreNum + 1}: "))
    #Evaluate if the score is valid, it should be between 0 and 100.
    while score < 0 or score > 100:
        print("\nERROR: INVALID Score entered!!!!\nScore should be between 0 and 100\n")
        score = float(input(f"Enter score #{scoreNum + 1}: "))
    scores.append(score)

#Calculating scores
lowestGrade = min(scores) 
scores.remove(lowestGrade)
scoresAvg = sum(scores) / len(scores)
if scoresAvg >= 90:
        letterGrade = 'A'
elif scoresAvg >= 80:
        letterGrade = 'B'
elif scoresAvg >= 70:
        letterGrade = 'C'
elif scoresAvg >= 60:
        letterGrade = 'C'
else:
        letterGrade = 'F'

#Results
print("")
print("--------------Results----------------")
print(f'{"Lowest Score:":<20}{lowestGrade:.1f}') #Lowest score entered
print(f'{"Modified List:":<20}{scores}') #Score List after dropping lowest score
print(f'{"Scores Average:":<20}{scoresAvg:.2f}') #The average of scores in modified list
print(f'{"Grade:":<20}{letterGrade}') #Determine the letter grade for the calculated average and display it to user
print("-------------------------------------",)

