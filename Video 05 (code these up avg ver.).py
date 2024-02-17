num = 0
tot = 0.0

while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    num += 1
    tot += fval

if num > 0:
    average = tot / num
    print('ALL DONE')
    print('Total:', tot, 'Count:', num, 'Average:', average)
else:
    print('No numbers were entered')
