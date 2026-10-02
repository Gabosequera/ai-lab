"""
PCEP CONTROL FLOW PRACTICE
Project: Secure Access Terminal

Goal:
Complete the TODO sections without changing the overall structure.

Topics:
- booleans
- if / elif / else
- while loops
- for loops
- range()
- break / continue
- counters
- basic function return values

Estimated time: 25-30 minutes
Difficulty: Medium
"""


# ---------------------------------------------------------
# PART 1 — ACCESS LEVEL
# ---------------------------------------------------------

def get_access_level(age, has_badge):
    """
    Return:
        "DENIED"   -> if the person does not have a badge
        "JUNIOR"   -> if they have a badge and are under 18
        "STANDARD" -> if they have a badge and are 18 to 64
        "SENIOR"   -> if they have a badge and are 65+
    """

    # TODO 1:
    # Use if / elif / else and the boolean has_badge.
    #
    # Hint:
    # The badge should be checked BEFORE the age.

    if has_badge == True:
        if age < 18:
            return "JUNIOR"
        elif 18<= age <= 64:
            return "STANDARD"
        else:
            return "SENIOR"
    else:
        return "DENIED"
            


# ---------------------------------------------------------
# PART 2 — PIN CHECKER
# ---------------------------------------------------------

def check_pin(correct_pin):
    """
    Give the user a maximum of 3 attempts.

    Return True if they enter the correct PIN.
    Return False if they fail 3 times.
    """

    attempts = 0

    # TODO 2:
    # Create a while loop that runs while attempts < 3.
    #
    # Inside the loop:
    # 1. Ask the user for a PIN using input()
    # 2. Convert it to int
    # 3. Increase attempts by 1
    # 4. If the PIN is correct:
    #       print("Access granted.")
    #       return True
    # 5. Otherwise:
    #       print("Incorrect PIN.")
    #
    # After the loop finishes:
    # print("Too many failed attempts.")
    # return False
    
    print("HOLAAAAAAAAAAAAAAAAAA\n")

    while attempts <= 3:
        usr_pin = int(input("what is the pin?: "))
        print(usr_pin)
        attempts += 1
        if usr_pin == correct_pin:
            print("we inside if")
            print("Access Granted")
            return True 
        else:
            print("Incorrect Pin")   
            return False
    print("Too many failed attempts.")
    return False
 
    
# ---------------------------------------------------------
# PART 3 — SECURITY SCAN
# ---------------------------------------------------------

def security_scan(limit):
    """
    Scan badge numbers from 1 up to and including 'limit'.

    Rules:
    - Numbers divisible by 5 are BLOCKED.
    - Other even numbers are REVIEW.
    - Odd numbers are CLEAR.

    Print one line for every badge number.

    Example for limit = 6:

    Badge 1: CLEAR
    Badge 2: REVIEW
    Badge 3: CLEAR
    Badge 4: REVIEW
    Badge 5: BLOCKED
    Badge 6: REVIEW

    Return the number of BLOCKED badges.
    """

    blocked_count = 0

    # TODO 3:
    # Use:
    #   for
    #   range()
    #   if / elif / else
    #
    # Remember:
    # range() does NOT include its stop value.
    #
    # Useful operator:
    # number % 5 == 0

    pass


# ---------------------------------------------------------
# PART 4 — COUNTDOWN
# ---------------------------------------------------------

def lockdown_countdown(seconds):
    """
    Print a countdown from 'seconds' down to 1,
    then print "LOCKED".

    Example:
        lockdown_countdown(3)

    Output:
        3
        2
        1
        LOCKED
    """

    # TODO 4:
    # Solve this using range().
    #
    # You need a NEGATIVE step.

    pass


# ---------------------------------------------------------
# PART 5 — FIND FIRST VALID ID
# ---------------------------------------------------------

def find_first_valid_id(start, end):
    """
    Search from start to end, inclusive.

    A valid ID:
    - must be even
    - must NOT be divisible by 3

    Return the FIRST valid ID.

    If there is no valid ID, return -1.

    Example:
        find_first_valid_id(3, 10)

    Checks:
        3 -> no
        4 -> valid

    Returns:
        4
    """

    # TODO 5:
    # Use a for loop and range().
    #
    # Use 'continue' to skip IDs that are not valid.
    # Return immediately when you find the first valid one.

    pass


# ---------------------------------------------------------
# PART 6 — TRACE THIS CODE BEFORE RUNNING IT
# ---------------------------------------------------------

def mystery_score():
    score = 0

    for number in range(1, 8):

        if number == 5:
            continue

        if number % 2 == 0:
            score += number
        else:
            score -= 1

    return score


# BEFORE RUNNING THE PROGRAM:
#
# TODO 6:
# Write your prediction here:
#
# mystery_score() returns: ______
#
# Trace it:
#
# number = 1 -> score = ______
# number = 2 -> score = ______
# number = 3 -> score = ______
# number = 4 -> score = ______
# number = 5 -> score = ______
# number = 6 -> score = ______
# number = 7 -> score = ______


# ---------------------------------------------------------
# AUTOMATIC CHECKS
# ---------------------------------------------------------

from unittest.mock import patch
from contextlib import redirect_stdout
from io import StringIO


def check(name, actual, expected):
    if actual == expected:
        print(f"PASS | {name}")
    else:
        print(f"FAIL | {name}")
        print(f"       Expected: {expected}")
        print(f"       Got:      {actual}")


def main():

    print("=" * 50)
    print("           SECURE ACCESS TEST SYSTEM")
    print("=" * 50)

    passed = 0
    total = 0


    # -----------------------------------------------------
    # TEST 1 — get_access_level()
    # -----------------------------------------------------

    print("\n--- TESTING get_access_level() ---")

    tests = [
        ((17, False), "DENIED"),
        ((17, True), "JUNIOR"),
        ((18, True), "STANDARD"),
        ((35, True), "STANDARD"),
        ((64, True), "STANDARD"),
        ((65, True), "SENIOR"),
        ((80, False), "DENIED"),
    ]

    for arguments, expected in tests:

        total += 1

        actual = get_access_level(*arguments)

        if actual == expected:
            print(f"PASS | {arguments} -> {actual}")
            passed += 1
        else:
            print(f"FAIL | {arguments}")
            print("       Expected:", expected)
            print("       Got:", actual)


    # -----------------------------------------------------
    # TEST 2 — check_pin()
    # -----------------------------------------------------

    print("\n--- TESTING check_pin() ---")

    # Correct PIN on second attempt
    total += 1

    with patch("builtins.input", side_effect=["1111", "2468"]):
        with redirect_stdout(StringIO()):
            result = check_pin(2468)

    if result is True:
        print("PASS | Correct PIN eventually returns True")
        passed += 1
    else:
        print("FAIL | Expected True")
        print("       Got:", result)


    # Three incorrect PINs
    total += 1

    with patch("builtins.input", side_effect=["1111", "2222", "3333"]):
        with redirect_stdout(StringIO()):
            result = check_pin(2468)

    if result is False:
        print("PASS | Three wrong PINs returns False")
        passed += 1
    else:
        print("FAIL | Expected False")
        print("       Got:", result)


    # -----------------------------------------------------
    # TEST 3 — security_scan()
    # -----------------------------------------------------

    print("\n--- TESTING security_scan() ---")

    total += 1

    # 1 through 12:
    # blocked = 5 and 10
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    blocked = security_scan(12)

    if blocked == 2:
        print("PASS | security_scan(12) -> 2 blocked")
        passed += 1
    else:
        print("FAIL | security_scan(12)")
        print("       Expected: 2")
        print("       Got:", blocked)


    # -----------------------------------------------------
    # TEST 4 — lockdown_countdown()
    # -----------------------------------------------------

    print("\n--- TESTING lockdown_countdown() ---")

    total += 1

    output = StringIO()

    with redirect_stdout(output):
        lockdown_countdown(3)

    result = output.getvalue().strip()

    expected = """
2
1
LOCKED"""

    if result == expected:
        print("PASS | Countdown output is correct")
        passed += 1
    else:
        print("FAIL | Countdown output")
        print("Expected:")
        print(expected)

        print("Got:")
        print(result)


    # -----------------------------------------------------
    # TEST 5 — find_first_valid_id()
    # -----------------------------------------------------

    print("\n--- TESTING find_first_valid_id() ---")

    tests = [
        ((3, 10), 4),
        ((5, 15), 8),
        ((6, 7), -1),
        ((8, 20), 8),
    ]

    for arguments, expected in tests:

        total += 1

        actual = find_first_valid_id(*arguments)

        if actual == expected:
            print(f"PASS | {arguments} -> {actual}")
            passed += 1
        else:
            print(f"FAIL | {arguments}")
            print("       Expected:", expected)
            print("       Got:", actual)


    # -----------------------------------------------------
    # TEST 6 — mystery_score()
    # -----------------------------------------------------

    print("\n--- TESTING mystery_score() ---")

    total += 1

    result = mystery_score()

    if result == 9:
        print("PASS | mystery_score() -> 9")
        passed += 1
    else:
        print("FAIL | mystery_score()")
        print("       Expected: 9")
        print("       Got:", result)


    # -----------------------------------------------------
    # FINAL RESULTS
    # -----------------------------------------------------

    print("\n" + "=" * 50)
    print("                FINAL RESULT")
    print("=" * 50)

    print("Passed:", passed)
    print("Failed:", total - passed)
    print("Total:", total)

    percentage = (passed / total) * 100

    print("Score:", round(percentage, 1), "%")

    if percentage == 100:
        print("PERFECT — all functions work correctly.")

    elif percentage >= 80:
        print("GOOD — only a few things need fixing.")

    elif percentage >= 50:
        print("KEEP WORKING — several functions need attention.")

    else:
        print("REVIEW CONTROL FLOW — multiple tests are failing.")


main()