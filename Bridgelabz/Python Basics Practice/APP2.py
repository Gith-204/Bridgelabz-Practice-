#Program 1: OOPS Banner
print(" ***     ***    ******    ***** ")
print("**  **  **  **  **   **  **   **")
print("**  **  **  **  **   **  **     ")
print("**  **  **  **  ******    ***** ")
print("**  **  **  **  **            **")
print("**  **  **  **  **            **")
print("**  **  **  **  **            **")
print(" ***     ***    **       ***** ")
print("                                 ") 

#Program 2: EMI Calculator
principal_entered = input("Enter the principal amount: ")
roi_entered = input("Enter the rate of interest: ") 
years_entered = input("Enter the time in years: ") 

principal = principal_entered.isdigit() and int(principal_entered) or None 
roi = roi_entered.isdigit() and float(roi_entered) or None 
years = years_entered.isdigit() and int(years_entered) or None 
if (principal is not None and roi is not None and years is not None and principal > 0 and roi > 0 and years > 0):
    interest_per_month = round(1 * roi / 12 * 100, 2) 
    months = years * 12 
    emi = round(principal * interest_per_month * (1 + interest_per_month) ** months / ((1 + interest_per_month) ** months - 1), 2) 
    balance = principal
    print(f"{'-' * 65}")
    print(f"| {'Month': ^8} | {'EMI': ^10} | {'Interest' : ^10}", 
          f"| {'Principal': ^10} | {'Balance': ^10} |") 
    
    total_month = total_emi = total_interest = total_principal = 0.0
    for month in range(1, months + 1):
        interest = round(balance * roi / (12 * 100), 2) 
        principal = round(emi - interest, 2) 
        balance = round(balance - principal, 2)
        if balance < 0:
            principal = round(principal + balance, 2) 
            emi = round(principal + interest, 2) 
            balance = 0
            total_month += 1; total_emi += emi; total_interest += interest; total_principal += principal
            print(f"| {month: ^8} | {emi: ^10} | {interest : ^10}", 
                  f"| {principal: ^10} | {balance: ^10} |") 
            print(f"{'-' * 65}") 
            print(f"{'Total' : ^8} | {total_emi: ^10.2f} | {total_interest : ^10.2f}")