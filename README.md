# Prepayment Calculator

## The idea
The idea behind this little block of code came then I was struggling in my current job (Accountant) to
calculate the expenses let's say of a insurance contract, which started in 2023-07-31 and will be expired in 2024-07-31.

## How it Works
The code starts by importing necessary modules, including sys and datetime.

The prepayment_calculator function takes the starting date (st_date), ending date (fin_date) and expense amount (exp_amount) as inputs. It calculates the number of days between st_date and fin_date, as well as the number of days between the start of the ending year and fin_date. Then, it calculates prepayment expenses and year expenses based on the provided formulas and prints the results.

The main loop of the program (while True:) allows the user to choose between two options:

Choosing '1' runs the prepayment calculation process.

Choosing '2' exits the program using sys.exit().

If an invalid choice is made, the user is informed that their choice is not va
