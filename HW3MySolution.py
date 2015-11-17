# Class 3 Homework: Chipotle data - HW3MySolutions.py
# Bruce Aker - 11/9/15

import csv
from collections import defaultdict

print
# PART 1
print "Read file data\chipotle.tsv"
with open('data\chipotle.tsv', mode='rU') as f:
    file_nested_list = [row for row in csv.reader(f, delimiter='\t')]

# PART 2
print "Separate header and data"
file_nested_list_hdr = file_nested_list[0]
file_nested_list_data = file_nested_list[1:]
print "Number of data rows = " + str(len(file_nested_list_data))

# PART 3
# Get a list of just the order_id's
file_order_id_list = [r[0] for r in file_nested_list_data]

# Get distinct order_id's and then determine how many
num_orders = len(set(file_order_id_list))
#num_orders = file_order_id_list[-1]
print "Number of orders = " + str(num_orders)

# Get a nested list just containing quantity and item_price
file_nested_qty_iprice_list = [[r[1], r[4]] for r in file_nested_list_data]

# Get a list of the product of quantity and item_price (slice off $)
file_itemtotalcost_list = [int(r[0])*float(r[1][1:]) for r in file_nested_qty_iprice_list]

# Sum all the item total costs
sum_orders_cost = sum(file_itemtotalcost_list)
print "Total cost of orders = " + str(sum_orders_cost)

print "Average cost of an order = " + str(sum_orders_cost/num_orders)

# PART 4
# From rows where item_name is Canned Soda or Canned Soft Drink get the type of soda (slice off brackets)
soda_list = [r[3][1:-1] for r in file_nested_list_data if r[2] in ["Canned Soda","Canned Soft Drink"]]
print "Number of soda line items = " + str(len(soda_list))

# Get distinct soda types
soda_distinct_list = set(soda_list)
print "Distinct sodas are " + str(soda_distinct_list)[5:-2] # slice off some extra characters, e.g. 'set([' and '])'

print "Number of distinct soda types = " + str(len(soda_distinct_list))

# PART 5
# Get a nested list of burrito line items and their toppings and number of toppings (number of commas + 1 in toppings field)
burrito_toppings_list = [[r[2],r[3],r[3].count(',')+1] for r in file_nested_list_data if 'Burrito' in r[2]]
num_burritos = len(burrito_toppings_list)
print "Number of burritos ordered = " + str(num_burritos)

# Get the total number of toppings (from a temporary list containing just the count of toppings for each burrito)
num_toppings = sum([r[2] for r in burrito_toppings_list])
print "Average number of toppings per burrito = " + str((float(num_toppings))/num_burritos)

# PART 6
# Get nested list of chip orders [Qty, item_name]
chip_orders_list = [[r[1],r[2]] for r in file_nested_list_data if 'Chips' in r[2]]

# Create a dictionary and add new entries (item_name of chip order) and sum up the quantities
#chip_dict = {}
#for r in chip_orders_list:
#    if r[1] in chip_dict:
#        chip_dict[r[1]] += int(r[0])
#    else:
#        chip_dict[r[1]] = int(r[0])
chip_dict = defaultdict(int)
for r in chip_orders_list:
    chip_dict[r[1]] += int(r[0])

print chip_dict






