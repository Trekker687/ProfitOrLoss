ActualCost = float(input("Enter the cost of the product"))
SellingPrice = float(input("Enter the selling price of the product"))

if SellingPrice > ActualCost:
    profit = SellingPrice - ActualCost
    print("Total Profit = {}.".format(profit))
else :
    print("No profit") 
