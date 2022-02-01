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
print('What was the commission rate?:' , Commission_Rate)
print(f'How many shares did you purchase?: {Num_Shares:,}')
print('What was the purchase price?: $',Purchase_Price)
print('What was the selling price?: $',Selling_Price)
print(f'Amount paid for stock: ${Amount_Paid_For_Stock:7,.2f}')
print(f'Commission paid on the purchase: ${Purchase_Commission:7,.2f}')
print(f'Amount the stock sold for: ${Stock_Sold_For:7,.2f}')
print(f'Commission paid on the sale: ${Selling_Commission:7,.2f}')
print(f'Profit: ${Profit_Or_Loss:7,.2f}')

