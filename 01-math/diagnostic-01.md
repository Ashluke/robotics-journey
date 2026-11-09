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

3. Why does this matrix represents a rotation?

    The matrix represents a pure rigid-body rotation rather than a scaling, shearing, or reflection transform due to algebraic properties of its columns and its determinant.

    * Orthonormal Columns: The columns c1 = (cosΘ, sinΘ) and c2 = (-sinΘ, cosΘ) track where the standard basis vectors land. Calculating their lengths using the Pythagorean identity yields ||c1|| = √(cos²Θ + sin²Θ) = 1 and ||c2|| = √((-sinΘ)² + cos²Θ) = √(sin²Θ + cos²Θ) = 1, showing neither axis stretches or shrinks. Computing their dot product yields c1 * c2 = (cosΘ)(-sinΘ) + (sinΘ)(cosΘ) = 0, confirming the axes remain strictly perpendicular. Because the columns are orthonormal, the matrix satisfies the algebraic condition R^TR = I (meaning R^-1 = R^T), which establishes that length and angle preservation hold for any vector.

    * Determinant and Orientation: The determinant evaluates to det(R) = (cosΘ)(cosΘ) - (-sinΘ)(sinΘ) = cos²Θ + sin²Θ = 1. While any matrix with |det| = 1 guarantees area  preservation (volume does not apply in 2D), the sign determines whether orientation is  preserved. For example, the reflection matrix M = [1 0]
    (1,0 ; 0,-1) also has orthonormal columns and preserves area (|det| = 1), but its determinant is -1 because it flips the plane's handedness. The positive determinant det(R) = +1 distinguishes a pure rotation from a reflection by guaranteeing orientation is preserved.

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

        For the -90° rotation, we compare the matrix R(-90°) = (0,1 ; -1,0) to the transpose of the original 90° rotation matrix, R(90°)^T = (0, -1; 1, 0)^T = (0,1 ; -1,0). We notice that R(-90°) is identically equal to R(90°)^T. This must be true because for any rotaion matrix, reversing the angle yields the inverse operation, expressed as R^-1(Θ) = R(-Θ). Because rotation matrices are orthogonal, their inverse is always equal to their transpose, meaning R^-1(Θ) = R^T(Θ), and consequently R(-Θ) = R^T(Θ). Physically, a rotation by -90° (clockwise) undoes a counter-clockwise 90° rotation, returning any rotated vector right back to its original starting orientation.

    2. Half-turn rotation by 180° (Θ = 180°)
        Using cos(180°) = -1 and sin(180°) = 0:
            R(180°) = [-1, 0]
                      [0, -1]
        Matrix multiplication with P=(2,0):
            P' = [-1, 0] [2]
                 [0, -1] [0]
               = [(-1)(2) + (0)(0)]
                 [(0)(2) + (-1)(0)]
               = [-2]
                 [ 0]
        Result: P'=(-2,0) 

        For the 180° rotation, the matrix R(180°) = (-1,0 ; 0,-1) has a different underlying relationship: it represents a composition of two successive 90° rotations. Multiplying R(90°) by itself yields R(90°)² = (0,-1 ; 1,0)(0,-1 ; 1,0) = (-1,0 ; 0,-1) = R(180°). This is why a half-turn can be achieved by executing a quarter-turn twice. Furthermore, because R(180°) is its own inverse (R(180°) = R^-1(180°)), applying it twice brings any vector completely full circle back to its starting position, satisfying R(180°)² = I. Physically, a 180° rotation acts as a point reflection through the origin that completely inverts both coordinates of any vector from (x,y) to (-x,-y).
            # Diagnostic 1

A gripper sits at (P = (2,0)) in the world frame. Rotate it
(90\^`\circ`{=tex}) counter-clockwise about the origin.

### 1. Rotation Matrix

The general (2 `\times 2`{=tex}) rotation matrix for a counter-clockwise
rotation by an angle (`\theta`{=tex}) is:

\[ R(`\theta`{=tex}) =
```{=tex}
\begin{bmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta
\end{bmatrix}
```
\]

Since the gripper rotates (90\^`\circ`{=tex}) counter-clockwise,
substitute (`\theta `{=tex}= 90\^`\circ`{=tex}).

Since:

\[ `\cos 90`{=tex}\^`\circ `{=tex}= 0,
`\qquad `{=tex}`\sin 90`{=tex}\^`\circ `{=tex}= 1 \]

Therefore:

\[ R(90\^`\circ`{=tex}) =
```{=tex}
\begin{bmatrix}
0 & -1 \\
1 & 0
\end{bmatrix}
```
\]

### 2. Matrix Multiplication and Resulting Point

Given the original point:

\[ P =
```{=tex}
\begin{bmatrix}
2 \\
0
\end{bmatrix}
```
\]

Multiply the rotation matrix by the original point:

\[ P' = R(90\^`\circ`{=tex})P \]

Substituting the values:

\[ P' =
```{=tex}
\begin{bmatrix}
0 & -1 \\
1 & 0
\end{bmatrix}
\begin{bmatrix}
2 \\
0
\end{bmatrix}
```
\]

Performing matrix multiplication:

\[ P' =
```{=tex}
\begin{bmatrix}
(0)(2) + (-1)(0) \\
(1)(2) + (0)(0)
\end{bmatrix}
```
\]

Therefore:

\[ P' =
```{=tex}
\begin{bmatrix}
0 \\
2
\end{bmatrix}
```
\]

The gripper originally located at ((2,0)) moves to ((0,2)) after a
(90\^`\circ`{=tex}) counter-clockwise rotation around the origin.

### 3. Why Does This Matrix Represent a Rotation?

The matrix represents a pure rigid-body rotation rather than a scaling,
shearing, or reflection transformation due to the algebraic properties
of its columns and its determinant.

**Orthonormal Columns:** The columns (c_1 = (`\cos`{=tex}`\theta`{=tex},
`\sin`{=tex}`\theta`{=tex})) and (c_2 = (-`\sin`{=tex}`\theta`{=tex},
`\cos`{=tex}`\theta`{=tex})) represent where the standard basis vectors
land after rotation. Calculating their lengths using the Pythagorean
identity yields:

\[ \|c_1\| = `\sqrt{\cos^2\theta + \sin^2\theta}`{=tex} = 1 \]

\[ \|c_2\| = `\sqrt{(-\sin\theta)^2 + \cos^2\theta}`{=tex} =
`\sqrt{\sin^2\theta + \cos^2\theta}`{=tex} = 1 \]

This shows that neither axis stretches nor shrinks. Computing their dot
product yields:

\[ c_1 `\cdot `{=tex}c_2 =
(`\cos`{=tex}`\theta`{=tex})(-`\sin`{=tex}`\theta`{=tex}) +
(`\sin`{=tex}`\theta`{=tex})(`\cos`{=tex}`\theta`{=tex}) = 0 \]

This confirms that the axes remain strictly perpendicular. Because the
columns are orthonormal, the matrix satisfies the algebraic condition:

\[ R\^T R = I \]

Meaning:

\[ R\^{-1} = R\^T \]

This establishes that lengths and angles are preserved for any vector.

**Determinant and Orientation:** The determinant evaluates to:

\[ `\det`{=tex}(R) =
(`\cos`{=tex}`\theta`{=tex})(`\cos`{=tex}`\theta`{=tex}) -
(-`\sin`{=tex}`\theta`{=tex})(`\sin`{=tex}`\theta`{=tex}) \]

\[ `\det`{=tex}(R) = `\cos`{=tex}\^2`\theta `{=tex}+
`\sin`{=tex}\^2`\theta `{=tex}= 1 \]

While any matrix with (\|`\det`{=tex}\| = 1) guarantees area
preservation (volume does not apply in 2D), the sign determines whether
orientation is preserved. For example, the reflection matrix:

\[ M =
```{=tex}
\begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix}
```
\]

also has orthonormal columns and preserves area because
(\|`\det`{=tex}(M)\| = 1). However, its determinant is (-1) because it
flips the plane's handedness. The positive determinant (`\det`{=tex}(R)
= +1) distinguishes a pure rotation from a reflection by guaranteeing
that orientation is preserved.

### 4. Rotations by (-90\^`\circ`{=tex}) and (180\^`\circ`{=tex}) Applied to (P = (2,0))

#### 1. Clockwise Rotation by (90\^`\circ`{=tex}) ((`\theta `{=tex}= -90\^`\circ`{=tex}))

Using:

\[ `\cos`{=tex}(-90\^`\circ`{=tex}) = 0, `\qquad`{=tex}
`\sin`{=tex}(-90\^`\circ`{=tex}) = -1 \]

The rotation matrix becomes:

\[ R(-90\^`\circ`{=tex}) =
```{=tex}
\begin{bmatrix}
0 & 1 \\
-1 & 0
\end{bmatrix}
```
\]

Matrix multiplication with (P = (2,0)):

\[ P' =
```{=tex}
\begin{bmatrix}
0 & 1 \\
-1 & 0
\end{bmatrix}
\begin{bmatrix}
2 \\
0
\end{bmatrix}
```
\]

\[ P' =
```{=tex}
\begin{bmatrix}
(0)(2) + (1)(0) \\
(-1)(2) + (0)(0)
\end{bmatrix}
```
\]

\[ P' =
```{=tex}
\begin{bmatrix}
0 \\
-2
\end{bmatrix}
```
\]

**Result:** (P' = (0,-2)).

For the (-90\^`\circ`{=tex}) rotation, we compare the matrix
(R(-90\^`\circ`{=tex})) to the transpose of the original
(90\^`\circ`{=tex}) rotation matrix:

\[ R(90^`\circ`{=tex})^T =
```{=tex}
\begin{bmatrix}
0 & -1 \\
1 & 0
\end{bmatrix}
```
# \^T

```{=tex}
\begin{bmatrix}
0 & 1 \\
-1 & 0
\end{bmatrix}
```
\]

We notice that:

\[ R(-90\^`\circ`{=tex}) = R(90^`\circ`{=tex})^T \]

This must be true because, for any rotation matrix, reversing the angle
yields the inverse operation, expressed as:

\[ R\^{-1}(`\theta`{=tex}) = R(-`\theta`{=tex}) \]

Because rotation matrices are orthogonal, their inverse is always equal
to their transpose:

\[ R\^{-1}(`\theta`{=tex}) = R\^T(`\theta`{=tex}) \]

Consequently:

\[ R(-`\theta`{=tex}) = R\^T(`\theta`{=tex}) \]

Physically, a rotation by (-90\^`\circ`{=tex}) (clockwise) undoes a
counter-clockwise (90\^`\circ`{=tex}) rotation, returning any rotated
vector to its original orientation.

#### 2. Half-Turn Rotation by (180\^`\circ`{=tex}) ((`\theta `{=tex}= 180\^`\circ`{=tex}))

Using:

\[ `\cos`{=tex}(180\^`\circ`{=tex}) = -1, `\qquad`{=tex}
`\sin`{=tex}(180\^`\circ`{=tex}) = 0 \]

The rotation matrix becomes:

\[ R(180\^`\circ`{=tex}) =
```{=tex}
\begin{bmatrix}
-1 & 0 \\
0 & -1
\end{bmatrix}
```
\]

Matrix multiplication with (P = (2,0)):

\[ P' =
```{=tex}
\begin{bmatrix}
-1 & 0 \\
0 & -1
\end{bmatrix}
\begin{bmatrix}
2 \\
0
\end{bmatrix}
```
\]

\[ P' =
```{=tex}
\begin{bmatrix}
(-1)(2) + (0)(0) \\
(0)(2) + (-1)(0)
\end{bmatrix}
```
\]

\[ P' =
```{=tex}
\begin{bmatrix}
-2 \\
0
\end{bmatrix}
```
\]

**Result:** (P' = (-2,0)).

For the (180\^`\circ`{=tex}) rotation, the matrix
(R(180\^`\circ`{=tex})) has a different underlying relationship: it
represents a composition of two successive (90\^`\circ`{=tex})
rotations. Multiplying (R(90\^`\circ`{=tex})) by itself yields:

\[ R(90^`\circ`{=tex})^2 =
```{=tex}
\begin{bmatrix}
0 & -1 \\
1 & 0
\end{bmatrix}
\begin{bmatrix}
0 & -1 \\
1 & 0
\end{bmatrix}
```
\]

# \[

```{=tex}
\begin{bmatrix}
-1 & 0 \\
0 & -1
\end{bmatrix}
```
= R(180\^`\circ`{=tex}) \]

This is why a half-turn can be achieved by executing a quarter-turn
twice. Furthermore, because (R(180\^`\circ`{=tex})) is its own inverse,
applying it twice brings any vector completely around a full circle back
to its starting position, satisfying:

\[ R(180^`\circ`{=tex})^2 = I \]

Physically, a (180\^`\circ`{=tex}) rotation acts as a point reflection
through the origin that completely inverts both coordinates of any
vector from ((x,y)) to ((-x,-y)).