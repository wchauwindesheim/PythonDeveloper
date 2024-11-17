import math

def split_list(orig_list):    
    # split the list with 3 numbers
    # begin = 0
    # eind
    # midden = berekening met len van de lijst

    midden = math.ceil(float(len(orig_list))/2)
    first_half = orig_list[0:midden]
    second_half = orig_list[midden:]
    return first_half, second_half


def main():
    colors = ["red", "blue", "green", "orange", "purple"]
    colors_split = split_list(colors)
    print(colors_split[0])
    print(colors_split[1])

main()