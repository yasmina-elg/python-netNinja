my_name = 'ryu'

def print_name():
    global my_name
    my_name = 'yoshi'
    print('the name is: ', my_name)

print_name()
print('outside the name is: ', my_name)
