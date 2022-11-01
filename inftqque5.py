#chocolates

child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates():
    sum = 0
    for choco in chocolates_received:
        sum = sum + choco

    return sum

def reward_child(child_id_rewarded,extra_chocolates):
    if extra_chocolates < 1:
        print("Extra chocolates is less than 1")
    elif child_id_rewarded not in child_id:
        print("Child id is invalid")
    else:
        length = len(child_id)

        for num in range(length-1):
            if child_id_rewarded == child_id[num]:
                chocolates_received[num] = chocolates_received[num] + extra_chocolates
        print(chocolates_received)


print(calculate_total_chocolates())
#Test your code by passing different values for child_id_rewarded,extra_chocolates
reward_child(20,2)
