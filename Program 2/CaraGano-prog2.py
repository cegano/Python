# Cara Gano - Program 2

# adds exam scores added by user and calculates average of scores

sum = 0
count = 0
score = 0
   
while True:
    score = float(input("Enter an exam score to average.  Enter 9999 to quit: "))
    if score == 9999:
        break
    elif score < 0 or score > 100:
        print("Enter valid sxam score.")
        continue
    else:
        sum += score
        count += 1
        
   
average = sum / count
average = round(average, 1)

print("Average of " + str(count) + " exam scores: " + str(average))
