# Diagnostic 1

A gripper sits at P = (2,0) in the world frame. Rotate it 90° counter-clockwise about the origin.

1. Rotation matrix

    The general 2x2 rotation matrix for a counter-clockwise rotation by an angle Θ is:
        R(Θ) = [cosΘ -sinΘ]
               [sinΘ  cosΘ]
    Since the gripper rotates 90° counter-clockwise, substitue Θ = 90°
    Since:
         cos90° = 0 & sin90° = 1
    Therefore:
        R(90°) = [0 -1]
                  [1  0]

2. Matrix multiplication & resulting point

    Given the original point: P = (2,0)
    Multiply: P' = R(90°)P
              P' = [0 -1] [2]
                   [1  0] [0]
              P' = [(0)(2) + (-1)(0)]
                   [(1)(2) + (0)(0)]
              P' = [0]
                   [2]
    The gripper originally located at (2,0) moves to (0,2) after a 90° counter-clockwise rotation around the origin.

3. Why is this matrix represents a rotation

    The matrix represents a pure rigid-body rotation rather than a scaling, shearing, or reflection transform due to algebraic properties of its columns and its determinant.

    * Orthonormal Columns: The columns c1 = (cos0, sin0) and c2 = (-sinΘ, cosΘ) track where the standard basis vectors land. Calculating their lengths using the Pythagorean identity yields ||c1|| = √(cos²Θ + sin²Θ) = 1 and ||c2|| = √(-sin²Θ + cos²Θ) = 1, showing neither axis stretches or shrinks. Computing their dot product yields c1 * c2 = (cosΘ)(-sinΘ) + (sinΘ)(cosΘ) = 0, confirming the axes remain strictly perpendicular. Because the columns are orthonormal, the matrix satisfies the algebraic condition R^TR = I (meaning R^-1 = R^T), which establshes that length and angle preservation hold for any vector.

    * Determinant and Orientation: The determinant evaluates to det(R) = cos²Θ - (-sin²Θ) = cos²Θ + sin²Θ = 1. While any matrix with |det| = 1 guarantees area preservation (volume does not apply in 2D), the sign determines whether orientation is preserved. For example, the reflection matrix M = (1,0 ; 0,-1) also has orthonormal columns and preserves area (|det| = 1), but its determinant is -1 because it flips the planes handedness. The positive determinant det(R) = +1 distinguishes a pure rotation from a reflection by guaranteeing orientation is preserved.