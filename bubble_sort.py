wakeup_times = [16, 49, 3, 12, 56, 49, 55, 22,
                13, 46, 19, 55, 46, 13, 25, 56, 9, 48, 45]
simple_list = [2, 4, 1, 0]


def bubble_sort_1(l):
    for iteration in range(len(l)):
        for index in range(1, len(l)):
            this = l[index]
            prev = l[index - 1]

            if prev <= this:
                continue

            l[index] = prev
            l[index - 1] = this


# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24, 13), (21, 55), (23, 20),
               (22, 5), (24, 23), (21, 58), (24, 3)]


def bubble_sort_2(l):
    for iteration in range(len(l)):
        for i in range(1, len(l)):
            this_hour, this_min = l[i]
            prev_hour, prev_min = l[i - 1]
            if prev_hour > this_hour or (prev_hour == this_hour and prev_min > this_min):
                continue

            l[i] = (prev_hour, prev_min)
            l[i - 1] = (this_hour, this_min)
    

if __name__ == "__main__":
    bubble_sort_2(sleep_times)
    print("Pass" if (sleep_times == [
        (24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)]) else "Fail")

    bubble_sort_1(wakeup_times)
    bubble_sort_1(simple_list)

    # print("Pass" if (wakeup_times[0] == 3) else "Fail")
    # print("Pass" if (simple_list[0] == 0) else "Fail")
