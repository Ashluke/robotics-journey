# math notes

## Diagnostic 1

A gripper sits at P = (2,0) in the world frame. Rotate it 90° counter-clockwise about the origin.

1. Rotation matrix

    The general 2x2 rotation matrix for a counter-clockwise rotation by an angle Θ is:
        R(Θ) = [cosΘ -sinΘ]
               [sinΘ -cosΘ]
    Since the gripper rotates 90° counter-clockwise, substitue Θ = 90°
    Since:
         cos90° = 0 & sin90° = 1
    Therefore:
        R(90°) = [0 -1]
                 [1  0]

2. Matrix multiplication & resulting point

    Given the original point: P = (2,0)
    Multiply: P' = R(-90°)P
              P' = [0 -1] [2]
                   [1  0] [0]
              P' = [(0)(2) + (-1)(0)]
                   [(1)(2) + (0)(0)]
              P' = [0]
                   [2]
    The gripper originally located at (2,0) moves to (0,2) after a 90° counter-clockwise rotation around the origin.

3. Why is this matrix a rotation and not some other transform?

    The matrix is considered a rotation matrix because its columns are perpendicular unit vectors. Its first column is (0,1), and its second column is (-1,0). Both columns have a lenght of 1, meaning they preserve the length of vectors, and they are perpendicular to each other.

    We can also verify using the determinant:
        det(R) = (0)(0) - (-1)(1)
        det(R) = 1

    A determinant of 1 means that the transformation preserves the area and orientation of the object. It does not stretch, shrink, reflect, or distort the gripper.

    Therefore this matrix represents a pure rotation because it changes the direction or orientation of the point while preserving its distance from the origin and maintaining its original shape and size.

    