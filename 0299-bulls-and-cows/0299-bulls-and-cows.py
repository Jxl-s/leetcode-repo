class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)

        # 1. correct positions
        correct = 0
        for i in range(n):
            if secret[i] == guess[i]:
                correct += 1
        
        counts_secret = Counter(secret)
        counts_guess = Counter(guess)

        # 2. included
        included = 0
        for letter in counts_guess.keys():
            included += min(counts_guess[letter], counts_secret[letter])

        included -= correct
        return f"{correct}A{included}B"