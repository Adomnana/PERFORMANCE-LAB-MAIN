```markdown
# HT Performance Lab - Python solutions

Repository layout (each task is in its folder; the checker will pick the single .py file in each task folder):
- task1/task1.py
- task2/task2.py
- task3/task3.py
- task4/task4.py
- author.txt

Replace the contents of author.txt with: "LastName Python" (LastName in Latin letters).

Requirements:
- Python 3.8+ recommended.
- Run scripts from the repository root (examples below assume you run commands from the root).

Examples and exact terminal commands with visible outputs:

Task 1
-------
Description: process two circular arrays (n1,m1) and (n2,m2) and print combined path.

Example run (from repo root):
$ python task1/task1.py 6 3 5 4
13514253

Explanation: For n1=6,m1=3 => path 135. For n2=5,m2=4 => path 14253. Combined: 13514253

Another example:
$ python task1/task1.py 4 2 6 4
123414

Task 2
-------
Description: classify points relative to an ellipse. Two input files required.

Create `ellipse.txt`:
0 0
5 3

Create `points.txt`:
0 3
0 0
6 0

Run:
$ python task2/task2.py ellipse.txt points.txt
0
1
2

Interpretation:
0 -> on ellipse
1 -> inside
2 -> outside

Task 3
-------
Description: fill "value" fields in tests.json structure using values.json, write filled structure to report.json.

Run:
$ python task3/task3.py values.json tests.json report.json
Wrote report to report.json

The script reads values.json and tests.json and writes the filled JSON into report.json. The program accepts various reasonable formats for values.json (flat map, list of {id,value}, nested structures).

Task 4
-------
Description: minimum number of +1/-1 moves to make all array elements equal. If minimum > 20 prints the required message.

Example 1 input file `nums1.txt`:
3
6
8
9

Run:
$ python task4/task4.py nums1.txt
8

Example 2 input file `nums2.txt`:
1
16
3
20

Run:
$ python task4/task4.py nums2.txt
20 moves are not enough to bring all the elements of the array to one number.

Notes
-----
- If you prefer the first line in numbers file to be a count, remove it before running or edit the script to skip the first line.
- All scripts validate arguments and will print usage hints on incorrect invocation.
```