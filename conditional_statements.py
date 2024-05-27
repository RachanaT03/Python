price = 185
if price > 100:
	print('it is costly')
	print('cannot buy')

print('end of program')

# 0 - 20 = cold
# 21 - 40 = mild
# > 40 = hot

temperature = input("temperature: ")
temperature = int('temperature')
if temperature < 20:
    print('it is cold')
    
if temperature >20 and temperature <40:
    print('it is mild')
    
if temperature > 40:
    print('it is hot')
    
    