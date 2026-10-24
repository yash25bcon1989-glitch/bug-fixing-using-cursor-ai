"""
Student Average & Pass/Fail Calculator — FIXED VERSION
=======================================================
This is the corrected version of buggy.py, produced through AI-assisted
debugging in the style of Cursor AI.

All three bugs from the original have been fixed:
  Fix 1: The average is now calculated correctly — sum of three marks / 3.
  Fix 2: The pass condition now uses >= 40 for PASS (and < 40 for FAIL).
  Fix 3: The average variable is now printed (not 'science' by mistake).
The function name was also corrected for clarity.
"""


def calculate_average(mark1, mark2, mark3):
    """Return the average (mean) of three marks."""
    total = mark1 + mark2 + mark3
    average = total / 3
    return average


# ---- Sample student marks (out of 100) ----
# Easy to verify by hand: (80 + 90 + 70) / 3 = 80.0 -> PASS
math = 80
science = 90
english = 70

print("===== Student Result =====")
print(f"Math: {math}")
print(f"Science: {science}")
print(f"English: {english}")

average = calculate_average(math, science, english)

# Fix 3: print the actual average, not the wrong variable
print(f"Average Marks: {average}")

# Fix 2: pass if average is 40 or above, fail otherwise
if average >= 40:
    result = "PASS"
else:
    result = "FAIL"

print(f"Result: {result}")
print("===== End =====")
