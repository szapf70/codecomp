def next_bigger(n):
    ns = list(str(n))
    pos = len(ns) - 1
    while pos:
        if ns[pos-1] < ns[pos]:
            ns[pos-1], ns[pos] = ns[pos], ns[pos-1]
            return int("".join(ns))
        pos -=1
    return -1     




print(next_bigger(144))

"""
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

  12 ==> 21
 513 ==> 531
2017 ==> 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):

  9 ==> -1
111 ==> -1
531 ==> -1

"""