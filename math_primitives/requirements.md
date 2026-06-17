# Project 1 — Linear Algebra + Broadcasting Primitives (Exhaustive)

**Scope:** the array/linear-algebra foundation everything else is built on. Nothing higher-level (no activations, no gradients yet).

**Three tracks per item:**

- **A. Pure-Python, functions** — nested lists for matrices, lists for vectors; `math` + `random` only.
- **B. Pure-Python, `Matrix`/`Vector` class** — wrap Track A in a class with operator overloading (this _is_ the OOP exercise; numpy's `ndarray` is itself exactly this).
- **C. NumPy** — `np.ndarray` gives you the class for free; write the call, and use the result as the **oracle** to verify A and B via `allclose`.

> Build A → B → C for the core ops. For the bounded/"use numpy" items, A is optional and C is the answer.

---

## 0. Representation & construction

- [ ] vector (list) and matrix (list-of-lists) representation — decide your convention
- [ ] `zeros(n)`, `zeros(m, n)`
- [ ] `ones(...)`, `full(..., value)`
- [ ] `eye(n)` / identity
- [ ] `from_nested_list(...)`
- [ ] `shape(x)`
- [ ] `random_matrix(m, n)` (pure: `random`; numpy: `np.random`)
- [ ] `reshape(x, new_shape)` _(fiddly in pure-python — do a basic version, lean on numpy for the general case)_

## 1. Indexing & slicing

- [ ] get element `x[i]`, `M[i][j]`
- [ ] get row, get column
- [ ] slice a submatrix (subset of rows/cols)
- [ ] **Class (B):** `__getitem__`, `__setitem__`, `__len__`

## 2. Vector operations

- [ ] element-wise add, sub, mul, div (vector–vector, equal length)
- [ ] scalar ops: `v + s`, `v * s`, `v - s`, `v / s`
- [ ] **dot product** (v · v)
- [ ] L1 norm, L2 norm, general Lp norm
- [ ] normalize to unit vector
- [ ] `sum`, `mean`, `min`, `max`, `argmin`, `argmax`
- [ ] outer product (v ⊗ v → matrix)
- [ ] cross product (3-D only) _(optional, geometry)_

## 3. Matrix operations

- [ ] element-wise add, sub, Hadamard mul, div (same shape)
- [ ] scalar ops on a matrix
- [ ] **transpose**
- [ ] matrix–vector product
- [ ] **matrix–matrix product (matmul)** ← the centerpiece; pure-python is the triple-nested loop, feel the O(n³)
- [ ] trace
- [ ] diagonal extraction
- [ ] determinant — 2×2 and 3×3 by hand _(general case → numpy; it's a rabbit hole)_
- [ ] inverse → **use `np.linalg`**; note the rule: _solve, don't invert_

## 4. Broadcasting (the conceptual centerpiece — most downstream bugs live here)

- [ ] shape-compatibility check (the broadcasting rule, explicit)
- [ ] broadcast scalar → matrix
- [ ] broadcast **row** vector across rows `M(m,n) + r(1,n)`
- [ ] broadcast **column** vector across columns `M(m,n) + c(m,1)`
- [ ] general `broadcast_add`, `broadcast_mul`
- [ ] **Class (B):** make `__add__`/`__mul__` broadcasting-aware

## 5. Reductions with axis semantics

- [ ] `sum`/`mean`/`max`/`min` along `axis=0` (down columns) and `axis=1` (across rows)
- [ ] **`keepdims`** behavior _(critical — it's what lets the reduced result broadcast back)_
- [ ] `argmax`/`argmin` along an axis

## 6. Linear systems (one bounded build, else numpy)

- [ ] solve `Ax = b` via Gaussian elimination — pure-python, **once** (illuminating)
- [ ] for everything after: `np.linalg.solve`
- [ ] (skip LU/QR from scratch — HPC track, not this project)

## 7. Class design (Track B — the OOP payload of this project)

Build `Vector` and/or `Matrix` after the functions work, wrapping them:

- [ ] `__init__`, `__repr__` (pretty-print)
- [ ] `__add__`, `__sub__`, `__mul__` (element-wise + scalar), `__truediv__`
- [ ] `__matmul__` → matmul (so `A @ B` works)
- [ ] `__radd__`, `__rmul__` (scalar-on-the-left: `2 * M`)
- [ ] `__neg__`, `__eq__`
- [ ] `__getitem__`, `__setitem__`, `__len__`, optionally `__iter__`
- [ ] `@property shape`, `@property T` (transpose)

## 8. Verification harness (do this from day one)

- [ ] `allclose(a, b, tol=1e-9)` tolerance compare
- [ ] for each op: run A and B on a random input → compare to the **C (numpy)** result with `allclose` → green means correct
- [ ] keep these as repeatable checks so your spaced re-implementations (build 2, build 3) self-verify

---

### Done-criteria for Project 1

You can open a blank file and, with no reference, implement `matmul`, broadcasting (row + column), and axis reductions with `keepdims` — and your pure-python `Matrix` class passes `allclose` against numpy on all of the above.
