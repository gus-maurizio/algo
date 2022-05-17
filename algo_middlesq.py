seed_number = int(input("Please enter a (n)-digit number:\n[####] "))
number = seed_number
already_seen = set()
counter = 0
n = len(f'{seed_number}')
while number not in already_seen:
    counter += 1
    already_seen.add(number)
    number = int(str(number * number).zfill(n*2)[n//2:2*n-n//2])  # zfill adds padding of zeroes
    print(f"#{counter}: {number:0{n}d}")

print(f"We began with {seed_number} and"
      f" have repeated ourselves after {counter} steps"
      f" with {number}.")
