seq = []

cur = int(input().strip())
while cur != -2*10**9:
    seq.append(cur)
    cur = int(input().strip())


seq_type = 'CONSTANT'
if len(seq) >= 2:
    if seq[1] > seq[0]:
        seq_type = 'ASCENDING'
    elif seq[0] > seq[1]:
        seq_type = 'DESCENDING'


if len(seq) >= 3:
    for i in range(1, len(seq)):
        if seq_type != 'RANDOM':

            if seq_type == 'CONSTANT':
                if seq[i] > seq[i - 1]:
                    seq_type = 'WEAKLY ASCENDING'
                elif seq[i] < seq[i - 1]:
                    seq_type = 'WEAKLY DESCENDING'

            if seq_type == 'ASCENDING':
                if seq[i] == seq[i - 1]:
                    seq_type = 'WEAKLY ASCENDING'
                elif seq[i] < seq[i - 1]:
                    seq_type = 'RANDOM'

            if seq_type == 'DESCENDING':
                if seq[i] == seq[i - 1]:
                    seq_type = 'WEAKLY DESCENDING'
                elif seq[i] > seq[i - 1]:
                    seq_type = 'RANDOM'


            if seq_type == 'WEAKLY ASCENDING' and seq[i] < seq[i - 1]:
                seq_type = 'RANDOM'

            if seq_type == 'WEAKLY DESCENDING' and seq[i] > seq[i - 1]:
                seq_type = 'RANDOM'


print(seq_type)