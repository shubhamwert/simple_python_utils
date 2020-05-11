import re

msg="my Name is ramu kaka and my phone number is 444-555-2222\n and I would like to order 3 pizzas,1 diet coke,3 Burgers,1 french fry."


def getDetails(order):
    order=order.lower()
    findname=re.compile(r'name is \w+ ')
    findnumber=re.compile(r'phone number is \d{3}-\d{3}-\d{3}')
    return findname.findall(order),findnumber.findall(order)

def getOrder(order):
    orderCompile=re.compile(r'\d+\s\w+\s*\w+')
    return orderCompile.findall(order)
print("customer details are\n")
print(getDetails(msg))
print(getOrder(msg))
