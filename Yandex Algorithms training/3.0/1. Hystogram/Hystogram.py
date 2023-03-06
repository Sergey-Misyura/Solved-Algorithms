s = input()

freq_dict, max_freq = {}, 0

for sym in s:
    freq_dict[sym] = freq_dict.setdefault(sym, 0) + 1

max_freq = max(freq_dict.values())
sorted_sym = sorted(freq_dict.keys())

for row_weight in range(max_freq, 0, -1):

    row = []
    for sym in sorted_sym:
        if freq_dict[sym] >= row_weight:
            row.append('#')
        else:
            row.append(' ')
    print("".join(row))

print("".join(sorted_sym))