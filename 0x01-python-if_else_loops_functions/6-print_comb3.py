#!/usr/bin/python3

last_number = 89

for letters in range(10):
    for num in range(letters + 1, 10):
        current_number = letters * 10 + num
        if current_number == last_number:
            print("{:02d}".format(current_number), end=" ")
        else:
            print("{:02d},".format(current_number), end=" ")
print()
