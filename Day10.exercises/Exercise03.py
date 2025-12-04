'''
List Analyzer

Hint:

Use built-in functions: min(lst), max(lst), sum(lst).

Calculate average as sum / len(lst).

Check if the list is empty first (if len(lst) == 0) to avoid errors.

Return all results in a dictionary.
'''

def list_analyzer(lst):
    if len(lst) == 0:
        return "List is empty"
    
    analysis = {
        "min": min(lst),
        "max": max(lst),
        "sum": sum(lst),
        "average": sum(lst) / len(lst)        
    }    
    return analysis

print(list_analyzer([1,2,3,4,5]))