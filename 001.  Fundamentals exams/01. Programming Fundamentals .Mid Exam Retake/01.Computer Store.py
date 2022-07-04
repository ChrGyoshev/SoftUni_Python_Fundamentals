queue = int(input())
lift_state = list(map(int, input().split()))
MAX_WAGON = 4
max_lift_state = len(lift_state) *MAX_WAGON

for el in range(len(lift_state)):
    to_be_seated = MAX_WAGON - lift_state[el]
    if queue - to_be_seated <0:
        to_be_seated = queue
    lift_state[el]+= to_be_seated
    queue -= to_be_seated

if queue <=0 and sum(lift_state)<max_lift_state:
    print("The lift has empty spots!")
    print(*lift_state, sep=" ")
elif queue > 0 and sum(lift_state)>=max_lift_state:
    print(f"There isn't enough space! {queue} people in a queue!")
    print(*lift_state,sep=" ")
else:
    print(*lift_state, sep=" ")