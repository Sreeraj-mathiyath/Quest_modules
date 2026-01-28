"""1. One pen costs ₹10. What is the cost of 5 pens?
2. A book costs ₹200. If a 10% discount is given, what is the final price?
3. You buy 3 pencils (₹5 each) and 2 erasers (₹7 each). What is the total bill?
4. If 2 chocolates cost ₹15, how much does 1 chocolate cost?
5. A bag originally costs ₹1000. After 25% discount, how much should you pay?
6. You have ₹100. How many pens can you buy if each costs ₹12?
7. Your bill is ₹350. You give ₹500. How much change should you get back?
8. You scored 45, 50, and 55 in 3 subjects. What is the average?
9. If 1 kg of apple costs ₹80, how much for 1.5 kg?
10. A shopkeeper increases the price of ₹500 by 18%. What is the new price?
11.The original price of a phone is ₹30,000.
If a user applies two discounts — 10% and then 5% — what will be the final price?

12.A shopkeeper offers a Buy 2 Get 1 Free deal.
If each item costs ₹250, write a program to calculate the total cost for n = 7 items.

13.Mobile recharge plan:

₹199 → 28 days

₹399 → 70 days

₹599 → 100 days

If user enters balance and plan cost, calculate how many full cycles they can buy and how many days total validity they get"""

#answer1:
cost_of_one_pen=10
print("cost of 5 pens is: ",cost_of_one_pen*5)

#answer2
cost_of_one_book=200
discount_price=(cost_of_one_book*10)/100
print("Final price of book after discount: ",cost_of_one_book-discount_price)

#answer3
cost_of_one_pencil=5
cost_of_one_eraser=7
print("total cost is:",(cost_of_one_pencil*3)+(cost_of_one_eraser*2))

#answer4
cost_for_two_chocolate=15
print("price of one chocolate:",cost_for_two_chocolate/2)

#answer5
cost_of_bag=1000
discount=(cost_of_bag*25)/100
print("after discount the price of bag:",cost_of_bag-discount)

#answer6
cash_in_hand=100
price_of_one_pen=12
print("Number of pens can buy using cash in hands:",cash_in_hand//price_of_one_pen)

#answer7
bill=350
paid=500
print("balance you get:",paid-bill)

#answer8
scores=[45,50,55]
avg_mark=sum(scores)/len(scores)
print("Avg mark is:",avg_mark)

#answer9
cost_of_1kg_apple=80
print("cost for 1.5kg apple",cost_of_1kg_apple*1.5)

#answer10
price=500
new_price=price+((price*18)/100)
print("new price",new_price)

#answer11
original_price=30000
price_after_first_discount=original_price-((original_price*10)/100)
price_after_second_discount=price_after_first_discount-((price_after_first_discount*5)/100)
print(f"original price:{original_price}, price after first discount: {price_after_first_discount}, price after second discount: {price_after_second_discount}")


#answer12
cost=250
n=7
number_of_product_got_free=n//3
print("total cost :",(n-number_of_product_got_free)*cost)

#answer13
print("Recharge plans\n₹199 → 28 days\n₹399 → 70 days\n₹599 → 100 days")
plan_dic={199:28,399:70,599:100}
plan=int(input("Enter selected recharge plan:"))
amount=int(input("Enter amount:"))
cycles=amount//plan
validity=int(cycles*plan_dic[plan])
print(f"you got {cycles} full cyles and {validity} days of validity")
