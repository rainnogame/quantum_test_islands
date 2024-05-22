## Task

You have a matrix `MxN` that represents a map. There are 2 possible states on the map: `1` - islands, `0` - the ocean.
Your task is to calculate the number of islands in the most effective way. Please write code in Python 3 and provide a
github repository with a solution.

```plaintext
Inputs:

M N
Matrix

Test cases:

Input:
3 3
0 1 0
0 0 0
0 1 1
Output: 2

Input:
3 4
0 0 0 1
0 0 1 0
0 1 0 0
Output: 3

Input:
3 4
0 0 0 1
0 0 1 1
0 1 0 1
Output: 2
```

## Task analysis

- Island is a set of points on 2d matrix that are connected to each other and have value 1.
- Connected means that the point has a neighbor (up/down or left/right) that has value 1.
- From the test cases it's clear that diagonal points are not considered as connected.
- Need to write the most effective algorithm to find the number of islands. By "effective" I assume:
    - Time complexity - Execution time on specified set of tests
    - Memory complexity - Memory requirement for an algorithm on specified set of tests
    - Scalability - Algorithm behaviour with lager input size
    - Extendability - An ability to extend algorithm behaviour (E.G. change the definition of connected points to
      include diagonal points, consider 3d matrix, etc.)
    - Possible edge cases

### Recursive search

- Each point in the matrix have 0 or 1 value to represent ocean or island
- Each point can be considered as visited or not visited by algorithm
- For each point in the matrix
    - If the point is an island and not visited
        - Mark the point as visited
        - Increment the number of islands
        - Recursively check all neighbors of the point (up, down, left, right)
- In order to not create an additional matrix, we can mark visited points as 0 in the original matrix

Algorithm analysis:

Time complexity - We need to check each point in the matrix of size `MxN`. For each point we need to check 4 neighbors.
In the worst case we need `4*M*N` checks + `M*N` checks to traverse the matrix. So the time complexity is `O(M*N)`. For
the best case we still need to check `N*M` points, so the complexity will not change

Memory complexity - There's no extra space required for the algorithm. But the recursion will use the stack memory. So
the worst case memory complexity is `O(M*N)` for the case when recursion is maximum (all 1)

Edge case - Since default max recursion depth is 1000, the algorithm will not work for large input. Large input means it
has an islands with more than 1000 points connected what is not realistic if we consider 50% filled matrix. But with
higher fill rate it's possible to hit the maximum recursion depth.

Scalability - The algorithm is scalable for larger input. Considering time complexity `O(M*N)` it will work fast
enough (seconds) for large matrix up to 10000x10000 elements (complexity is linear in relation to the number of element
in matrix and quadratic in relation to the number of rows/columns). But the maximum recursion depth can be a problem for
large islands. So the fill rate is also should be considered additionally.

Extendability - The algorithm can be easily extended to include diagonal points as connected. Also, 3d can be easily
modified to 3d matrix.

## Running notes

Implemented under `python v3.12`

To install requirements:

```bash
pip install -r requirements.txt
```

To run test

```bash
pytest
```

## Algorithm description:

## Implementation notes

- Some important parts of the code were not implemented because this is a test task
    - The code is not assert input fully. It assumes that the input is a 2D matrix with 0 and 1
    - Test code is not full and written just to check test task cases

