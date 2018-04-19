# python allows for multi line statements using
# the line continuation character (\)

price_one = 1.99
price_two = 2.45
price_three = 15.09

total = price_one + \
        price_two + \
        price_three

print(total)

# statements contained within the [], {}, or () brackets
# do not need to use the line continuation character

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

print(days)