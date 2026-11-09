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