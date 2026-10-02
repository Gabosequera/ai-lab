"""
Python Collections, Part 2: Mixing Collections with Loops
PCEP Objective: PCEP-30-02 2.2 (loops), 3.1 (lists), 3.2 (tuples and dictionaries)
Difficulty: Intermediate

DESCRIPTION:
An extension of collections_practice.py. Real programs rarely use one
collection by itself. Each function here combines two or more collection
types (lists, tuples, sets, dictionaries) and processes them with for
and while loops.

LEARNING OBJECTIVES:
- Loop over lists of tuples and unpack each tuple in the loop header
- Build dictionaries whose values are lists or sets
- Use tuples as dictionary keys
- Use a while loop when you don't know ahead of time how many steps
  the work will take

EXPECTED OUTCOMES:
After completing this assignment, students will be able to:
- Choose a collection type for each part of a problem
- Combine for loops, while loops, and nested loops with collections
- Change one collection while leaving another untouched

INSTRUCTIONS:
1. Read each function's docstring and examples carefully. They are
   your only guide, so read them more than once.
2. Replace "pass" with your own code.
3. Run this file. The tests at the bottom print PASS or FAIL for
   each function.
4. Keep going until every function prints PASS.
"""


def roster_by_period(enrollments):
    """
    Turn a messy enrollment list into a class roster for each period.

    Each enrollment is a (name, period) tuple. The same student may be
    listed more than once for the same period (the office entered them
    twice), but each student should appear only once on that period's
    roster. A student can be enrolled in more than one period.

    Parameters:
        enrollments (list): a list of (name, period) tuples, where
                            name is a str and period is an int

    Returns:
        dict: {period: list of names}, where each list has no
              duplicates and is sorted alphabetically

    Example:
        >>> roster_by_period([("Ben", 2), ("Ava", 1), ("Cy", 1), ("Ava", 1)])
        {2: ['Ben'], 1: ['Ava', 'Cy']}
        >>> roster_by_period([("Dee", 3), ("Dee", 4), ("Dee", 3)])
        {3: ['Dee'], 4: ['Dee']}
        >>> roster_by_period([])
        {}
    """
    my_dict = {}
    for name, period in enrollments:
        if period not in my_dict:
            my_dict[period] = [name]
        else:
            if name not in my_dict[period]:
                my_dict.setdefault(period, []).append(name)
        my_dict[period] = sorted(my_dict[period])
    return my_dict




def process_orders(inventory, orders):
    """
    Fill supply orders in the order they arrived, until one can't be
    filled.

    Orders are handled first-come, first-served. Check the order at the
    front of the line.
    
    If there is enough of that item in stock, take it out of the inventory,
    
    record the item as filled, and move to the
    next order. As soon as an order can't be filled, STOP:
    
    
    that order and every order behind it keep waiting, even if a later one could
    have been filled.
    
    An item that isn't in the inventory has a stock of 0.
    
    
    
    You must use a while loop for this function.

    The inventory dictionary IS changed by this function. The orders
    list passed in must NOT be changed.

    Parameters:
        inventory (dict): {item: quantity in stock}
        orders (list): a list of (item, quantity) tuples, in arrival order

    Returns:
        tuple: (filled, waiting) where
               filled is a list of item names that were filled, in order
               waiting is a list of the (item, quantity) tuples not filled

    Example:
        >>> stock = {"pens": 10, "paper": 3}
        >>> line = [("pens", 4), ("paper", 2), ("paper", 2), ("pens", 1)]
        >>> process_orders(stock, line)
        (['pens', 'paper'], [('paper', 2), ('pens', 1)])
        >>> stock
        {'pens': 6, 'paper': 1}
        >>> line
        [('pens', 4), ('paper', 2), ('paper', 2), ('pens', 1)]
        >>> process_orders({"tape": 5}, [("glue", 1), ("tape", 1)])
        ([], [('glue', 1), ('tape', 1)])
    """
    fulfilled_orders = []
    waiting_orders = []
    i = 0
    while i < len(orders):
        
        print(f"this is 'I': {orders[i]}--------------------\n")
        
        if orders[i][0] in inventory:
            
            quantity = orders[i][1]
            stock = inventory.get(orders[i][0], 0)
            
            if (stock - quantity) < 0:
                #put the other orders into the waiting list
                #print("inside if")
                waiting_orders.append(orders[i])
            else:
                #Completing the order is possible
                #We need to subtract order_quantity from inventory
                #print("inside else")
                inventory[orders[i][0]] = stock - quantity
                fulfilled_orders.append(orders[i][0])

        i += 1
    
    print("")
    print(f"fullfilled: {fulfilled_orders}")
    print(f"waigin: {waiting_orders}-----------------------\n")
        
    return fulfilled_orders, waiting_orders


def shared_interests(students):
    """
    Find every pair of students who share at least one interest.

    Each student has a set of interests. Compare every student with
    every other student exactly once. Each pair is stored as a tuple of
    the two names in alphabetical order, like ("Ava", "Ben"), never
    ("Ben", "Ava"). Pairs with nothing in common are left out.

    Parameters:
        students (dict): {name: set of interests}

    Returns:
        dict: {(name1, name2): set of interests they share}

    Example:
        >>> clubs = {
        ...     "Cy":  {"robotics", "chess"},
        ...     "Ava": {"robotics", "art", "chess"},
        ...     "Ben": {"art"},
        ... }
        >>> result = shared_interests(clubs)
        >>> result[("Ava", "Cy")] == {"robotics", "chess"}
        True
        >>> result[("Ava", "Ben")]
        {'art'}
        >>> ("Ben", "Cy") in result
        False
        >>> len(result)
        2
    """
    pass


def take_turns(teams):
    """
    Build the speaking order for a team presentation day.

    Teams take turns one player at a time. In each round, go through
    the team names in alphabetical order, and each team sends up its
    next player (players go in the order they are listed). A team that
    has run out of players is skipped. Keep going round after round
    until every player on every team has had a turn.

    You must use a while loop for this function. The teams dictionary
    and its lists must NOT be changed.

    Parameters:
        teams (dict): {team name: list of player names}

    Returns:
        list: (team name, player name) tuples in speaking order

    Example:
        >>> take_turns({"Red": ["Ava", "Ben", "Cy"], "Blue": ["Dee", "Eli"]})
        [('Blue', 'Dee'), ('Red', 'Ava'), ('Blue', 'Eli'), ('Red', 'Ben'), ('Red', 'Cy')]
        >>> take_turns({"Solo": ["Zoe"], "Empty": []})
        [('Solo', 'Zoe')]
        >>> take_turns({})
        []
    """
    pass


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
        return all(test_function())
    except Exception as error:
        print(f"  ERROR {type(error).__name__}: {error}")
        return False


def test_roster_by_period():
    data = [("Ben", 2), ("Ava", 1), ("Cy", 1), ("Ava", 1)]
    return [
        check("duplicates removed, names sorted", roster_by_period(data),
              {1: ["Ava", "Cy"], 2: ["Ben"]}),
        check("input list not changed", data, [("Ben", 2), ("Ava", 1), ("Cy", 1), ("Ava", 1)]),
        check("one student in two periods", roster_by_period([("Dee", 3), ("Dee", 4), ("Dee", 3)]),
              {3: ["Dee"], 4: ["Dee"]}),
        check("sorting within a period", roster_by_period([("Zoe", 5), ("Max", 5), ("Ann", 5), ("Max", 5)]),
              {5: ["Ann", "Max", "Zoe"]}),
        check("empty list", roster_by_period([]), {}),
    ]


def test_process_orders():
    stock = {"pens": 10, "paper": 3}
    line = [("pens", 4), ("paper", 2), ("paper", 2), ("pens", 1)]
    result = process_orders(stock, line)
    r = [
        check("stops at the first order that can't be filled", result,
              (["pens", "paper"], [("paper", 2), ("pens", 1)])),
        check("inventory is updated", stock, {"pens": 6, "paper": 1}),
        check("orders list not changed", line, [("pens", 4), ("paper", 2), ("paper", 2), ("pens", 1)]),
        check("unknown item blocks the line", process_orders({"tape": 5}, [("glue", 1), ("tape", 1)]),
              ([], [("glue", 1), ("tape", 1)])),
    ]
    stock2 = {"cups": 3}
    r.append(check("exact amount empties the stock",
                   process_orders(stock2, [("cups", 2), ("cups", 1)]), (["cups", "cups"], [])))
    r.append(check("stock can reach zero", stock2, {"cups": 0}))
    r.append(check("no orders", process_orders({"pens": 1}, []), ([], [])))
    return r


def test_shared_interests():
    clubs = {"Cy": {"robotics", "chess"}, "Ava": {"robotics", "art", "chess"}, "Ben": {"art"}}
    result = shared_interests(clubs)
    r = [
        check("pairs with shared interests", result,
              {("Ava", "Cy"): {"robotics", "chess"}, ("Ava", "Ben"): {"art"}}),
        check("input not changed", clubs,
              {"Cy": {"robotics", "chess"}, "Ava": {"robotics", "art", "chess"}, "Ben": {"art"}}),
        check("nobody shares anything", shared_interests({"A": {"x"}, "B": {"y"}}), {}),
        check("one student, no pairs", shared_interests({"Solo": {"x"}}), {}),
    ]
    four = {"Dee": {"x", "y"}, "Bo": {"y"}, "Al": {"x", "y", "z"}, "Cam": {"z"}}
    r.append(check("four students", shared_interests(four),
                   {("Al", "Bo"): {"y"}, ("Al", "Cam"): {"z"}, ("Al", "Dee"): {"x", "y"}, ("Bo", "Dee"): {"y"}}))
    return r


def test_take_turns():
    teams = {"Red": ["Ava", "Ben", "Cy"], "Blue": ["Dee", "Eli"]}
    r = [
        check("alternates teams, alphabetical, uneven sizes", take_turns(teams),
              [("Blue", "Dee"), ("Red", "Ava"), ("Blue", "Eli"), ("Red", "Ben"), ("Red", "Cy")]),
        check("teams not changed", teams, {"Red": ["Ava", "Ben", "Cy"], "Blue": ["Dee", "Eli"]}),
        check("empty team skipped", take_turns({"Solo": ["Zoe"], "Empty": []}), [("Solo", "Zoe")]),
        check("no teams", take_turns({}), []),
        check("three teams", take_turns({"C": ["c1"], "A": ["a1", "a2"], "B": ["b1", "b2"]}),
              [("A", "a1"), ("B", "b1"), ("C", "c1"), ("A", "a2"), ("B", "b2")]),
    ]
    return r


if __name__ == "__main__":
    tests = [
        ("roster_by_period", test_roster_by_period),
        ("process_orders", test_process_orders),
        ("shared_interests", test_shared_interests),
        ("take_turns", test_take_turns),
    ]
    passed = sum(run_test(name, test) for name, test in tests)
    print("\n" + "=" * 45)
    print(f"{passed} of {len(tests)} functions passing")
    if passed == len(tests):
        print("All tests passed! Nice work.")
