import pytest
from Parametrized_Testing.triangle import triangle_type


# ------------------------------------------
# Version 1 -> with passed all the data to the mark.function

# @pytest.mark.parametrize( 'a, b, c, expected', [
#     (90, 60, 30, "right"),
#     (100, 40, 40, "obtuse"),
#     (60, 60, 60, "acute"),
#     (0, 0, 0, "invalid")])

# @pytest.mark.parametrize('a, b, c, expected', many_triangles())
# def test_func(a, b, c, expected):
#     assert triangle_type(a, b, c) == expected



# ------------------------------------------
# Version 2 -> parameters passed from outer list

# many_triangles = [
#     (90, 60, 30, "right"),
#     (100, 40, 40, "obtuse"),
#     (60, 60, 60, "acute"),
#     (0, 0, 0, "invalid")
# ]
#
# @pytest.mark.parametrize( 'a, b, c, expected', many_triangles)
# def test_func(a, b, c, expected):
#     assert triangle_type(a, b, c) == expected


# ------------------------------------------
# Version 3 -> passed parameters are generated by many_triangles function

# def many_triangles():
#     return [ (90, 60, 30, "right"),
#     (100, 40, 40, "obtuse"),
#     (60, 60, 60, "acute"),
#     (0, 0, 0, "invalid") ]

# @pytest.mark.parametrize('a, b, c, expected', many_triangles())
# def test_func(a, b, c, expected):
#     assert triangle_type(a, b, c) == expected


# ----------------------------------------------
# Version 4 -> many_triangles function can also be a function generator

# def many_traingles():
#     for t in [ (90, 60, 30, "right"),
#               (100, 40, 40, "obtuse"),
#               (60, 60, 60, "acute"),
#               (0, 0, 0, "invalid") ]:
#         yield t
#
# @pytest.mark.parametrize('a, b, c, expected', many_traingles())
# def test_func(a, b, c, expected):
#     assert triangle_type(a, b, c) == expected


# ---------------------------------------
# Version 5 -> using file context manager, pulling out the data form outer .csv file

# import csv
# def many_triangles():
#     with open('triangle_data.csv') as csvfile:
#         for a, b, c, expected in csv.reader(csvfile):
#             yield (int(a), int(b), int(c), expected)
#
# @pytest.mark.parametrize( 'a, b, c, expected', many_triangles())
# def test_func(a, b, c, expected):
#     assert triangle_type(a, b, c) == expected




