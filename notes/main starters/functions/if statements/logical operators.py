high_income = True
good_credit = True
criminal_record = False

if high_income or good_credit:    #(and) can be used instead of or to make it require both true 
    print("Eligible for loan")
else:
    print("Not eligible for loan")

if good_credit and not criminal_record:
    print("Eligible for loan")
else:
    print("Not eligible for loan")