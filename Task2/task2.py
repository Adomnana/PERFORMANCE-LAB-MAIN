import sys
from decimal import Decimal, getcontext, InvalidOperation

# Increase precision for wide-ranging rational inputs
getcontext().prec = 60

def parse_pair(line: str):
    parts = line.strip().split()
    if len(parts) != 2:
        raise ValueError(f"Expected two numbers on the line, got: {line!r}")
    return Decimal(parts[0]), Decimal(parts[1])

def classify_points(ellipse_path: str, points_path: str):
    with open(ellipse_path, "r", encoding="utf-8") as f:
        lines = [l for l in (ln.strip() for ln in f) if l != ""]
    if len(lines) < 2:
        raise ValueError("Ellipse file must contain at least two non-empty lines.")
    x0, y0 = parse_pair(lines[0])
    a, b = parse_pair(lines[1])
    if a == 0 or b == 0:
        raise ValueError("Ellipse radii must be non-zero.")

    with open(points_path, "r", encoding="utf-8") as f:
        point_lines = [l for l in (ln.strip() for ln in f) if l != ""]

    out = []
    for line in point_lines:
        x, y = parse_pair(line)
        try:
            dx = (x - x0) / a
            dy = (y - y0) / b
        except (InvalidOperation, ZeroDivisionError):
            raise ValueError("Invalid numeric operation when scaling coordinates.")
        val = dx * dx + dy * dy
        if val == Decimal(1):
            out.append("0")
        elif val < Decimal(1):
            out.append("1")
        else:
            out.append("2")
    return out

def main(argv):
    if len(argv) != 2:
        print("Usage: python task2.py ellipse_file points_file", file=sys.stderr)
        return 2
    try:
        results = classify_points(argv[0], argv[1])
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        return 2
    for r in results:
        print(r)
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))