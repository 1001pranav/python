"""
=============================================================================
03 — POLYMORPHISM
Method Overriding, Duck Typing, isinstance checks
=============================================================================
"""


# ── Polymorphism via method overriding ────────────────────────────────────
class Shape:
    def area(self) -> float:
        raise NotImplementedError("Subclasses must implement area()")

    def describe(self) -> str:
        # same interface — each subclass provides its OWN area()
        return f"{self.__class__.__name__} with area = {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width  = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        self.base   = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height


# ── Duck Typing — Python's informal polymorphism ──────────────────────────
# "If it walks like a duck and quacks like a duck, it IS a duck."
# No shared base class needed — just the same method signature.

class Logger:
    def log(self, msg: str) -> None:
        print(f"[LOG]   {msg}")


class SlackNotifier:
    def log(self, msg: str) -> None:
        print(f"[SLACK] 📢 {msg}")


class EmailNotifier:
    def log(self, msg: str) -> None:
        print(f"[EMAIL] ✉️  {msg}")


def notify_all(notifiers: list, message: str) -> None:
    """Doesn't care about TYPE — only that .log() exists."""
    for n in notifiers:
        n.log(message)


# ── Demo ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("── Shape Polymorphism (overriding) ──")
    shapes: list[Shape] = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]
    for shape in shapes:
        print(f"  {shape.describe()}")

    print("\n── Duck Typing ──")
    notify_all([Logger(), SlackNotifier(), EmailNotifier()], "Server deployed!")

    print("\n── isinstance checks ──")
    c = Circle(3)
    print(f"  is Shape?     {isinstance(c, Shape)}")
    print(f"  is Circle?    {isinstance(c, Circle)}")
    print(f"  is Rectangle? {isinstance(c, Rectangle)}")
