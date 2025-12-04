'''
Even and Odd Counter

Task:

Create a function count_even_odd(*numbers) that accepts any number of integers.

Count how many are even and how many are odd.

Return the result as a dictionary.

'''
#Day 10 of Learning Python
def count_even_odd (*numbers):
    even_count = 0
    odd_count = 0
    
    for n in numbers:
        if n % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            
    return {"even": even_count, "odd": odd_count}
    
print( count_even_odd(1,2,3.4,5,6,7))
print(count_even_odd(10, 12, 14, 15, 17))
print(count_even_odd())
    