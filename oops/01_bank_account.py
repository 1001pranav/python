"""
=============================================================================
01 — OOP CONCEPTS
Classes, Objects, Constructors, Instance vs Class variables,
@classmethod, @staticmethod, @property
=============================================================================
"""


class BankAccount:
    """A simple bank account demonstrating core OOP concepts."""

    # ── Class variable (shared across ALL instances) ──────────────────────
    bank_name: str = "PyBank"
    _total_accounts: int = 0          # "protected" by convention

    # ── Constructor (__init__) ────────────────────────────────────────────
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        # Instance variables (unique per object)
        self.owner    = owner         # public
        self._balance = balance       # protected (single underscore)
        self.__pin    = "0000"        # private (name-mangled to _BankAccount__pin)
        BankAccount._total_accounts += 1

    # ── Instance methods ──────────────────────────────────────────────────
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
        print(f"[{self.owner}] Deposited ₹{amount:.2f} | Balance: ₹{self._balance:.2f}")

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        print(f"[{self.owner}] Withdrew ₹{amount:.2f} | Balance: ₹{self._balance:.2f}")

    # ── Class method (operates on class-level state) ──────────────────────
    @classmethod
    def get_total_accounts(cls) -> int:
        """Returns how many BankAccount objects have been created."""
        return cls._total_accounts

    # ── Static method (utility; no self/cls needed) ───────────────────────
    @staticmethod
    def validate_amount(amount: float) -> bool:
        """Pure utility — doesn't need instance or class state."""
        return isinstance(amount, (int, float)) and amount > 0

    # ── Property — controlled getter/setter ───────────────────────────────
    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    def __repr__(self) -> str:
        return f"BankAccount(owner={self.owner!r}, balance={self._balance})"


# ── Demo ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    acc1 = BankAccount("Pranav", 5000)
    acc2 = BankAccount("Alice",  2000)

    acc1.deposit(1500)
    acc1.withdraw(500)

    print(f"\nTotal accounts : {BankAccount.get_total_accounts()}")
    print(f"Valid amount?  : {BankAccount.validate_amount(100)}")
    print(f"Balance (prop) : ₹{acc1.balance}")
    print(acc1)

    # Name mangling demo — private attr is accessible but discouraged
    print(f"\nPrivate pin (mangled): {acc1._BankAccount__pin}")
