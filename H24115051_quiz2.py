x = int(input("Enter the shopping amount: "))
y = input("Enter the membership level (Regular or Gold)")

if y == "Regular":  # if regular member
    if x < (2000) and x > 1000:   #if purchases is over 1000 but lower than 2000 we give 10 percent discount
       print(y,"$",x * 0.9)
    elif x < 3000 and x > 2000:  #if purchases is over 2000 but lower  than 3000 we give 15 percent discount
        print(y, "$",x * 0.85)
    elif x > 3000: #over purchase of 3000 we give 20 percent discount
        print(y, "$",x * (8/10))
    else:
        print(y,"$", x) # if purchase does not reach 1000 then there will be no discount
elif y == "Gold":  # if member has gold membership
    if x < 2000 and x > 1000:
        print(y, "$",x * 0.85) #if purchases is over 1000 but lower than 2000 we give 15 percent discount
    elif x < 3000 and x > 2000:
        print(y,"$", x * (0.80)) #if purchases is over 2000 but lower than 3000 we give 20 percent discount
    elif x > 3000:
        print(y,"$", x * 0.65)  #if purchases is over 3000  we give 25 percent discount
    else:
        print(y, "$",x)# if purchase does not reach 1000 then there will be no discount
else:
    print("Invalid membership level. Please enter 'Regular' or 'Gold'")# a condition where if user does not input a membership level