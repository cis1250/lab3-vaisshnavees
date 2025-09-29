#!/usr/bin/env python3
# Fibonacci Sequence Exercise
def main():
    # making sure the input is a positive integer
    while True;
        user_input = input("How many terms of the Fibonacci sequence do you want? ")
        if user_input.isdigit();
            n = int(user_input)  # converting string to integer
            if n > 0:
                break  # if input is valid exiting the loop
            else:
                print("Please enter a positive integer.")
        else:
            print("Please enter a positive integer.")
    
    # print Fibonacci sequence using a for loop
  
    if n == 1:
        # if user wants 1 term print 1
        print("0")
    elif n == 2:
        #if user want 2 terms
        print("0 1")
    else:
        # for more terms useing the for loop
        fib_sequence = [0, 1] #showing the first fibnacci numbera
        
        # showing the remaining terms 
        for i in range(2, n):
            next_term = fiq_sequence[i-1] + fib_sequence[i-2]
            fib_sequence.append(next_term)  # adding a new term
        
        # making sure all numbers are turned to strings to get an output
        print(" ".join(str(term) for term in fib_sequence))

# to run the progam
if __name__ == "__main__":
    main()
