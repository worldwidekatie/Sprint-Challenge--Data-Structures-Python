import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
old_end_time = end_time - start_time
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"Original runtime: {old_end_time} seconds")

start_time = time.time()
# My approach
for i in names_1:
    if i in names_2:
        duplicates.append(i)
end_time = time.time()
new_end_time = end_time - start_time

print (f"New runtime: {new_end_time} seconds")
print(f"Runtime improved by {old_end_time - new_end_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# original runtime 6.554 Seconds
# new runtime 1.49 seconds