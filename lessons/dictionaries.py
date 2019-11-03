def ninja_intro(dictionary):
    for key,val in dictionary.items():
        print(f'I am {key} and i am a {val} belt')


ninja_belts = {}

while True:
    ninja_name= input('enter a ninja name: ')
    belt = input('enter a belt color: ')
    ninja_belts[ninja_name] = belt

    another = input('add another? (y/n)')
    if another =='y':
        continue
    else:
        break
ninja_intro(ninja_belts)
