import sys

#!/usr/bin/env python3
"""
Task 1 - Circular array path generator for two arrays.

Usage:
    python task1.py n1 m1 n2 m2

Example:
    python task1.py 6 3 5 4
    -> prints: 13514253
"""

def path_for(n: int, m: int) -> str:
    """
    Compute the path (concatenated start positions) for a circular array 1..n
    where each interval has length m and the next interval starts at the end
    of the previous interval. Stop when an interval ends at element 1.
    """
    if n <= 0 or m <= 0:
        raise ValueError("n and m must be positive integers")

    starts = []
    s = 1
    while True:
        starts.append(str(s))
        # end = ((s - 1) + (m - 1)) % n + 1
        end = ((s + m - 2) % n) + 1
        if end == 1:
            break
        s = end
    return "".join(starts)

def main(argv):
    if len(argv) != 4:
        print("Usage: python task1.py n1 m1 n2 m2", file=sys.stderr)
        return 2
    try:
        n1, m1, n2, m2 = map(int, argv)
    except ValueError:
        print("All arguments must be integers.", file=sys.stderr)
        return 2
    try:
        out = path_for(n1, m1) + path_for(n2, m2)
    except ValueError as e:
        print("Error:", e, file=sys.stderr)
        return 2

    print(out)
    return 0

if __name__ == "_main_":
    sys.exit(main(sys.argv[1:]))