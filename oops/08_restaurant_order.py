"""
=============================================================================
08 — BONUS: Complete System — RestaurantOrder
Combines: ABC, @property, @total_ordering, magic methods,
operator overloading, method chaining, class variables
=============================================================================
"""

from abc import ABC, abstractmethod
from functools import total_ordering
from typing import List


# ── Abstract interface ────────────────────────────────────────────────────
class Priceable(ABC):
    @abstractmethod
    def get_price(self) -> float: ...


# ── MenuItem — encapsulation + operator overloading + @total_ordering ─────
@total_ordering     # auto-generates <=, >, >= from __eq__ and __lt__
class MenuItem(Priceable):
    def __init__(self, name: str, price: float, category: str) -> None:
        self._name    = name
        self._price   = price
        self.category = category

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    def get_price(self) -> float:
        return self._price

    # ── Operator overloading ──────────────────────────────────────────────
    def __add__(self, other: "MenuItem") -> float:
        """item1 + item2 = combined price."""
        return self._price + other._price

    def __mul__(self, qty: int) -> float:
        """item * qty = subtotal."""
        return self._price * qty

    def __rmul__(self, qty: int) -> float:
        return self.__mul__(qty)

    # ── Comparison (for sorting) ──────────────────────────────────────────
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MenuItem):
            return NotImplemented
        return self._price == other._price

    def __lt__(self, other: "MenuItem") -> bool:
        return self._price < other._price

    def __hash__(self) -> int:
        return hash(self._name)

    def __str__(self) -> str:
        return f"{self._name} (₹{self._price:.2f})"

    def __repr__(self) -> str:
        return f"MenuItem({self._name!r}, {self._price})"


# ── Order — magic methods + fluent interface + class variable ─────────────
class Order:
    _order_counter = 0       # class variable — tracks all orders ever created

    def __init__(self, customer: str) -> None:
        Order._order_counter += 1
        self.order_id = f"ORD-{Order._order_counter:04d}"
        self.customer = customer
        self._items: List[tuple[MenuItem, int]] = []
        self._is_paid = False

    # ── Fluent interface (method chaining) ────────────────────────────────
    def add_item(self, item: MenuItem, qty: int = 1) -> "Order":
        self._items.append((item, qty))
        return self     # return self enables chaining

    def remove_item(self, item_name: str) -> "Order":
        self._items = [(i, q) for i, q in self._items if i.name != item_name]
        return self

    def mark_paid(self) -> "Order":
        self._is_paid = True
        return self

    # ── Computed properties ───────────────────────────────────────────────
    @property
    def subtotal(self) -> float:
        return sum(item * qty for item, qty in self._items)

    @property
    def tax(self) -> float:
        return self.subtotal * 0.05

    @property
    def total(self) -> float:
        return self.subtotal + self.tax

    @property
    def is_paid(self) -> bool:
        return self._is_paid

    # ── Magic methods ─────────────────────────────────────────────────────
    def __len__(self) -> int:
        """len(order) → total quantity of items."""
        return sum(qty for _, qty in self._items)

    def __contains__(self, item_name: str) -> bool:
        """'Lassi' in order"""
        return any(i.name == item_name for i, _ in self._items)

    def __iter__(self):
        return iter(self._items)

    def __bool__(self) -> bool:
        """An order is truthy only if it has items."""
        return len(self._items) > 0

    def __str__(self) -> str:
        status = "✅ PAID" if self._is_paid else "⏳ PENDING"
        lines = [
            f"Order {self.order_id} — {self.customer}  [{status}]",
            "─" * 40,
        ]
        for item, qty in self._items:
            lines.append(f"  {item.name:<22} x{qty}  ₹{item * qty:>7.2f}")
        lines += [
            "─" * 40,
            f"  {'Subtotal':<22}      ₹{self.subtotal:>7.2f}",
            f"  {'GST (5%)':<22}      ₹{self.tax:>7.2f}",
            f"  {'TOTAL':<22}      ₹{self.total:>7.2f}",
        ]
        return "\n".join(lines)

    def __repr__(self) -> str:
        return f"Order(id={self.order_id!r}, customer={self.customer!r}, items={len(self._items)})"


# ── Demo ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Build menu
    masala_dosa  = MenuItem("Masala Dosa",   120, "Main")
    paneer_tikka = MenuItem("Paneer Tikka",  280, "Starter")
    lassi        = MenuItem("Lassi",          80, "Drink")
    gulab_jamun  = MenuItem("Gulab Jamun",    60, "Dessert")

    # Build order using method chaining
    order = (
        Order("Pranav")
        .add_item(masala_dosa,  2)
        .add_item(paneer_tikka, 1)
        .add_item(lassi,        2)
        .add_item(gulab_jamun,  3)
    )

    print(order)

    print(f"\nTotal items   : {len(order)}")
    print(f"Has Lassi?    : {'Lassi' in order}")
    print(f"Has Biryani?  : {'Biryani' in order}")
    print(f"Truthy?       : {bool(order)}")
    print(f"Empty order?  : {bool(Order('Bob'))}")

    # Pay and reprint
    order.mark_paid()
    print(f"\nAfter payment : {'✅ Paid' if order.is_paid else '⏳ Pending'}")

    # Sorting uses __lt__ from MenuItem
    menu = [masala_dosa, paneer_tikka, lassi, gulab_jamun]
    print("\n── Menu sorted by price ──")
    for item in sorted(menu):
        print(f"  {item}")

    # Operator overloading on items
    print(f"\nDosa + Tikka  : ₹{masala_dosa + paneer_tikka:.2f}")
    print(f"3 × Lassi     : ₹{lassi * 3:.2f}")
    print(f"3 × Lassi (r) : ₹{3 * lassi:.2f}")
