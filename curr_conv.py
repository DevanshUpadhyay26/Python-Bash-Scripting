#Currency converter
rates = {'USD':76.49 ,'EUR':80.43, 'RUB':1.13, 'Yuan':11.50, 'Yen':0.59, 'AUD':54.39, 'SGD':55.14} #currency rates with respect to INR 

print('Available currency codes: ')
print('- USD (US Dollar)')
print('- EUR (Euro)')
print('- RUB (Russian Rouble)')
print('- Yuan (Chinese Yuan)')
print('- Yen (Japanese Yen)')
print('- AUD (Australian Dollar)')
print('- SGD (Singapore Dollar)')
print('------------------------------------------------------------------------------')
to_curr = input('Enter Currency code to convert from: ')

if to_curr in rates.keys():
    print('Enter Amount in', to_curr, ': ', end="")
    amt = float(input())
    op = amt*(rates[to_curr])
    print(amt, to_curr, '=',op, 'INR')
else:
    print("Enter Valid Currency code")
    
