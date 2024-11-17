import random

def remove_random(the_list):
    getal = random.randint(0,4)
    print('the removed color was', the_list[getal])
    del(the_list[getal])
    print('the remaining list is',the_list)

def main():
    colors = ['red', 'blue', 'green', 'orange']
    # Your code here
    remove_random(colors)

main()