# More test cases

many_triangles = [
                  (1, 1, 178, "obtuse"),  # big angles
                  (91, 44, 45, "obtuse"),  # just over 90
                  (0.01, 0.01, 179.98, "obtuse"), # floats

                  (90, 60, 30, "right"),  # check 90 for each angle
                  (10, 90, 80, "right"),
                  (85, 5, 90, "right"),

                  (89, 89, 2, "acute"),  # just under 90

                  (0, 0, 0, "invalid"),  # zeros
                  (61, 60, 60) # sum > 180
                  (90, 91, -1, "invalid"),  # negative numbers
                  ]
