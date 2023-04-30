import time

def focus_timer(duration):
    start_time = time.time()
    end_time = start_time + duration
    while time.time() < end_time:
        time_left = end_time - time.time()
        print(f"\rTime left: {int(time_left // 60)}:{int(time_left % 60)}", end="")
        time.sleep(1)
    print("\nTime's up!")

duration = int(input("Enter focus duration in minutes: ")) * 60
focus_timer(duration)
