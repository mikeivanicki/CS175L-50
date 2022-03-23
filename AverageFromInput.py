#AverageFromInput
#CS175-50L
#Michael Ivanicki

def main(): #5
    try:
        numbers_file = open('numbers.txt', 'r')
        count = 0 #10
        line = 0
        total = 0 
        for line in numbers_file:
            try:
                count = count + 1 #15
                total = total + float(line)
                print (f'I read in {count} number(s) Current number is: {line} Total is: {total}')
            except ValueError: #20
                print('There was an error in one of the values in numbers.txt')
        average = total / 3
        print (f'Average: {average}')
        numbers_file.close()
    except IOError:
        print('Error: The file numbers.txt not found')
if __name__ == '__main__':
    main()
#25
