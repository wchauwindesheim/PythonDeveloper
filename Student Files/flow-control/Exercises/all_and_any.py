def all_true(iterable):
    # write function
    all_is_true = True
    for num in iterable:
        if num == 0:
            all_is_true = False
    return all_is_true        

def any_true(iterable):
    # write function
    pass

def main():
    a = all_true([1, 0, 1, 1, 1])
    b = all_true([1, 1, 1, 1, 1])
    # c = any_true([0, 0, 0, 1, 1])
    # d = any_true([0, 0, 0, 0, 0])

    print(a, b) # Should be: False True True False

main()