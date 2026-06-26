menu_catalog = {
    'pizza': 250,
    'burger': 180,
    'pasta': 220,
    'sushi': 400,
    'salad': 120
} 

order_logs = [
    ("alice", ["pizza","burger","salad"], "Spice Hub"),
    ("bob", ["sushi","pasta"], "Zen Kitchen"),
    ("alice", ["burger","burger","pasta"], "Spice Hub"),
    ("charlie", ["pizza","sushi"], "Zen Kitchen"),
    ("bob", ["salad","pizza"], "Spice Hub") 
]


customer_spend = {} 
restaurant_revenue = {}
item_freq = {} 

total_value = 0

for customer, items, restaurant in order_logs:
    order_total = 0

    for item in items:
        order_total += menu_catalog[item]

        
        if item in item_freq:
            item_freq[item] += 1 
        else:
            item_freq[item] = 1

   
    if customer in customer_spend:
        customer_spend[customer] += order_total
    else:
        customer_spend[customer] = order_total

    
    if restaurant in restaurant_revenue:
        restaurant_revenue[restaurant] += order_total
    else:
        restaurant_revenue[restaurant] = order_total

    total_value += order_total

top_customer = max(customer_spend.items(), key=lambda x: x[1])[0]

most_ordered = ""
max_count = 0

for item in item_freq:
    if item_freq[item] > max_count:
        max_count = item_freq[item]
        most_ordered = item



avg_order_value = total_value / len(order_logs)



top_3_items = sorted(item_freq.items(), key=lambda x: x[1], reverse=True)[:3]



print("Customer Spend:", customer_spend)
print("Restaurant Revenue:", restaurant_revenue)
print("Top Customer:", top_customer)
print("Most Ordered Item:", most_ordered)
print("Average Order Value:", avg_order_value)
print("Top 3 Items:", top_3_items) 