# Longest Common Subsequence

def longest_common_subsequence(X, Y):
  m = len(X)
  n = len(Y)

  # DP table init with 0s
  # shape: (m+1) x (n+1)
  dp = [[0] * (n+1) for _ in range(m+1)]

  # 1. Fill table (bottom-up)
  for i in range(1, m+1):
    for j in range(1, n+1):
      if X[i-1] == Y[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i][j-1])

  # Length of LCS is now in dp[m][n]

  # 2. Reconstruct the LCS String (Backtracking)
  lcs_str = []
  i, j = m, n
  while i > 0 and j > 0:
    # If characters match, it came from a diagonal
    if X[i-1] == Y[j-1]:
      lcs_str.append(X[i-1])
      i -= 1
      j -= 1

    # If not, move in the direction of the larger value. Ties go horizontally
    elif dp[i-1][j] >= dp[i][j-1]:
      i -=1
    
    else:
      j -= 1

  return "".join(reversed(lcs_str))

"""Intuition

First note that the problem has optimal substructure (the LCS of prefixes build up the LCS of the full strings)

Part 1:

dp[i][j] -> State answering "What is the LCS length between the first i chars of X and the first j chars of Y?"

Due to optimal substructure, make a decision at each cell based on the characters x[i - 1] and y[j - 1]

if y_j == x_i -> they contribute to LCS (add 1 to the len of the LCS from before these were processed)

if y_j != x_i -> one of the chars is useless. We carry forward the best result found so far, ignoring x_i or y_j


Part 2:

dp[m][n] holds the maximum length of the LCS -> Start by asking "How did I get this value?"

if X[i] == Y[j] -> Value came from diagonal +1, record the character and move diagonally up-left in the table

if X[i] != Y[j] -> Value was simply copied from top or left. Move to whichever neighbor has the larger value



Leetcode / Interview model:

2 Strings and an optimization problem? -> 2D Matrix pattern

1. Define state dp[i][j] = soln for s1[0..i] s2[0..j]

2. Base case row 0 and col 0 are usually 0 (LCS) or i/j (edit dist)

3. The Recurrence (choice):

if s1[i] == s2[j] -> usually dp[i-1][j-1] + 1 (or no cost)

if s1[i] != s2[j] -> usually min or max of dp[i-1][j], dp[i][j-1], and sometimes dp[i-1][j-1] (for replacement)


Cast to edit distance (minimize ops from A -> B):

x[i] == y[j] -> dp[i][j] = dp[i-1][j-1]

x[i] != y[j] -> 1 + min(insert, delete, replace)

base -> i, j (transforming empty string req's n inserts)


insert -> dp[i][j-1]

deletion -> dp[i-1][j]

replacement -> dp[i-1][j-1]
"""



def main():
  seq1 = "SPANKING"
  seq2 = "AMPUTATION"
  
  result = longest_common_subsequence(seq1, seq2)

  print(f"The longest common subsequence of {seq1} and {seq2} is: {result}.")


if __name__ == "__main__":
  main()

# Time complexity: O(mxn) -> Fill a table of m+1 x n+1 w/ constant work per call

# Space complexity: O(mxn) -> Store a table of m+1 x n+1

