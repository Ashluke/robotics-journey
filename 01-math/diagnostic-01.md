# Diagnostic 1

A gripper sits at P = (2, 0) in the world frame. Rotate it 90° counter-clockwise about the origin.

All matrices are written one row per line.

## 1. Rotation matrix

The general 2x2 rotation matrix for a counter-clockwise rotation by an angle Θ is:

```
R(Θ) = [ cosΘ  -sinΘ ]
       [ sinΘ   cosΘ ]
```

Since the gripper rotates 90° counter-clockwise, substitute Θ = 90°. Since cos 90° = 0 and sin 90° = 1:

```
R(90°) = [ 0  -1 ]
         [ 1   0 ]
```

## 2. Matrix multiplication and resulting point

```
P' = R(90°) P

   = [ 0  -1 ] [ 2 ]
     [ 1   0 ] [ 0 ]

   = [ (0)(2) + (-1)(0) ]
     [ (1)(2) + (0)(0)  ]

   = [ 0 ]
     [ 2 ]
```

The gripper originally located at (2, 0) moves to (0, 2) after a 90° counter-clockwise rotation around the origin.

## 3. Why does this matrix represent a rotation?

The matrix represents a pure rigid-body rotation rather than a scaling, shearing, or reflection, because of the algebraic properties of its columns and its determinant.

### Orthonormal columns

The columns are c1 = (cosΘ, sinΘ) and c2 = (-sinΘ, cosΘ). They track where the standard basis vectors land.

```
||c1|| = sqrt(cos²Θ + sin²Θ) = 1
||c2|| = sqrt((-sinΘ)² + cos²Θ) = sqrt(sin²Θ + cos²Θ) = 1
c1 · c2 = (cosΘ)(-sinΘ) + (sinΘ)(cosΘ) = 0
```

Neither axis stretches or shrinks, and the axes stay strictly perpendicular. Because the columns are orthonormal, the matrix satisfies RᵀR = I, meaning R⁻¹ = Rᵀ. This establishes that length and angle preservation hold for any vector.

### Determinant and orientation

```
det(R) = (cosΘ)(cosΘ) - (-sinΘ)(sinΘ) = cos²Θ + sin²Θ = 1
```

Any matrix with |det| = 1 preserves area (volume does not apply in 2D). The sign determines whether orientation is preserved. For example, the reflection matrix M also has orthonormal columns and preserves area, but its determinant is -1 because it flips the plane's handedness:

```
M = [ 1   0 ]
    [ 0  -1 ]

det(M) = (1)(-1) - (0)(0) = -1
```

The positive determinant det(R) = +1 distinguishes a pure rotation from a reflection by guaranteeing that orientation is preserved.

## 4. Rotations by -90° and 180° applied to P = (2, 0)

### 4.1 Clockwise rotation by 90° (Θ = -90°)

Using cos(-90°) = 0 and sin(-90°) = -1:

```
R(-90°) = [  0  1 ]
          [ -1  0 ]
```

```
P' = R(-90°) P

   = [  0  1 ] [ 2 ]
     [ -1  0 ] [ 0 ]

   = [ (0)(2)  + (1)(0) ]
     [ (-1)(2) + (0)(0) ]

   = [  0 ]
     [ -2 ]
```

Result: P' = (0, -2)

### 4.2 Half-turn by 180° (Θ = 180°)

Using cos(180°) = -1 and sin(180°) = 0:

```
R(180°) = [ -1   0 ]
          [  0  -1 ]
```

```
P' = R(180°) P

   = [ -1   0 ] [ 2 ]
     [  0  -1 ] [ 0 ]

   = [ (-1)(2) + (0)(0) ]
     [ (0)(2) + (-1)(0) ]

   = [ -2 ]
     [  0 ]
```

Result: P' = (-2, 0)

R(180°) is a composition of two successive 90° rotations. Multiplying R(90°) by itself:

```
R(90°)² = [ 0  -1 ] [ 0  -1 ]
          [ 1   0 ] [ 1   0 ]

        = [ -1   0 ]
          [  0  -1 ]

        = R(180°)
```

This is why a half-turn can be achieved by executing a quarter-turn twice. Because R(180°) is its own inverse, applying it twice brings any vector back to its starting position, so R(180°)² = I. Physically, a 180° rotation acts as a point reflection through the origin that inverts both coordinates of any vector, from (x, y) to (-x, -y).

**TODO (write in your own words):** one sentence on why "point reflection" does not contradict Part 3. Hint: compare det(R(180°)) with det(M).

## 5. R(-90°) versus the transpose of R(90°)

```
R(90°)  = [ 0  -1 ]
          [ 1   0 ]

R(90°)ᵀ = [ 0   1 ]
          [ -1  0 ]

R(-90°) = [  0  1 ]
          [ -1  0 ]
```

R(-90°) = R(90°)ᵀ, entry by entry.

This must be true because, for any rotation matrix, reversing the angle yields the inverse operation: R⁻¹(Θ) = R(-Θ). Because rotation matrices are orthogonal, their inverse equals their transpose: R⁻¹(Θ) = Rᵀ(Θ). Consequently R(-Θ) = Rᵀ(Θ).

Physically, a rotation by -90° (clockwise) undoes a counter-clockwise 90° rotation, returning any rotated vector to its original orientation.

Numerical check: see `03-python/rotation_check.py`.