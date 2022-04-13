#Michael Ivanicki
#CS 175 - 50L
#expense_pie_chart

def get_expenses_list():
    try:
        expenses_file = open('expenses.txt', 'r')
        expense_list =[]
        for n in expenses_file:
            expense = n.rsplit()
            expense_list.append(expense)    
        return (expense_list)
    except IOError: 
        print('The file expenses.txt was not found. Try again.')
def get_expense_name(expense_list):
    name_list = []
    for x in range (0, len(expense_list)):
        if x != 4:
            name_list.append (expense_list[x][0])
        if x == 4:
            name_list.append (expense_list[x][0] + ' ' + expense_list[x][1])
            
    return name_list
    
def get_expense_cost(expense_list):
    value_list = []
    for x in range (0, len(expense_list)):
        if x != 4:
            value_list.append (expense_list[x][1])
        if x == 4:
            value_list.append (expense_list[x][2])
    return value_list
    
def main():
    expense_list = get_expenses_list()
    name_list = get_expense_name(expense_list)
    value_list = get_expense_cost(expense_list)
    import matplotlib.pyplot as plt
    plt.pie(value_list, labels = name_list)
    plt.show()


if __name__ == '__main__':
    main()
