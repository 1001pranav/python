"""
=============================================================================
06 — MAGIC METHODS (Dunder Methods)
__str__, __repr__, __add__, __sub__, __mul__, __rmul__, __truediv__,
__neg__, __abs__, __eq__, __lt__, __le__, __len__, __getitem__,
__iter__, __contains__, __enter__, __exit__, __hash__, __bool__
=============================================================================
"""


class Vector:
    """2D Vector — demonstrates 15+ magic methods."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    # ── String representations ────────────────────────────────────────────
    def __str__(self) -> str:
        """Called by print() and str() — human-readable."""
        return f"Vector({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Called by repr() and in REPL — developer/debug view."""
        return f"Vector(x={self.x!r}, y={self.y!r})"

    # ── Arithmetic ────────────────────────────────────────────────────────
    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector":
        """v * 3"""
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> "Vector":
        """3 * v  — scalar on the LEFT side."""
        return self.__mul__(scalar)

    def __truediv__(self, scalar: float) -> "Vector":
        if scalar == 0:
            raise ZeroDivisionError("Cannot divide vector by zero")
        return Vector(self.x / scalar, self.y / scalar)

    def __neg__(self) -> "Vector":
        """-v"""
        return Vector(-self.x, -self.y)

    def __abs__(self) -> float:
        """abs(v) → magnitude / length of the vector."""
        import math
        return math.sqrt(self.x**2 + self.y**2)

    # ── Comparison ────────────────────────────────────────────────────────
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __lt__(self, other: "Vector") -> bool:
        return abs(self) < abs(other)

    def __le__(self, other: "Vector") -> bool:
        return abs(self) <= abs(other)

    # ── Hash — MUST define when __eq__ is defined ─────────────────────────
    # Python sets __hash__ = None automatically if __eq__ is defined and
    # __hash__ is not — making the object unhashable. Always pair them.
    def __hash__(self) -> int:
        return hash((self.x, self.y))

    # ── Bool ──────────────────────────────────────────────────────────────
    def __bool__(self) -> bool:
        """Zero vector is falsy; any non-zero vector is truthy."""
        return self.x != 0 or self.y != 0

    # ── Container protocol ────────────────────────────────────────────────
    def __len__(self) -> int:
        return 2     # a 2D vector always has exactly 2 components

    def __getitem__(self, index: int) -> float:
        return (self.x, self.y)[index]

    def __iter__(self):
        yield self.x
        yield self.y

    def __contains__(self, value: float) -> bool:
        return value in (self.x, self.y)

    # ── Context manager ───────────────────────────────────────────────────
    def __enter__(self) -> "Vector":
        print(f"  Entering context: {self}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        print("  Exiting vector context")
        return False    # False = don't suppress exceptions


# ── Demo ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    print(f"str      : {v1}")
    print(f"repr     : {repr(v1)}")
    print(f"add      : {v1 + v2}")
    print(f"sub      : {v1 - v2}")
    print(f"v * 2    : {v1 * 2}")
    print(f"3 * v    : {3 * v1}")
    print(f"v / 2    : {v1 / 2}")
    print(f"-v       : {-v1}")
    print(f"abs(v)   : {abs(v1)}")
    print(f"v1 == v1 : {v1 == Vector(3, 4)}")
    print(f"v2 < v1  : {v2 < v1}")
    print(f"len(v1)  : {len(v1)}")
    print(f"v1[0]    : {v1[0]}")
    print(f"list(v1) : {list(v1)}")
    print(f"3 in v1  : {3 in v1}")
    print(f"bool(v1) : {bool(v1)}")
    print(f"bool(0v) : {bool(Vector(0, 0))}")

    print("\n── Context Manager ──")
    with Vector(5, 6) as v:
        print(f"  Inside: {v}")

    print("\n── Hashable — usable in set/dict ──")
    vector_set = {Vector(1, 2), Vector(3, 4), Vector(1, 2)}   # deduplicates
    print(f"  Set: {vector_set}")
