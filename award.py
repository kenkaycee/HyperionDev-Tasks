# request user to enter time taken (in minutes) to finish triathlon events
swimming = int(input("Enter time taken to complete swimming in minutes: "))
cycling = int(input("Enter time taken to complete cycling in minutes: "))
running = int(input("Enter time taken to complete running in minutes: "))

# calculate the total time taken to complete the above three events 
total_time = swimming + cycling + running

# display award based on qualifying criteria - award is based on total time taken to complete the three triathlon events
if(total_time > 0 and total_time <= 100):
    print(f"You completed the triathlon in {total_time} minutes. You've won 'Honoray colours' award ")
elif(total_time >= 101 and total_time <= 105):
    print(f"You completed the triathlon in {total_time} minutes. You've won 'Honoray half colours' award")
elif(total_time >= 106 and total_time <= 110):
    print(f"You completed the triathlon in {total_time} minutes. You've won 'Honoray scroll' award")
elif(total_time > 110):
    print(f"You completed the triathlon in {total_time} minutes. I am sorry, you won 'No award' ")



