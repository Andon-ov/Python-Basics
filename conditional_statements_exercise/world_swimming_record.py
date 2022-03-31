record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_1_m = float(input())
delay = distance_in_meters // 15 * 12.5
total_time = time_in_seconds_for_1_m * distance_in_meters + delay
need_sec = abs(record_in_seconds - total_time)
if total_time < record_in_seconds:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {need_sec:.2f} seconds slower.")