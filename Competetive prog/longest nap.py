import operator

def to_min(time):
    # Convert time from HH:MM format to minutes
    time = time.split(":")
    return int(time[0]) * 60 + int(time[1])

def to_date(mins):
    # Convert minutes to human-readable format (hours and minutes)
    hrs, mins = divmod(mins, 60)
    if hrs > 0:
        return "{} hours and {} minutes".format(hrs, mins)
    else:
        return "{} minutes".format(mins)

# Get the number of test inputs from the user
num_tests = int(input("Enter the number of test inputs: "))

# Iterate over each test input
for test in range(num_tests):
    print("Day #{}".format(test + 1))

    # Get the number of events for the current test input
    n = int(input("Enter the number of events: "))

    # Initialize the events list with default values
    events = [[600, 600, "10:00"], [1080, 1080, "18:00"]]

    # Read the start and end times for each event and convert them to minutes
    for i in range(n):
        line = input().strip().split()
        start = line[0]
        end = line[1]
        events.append([to_min(start), to_min(end), end])

    # Sort the events list based on the start times
    events.sort()

    # Calculate the gaps between consecutive events
    gaps = [events[i + 1][0] - events[i][1] for i in range(len(events) - 1)]

    # Find the index and duration of the longest gap
    max_id, max_val = max(enumerate(gaps), key=operator.itemgetter(1))

    # Print the information about the longest nap for the current test input
    print("Day #{}: the longest nap starts at {} and will last for {}.".format(
        test + 1, events[max_id][2], to_date(max_val)
    ))
