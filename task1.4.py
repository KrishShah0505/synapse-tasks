def average_waiting_time():
    num_customers = int(input("Enter the number of customers: "))

    arrival_times = []
    time_required = []

   
    for i in range(num_customers):
        arrival_time = int(input(f"Enter arrival time for customer {i+1}: "))
        time_needed = int(input(f"Enter time required for customer {i+1}: "))

        arrival_times.append(arrival_time)
        time_required.append(time_needed)

    total_waiting_time = 0
    total_customers = 0

    current_time = 0

    for i in range(len(arrival_times)):
       
        current_time = max(current_time, arrival_times[i])

        waiting_time = current_time - arrival_times[i]

        total_waiting_time += waiting_time

        
        total_customers += 1

       
        current_time += time_required[i]

    average_time = total_waiting_time / total_customers

    print(f"Average waiting time: {average_time:.2f} minutes")

# Call the function
average_waiting_time()