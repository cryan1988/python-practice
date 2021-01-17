# Initialize dummy variable at zero for our sum
even_sum = 0

# We'll only keep track of the last two fibonacci numbers, from the problem, the first two are:
current_fibonacci = 2
previous_fibonacci = 1

# Move through the fibonacci sequence until we hit 4 million
while current_fibonacci <= 4000000:
    # If our current term is even, add it to even_sum
    if current_fibonacci % 2 == 0:
        even_sum += current_fibonacci
    # Whether or not our current term is even, move up one place in the fibonacci sequence
    # by setting the current_fibonacci variable to the sum of the current term and the
    # previous term
    current_fibonacci += previous_fibonacci
    # Since our current fibonacci is actually now two places ahead of "previous_fibonacci",
    # set previous fibonacci equal to current minus previous (essentially reversing what we did
    # to current above)
    previous_fibonacci = current_fibonacci - previous_fibonacci
    
    # continue to do this until current_fibonacci is greater than 4 million, then stop.

    
print(even_sum)
