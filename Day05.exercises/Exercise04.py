''' 
EXERCISE 4 — Age Statistics Program (Advanced)

Use this list:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

Tasks:

Sort the list

Find:

min age

max age

Add the min and max again into the list

Find:

median

average

range

Compare:

abs(min - average)

abs(max - average)

Count how many times 24 appears

Get index of:

19

26
'''
#Day 05 of learning python

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

print("---------- Sort List ----------")
ages.sort()
print(ages)

print("\n---------- MAX - MIN  ----------")
max_num = max(ages)
min_num = min(ages)

print(f"The Maximum Age is: {max_num}")
print(f"The Minimum Age is: {min_num}")


print("\n---------- MAX -MIN TO LIST ----------")
max_list = ages.insert(-1,max_num)
print(ages)
min_list = ages.insert(-1,min_num)
print(ages)

print("\n---------- RANGE ----------")
range_value = max_num - min_num
print(range_value)

print("\n---------- AVERAGE -----------")
average = sum(ages) / len(ages)
print(average)

print("\n---------- ABSOLUTE -----------")
abs_min_avg = abs(min_num - average)
abs_max_avg = abs(max_num - average)

print(abs_max_avg)
print(abs_min_avg)


print("\n---------- COUNT -----------")
count_ages = ages.count(24)
print(count_ages)


print("\n---------- MEDIAN -----------")
median = (ages[len(ages)//2] + ages[len(ages)//2 - 1]) / 2
print(median)