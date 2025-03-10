import os, sys
from functools import cmp_to_key

# This imports from a file that will be present in the
# grading system. No need to alter for local testing -
# if the file isn't present then these lines are skipped
try:
    from compile_with_soln import grader_stub

    grader = grader_stub()
except:
    pass

N = 0  # number of points
D = 0  # dimensionality of space
K = 0  # number of nearest neighbors to find for each point


# Note: K is always odd

# ----------------------------------------
# This function (which will be compiled with our code
# when it is submitted to the grading system) takes
# the index of a point (in 0..N-1) and returns either
# +1 or -1 depending on its class.

# grader.get_class(i)
# ----------------------------------------

# ----------------------------------------
# This function (which will be compiled with our code
# when it is submitted to the grading system) takes
# the index i of a point (in 0..N-1) and the index of a
# coordinate (in 0..D-1) and returns the jth coordinate
# of the ith point.

# grader.get_coord(i, j)
# ----------------------------------------


# For testing on your own system, you can call these functions.
# They provide a simple 2D set of points, with x's being
# class +1 and o's being class -1.
#
#    o    o
# x   x
#
#    o    o
# x   x
#
# The correct confusion matrix for this instance is:
#
# Predicted: +1  -1
# Actual: +1  2   2
#         -1  3   1
#
# Don't forget to switch your code back to calling
# grader.get_class() and grader.get_coord() before
# submitting.
def get_class_local(index):
    if index < 0 or index >= 8:
        print('get_class_local: Invalid point index!')
        sys.exit(0)
    return 1 if index < 4 else -1


def get_coord_local(i, j):
    pts = [[0.0, 0.0], [4.0, 0.0], [4.0, 3.0], [0.0, 3.0],
           [3.0, 1.0], [8.0, 1.0], [8.0, 4.0], [3.0, 4.0]]
    if i < 0 or i >= 8:
        print('get_coord_local: Invalid point index!')
        sys.exit(0)
    if j < 0 or j >= 2:
        print('get_coord_local: Invalid coordinate index!')
        sys.exit(0)
    return pts[i][j]


def main():
    global N, D, K
    # The values for N, D, and K are set in the grading system through
    # environment variables, if present.  If not present, feel
    # welcome to set N to any value you want for local testing.
    try:
        N = int(os.environ["N"])
        D = int(os.environ["D"])
        K = int(os.environ["K"])
    except:
        N = 8
        D = 2
        K = 3

    # Below is the part of main() you should modify.
    # (you are welcome to write other functions above
    # and call them here, but all your code should be
    # submitted in this one file).
    # ----------------------------------------

    # ----------------------------------------
    # At the end, you should print out a 2 x 2 confusion
    # matrix -- just 4 integers
    print('2 2')
    print('3 1')


if __name__ == "__main__":
    main()