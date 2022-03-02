#Michael Ivanicki
#CS 175 - 50L
#Grade Average Assignment
def main():
    a=0
    a, s1, s2, s3, s4, s5 = calc_average()
    determine_grade(a,s1,s2,s3,s4,s5)
    repeat()
    
def calc_average():
    for x in range (1,5):
        s1 = my_random.number()
        s2 = my_random.number()
        s3 = my_random.number()
        s4 = my_random.number()
        s5 = my_random.number()
    a=float((s1+s2+s3+s4+s5)/5)
    return a, s1, s2, s3, s4, s5

def determine_grade(a,s1,s2,s3,s4,s5):
    if s1 > 90 and s1<=100:
        g1 = ('A')
    elif s1 > 80:
        g1 = ('B')
    elif s1 > 70:
        g1 = ('C')
    elif s1 > 60:
        g1 = ('D')
    else:
        g1 = ('F')
        
    if s2 > 90 and s2<=100:
        g2 = ('A')
    elif s2 > 80:
        g2 = ('B')
    elif s2 > 70:
        g2 = ('C')
    elif s2 > 60:
        g2 = ('D')
    else:
        g2 = ('F')
        
    if s3 > 90 and s1<=100:
        g3 = ('A')
    elif s3 > 80:
        g3 = ('B')
    elif s3 > 70:
        g3 = ('C')
    elif s3 > 60:
        g3 = ('D')
    else:
        g3 = ('F')

    if s4 > 90 and s4<=100:
        g4 = ('A')
    elif s4 > 80:
        g4 = ('B')
    elif s4 > 70:
        g4 = ('C')
    elif s4 > 60:
        g4 = ('D')
    else:
        g4 = ('F')

    if s5 > 90 and s5<=100:
        g5 = ('A')
    elif s5 > 80:
        g5 = ('B')
    elif s5 > 70:
        g5 = ('C')
    elif s5 > 60:
        g5 = ('D')
    else:
        g5 = ('F')

    if a > 90 and a<=100:
        la = ('A')
    elif a > 80:
        la = ('B')
    elif a > 70:
        la = ('C')
    elif a > 60:
        la = ('D')
    else:
        la = ('F')
        
    print('Score\t\tNumeric Grade\t\tLetter Grade')
    print('----------------------------------------------------')
    print(f'score 1: \t{s1:>7}\t\t\t{g1:>7}')
    print(f'score 2: \t{s2:>7}\t\t\t{g2:>7}')
    print(f'score 3: \t{s3:>7}\t\t\t{g3:>7}')
    print(f'score 4: \t{s4:>7}\t\t\t{g4:>7}')
    print(f'score 5: \t{s5:>7}\t\t\t{g5:>7}')
    print(f'Average Score: \t{a:>8}\t\t{la:>7}')

def repeat():
    re=input('Enter yes if you would like to continue: ')
    if re=='yes':
        main()

import my_random

main()    
