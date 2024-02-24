reader = open('input.txt', 'r')
n = int(reader.readline().strip())
arr = [0] * n
for i in range(n):
    arr[i] = reader.readline().strip()
reader.close()

# initial array
print('Initial array:')
print(*arr, sep=', ')
# buckets forming
len_num = len(arr[0])
buckets = [[] for _ in range(10)]

# first pass, Phase 1
for num in arr:
    buckets[int(num[-1])].append(num)
print('**********', 'Phase 1', sep='\n')
print('\n'.join([f'Bucket {n}: {", ".join(bucket) or "empty"}' for n, bucket in enumerate(buckets)]))

# next passes, Phases to len_num
for phase in range(2, len_num+1):
    temp_buckets = [[] for _ in range(10)]
    for bucket in buckets:
        if bucket:
            for num in bucket:
                temp_buckets[int(num[-phase])].append(num)
    buckets = temp_buckets
    print('**********', f'Phase {phase}', sep='\n')
    print('\n'.join([f'Bucket {n}: {", ".join(bucket) or "empty"}' for n, bucket in enumerate(buckets)]))

# sorted array
print('**********', 'Sorted array:', ', '.join([', '.join(bucket) for bucket in buckets if bucket]), sep='\n')