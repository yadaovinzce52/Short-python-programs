weight = 41.5

#Ground Shipping
ground_cost = 0
premium_flat_rate = 125.00
flat_rate = 20
if weight <= 2:
  ground_cost = flat_rate + (weight * 1.50)
if weight > 2 and weight <= 6:
  ground_cost = flat_rate + (weight * 3.00)
if weight > 6 and weight <= 10:
  ground_cost = flat_rate + (weight * 4.00)
if weight > 10:
  ground_cost = flat_rate + (weight * 4.75)

ground_cost = round(ground_cost, 2)
print('Ground cost of ' + str(weight) + 'lbs package: $' + str(ground_cost))
print('Premium ground shipping cost: $' + str(premium_flat_rate))

#Drone Shipping
drone_cost = 0
if weight <= 2:
  drone_cost = weight * 4.50
if weight > 2 and weight <= 6:
  drone_cost = weight * 9.00
if weight > 6 and weight <= 10:
  drone_cost = weight * 12.00
if weight > 10:
  drone_cost = weight * 14.25

drone_cost = round(drone_cost, 2)
print('Drone cost of ' + str(weight) + 'lbs package: $' + str(drone_cost))