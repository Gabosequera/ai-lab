"""
Terminal Shapes: Control Flow & Loops          (~60 min)
PCEP 2.1 (if / elif / else)  |  PCEP 2.2 (for, while, nested loops)

RULES
- Every function RETURNS a string. Rows are joined with "\n".
- No trailing spaces at the end of any row.
- Size 0 or negative -> return "" (empty string).
- Run this file to test:  python loop_patterns.py
"""


def rectangle(width, height, char="*"):
    """
    Solid rectangle. Use NESTED for loops (no "*" * width shortcut).

    rectangle(4, 2)      rectangle(3, 2, "#")
    ****                 ###
    ****                 ###
    """
    for i in range(width):
        for x in range(height):
            print(char, " ")


def triangle(height, align="left"):
    """
    Right-angle triangle. Use a for loop and if / elif / else.
    align must be "left" or "right"; anything else -> "".

    triangle(3)          triangle(3, "right")
    *                      *
    **                    **
    ***                  ***
    """
    pass


def hollow_rectangle(width, height):
    """
    Border only. Inside each row, use if / elif / else to decide
    whether it is a top/bottom row or a middle row.

    hollow_rectangle(5, 3)
    *****
    *   *
    *****
    """
    pass


def diamond(size):
    """
    size = number of rows in the top half. Use WHILE loops only.

    diamond(3)
      *
     ***
    *****
     ***
      *
    """
    pass


def wildcard(size):
    """
    YOUR shape! Invent one (checkerboard, X, arrow, hourglass, stairs...).
    Requirements: at least one loop and one if-statement,
    `size` changes the output, and it is not a shape above.

    Name your shape here: ____________________
    """
    pass


def draw(shape, size):
    """
    Dispatcher. Use an if / elif / else chain:
        "rectangle" -> rectangle(size * 2, size)
        "triangle"  -> triangle(size)
        "hollow"    -> hollow_rectangle(size * 2, size)
        "diamond"   -> diamond(size)
        "wildcard"  -> wildcard(size)
        anything else -> "Unknown shape: <shape>"
    """
    pass


# ======================= TESTS (do not edit) =======================
if __name__ == "__main__":
    passed = 0
    total = 0

    def check(name, actual, expected):
        global passed, total
        total += 1
        if actual == expected:
            passed += 1
            print("PASS", name)
        else:
            print("FAIL", name)
            print("  expected:\n" + str(expected))
            print("  got:\n" + str(actual))

    # 1. rectangle
    check("rectangle 4x2", rectangle(4, 2), "****\n****")
    check("rectangle char", rectangle(3, 2, "#"), "###\n###")
    check("rectangle 1x1", rectangle(1, 1), "*")
    check("rectangle zero", rectangle(0, 5), "")

    # 2. triangle
    check("triangle left", triangle(3), "*\n**\n***")
    check("triangle right", triangle(3, "right"), "  *\n **\n***")
    check("triangle bad align", triangle(3, "up"), "")
    check("triangle zero", triangle(0), "")

    # 3. hollow_rectangle
    check("hollow 5x3", hollow_rectangle(5, 3), "*****\n*   *\n*****")
    check("hollow 4x4", hollow_rectangle(4, 4), "****\n*  *\n*  *\n****")
    check("hollow 3x1", hollow_rectangle(3, 1), "***")
    check("hollow 2x2", hollow_rectangle(2, 2), "**\n**")

    # 4. diamond
    check("diamond 1", diamond(1), "*")
    check("diamond 3", diamond(3), "  *\n ***\n*****\n ***\n  *")
    check("diamond zero", diamond(-2), "")

    # 5. wildcard (you design it, so tests check the rules)
    w3, w5 = wildcard(3), wildcard(5)
    check("wildcard returns text", isinstance(w3, str) and len(w3) > 0, True)
    check("wildcard size matters", w3 != w5, True)
    check("wildcard is new", w5 not in (rectangle(5, 5), triangle(5), diamond(5)), True)
    check("wildcard zero", wildcard(0), "")

    # 6. draw
    check("draw rectangle", draw("rectangle", 2), "****\n****")
    check("draw diamond", draw("diamond", 2), " *\n***\n *")
    check("draw hollow", draw("hollow", 3), "******\n*    *\n******")
    check("draw unknown", draw("star", 3), "Unknown shape: star")

    print(f"\n{passed}/{total} tests passed")
    print("\nYour wildcard (size 5):\n" + str(wildcard(5)))
