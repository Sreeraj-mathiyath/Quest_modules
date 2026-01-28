item=input("What would you like to order? ")
price=float(input("What is the price of the item? "))
overnight_delivery=bool(input("Do you want overnight delivery? 0==no, 1==yes: "))
overnight_delivery_price=5.0 if overnight_delivery else 0.0
shipping_cost=2.0 if price<10.0 else 3.0
total_cost=price+shipping_cost+overnight_delivery_price
print(f"invoice for {item}:\nitem price: ${price}\nshipping cost: ${shipping_cost}\novernight delivery: ${overnight_delivery_price}\ntotal cost: ${total_cost}"
      )