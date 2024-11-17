def main():
    english_grade = int(input('English grade:'))
    dict = {}
    dict['English'] = english_grade
    math_grade = int(input('Math grade:'))
    dict['Math'] = math_grade
    print(dict)
    lijst = list(dict.values())
    avg = sum(lijst)/len(lijst)
    print ('Your average is', avg)

    subject = input('give the subject')
    new_grade = int(input('give the grade'))
    dict[subject] = new_grade
    lijst = list(dict.values())
    avg = sum(lijst)/len(lijst)
    print ('Your new average is', avg)


main()