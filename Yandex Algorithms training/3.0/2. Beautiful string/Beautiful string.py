with open("input.txt", encoding="UTF-8") as file_in:
    k, S = int(file_in.readline()), file_in.readline().strip()

chars, max_chars, l_pointer, r_pointer, beauty = {}, 0, 0, 0, 0


while r_pointer < len(S):

    if S[r_pointer] not in chars:
        chars[S[r_pointer]] = 0

    chars[S[r_pointer]] += 1
    max_chars = max(max_chars, chars[S[r_pointer]])

    if k < r_pointer - l_pointer - max_chars + 1:
        chars[S[l_pointer]] -= 1
        l_pointer += 1

    beauty = max(beauty, r_pointer - l_pointer + 1)
    r_pointer += 1

print(beauty)