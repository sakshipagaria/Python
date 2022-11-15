def purchase(product_type,price,material,brand):
    if product_type=="Mobile":
        if brand=="Apple":
            discount=10
        else:
            discount=5
        total_price = price-price*discount/100
    else:
        if material=="leather":
            tax=5
        else:
            tax=2
        total_price=price+price*tax/100
    print("Totalprice of "+product_type+" is "+str(total_price))

purchase("Mobile",85000,"Apple",None)
purchase("Shoe",80000,None,"Leather")



---------------------------------------------
#output
Totalprice of Mobile is 80750.0
Totalprice of Shoe is 81600.0
