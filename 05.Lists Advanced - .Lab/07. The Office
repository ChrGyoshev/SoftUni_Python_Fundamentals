employes = input().split()
factor = int(input())

employes = list(map(lambda x: int(x) * factor, employes))

filtered = list(filter(lambda x: x >= sum(employes) / len(employes), employes))

if len(filtered) >= len(employes) / 2:
    print(f"Score: {len(filtered)}/{len(employes)}. Employees are happy!")
else:
    print(f'Score: {len(filtered)}/{len(employes)}. Employees are not happy!')
