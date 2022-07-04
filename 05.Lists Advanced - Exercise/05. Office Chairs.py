rooms = int(input())
chairs_available = 0
enough = True
for n in range (1,rooms + 1):
    chairs, visitors = input().split()
    chairs = len(chairs)
    visitors = int(visitors)
    if chairs < visitors:
        enough = False
        print(f'{abs(chairs-visitors)} more chairs needed in room {n}')
        continue
    chairs_available += chairs - visitors

if enough :
    print(f"Game On, {chairs_available} free chairs left")
