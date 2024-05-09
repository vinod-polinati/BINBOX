import random
import numpy as np
import csv

# Define item properties ranges
length_min, length_max = 10, 50
width_min, width_max = 5, 30
height_min, height_max = 5, 20
weight_min, weight_max = 0.1, 10  # kg

# Define fragility probabilities
fragility_options = ["Very Fragile", "Fragile", "Normal"]
fragility_probs = [0.1, 0.2, 0.7]

# Function to generate item data
def generate_item_data():
  length = random.uniform(length_min, length_max)
  width = random.uniform(width_min, width_max)
  height = random.uniform(height_min, height_max)
  weight = random.uniform(weight_min, weight_max)
  fragility = np.random.choice(fragility_options, p=fragility_probs)
  stackable = random.choice([True, False])
  return {"length": length, "width": width, "height": height, "weight": weight, 
          "fragility": fragility, "stackable": stackable}

# Generate data for multiple orders
order_data = []
for _ in range(1000):  # Generate 1000 orders (adjust as needed)
  num_items = random.randint(1, 10)  # Random number of items per order (1-10)
  order_items = [generate_item_data() for _ in range(num_items)]
  order_data.append({"date": generate_random_date(), "items": order_items})

# Save data to CSV file
with open("order_data.csv", 'w', newline='') as csvfile:
  fieldnames = ["date", "items"]
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()
  for order in order_data:
    writer.writerow(order)

print("Order data saved to order_data.csv")
