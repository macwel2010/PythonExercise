p_share_no = 2000
p_share_price = 40
p_commi = 0.03
s_share_no = 2000
s_share_price = 42.75
s_commi = 0.03
p_money_paid = p_share_no*p_share_price
p_commi_paid = p_money_paid * p_commi
s_money_sold = s_share_no* s_share_price
s_commi_sold = s_money_sold*s_commi
amt_money_made = s_money_sold-p_money_paid-p_commi_paid-s_commi_sold
print(f'the amount of money joe paid for the stock is ${p_money_paid}')
print(f'the amount of commision joe paid for the stocks is ${p_commi_paid}')
print(f'the amount of money for which joe sold the stocks is ${s_money_sold}')
print(f'the amount of commision paid for selling stocks is ${s_commi_sold}')
print(f'total profit made by joe is ${amt_money_made}')