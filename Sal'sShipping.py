weight = 8.4

if  weight <= 2:
  cost_ground = weight * 1.50 + 20.00
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3.00 + 20.00
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4.00 + 20.00
elif weight > 10:
  cost_ground = weight * 4.75 + 20.00
print(cost_ground)

cost_ground_premium = 125.00
print("Ground Shipping Premium", cost_ground_premium)

if drone shipping <= 2:
  cost_ground_premium = weight * 4.50 
elif drone shipping > 2 and weight <= 6:
  cost_ground_premium = weight * 9.00
elif drone shipping > 6 and weight <= 10:
  cost_ground_premium = weight * 12.00
elif drone shipping > 10:
  cost_ground = weight * 14.25

  