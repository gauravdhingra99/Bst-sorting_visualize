
def quicksort(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x <  lst[0]])
            + [lst[0]] +
            quicksort([x for x in lst[1:] if x >= lst[0]]))

unsort_list = ['BASDASDAS', 'ASDASDASDD', 'ACDCD', 'EDSADSAD', 'LPKPJC']
sort_list   = quicksort(unsort_list)

print(sort_list) 