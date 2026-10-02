"""
Python Collections: Lists, Tuples, Sets & Dictionaries
PCEP Objective: PCEP-30-02 3.1 (lists), 3.2 (tuples and dictionaries)
Difficulty: Beginner / Intermediate

DESCRIPTION:
Eight functions, two for each collection type. Each pair shows off what
makes that collection special AND the rule that limits it: lists can
change (which can surprise you), tuples cannot change, sets throw away
duplicates, and dictionaries crash on missing keys.

LEARNING OBJECTIVES:
- Modify a list in place and make a copy when the original must stay safe
- Pack, unpack, and "replace" values in a tuple without changing it
- Use sets to remove duplicates and compare groups (| & - ^)
- Build dictionaries, handle repeated keys, and look up keys safely

EXPECTED OUTCOMES:
After completing this assignment, students will be able to:
- Choose the right collection type for a job and explain why
- Predict when a list will be changed by a function
- Explain why tuples and sets raise the errors they do
- Avoid a KeyError with .get() or the "in" operator

INSTRUCTIONS:
1. Read each function's docstring carefully. The examples show exactly
   what your function should return.
2. Replace "pass" (or the TODO comments) with your own code.
3. Run this file. The tests at the bottom print PASS or FAIL for
   each function.
4. Keep going until every function prints PASS.
"""


# =====================================================================
# PART 1: LISTS  [ ]   Ordered, changeable, duplicates allowed
# =====================================================================

def add_to_lineup(lineup, name, vip=False):
    """
    Add a person to a lunch line (a list). VIPs go to the FRONT of the
    line; everyone else goes to the END.

    This function demonstrates that lists are ORDERED and CHANGEABLE:
    you change the list that was passed in. Do NOT create a new list.
    Duplicates are allowed, so the same name can be in line twice.

    Parameters:
        lineup (list): the current line of names (will be changed)
        name (str): the person joining the line
        vip (bool): True if the person goes to the front

    Returns:
        None: nothing is returned. The original list is changed.

    Example:
        >>> line = ["Ava", "Ben"]
        >>> add_to_lineup(line, "Cy")
        >>> line
        ['Ava', 'Ben', 'Cy']
        >>> add_to_lineup(line, "Dee", vip=True)
        >>> line
        ['Dee', 'Ava', 'Ben', 'Cy']
        >>> add_to_lineup(line, "Ava")
        >>> line
        ['Dee', 'Ava', 'Ben', 'Cy', 'Ava']

    Hint: Look at the list methods .append() and .insert().
    """
    if vip == True:
        lineup.insert(0, name)
    else:
        lineup.append(name)



def top_scores(scores, n):
    """
    Return the n highest scores, largest first, WITHOUT changing the
    original list.

    This function demonstrates the danger of lists being changeable.
    If you call scores.sort(), you rearrange the caller's list too!
    Your function must leave the original list exactly as it was.

    Parameters:
        scores (list): a list of numbers (must NOT be changed)
        n (int): how many top scores to return

    Returns:
        list: a NEW list of the n highest scores, largest first.
              If n is bigger than the list, return all of them.

    Example:
        >>> quiz = [72, 95, 88, 61, 95]
        >>> top_scores(quiz, 3)
        [95, 95, 88]
        >>> quiz
        [72, 95, 88, 61, 95]
        >>> top_scores([50, 80], 5)
        [80, 50]

    Hint: sorted() returns a new list, and it has a reverse=True option.
          A slice like my_list[:n] also makes a new list.
    """
    new_list = sorted(scores, key=int, reverse=True)
    return new_list[:n]


# =====================================================================
# PART 2: TUPLES  ( )   Ordered, unchangeable
# =====================================================================

def stats_summary(numbers):
    """
    Return the lowest value, highest value, and average of a list of
    numbers, all packed into ONE tuple.

    This function demonstrates tuple PACKING: a function can only
    return one thing, but that one thing can be a tuple holding several
    values. The caller can then UNPACK it:
        low, high, avg = stats_summary([4, 9, 1, 7])

    Parameters:
        numbers (list): a non-empty list of numbers

    Returns:
        tuple: (lowest, highest, average), with the average rounded
               to 1 decimal place

    Example:
        >>> stats_summary([4, 9, 1, 7])
        (1, 9, 5.2)
        >>> low, high, avg = stats_summary([10, 20])
        >>> high
        20

    Hint: min(), max(), sum(), len() and round() are all built in.
    """
    new_list = sorted(numbers, key=int)
    low = new_list[0]

    new_list.sort(reverse=True)
    high = new_list[0]
    
    avg = sum(new_list) / len(new_list)
    
    return low, high, round(avg, 1)


def replace_in_tuple(original, index, new_value):
    """
    "Change" one item in a tuple by building a brand-new tuple.

    This function demonstrates that tuples are UNCHANGEABLE (immutable).
    The line  original[index] = new_value  raises a TypeError. Instead,
    build a new tuple from slices of the old one plus the new value.
    The original tuple must stay the same.

    Parameters:
        original (tuple): the starting tuple
        index (int): the position to replace (0 or higher, and valid)
        new_value: the value to put at that position

    Returns:
        tuple: a NEW tuple with the item at index replaced

    Example:
        >>> color = (255, 128, 0)
        >>> replace_in_tuple(color, 1, 64)
        (255, 64, 0)
        >>> color
        (255, 128, 0)
        >>> replace_in_tuple(("a", "b", "c"), 0, "z")
        ('z', 'b', 'c')

    Hint: Tuples can be sliced and joined with +. Remember that a
          one-item tuple needs a comma: (new_value,)
    """
    pass  # TODO: Implement this function


# =====================================================================
# PART 3: SETS  { }   Unordered, no duplicates
# =====================================================================

def unique_visitors(visit_log):
    """
    A website logs a username every time someone visits. Return how
    many DIFFERENT people visited, plus their names in alphabetical
    order.

    This function demonstrates that sets automatically REMOVE
    DUPLICATES. It also shows that sets have NO ORDER: you cannot
    index a set, so you must turn it into a sorted list to put the
    names in order.

    Parameters:
        visit_log (list): usernames, one per visit (repeats allowed)

    Returns:
        tuple: (count, names) where count is an int and names is a
               sorted list of the unique usernames

    Example:
        >>> unique_visitors(["cy", "ava", "cy", "ben", "ava", "cy"])
        (3, ['ava', 'ben', 'cy'])
        >>> unique_visitors([])
        (0, [])

    Hint: set() removes duplicates. sorted() works on a set and
          returns a list.
    """
    pass  # TODO: Implement this function


def compare_clubs(club_a, club_b):
    """
    Compare the members of two clubs using set operations.

    This function demonstrates SET MATH, something lists cannot do
    directly:
        a | b   union         (in either club)
        a & b   intersection  (in both clubs)
        a - b   difference    (in a but not b)
        a ^ b   symmetric difference (in exactly one club)

    Parameters:
        club_a (set): names of members in the first club
        club_b (set): names of members in the second club

    Returns:
        dict: a dictionary with these four keys, each holding a set:
              "both", "only_a", "only_b", "either"

    Example:
        >>> robotics = {"Ava", "Ben", "Cy", "Dee"}
        >>> cyber = {"Cy", "Dee", "Eli"}
        >>> result = compare_clubs(robotics, cyber)
        >>> sorted(result["both"])
        ['Cy', 'Dee']
        >>> sorted(result["only_a"])
        ['Ava', 'Ben']
        >>> sorted(result["only_b"])
        ['Eli']
        >>> len(result["either"])
        5

    Hint: Be careful: club_a - club_b is NOT the same as club_b - club_a.
    """
    result = {}
    # TODO: Fill in the four keys using set operators
    return result


# =====================================================================
# PART 4: DICTIONARIES  {key: value}   Look up by key
# =====================================================================

def build_gradebook(names, scores):
    """
    Build a dictionary that maps each student's name to their score.
    The two lists line up: names[0] goes with scores[0], and so on.

    This function demonstrates that dictionary KEYS ARE UNIQUE. If a
    name appears twice (the student retook the quiz), the later score
    REPLACES the earlier one. There can never be two "Ben" keys.

    Parameters:
        names (list): student names (may contain repeats)
        scores (list): scores, same length as names

    Returns:
        dict: {name: score}, keeping the LAST score for repeated names

    Example:
        >>> build_gradebook(["Ava", "Ben", "Cy"], [92, 85, 78])
        {'Ava': 92, 'Ben': 85, 'Cy': 78}
        >>> build_gradebook(["Ava", "Ben", "Ben"], [92, 70, 88])
        {'Ava': 92, 'Ben': 88}

    Hint: Loop over the positions with range(len(names)). Assigning
          gradebook[key] = value adds a new key OR replaces an old one.
    """
    gradebook = {}
    # TODO: Add each name and score to the gradebook
    return gradebook


def grade_report(gradebook, students):
    """
    Create a report line for each student in a list. Some of the
    students might NOT be in the gradebook.

    This function demonstrates the dictionary's biggest trap: using
    gradebook[name] with a missing key raises a KeyError and crashes
    the program. Use .get() or the "in" operator to handle missing
    students safely.

    Parameters:
        gradebook (dict): {name: score}
        students (list): the names to report on, in order

    Returns:
        list: one string per student, in the same order:
              "Name: score"         if the student is in the gradebook
              "Name: not enrolled"  if the student is not

    Example:
        >>> book = {"Ava": 92, "Ben": 88}
        >>> grade_report(book, ["Ben", "Zoe", "Ava"])
        ['Ben: 88', 'Zoe: not enrolled', 'Ava: 92']
        >>> grade_report(book, [])
        []

    Hint: f"{name}: {score}" builds a string like "Ben: 88".
    """
    pass  # TODO: Implement this function


# =====================================================================
# TESTS: Run this file to check your work. Do not change below here.
# =====================================================================

def check(label, actual, expected):
    """Print PASS or FAIL for one test and return True if it passed."""
    if actual == expected:
        print(f"  PASS  {label}")
        return True
    print(f"  FAIL  {label}")
    print(f"        expected: {expected!r}")
    print(f"        got:      {actual!r}")
    return False


def run_test(name, test_function):
    """Run one group of tests, catching errors so later tests still run."""
    print(f"\nTesting {name}...")
    try:
        results = test_function()
        return all(results)
    except Exception as error:
        print(f"  ERROR {type(error).__name__}: {error}")
        return False


def test_add_to_lineup():
    line = ["Ava", "Ben"]
    returned = add_to_lineup(line, "Cy")
    r = [check("returns None (changes the list instead)", returned, None),
         check("regular person goes to the end", line, ["Ava", "Ben", "Cy"])]
    add_to_lineup(line, "Dee", vip=True)
    r.append(check("VIP goes to the front", line, ["Dee", "Ava", "Ben", "Cy"]))
    add_to_lineup(line, "Ava")
    r.append(check("duplicates are allowed", line, ["Dee", "Ava", "Ben", "Cy", "Ava"]))
    empty = []
    add_to_lineup(empty, "Eli", vip=True)
    r.append(check("VIP joins an empty line", empty, ["Eli"]))
    return r


def test_top_scores():
    quiz = [72, 95, 88, 61, 95]
    r = [check("top 3, largest first", top_scores(quiz, 3), [95, 95, 88]),
         check("original list NOT changed", quiz, [72, 95, 88, 61, 95]),
         check("n bigger than the list", top_scores([50, 80], 5), [80, 50]),
         check("n is 0", top_scores(quiz, 0), [])]
    return r


def test_stats_summary():
    result = stats_summary([4, 9, 1, 7])
    r = [check("returns a tuple", type(result), tuple),
         check("low, high, average", result, (1, 9, 5.2))]
    low, high, avg = stats_summary([10, 20])
    r.append(check("can be unpacked", (low, high, avg), (10, 20, 15.0)))
    r.append(check("single number", stats_summary([7]), (7, 7, 7.0)))
    return r


def test_replace_in_tuple():
    color = (255, 128, 0)
    result = replace_in_tuple(color, 1, 64)
    r = [check("middle item replaced", result, (255, 64, 0)),
         check("returns a tuple", type(result), tuple),
         check("original tuple unchanged", color, (255, 128, 0)),
         check("first item replaced", replace_in_tuple(("a", "b", "c"), 0, "z"), ("z", "b", "c")),
         check("last item replaced", replace_in_tuple((1, 2, 3), 2, 99), (1, 2, 99))]
    return r


def test_unique_visitors():
    log = ["cy", "ava", "cy", "ben", "ava", "cy"]
    r = [check("counts and sorts unique names", unique_visitors(log), (3, ["ava", "ben", "cy"])),
         check("original log unchanged", log, ["cy", "ava", "cy", "ben", "ava", "cy"]),
         check("empty log", unique_visitors([]), (0, [])),
         check("one person, many visits", unique_visitors(["x"] * 10), (1, ["x"]))]
    return r


def test_compare_clubs():
    robotics = {"Ava", "Ben", "Cy", "Dee"}
    cyber = {"Cy", "Dee", "Eli"}
    result = compare_clubs(robotics, cyber)
    r = [check("both", result.get("both"), {"Cy", "Dee"}),
         check("only_a", result.get("only_a"), {"Ava", "Ben"}),
         check("only_b", result.get("only_b"), {"Eli"}),
         check("either", result.get("either"), {"Ava", "Ben", "Cy", "Dee", "Eli"})]
    none_shared = compare_clubs({"A"}, {"B"})
    r.append(check("no shared members", none_shared.get("both"), set()))
    return r


def test_build_gradebook():
    r = [check("basic gradebook", build_gradebook(["Ava", "Ben", "Cy"], [92, 85, 78]),
               {"Ava": 92, "Ben": 85, "Cy": 78}),
         check("repeated name keeps the LAST score", build_gradebook(["Ava", "Ben", "Ben"], [92, 70, 88]),
               {"Ava": 92, "Ben": 88}),
         check("empty lists", build_gradebook([], []), {})]
    return r


def test_grade_report():
    book = {"Ava": 92, "Ben": 88}
    r = [check("mix of enrolled and missing", grade_report(book, ["Ben", "Zoe", "Ava"]),
               ["Ben: 88", "Zoe: not enrolled", "Ava: 92"]),
         check("empty student list", grade_report(book, []), []),
         check("gradebook not changed", book, {"Ava": 92, "Ben": 88})]
    return r


if __name__ == "__main__":
    tests = [
        ("add_to_lineup", test_add_to_lineup),
        ("top_scores", test_top_scores),
        ("stats_summary", test_stats_summary),
        ("replace_in_tuple", test_replace_in_tuple),
        ("unique_visitors", test_unique_visitors),
        ("compare_clubs", test_compare_clubs),
        ("build_gradebook", test_build_gradebook),
        ("grade_report", test_grade_report),
    ]
    passed = sum(run_test(name, test) for name, test in tests)
    print("\n" + "=" * 45)
    print(f"{passed} of {len(tests)} functions passing")
    if passed == len(tests):
        print("All tests passed! Nice work.")