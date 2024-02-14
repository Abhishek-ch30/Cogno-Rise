import time
# Define the countdown timer function
def countdown_timer(seconds):
    while seconds:
        #calculate minutes and seconds
        mins, secs = divmod(seconds, 60)
        #format the time in "MM:SS" format
        timer_format = "{:02d}:{:02d}".format(mins, secs)
        #print a newline character to separate lines
        print('\n')
        #print the formatted time, overwriting the previous line
        print(timer_format, end='\r')
        #pause the program for 1 second
        time.sleep(1)
        #decrease the remaining seconds
        seconds -= 1

    print("\nTIME'S UP!!!")

def main():
    try:
         #gets user input for the countdown duration
        duration = int(input("Enter the countdown duration in seconds: "))
        #checks if the input is a positive number
        if duration <= 0:
            print("Please enter a positive duration.")
            return
        countdown_timer(duration)
         #handle the case where the user enters an invalid input
    except ValueError:
        print("Invalid input. Please enter a valid number.")

main()
