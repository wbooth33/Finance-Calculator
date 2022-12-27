import math

print("Investment - To calculate the amount of interest you will earn on your investment.")
print("Bond - To calculate the amount you will have to pay on a home loan.")

#Ask user to input whether they want to calculate for investment or bond.
option = input("Please enter either Investment or Bond to proceed: \n").lower()

#If option does not equal investment and option does not equal bond, print an error message.
if option != "investment" and option != "bond":
    print("Error: Please enter either Investment or Bond! \n")

#If option is equal to investment.
if option == "investment":
    #Ask user how much he will be depositing, the interest rate, how long they will be investing for and what type of interest package they require.
    deposit = float(input("How much money will you be depositing? \n"))
    interest_rate = (float(input("What is the interest rate? (No need for %) \n")) / 100)
    duration = int(input("How many years will you be investing for? \n"))
    interest = input("What type of interest package do you want? (Simple or Compound) \n").lower()

    #If simple, calculate using deposit * (1+(interest rate * duration))
    if interest == "simple":
        total_after_interest = (deposit * (1 + (interest_rate * duration)))
        print("Your total after interest will be £", round(total_after_interest, 2), "after", duration, "years!")

    #Else If compound, calculate using (deposit * (math.pow((1+interest rate), duration)))
    elif interest == "compound":
        total_after_interest = (deposit * (math.pow ((1 + interest_rate), duration)))
        print("Your total after interest will be £", round(total_after_interest, 2), "after", duration, "years!")

    #Else not simple or compound, error message.
    else:
        print("Error! Please enter either Simple or Compound")

#If option is equal to bond.
if option == "bond":
    #Ask user for house value, interest rate and repayment duration.
    house_value = float(input("What is the current value of the house? \n"))

    #Ask user for interest rate, Interest rate needs to be per month, take yearly value, divide by 100 and then divide that value by 12.

    interest_rate = (float(input("What is the interest rate? (No need for %) \n")) / 100) / 12
    repay_duration = int(input("How many months will it take you to repay the bond? \n"))

    #Repayment calcualtion is (interest rate * house value) / (1 - ((1 + interest rate) ** ( -repay duration))).
    repayment = (interest_rate * house_value) / (1 - ((1 + interest_rate) ** (-repay_duration)))
    print("Your monthly repayment is £", round(repayment, 2))

'''
Really enjoyed this capstone, it was good to see everything so far coming together.
'''



