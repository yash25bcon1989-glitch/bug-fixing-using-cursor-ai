"""
Student Average & Pass/Fail Calculator — BUGGY VERSION (DO NOT USE)
===================================================================
This is the ORIGINAL buggy program for the "Bug Fixing Using Cursor AI" exercise.

It contains at least three intentional bugs. The fixed version is in fixed.py.
Do NOT run this file expecting correct results — its purpose is to show
what broken code looks like before AI-assisted debugging.

Intentional bugs (DO NOT fix them here — they are fixed in fixed.py):
  Bug 1: The average is calculated incorrectly (adds an extra mark).
  Bug 2: The pass/fail condition is reversed (>= should be the check).
  Bug 3: A variable-name mistake — the wrong variable is printed in one line.
"""


def calcuate(m1, m2, m3):  # typo in function name kept as part of the mess
    """Calculate the average of three marks."""
    # BUG 1: adds m1 a second time, inflating the average
    total = m1 + m2 + m3 + m1
    avg = total / 4
    return avg


# ---- Sample student marks (out of 100) ----
# Chosen so the correct answer is easy to verify by hand:
#   Correct average = (80 + 90 + 70) / 3 = 80.0  ->  PASS
math = 80
science = 90
english = 70

print("===== Student Result =====")
print(f"Math: {math}")
print(f"Science: {science}")
print(f"English: {english}")

average = calcuate(math, science, english)

# BUG 3: prints 'science' instead of 'average' (variable-name mistake)
print(f"Average Marks: {science}")

# BUG 2: pass condition is reversed — should be >= 40 to PASS
if average <= 40:
    result = "PASS"
else:
    result = "FAIL"

print(f"Result: {result}")
print("===== End =====")
