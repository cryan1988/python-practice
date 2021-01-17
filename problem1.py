# Build the list (note that the problem states "below" 1000,
# so we can safely use 1000 rather than 1001 in range)
multiples_of_three_and_five = [number for number in range(1,1000) if number % 3 == 0 or number % 5 == 0]

# Initialize a dummy variable at zero to hold our result
sum_of_multiples = 0

# Loop over our list, adding each number in the list to sum_of_multiples
for number in multiples_of_three_and_five:
  sum_of_multiples += number

print(sum_of_multiples)
