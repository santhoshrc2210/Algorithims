'''
Sorting algorithim that caculates wether the number of
permutations to sort the list is even or odd
'''
def is_even(p):
    idx=0
    counter=0
    a_lst_copy=p
    while idx<len(p)-1:
        idx+=1
        if idx!=p[idx]:
            counter+=1
            for i in range(len(p)):
                #find the index where the number is
                idx_val=a_lst_copy.index(idx)
                curr_val_idx=a_lst_copy[idx]
                #swap these values
                a_lst_copy[idx]=idx
                a_lst_copy[idx_val]=curr_val_idx
    if counter%2==0:
        return True
    else:
        return False



       
