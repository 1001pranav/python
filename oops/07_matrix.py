"""
=============================================================================
07 — OPERATOR OVERLOADING
Matrix class: +, -, *, @, **, ~, abs(), ==, !=, unary -
=============================================================================
"""


class Matrix:
    """
    2×2 Matrix — rich operator overloading example.

    Supported operators:
      A + B   → element-wise addition      (__add__)
      A - B   → element-wise subtraction   (__sub__)
      A * B   → matrix multiplication      (__mul__)
      A @ B   → matrix multiplication      (__matmul__)
      n * A   → scalar multiplication      (__rmul__)
      A ** n  → matrix power               (__pow__)
      ~A      → transpose                  (__invert__)
      abs(A)  → determinant                (__abs__)
      -A      → negate all elements        (__neg__)
      A == B  → equality                   (__eq__)
      A != B  → inequality (auto from ==)  (__ne__)
    """

    def __init__(self, data: list[list[float]]) -> None:
        if len(data) != 2 or any(len(row) != 2 for row in data):
            raise ValueError("Only 2×2 matrices are supported")
        self.data = [row[:] for row in data]   # defensive copy

    # ── Representations ───────────────────────────────────────────────────
    def __str__(self) -> str:
        rows = [f"  [{r[0]:7.2f}  {r[1]:7.2f}]" for r in self.data]
        return "\n".join(rows)

    def __repr__(self) -> str:
        return f"Matrix({self.data})"

    # ── Addition / Subtraction ────────────────────────────────────────────
    def __add__(self, other: "Matrix") -> "Matrix":
        return Matrix([
            [self.data[i][j] + other.data[i][j] for j in range(2)]
            for i in range(2)
        ])

    def __sub__(self, other: "Matrix") -> "Matrix":
        return Matrix([
            [self.data[i][j] - other.data[i][j] for j in range(2)]
            for i in range(2)
        ])

    # ── Multiplication ────────────────────────────────────────────────────
    def __mul__(self, other) -> "Matrix":
        if isinstance(other, (int, float)):
            return Matrix([[v * other for v in row] for row in self.data])
        # matrix × matrix
        a, b = self.data, other.data
        return Matrix([
            [a[0][0]*b[0][0] + a[0][1]*b[1][0],  a[0][0]*b[0][1] + a[0][1]*b[1][1]],
            [a[1][0]*b[0][0] + a[1][1]*b[1][0],  a[1][0]*b[0][1] + a[1][1]*b[1][1]],
        ])

    def __matmul__(self, other: "Matrix") -> "Matrix":
        """Enables A @ B syntax (PEP 465)."""
        return self.__mul__(other)

    def __rmul__(self, scalar: float) -> "Matrix":
        """Enables n * A when scalar is on the left."""
        return self.__mul__(scalar)

    # ── Power ─────────────────────────────────────────────────────────────
    def __pow__(self, n: int) -> "Matrix":
        """A ** n — repeated matrix multiplication."""
        result = Matrix([[1, 0], [0, 1]])    # identity matrix
        for _ in range(n):
            result = result * self
        return result

    # ── Unary operators ───────────────────────────────────────────────────
    def __neg__(self) -> "Matrix":
        return Matrix([[-v for v in row] for row in self.data])

    def __invert__(self) -> "Matrix":
        """~A → transpose."""
        d = self.data
        return Matrix([[d[0][0], d[1][0]], [d[0][1], d[1][1]]])

    def __abs__(self) -> float:
        """abs(A) → determinant (ad - bc)."""
        d = self.data
        return d[0][0]*d[1][1] - d[0][1]*d[1][0]

    # ── Equality ──────────────────────────────────────────────────────────
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Matrix):
            return NotImplemented
        return self.data == other.data


# ── Demo ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[5, 6], [7, 8]])

    def show(label: str, value) -> None:
        if isinstance(value, Matrix):
            print(f"{label}\n{value}\n")
        else:
            print(f"{label} {value}\n")

    show("A =",        A)
    show("B =",        B)
    show("A + B =",    A + B)
    show("A - B =",    A - B)
    show("A * B =",    A * B)
    show("A @ B =",    A @ B)
    show("2 * A =",    2 * A)
    show("A ** 2 =",   A ** 2)
    show("~A (T) =",   ~A)
    show("-A =",       -A)
    show("det(A) =",   abs(A))
    show("A == A :",   A == A)
    show("A == B :",   A == B)
