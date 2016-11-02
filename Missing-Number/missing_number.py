def missing_number(lst1, lst2):
    '''
    Compares the numbers in list1 and list2 and return the number that is not in
    both lists
    '''
    if lst1 == lst2:
        return 0
    else:
        '''Looking if a number is not in both list.'''
        for number in lst2:
            if number not in lst1:
                return number

print(missing_number([1,2], [1,2]))
