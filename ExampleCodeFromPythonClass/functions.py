def get_points(num_points):
    """Get num_points from the user. Return a list of (x,y) tuples."""
    raise NotImplementedError # will throw error because it's not implemented yet

def get_name():
    global employee_name
    employee_name = employee_name + ' ' + 'Nash'

employee_name = 'Derek'
get_name()
print('Employee name:', employee_name)



def print_sandwich(bread, meat, *args): # *args is an arbitrary argument list
    print(f'{meat} on {bread}', end=' ')
    if len(args) > 0:
        print('with', end=' ')
    for extra in args:
        print(extra, end=' ')
    print('')

print_sandwich('sourdough', 'turkey', 'mayo')
print_sandwich('wheat', 'ham', 'mustard', 'tomato', 'lettuce')
print()


def print_sandwich(meat, bread, **kwargs): # **kwargs is arbitrary number of keyword arguments
    print(f'{meat} on {bread}')
    for category, extra in kwargs.items():
        print(f'   {category}: {extra}')
    print()

print_sandwich('turkey', 'sourdough', sauce='mayo')
print_sandwich('ham', 'wheat', sauce1='mustard', veggie1='tomato', veggie2='lettuce')
