#Stocks
#CS175-50L
#Michael Ivanicki 
Commission_Rate=0.03
Num_Shares=2000
Purchase_Price=40.0
Selling_Price=42.75
Amount_Paid_For_Stock=Num_Shares*Purchase_Price
Purchase_Commission=Commission_Rate*Amount_Paid_For_Stock
Total_Paid=Amount_Paid_For_Stock+Purchase_Commission
Stock_Sold_For=Num_Shares*Selling_Price
Selling_Commission=Commission_Rate*Stock_Sold_For
Total_Recieved=Stock_Sold_For-Selling_Commission
Profit_Or_Loss=Total_Recieved-Total_Paid
print('Amount paid for stock:$',Amount_Paid_For_Stock)
print('Commission paid on the purchase: $', Purchase_Commission)
print('Amount the stock sold for: $', Stock_Sold_For)
print('Commission paid on the sale: $', Selling_Commission)
print('Profit: $', Profit_Or_Loss)

