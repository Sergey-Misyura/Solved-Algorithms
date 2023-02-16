"""
299. Bulls and Cows
(Medium complexity)

You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. 
When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. 
Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. 
Note that both secret and guess may contain duplicate digits.
"""

class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        bulls, cows = 0, 0
        secret_dict, guess_dict = defaultdict(int), defaultdict(int)

        for num_s, num_g in zip(secret, guess):
            if num_s == num_g: bulls+=1
            else:secret_dict[num_s], guess_dict[num_g] = secret_dict[num_s]+1, guess_dict[num_g]+1

        cows = sum(min(secret_dict[i], guess_dict[i]) for i in secret_dict)

        return f'{bulls}A{cows}B'