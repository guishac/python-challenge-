import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
pathout = os.path.join("Resources", "budget_analysis.txt")
budget_csv = ("budget_data.csv")
months_total = 0
total_net = 0
average_change = 0
prevmonth = 0
net_list = []
months_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
# with open("Resources/budget_data.csv", newline="") as csvfile:
with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    # next(csvreader)
    first_row = next(csvreader)

# The total number of months included in the dataset
    months_total = months_total + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])

    for row in csvreader:
         months_total = months_total + 1
        #  total_net = total_net + int(first_row[1])
        #  prev_net = int(first_row[1])
         
         total_net = total_net + int(row[1])

         net_change = int(row[1]) - prev_net
         prev_net = int(row[1])
         net_list = net_list + [net_change]
         months_list = months_list + [row[0]]


    
    # greatest increase
         if (net_change > greatest_increase[1]):
            greatest_increase[1] = net_change
            greatest_increase[0] = row[0]

         if (net_change < greatest_decrease[1]):
           greatest_decrease[0] = row[0]
           greatest_decrease[1] = net_change
        

    
average_netchange = sum(net_list)/len(net_list)


output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {months_total}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${average_netchange}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
# :.2f

print(output)

# Writing a path to the text file
filename = ("budget.txt")
with open(filename, "w") as txt_file:
    txt_file.write(output)


