# Diagnostic 1

A gripper sits at P = (2,0) in the world frame. Rotate it 90° counter-clockwise about the origin.

1. Rotation matrix

    The general 2x2 rotation matrix for a counter-clockwise rotation by an angle Θ is:
        R(Θ) = [cosΘ -sinΘ]
               [sinΘ  cosΘ]
    Since the gripper rotates 90° counter-clockwise, substitute Θ = 90°
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

3. Why is this matrix represents a rotation?

    The matrix represents a pure rigid-body rotation rather than a scaling, shearing, or reflection transform due to algebraic properties of its columns and its determinant.

    * Orthonormal Columns: The columns c1 = (cosΘ, sinΘ) and c2 = (-sinΘ, cosΘ) track where the standard basis vectors land. Calculating their lengths using the Pythagorean identity yields ||c1|| = √(cos²Θ + sin²Θ) = 1 and ||c2|| = √((-sinΘ)² + cos²Θ) = √(sin²Θ + cos²Θ) = 1, showing neither axis stretches or shrinks. Computing their dot product yields c1 * c2 = (cosΘ)(-sinΘ) + (sinΘ)(cosΘ) = 0, confirming the axes remain strictly perpendicular. Because the columns are orthonormal, the matrix satisfies the algebraic condition R^TR = I (meaning R^-1 = R^T), which establishes that length and angle preservation hold for any vector.

    * Determinant and Orientation: The determinant evaluates to det(R) = (cosΘ)(cosΘ) - (-sinΘ)(sinΘ) = 1. While any matrix with |det| = 1 guarantees area preservation (volume does not apply in 2D), the sign determines whether orientation is preserved. For example, the reflection matrix M = (1,0 ; 0,-1) also has orthonormal columns and preserves area (|det| = 1), but its determinant is -1 because it flips the plane's handedness. The positive determinant det(R) = +1 distinguishes a pure rotation from a reflection by guaranteeing orientation is preserved.

4. Rotations by -90° and 180° applied to P=(2,0):

    1. Clockwise rotation by 90° (Θ = -90°)
        Using cos(-90°) = 0 and sin(-90°) = -1:
            R(-90°) = [0,  1]
                      [-1, 0]
        Matrix multiplication with P=(2,0):
            P' = [0, 1] [2]
                 [-1 0] [0]
               = [(0)(2)  + (1)(0)]
                 [(-1)(2) + (0)(0)]
               = [ 0]
                 [-2]
        Result: P'=(0,-2)

    2. Half-turn rotation by 180° (Θ = 180°)
        Using cos(180°) = -1 and sin(180°) = 0:
            R(180°) = [-1, 0]
                      [0, -1]
        Matrix multipication with P=(2,0):
            P' = [-1, 0] [2]
                 [0, -1] [0]
               = [(-1)(2) + (0)(0)]
                 [(0)(2) + (-1)(0)]
               = [-2]
                 [ 0]
        Result: P'=(-2,0) 
            