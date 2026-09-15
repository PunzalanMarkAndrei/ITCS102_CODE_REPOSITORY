age = int(input("Enter your ager -->"))
is_employed = bool(input("Are you employed? True/False"))                                   
credits_score = int(input("What is your CREDIT SCORE -->"))
annual_income = float(input("What is your ANNUAL INCOME -->"))
has_collateral = bool(input("Do you have collateral? (true/false) --> "))

base_rate = 0.0
#tier1
if age >- 21 and is_employed == True:
    print("your are eligible")
    if 