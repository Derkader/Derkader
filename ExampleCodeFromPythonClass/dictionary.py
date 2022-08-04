caffeine_content_mg = {
    'Mr. Goodbar chocolate': 122,
    'Red Bull': 33,
    'Monster Hitman Sniper energy drink': 270,
    'Lipton Brisk iced tea - lemon flavor': 2,
    'dark chocolate coated coffee beans': 869,
    'Regular drip or percolated coffee': 60,
    'Buzz Bites Chocolate Chews': 1639
}

#print(caffeine_content_mg)
print(caffeine_content_mg['Mr. Goodbar chocolate'])
caffeine_content_mg['Mr. Goodbar chocolate'] = 132
print(caffeine_content_mg['Mr. Goodbar chocolate'])

for key in caffeine_content_mg:
    print(key, caffeine_content_mg[key])
