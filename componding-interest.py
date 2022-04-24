

print("How many years will you be saving?")
years=int(input("Enter Years: "))

print("How much money is currently in your account?")
principal=float(input("Enter current amount in account: "))

print("How much money do you plan on investing monthly?")
mon_invest=float(input("Enter Amount: "))

print("What do you estimate will be the yearly interest of this investment? ")
interest=float(input("Enter interest in decimal numbers (10%=0.1): "))

print(' ')

mon_invest= mon_invest*12
final_amt=0

for i in range(0,years):
    if final_amt==0:
        final_amt=principal

    final_amt=(final_amt+mon_invest) * (1+interest)

print("This is how much money you would have in your account after {} years: ".format(years)+str(final_amt))
#THIS SCRIPT IS USED FOR CALCULATING COMPOND INTEREST. WHICH IS USED FOR DAILY LIFE