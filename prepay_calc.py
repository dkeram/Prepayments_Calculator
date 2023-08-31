import sys
from datetime import datetime


# This function calculate the days between two dates.
# Also calculate the amount of future and present expenses.
def prepayment_calculator(st_date, fin_date, exp_amount, fin_year):
    df_days = fin_date - st_date
    start_date = datetime(fin_year, 1, 1)
    next_year_days = fin_date - start_date
    prepayment_expenses = round((exp_amount * next_year_days) / df_days, 2)
    year_expenses = exp_amount - prepayment_expenses
    print(f'The prepaid expenses for the next year ar: {prepayment_expenses}')
    print(f'This year expenses are: {year_expenses}', '\n')


# This code runs in an infinite loop until the user give the number 2 as input.
while True:
    print('To calculate your prepayments choose 1:')
    print('To exit the program choose 2:')

    choice = int(input('Your choice: '))
    if choice == 1:

        # In this block user give a string in the right format and the code convert it to date.
        d1 = input('Give the starting date of insurance contract in format (YYYY-MM-DD): ')
        y1, m1, ds1 = map(int, d1.split('-'))
        date1 = datetime(y1, m1, ds1)
        d2 = input('Give the ending date of insurance contract in format (YYYY-MM-DD): ')
        y2, m2, ds2 = map(int, d2.split('-'))
        date2 = datetime(y2, m2, ds2)
        expenses = round(float(input('Give the amount of insurance contract: ')), 2)
        print('\n')

        prepayment_calculator(date1, date2, expenses, y2)
    elif choice == 2:
        sys.exit()
    else:
        print('Give a valid choice')
