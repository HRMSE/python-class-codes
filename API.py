client = Client(key, secret)


# different order functions for binance exchange:

# market buy order:
buy = client.order_market_buy(symbol=pair, quantity=quantity)


# market sell order:
sell_tp_base = client.order_market_sell(symbol=pair, quantity=quantity)


# limit buy:
limitBuy = client.order_limit_buy(symbol=symbol, quantity=quantity, price=price)

# limit sell:
limitSell = client.order_limit_sell(symbol=symbol, quantity=quantity, price=price)




# turn scientific notation  to normal notation:
a = 0.0000000002
print(f'{a:-17.8f}')



# print variable in a string
a = "ali"
print(f"hello {a}")
