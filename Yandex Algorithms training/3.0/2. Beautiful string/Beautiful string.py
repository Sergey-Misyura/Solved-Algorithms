# beautiful string
import string

alphabet = string.ascii_lowercase
k = 2
stri = 'helto'
max_beauty = 0

for letter in alphabet:

    k_curr = k
    left_border = 0
    for right_border in range(len(stri)):

        if stri[right_border] != letter or (right_border == len(stri) - 1):

            if (k_curr == 0) or (right_border == len(stri) - 1):
                cur_beauty = right_border - left_border
                max_beauty = cur_beauty if cur_beauty > max_beauty else max_beauty

                while k_curr == 0:
                    k_curr += 1 if stri[left_border] != letter else 0
                    left_border += 1

            k_curr -= 1

print(max_beauty)