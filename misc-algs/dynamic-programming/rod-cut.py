# Rod cutting from clrs
import timeit
import random


def cut_rod(p, n):
  if n == 0:
    return 0
  q = -float('inf')
  for i in range(1,n+1):
    q = max(q, p[i-1] + cut_rod(p, n-i))
  return q


def aux(p, n, r):
  if r[n] >= 0:
    return r[n]
  if n == 0:
    q = 0
  else:
    q = -float("inf")
    for i in range(1, n+1):
      q = max(q, p[i-1] + aux(p, n-i, r))
  r[n] = q
  return q

def memoized_cut_rod(p, n):
  r = [-float("inf")]*(n + 1)
  return aux(p, n, r)


def bottom_up_rod_cut(p, n):
  r = [0] * (n+1)
  for j in range(1, n+1):
    q = -float("inf")
    for i in range(1, j+1):
      q = max(q, p[i-1] + r[j-i])
    r[j] = q
  return r[n]

def extended_bottom_up_cut_rod(p, n):
  r = [0] * (n+1)
  s = [0] * n

  for j in range(1, n+1):
    q = -float("inf")
    for i in range(1, j+1):
      if q < p[i-1] + r[j-i]:
        q = p[i-1] + r[j-i]
        s[j-1] = i
    r[j] = q
  return r, s

def print_cut_rod_solution(p, n):
  r, s = extended_bottom_up_cut_rod(p, n)
  print(f"Revenue: {r[n]}, cuts:")
  while n > 0:
    print(s[n-1])
    n = n - s[n-1]


def main():
  p = [1,5,8,9,10,17,17,20,24,30]  # [random.randint(0,100) for _ in range(20)]

  for i in range(len(p)):
    print(cut_rod(p, i))

  for i in range(len(p)):
    print(memoized_cut_rod(p, i))

  for i in range(len(p)):
    print(bottom_up_rod_cut(p, i))

  t_rec = timeit.timeit(lambda: cut_rod(p, len(p)), number = 10)
  t_dyn = timeit.timeit(lambda: memoized_cut_rod(p, len(p)), number = 10)
  t_bot = timeit.timeit(lambda: bottom_up_rod_cut(p, len(p)), number = 10)
  
  print(f"Recursive time Theta(2^n): {t_rec:.5f}, memoized time Theta(n^2): {t_dyn:.5f}, bottom up time Theta(n^2): {t_bot:.5f}")


  print("\nBottom bup with solution printing")
  print_cut_rod_solution(p, 2)
  print_cut_rod_solution(p, 3)
  print_cut_rod_solution(p, 5)

if __name__ == "__main__":
  main()
