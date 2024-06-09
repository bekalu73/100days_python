print("Welcome to the Tip Calculator App")

totalBill= float(input("What was the total bill?\n"))
percentage= int(input("What Percentage tip would you like to give?10, 12 or 15?\n"))
split= int(input("how Many Person to Split the bill\n"));

bill=round((((percentage/100)*totalBill)+totalBill)/7,2)

print(f"Each Person Should Pay {bill}")



