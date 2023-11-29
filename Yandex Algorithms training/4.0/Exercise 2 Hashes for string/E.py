s = input().strip()

n = len(s)
p = 10 ** 9 + 7
x_ = 257
h = [0] * (n + 1)
h_rev = [0] * (n + 2) # add fictive hash in end to not goint cursor beyond boundaries
x = [0] * (n + 1)
x[0] = 1
s = ' ' + s

for i in range(1, n+1):
    h[i] = (h[i - 1] * x_ + ord(s[i])) % p
    x[i] = (x[i - 1] * x_) % p

for i in range(n, 0, -1):
    h_idx = n+1-i
    h_rev[h_idx] = (h_rev[h_idx - 1] * x_ + ord(s[i])) % p


def isequal_reversed(from1, from2, slen):
    """
    :param from1: start index to hash massive
    :param from2: start index to reversed hash massive
    :param slen: len of of searched string to difine index in hash and reversed hash massive
    :return: True if strings are the same, else False
    """
    return (h[from1 + slen - 1] + h_rev[from2 - 1] * x[slen]) % p == \
           (h_rev[from2 + slen - 1] + h[from1 - 1] * x[slen]) % p

def binary_search(lf, rg, idx, shift):
    """
    :param lf: left of bin search of len palindrome
    :param rg: right of bin search of len palindrome
    :param idx: index symbol in array
    :param shift: shift index in reversed hash massive to even binary search
    :return: len of palindrome in odd string, len - 1 of palindrome in even string
    """
    while lf <= rg:
        mid = (lf + rg) // 2
        if isequal_reversed(idx + 1, n - idx + 1 + shift, mid):
            lf = mid + 1
        else:
            rg = mid - 1

    return lf - 1

total = 0
for i in range(1, n): # from 1 to pre-end symbol

    # boundaries of bin search
    len_rg = n - i
    len_lf = i
    len_seq = min(len_rg, len_lf)

    bin_even = binary_search(0, len_seq, i, 1) + 1  # even bin search
    bin_odd = binary_search(0, len_seq, i, 0)  # odd bin search
    total += bin_odd + bin_even

total += 1  # add end symbol palindrome
print(total)
