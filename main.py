#greet with welcome
print("welcome to tip calculator!")
#Ask Bill amount
bill= float(input("What is your total bill?$"))
#Ask for tip
tip= int(input("how much tip would you like to give ? 10,12 or 15 :"))
#ask for people
people= int (input("How many people to split the bill? "))
#percent
tip_as_percent=tip/100
#tip amount
total_tip_amount= bill*tip_as_percent
#bill+tip
total_bill= bill+total_tip_amount
#bill for each person
bill_per_person= total_bill/people
#amount with 2 decimal 
final_amount="{:.2f}".format(bill_per_person)
#final amt
print(f"Each should pay {final_amount}")