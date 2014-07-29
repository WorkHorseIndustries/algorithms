"""
    radix_sort.py

    Implements a radix sort on a list of integers, or objects that can be 
    converted to integers, and returns a list sorted by there integer 
    representation order.

    Radix Sort Overview:
    --------------------
    A sorting algortim that groups values by their significant position and 
    value. 

    Time Complexity: O(kN) 
    k = The largest place value of the second largest number (or numerical 
    representation) in the list.

    Space Complexity: O(k+N)

    Stable: Yes

    Psuedo code: http://en.wikipedia.org/wiki/Radix_sort

"""



def sort(seq):
    while:
        non_zero_count = 0
        buckets = {}
        mod_num += 10
        for item in seq:
            key = int(item) % mod_num 
            if key > 0:
                non_zero_count += 1

            buckets[key] = buckets.get(key, []).append(item)
        seq = []
        for i in xrange(9):
            seq += buckets.get(i, [])
        if non_zero_count > 0:
            break

    return seq







