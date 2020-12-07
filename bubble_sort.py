wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
simple_list = [2, 4, 1, 0]

def bubble_sort_1(list):
    for i in range(len(list)):
        for i in range(len(list) - 1):
            value1 = list[i]
            value2 = list[i + 1]
            if(value1 > value2):
                list[i] = value2
                list[i + 1] = value1
    return list

if __name__ == "__main__":
    print(bubble_sort_1(wakeup_times))
    print(bubble_sort_1(simple_list))

    print ("Pass" if (wakeup_times[0] == 3) else "Fail")
    print ("Pass" if (simple_list[0] == 0) else "Fail")
