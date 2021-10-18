from Parametrized_Testing.triangle import triangle_type


""""
all 4 tests combined into one test. DO NOT DO THAT!!!!

"""

def test_type():
    many_triangles = [
        (90, 60, 30, "right"),
        (100, 40, 40, "obtuse"),
        (60, 60, 60, "acute"),
        (0, 0, 0, "invalid")
    ]
    for a, b, c, expected in many_triangles:
        assert triangle_type(a, b, c) == expected