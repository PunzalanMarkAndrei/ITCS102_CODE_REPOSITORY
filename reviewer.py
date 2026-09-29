owner_age = int(input("Enter your age: "))
monthly_revenue = float(input("What is your monthly revenue: "))
credit_score = int(input("Input your credit score"))
years_in_business = float(input("How many years in business"))
has_defaults = bool(input("You have defaults? True/False: "))
collateral_name = str(input("Enter your CN: "))
collateral_valuue = float(input("Enter your CV: "))

max_loan = 0.0
base_fee = 0.0

if owneer_age >= 21 and years_in_business >= 2.0 and has_defaults == False:
    print("You are Qualified")
    if credit_score >= 720: #Tier1
        max_loan = 3 * monthly_revenue
        print("High Credit Score: ")
        if monthly_revenue >= 50000: 
            print("revenue higher than 50k ")
            max_loan = base * 0.025
        else
            print("Revenue Lower than 50k")
            max_loan = base_fee * 0.025
            print("base fee rate", base_fee)

            if collateral_value >= max_loan:
                print("Collateral", collateral_name, "with the value of ", collateral_value, "is ACCEPTED")
            else:
                print("rejected: Insufficient collateral value for", collateral_name)
                      
            surge_fee_rate = max_loan * base_fee
            if max_loan % 500