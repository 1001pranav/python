"""
=============================================================================
02 — INHERITANCE
Single, Multi-Level, Multiple, Hierarchical Inheritance + MRO
=============================================================================
"""


# ── Base (Parent) Class ───────────────────────────────────────────────────
class Employee:
    def __init__(self, name: str, emp_id: str, salary: float) -> None:
        self.name   = name
        self.emp_id = emp_id
        self.salary = salary

    def get_details(self) -> str:
        return f"[{self.emp_id}] {self.name} — ₹{self.salary:,.0f}"

    def calculate_bonus(self) -> float:
        return self.salary * 0.10     # 10% base bonus

    def __str__(self) -> str:
        return self.get_details()


# ── Single Inheritance ────────────────────────────────────────────────────
class Developer(Employee):
    def __init__(self, name: str, emp_id: str, salary: float, stack: list) -> None:
        super().__init__(name, emp_id, salary)   # delegate to parent
        self.stack = stack

    def get_details(self) -> str:                # override
        base = super().get_details()
        return f"{base} | Stack: {', '.join(self.stack)}"

    def calculate_bonus(self) -> float:          # override
        return self.salary * 0.20                # devs earn 20%


# ── Multi-Level Inheritance ───────────────────────────────────────────────
class SeniorDeveloper(Developer):
    def __init__(self, name, emp_id, salary, stack, team_size: int) -> None:
        super().__init__(name, emp_id, salary, stack)
        self.team_size = team_size

    def get_details(self) -> str:
        return f"{super().get_details()} | Team: {self.team_size} devs"

    def calculate_bonus(self) -> float:
        return self.salary * 0.30 + (self.team_size * 5000)  # leadership bonus


# ── Multiple Inheritance ──────────────────────────────────────────────────
class Freelancer:
    def __init__(self, hourly_rate: float) -> None:
        self.hourly_rate = hourly_rate

    def calculate_payment(self, hours: int) -> float:
        return self.hourly_rate * hours


class FreelanceDeveloper(Developer, Freelancer):
    """Inherits from both Developer AND Freelancer (Diamond Problem handled by MRO)."""
    def __init__(self, name, emp_id, salary, stack, hourly_rate) -> None:
        Developer.__init__(self, name, emp_id, salary, stack)
        Freelancer.__init__(self, hourly_rate)


# ── Hierarchical Inheritance ──────────────────────────────────────────────
class Designer(Employee):
    """Designer and Developer both inherit from Employee — hierarchical."""
    def __init__(self, name, emp_id, salary, tools: list) -> None:
        super().__init__(name, emp_id, salary)
        self.tools = tools

    def get_details(self) -> str:
        base = super().get_details()
        return f"{base} | Tools: {', '.join(self.tools)}"

    def calculate_bonus(self) -> float:
        return self.salary * 0.15


# ── Demo ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    dev = Developer("Pranav", "DEV001", 120_000, ["Node.js", "Python", "AWS"])
    sr  = SeniorDeveloper("Alice", "SR001", 180_000, ["Python", "K8s"], team_size=5)
    fl  = FreelanceDeveloper("Bob", "FL001", 0, ["React"], hourly_rate=2500)
    des = Designer("Carol", "DES001", 100_000, ["Figma", "Photoshop"])

    print("── Employee Details & Bonuses ──")
    for person in [dev, sr, des]:
        print(person.get_details())
        print(f"  Bonus: ₹{person.calculate_bonus():,.0f}\n")

    print(f"Freelancer Bob earned: ₹{fl.calculate_payment(40):,.0f} for 40 hrs")

    # MRO — Python resolves method calls left-to-right, depth-first
    print("\n── MRO of FreelanceDeveloper ──")
    for cls in FreelanceDeveloper.__mro__:
        print(f"  → {cls.__name__}")
