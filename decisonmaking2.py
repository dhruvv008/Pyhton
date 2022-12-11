a=int(input("Enter Pricce of product: "))

b=int(input("Enter Pricce of qty: "))
ammount=a*b
print("Billing ammount", ammount)
if ammount>1000:
    print("YOu will get discount of falt 30%")
    Discount=ammount*30/100
    ammount=ammount-Discount
    print("Ammount you pay" ,ammount)
        
elif ammount>700 :
    print("you wil get 20% Discount")

    Discount=ammount*20/100
    ammount=ammount-Discount
    print("Ammount you pay" ,ammount)

elif ammount>500:
    print("you wil get 10 Discount")

    Discount=ammount*20/100
    ammount=ammount-Discount
    print("Ammount you pay" ,ammount)
            


else:
    print("Not Eligible for this offer Sorry :)")
