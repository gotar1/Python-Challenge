# PyBank Data Code:
import os
import csv
# pybank_csv = os.path.join('..', 'Resources', 'budget_data.csv')
# V.S code csv filepath
pybank_csv = os.path.join('.', 'Desktop', 'repos', 'Python-Challenge', 'PyBank', 'Resources', 'budget_data.csv')

def average(list1): 
    return round((sum(list1) / len(list1)), 2)
with open(pybank_csv) as csvfile:
    bank_reader = csv.reader(csvfile, delimiter = ",") 
    csv_header = next(bank_reader)
    total_month = 0
    month_inc_list = []
    month_dec_list = []
    new_list = []
    positive_numbers = []
    negative_numbers = []
    for row in bank_reader:
        # total_month += 1
        new_list.append(int(row[1]))
        total_months = len(new_list)
        if int(row[1]) >= 0:
            positive_numbers.append(int(row[1]))
            month_inc_list.append(str(row[0]))
            greatest_increase = max(positive_numbers)
            index_num_inc = positive_numbers.index(greatest_increase)
            month_inc = month_inc_list[index_num_inc]
        elif int(row[1]) < 0:   
            negative_numbers.append(int(row[1]))
            month_dec_list.append(str(row[0]))
            greatest_decrease = min(negative_numbers)
            average_change = average((negative_numbers))
            index_num_dec = negative_numbers.index(greatest_decrease)
            month_dec = month_dec_list[index_num_dec]
    for row in bank_reader:
        if row[1] == greatest_increase:
            month_inc_list.append(str(row[0]))
    print(f"Total Months: {total_months}")       
    print(f"Total: ${sum((new_list))}")
    print(f"Average Change:  ${average_change}")
    print(f"Greatest Increase in Profits:  {month_inc} (${greatest_increase})")
    print(f"Greatest Decrease in Profits:  {month_dec} (${greatest_decrease})")
    # print(new_list)
   

    

   