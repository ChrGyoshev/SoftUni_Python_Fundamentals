version = input().split(".")
new_version = int("".join(version))
new_version = new_version + 1
print(".".join(str(new_version)))
