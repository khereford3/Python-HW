# Function to calculate time saved in minutes
def calculate_time_saved(average_speed, speed_limit, distance):
    time_at_speed_limit = distance / speed_limit * 60  # time in minutes at speed limit
    time_at_average_speed = distance / average_speed * 60  # time in minutes at average speed
    time_saved = time_at_speed_limit - time_at_average_speed
    return time_saved

# Get user input
average_speed = float(input("Enter your average speed (mph): "))
speed_limit = float(input("Enter the speed limit (mph): "))
distance = float(input("Enter the distance traveled (miles): "))

# Calculate time saved
time_saved = calculate_time_saved(average_speed, speed_limit, distance)

# Print the result
print(f"You saved {time_saved:.25} minutes.")
