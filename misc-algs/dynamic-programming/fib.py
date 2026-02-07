# Fibonacci algorithms
import timeit


def naive_fib(m):
  if m <= 1:
    return m
  return naive_fib(m-1) + naive_fib(m-2)

def top_down_fib(n, f):
  if n <= 1:
    return n
  if f[n] == 0:
    f[n] = top_down_fib(n-1, f) + top_down_fib(n-2, f)
  return f[n]

def bottom_up_fib(n):
  if n <= 1:
    return n

  f = [0 for i in range(n+1)]
  f[0] = 0
  f[1] = 1

  for i in range(2, n+1):
    f[i] = f[i - 1] + f[i - 2]
  return f[n]

def alt_bu_fib(n):
  # O(1) space
  if n <= 1:
    return n
  A = 0
  B = 1
  for i in range(2, n+1):
    temp = A + B
    A = B
    B = temp
  return temp


def main():

  n_nums = 30

  for i in range(n_nums):
    print(naive_fib(i))

  for i in range(n_nums):
    print(top_down_fib(i, [0]*(i+1)))

  for i in range(n_nums):
    print(bottom_up_fib(i))

  for i in range(n_nums):
    print(alt_bu_fib(i))
  
  t_nfib = timeit.timeit(lambda: naive_fib(n_nums), number=10)
  t_tdf = timeit.timeit(lambda: top_down_fib(n_nums, [0]*(n_nums+1)), number=10)
  t_buf = timeit.timeit(lambda: bottom_up_fib(n_nums), number=10)
  t_abuf = timeit.timeit(lambda: alt_bu_fib(n_nums), number=10)
  
  print(f"First {n_nums} Fibonacci numbers. Naive alg O(phi^n): {t_nfib}, top-down-fib O(n): {t_tdf}, bottom-up-fib O(n): {t_buf}, bottom-up fib O(1) space: {t_abuf} ")

if __name__ == "__main__":
  main()

