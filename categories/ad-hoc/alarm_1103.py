def to_min(hour,minute):
    return hour*60+minute


while True:
    h1,m1,h2,m2 = input().split()
    h1,m1,h2,m2 = int(h1),int(m1),int(h2),int(m2)
    if h1 == 0 and m1 ==0 and h2 ==0 and m2 == 0:
        break
    hour1 = to_min(h1,m1)
    hour2 = to_min(h2,m2)
    max_hour = 24*60
    if(hour1>hour2):
        hour1 = max_hour - hour1
        print(hour1+hour2)
    else:
        print(hour2-hour1)

