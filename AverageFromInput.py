#AverageFromInput
#CS175-50L
#Michael Ivanicki

def main():
    numbers_file = open('numbers.txt', 'r')
    count = 0
    line = 0
    total = 0
    
    for line in numbers_file:
        count = count + 1
        total = total + float(line)
        print (f'I read in {count} number(s) Current number is: {line} Total is: {total}')
    average = total / 3
    print (f'Average: {average}')
        
    numbers_file.close()

if __name__ == '__main__':
    main()
