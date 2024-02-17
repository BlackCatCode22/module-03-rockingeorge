num = 0
tot = 0.0
max_val = None
min_val = None

while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    num = num + 1
    tot = tot + fval
    if max_val is None or fval > max_val:
        max_val = fval
    if min_val is None or fval < min_val:
        min_val = fval

if num > 0:
    print('ALL DONE')
    print('Total:', tot, 'Count:', num, 'Max:', max_val, 'Min:', min_val)
else:
    print('No numbers were entered')
