'''
Author: Joseph Macalinao
Credit: Lab
Description - making a set attribute calculator
Cis lab 6 Sprint 2021
'''

#initialize variables
count = 0
total_scores = 0
average = 0
high_score = 0
low_score = 100
input_grades = True
while input_grades:
    # input grades
    score = input("Enter score:")

    #check if input string is empty
    if len(score) == 0:

        #Exit loop
        input_grades = False
    #otherwise, convert input to an int and add it to
    #total score
    else:
        # #otherwise, if nothing was entered, finish entering grades
        # # # update variables

        count += 1
        score = int(score)
        total_scores = total_scores + score
        if score < low_score:
            low_score = score
        if score > high_score:
            high_score = score



#calculate average
if count > 0:
    average = total_scores / count

#output the results

    print(f'count: {count}')
    print(f'average: {average}')
    print(total_scores)
    print(f'high: {high_score}')
    print(f'low: {low_score}')
#output "no scores entered" if no scores were entered
else:
    print('No scores entered')



