import os
import csv
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0
with open(file_to_load) as financial_data:
   reader = csv.reader(financial_data)
# Read the header row
   header = next(reader)
# Extract first row to avoid appending to net_change_list
   first_row = next(reader)
   total_months = total_months + 1
   total_net = total_net + int(first_row[1])
   prev_net = int(first_row[1])
    # Track the total
   total_months = total_months + 1
   total_net = total_net + int(row[1])
       # Track the net change
   net_change = int(row[1]) - prev_net
   prev_net = int(row[1])
   net_change_list = net_change_list + [net_change]
   month_of_change = month_of_change + [row[0]]
       # Calculate the greatest increase
   if net_change > greatest_increase[1]:
    greatest_increase[0] = row[0]
    greatest_increase[1] = net_change
       # Calculate the greatest decrease
   if net_change < greatest_decrease[1]:
    greatest_decrease[0] = row[0]
    greatest_decrease[1] = net_change
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
print(output)

