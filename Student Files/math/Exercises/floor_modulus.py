# write the divide() function

def divide(x,y):
    uitkomst = x//y
    restwaarde = x%y
    print(x,'divided by', y, 'equals', uitkomst, 'with a remainder of', restwaarde)

def main():
    divide(5, 2)
    divide(6, 3)
    divide(12, 5)
    divide(1, 2)

main()

