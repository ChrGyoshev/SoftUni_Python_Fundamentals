command = input()
database = {}
while not command  == "End":
    company_name, id = command.split(" -> ")
    if company_name not in database:
        database[company_name] = []
    if id not in database[company_name]:
        database[company_name].append(id)
    command = input()

for company, id in database.items():
    print(company)
    for i in id:
        print(f'-- {i}')
