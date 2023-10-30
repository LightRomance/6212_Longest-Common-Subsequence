import random
import string
import time

def generate_random_string(length):
    # Generates a string containing random characters
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def longestCommonSubsequence(str1, str2) -> (int, str):
    n1, n2 = len(str1), len(str2)
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i-1][j-1]  # Increase the LCS length by 1 when characters match
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # Take the maximum of the two adjacent cells
    # Reconstruct the LCS string
    i, j = n1, n2
    lcs = []
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs.insert(0, str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[-1][-1], ''.join(lcs)

# Test time complexity
input_sizes = [10, 50, 100, 500, 1000, 10000]  # Different lengths of strings
for size in input_sizes:
    str1 = generate_random_string(size)
    str2 = generate_random_string(size)

    if size <= 20:
        print(f"str1: {str1}")
        print(f"str2: {str2}")

    start_time = time.time()
    result_length, result_string = longestCommonSubsequence(str1, str2)
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Input size: {size}, Execution time: {execution_time:.6f} seconds")
    
    # Show LCS length and String to verify
    if size <= 100:
        print(f"Longest Common Subsequence Length: {result_length}")
        print(f"Longest Common Subsequence: {result_string}\n")
