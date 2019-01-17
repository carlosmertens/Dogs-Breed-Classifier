from time import time, sleep

# Sets start time
start_time = time()

# Replace sleep(75) below with code you want to time
sleep(75)

# Sets end time
end_time = time()

# Computes overall runtime in seconds
tot_time = end_time - start_time

# Prints overall runtime in seconds
print("\nTotal Elapsed Runtime:", tot_time, "in seconds.")

# Prints overall runtime in format hh:mm:ss
print("\nTotal Elapsed Runtime:", str(int((tot_time / 3600))) + ":" +
      str(int(((tot_time % 3600) / 60))) + ":" +
      str(int(((tot_time % 3600) % 60))))

tot_time_formatted = str(int(tot_time / 3600)) + ":" + \
                     str(int((tot_time % 3600) / 60)) + ":" + \
                     str(int(tot_time % 3600) % 60)
print("Total Elapsed Runtime in hh:mm:ss format:", tot_time_formatted)
