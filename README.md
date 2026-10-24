# Bug Fixing Using Cursor AI

An AI-assisted debugging exercise based on **Lecture — Bug Fixing Using Cursor AI**. A deliberately buggy student-marks program is debugged and corrected, demonstrating the kind of AI-assisted workflow that tools like Cursor AI enable.

## Objective

Show how AI-assisted tools can identify and fix bugs in Python code. The project contains two versions of the same student average-marks calculator:

| File | Description |
|------|-------------|
| `buggy.py` | The original program with at least three intentional bugs. |
| `fixed.py` | The corrected version with all bugs fixed. |

> **Note:** This project demonstrates AI-assisted debugging in the style of Cursor AI. Cursor itself was not used for this exercise; the debugging approach is the same.

## The Program

Both versions calculate a student's average marks across three subjects and display whether the student has passed or failed. The pass threshold is an average of **40 or above**.

### Sample Marks

| Subject | Marks (out of 100) |
|---------|-------------------|
| Math    | 80                |
| Science | 90                |
| English | 70                |

### Expected Correct Result

- Average = (80 + 90 + 70) / 3 = **80.0**
- Since 80.0 >= 40, the result is **PASS**

## Bugs Found in `buggy.py`

### Bug 1 — Incorrect average calculation

```python
total = m1 + m2 + m3 + m1   # adds m1 twice
avg = total / 4              # divides by 4 instead of 3
```

The original code adds the first mark (`m1`) a second time and divides by 4, inflating the average. With the sample marks this gives (80+90+70+80)/4 = **80.0** for the internal `average` variable — but this is coincidentally correct only because of the numbers chosen; the logic itself is wrong and would fail with other inputs (e.g. marks of 60, 60, 60 would give 75.0 instead of the correct 60.0).

**Fix:** Sum only the three marks and divide by 3.

```python
total = mark1 + mark2 + mark3
average = total / 3
```

### Bug 2 — Reversed pass/fail condition

```python
if average <= 40:
    result = "PASS"
else:
    result = "FAIL"
```

The condition is backwards — it says PASS when the average is 40 or below, and FAIL when it's above 40. With an internal average of 80.0, the buggy code prints **FAIL**.

**Fix:** PASS when average is 40 or above.

```python
if average >= 40:
    result = "PASS"
else:
    result = "FAIL"
```

### Bug 3 — Variable-name mistake (wrong variable printed)

```python
print(f"Average Marks: {science}")   # prints the science mark, not the average
```

The line is supposed to display the calculated average, but it accidentally prints the `science` variable (90) instead of the `average` variable.

**Fix:** Print the correct variable.

```python
print(f"Average Marks: {average}")
```

## How Each Bug Was Corrected

| Bug | Problem in `buggy.py` | Fix in `fixed.py` |
|-----|----------------------|-------------------|
| 1 | Extra `m1` added; division by 4 | Sum only 3 marks; divide by 3 |
| 2 | `<= 40` gives PASS (reversed) | `>= 40` gives PASS (correct) |
| 3 | Prints `science` instead of `average` | Prints `average` |

Additionally, the misspelled function name `calcuate` was corrected to `calculate_average` for clarity.

## Requirements

- **Python 3.7 or later**

No external libraries are needed.

## How to Run

Open a terminal in this folder and run:

```bash
# Run the buggy version (incorrect output)
python buggy.py

# Run the fixed version (correct output)
python fixed.py
```

## Actual Test Results

Both programs were run during development. Here is the real output:

### buggy.py output

```
===== Student Result =====
Math: 80
Science: 90
English: 70
Average Marks: 90
Result: FAIL
===== End =====
```

- **Average Marks: 90** — wrong (shows `science` instead of the average; Bug 3).
- **Result: FAIL** — wrong (pass condition is reversed; Bug 2).

### fixed.py output

```
===== Student Result =====
Math: 80
Science: 90
English: 70
Average Marks: 80.0
Result: PASS
===== End =====
```

- **Average Marks: 80.0** — correct ((80 + 90 + 70) / 3 = 80.0).
- **Result: PASS** — correct (80.0 >= 40).

The fixed program runs successfully and produces the expected correct output. Both programs were executed and their real output is shown above.

## File Structure

```
bug-fixing-using-cursor-ai/
├── buggy.py     # Original buggy program
├── fixed.py      # Corrected version
└── README.md     # This file
```

## Author

Yash Sharma — B.Tech Computer Science Engineering (AI & ML specialization)
