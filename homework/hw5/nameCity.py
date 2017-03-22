(first,last,city) = input('Enter the first name, last name, and the city of the person (comma-separated): ').lower().replace(' ', '').split(',')

def dummy(i):
    j = 0 if i == 0 else 1 if i == 1 else 2 if i == 2 else 'j is not in [0,1,2]'
    return j
