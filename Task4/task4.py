import sys

def read_ints_from_file(path: str):
    vals = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if s == "":
                continue
            vals.append(int(s))
    return vals

def min_moves_to_equal(nums):
    if not nums:
        return 0
    nums_sorted = sorted(nums)
    n = len(nums_sorted)
    if n % 2 == 1:
        med = nums_sorted[n//2]
        moves = sum(abs(x - med) for x in nums_sorted)
    else:
        med1 = nums_sorted[n//2 - 1]
        med2 = nums_sorted[n//2]
        moves1 = sum(abs(x - med1) for x in nums_sorted)
        moves2 = sum(abs(x - med2) for x in nums_sorted)
        moves = min(moves1, moves2)
    return moves

def main(argv):
    if len(argv) != 1:
        print("Usage: python task4.py numbers_file", file=sys.stderr)
        return 2
    try:
        nums = read_ints_from_file(argv[0])
    except Exception as e:
        print("Error reading numbers file:", e, file=sys.stderr)
        return 2
    moves = min_moves_to_equal(nums)
    if moves <= 20:
        print(moves)
    else:
        print("20 moves are not enough to bring all the elements of the array to one number.")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))