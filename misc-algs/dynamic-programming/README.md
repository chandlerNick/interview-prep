# Dynamic programming


Big Idea: When you have repeated subproblems (repeated work), save the results instead of recomputing them.

Top down: Start with the largest sub-problem and break it down, typically recursively, checking first if you have the needed sub-problem result

Bottom Up: Start with the smallest sub-problems to build up to the biggest subproblem, checking at each step to see if you already have the result.

Often algorithms with a recursive solution / formulation will have a dynamic programming alternative (e.g. nth fibonacci number, backprop, rod cutting, etc)

Also note that dynamic programming allows you to take some solutions from exponential time to polynomial time. This is goes from infeasible to feasible.

