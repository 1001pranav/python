"""
=============================================================================
run_all.py — Runs all OOP modules in sequence
=============================================================================
Usage:
    python run_all.py
Or run any module individually:
    python 01_concepts/bank_account.py
=============================================================================
"""

import sys
import os
import importlib.util


MODULES = [
    ("01 — OOP Concepts",          "01_concepts/bank_account.py"),
    ("02 — Inheritance",            "02_inheritance/employee_hierarchy.py"),
    ("03 — Polymorphism",           "03_polymorphism/shapes.py"),
    ("04 — Encapsulation",          "04_encapsulation/medical_record.py"),
    ("05 — Abstraction",            "05_abstraction/payment_gateway.py"),
    ("06 — Magic Methods",          "06_magic_methods/vector.py"),
    ("07 — Operator Overloading",   "07_operator_overloading/matrix.py"),
    ("08 — Bonus System",           "08_bonus/restaurant_order.py"),
]

BASE = os.path.dirname(os.path.abspath(__file__))


def run_module(label: str, rel_path: str) -> None:
    full_path = os.path.join(BASE, rel_path)
    print("\n" + "═" * 60)
    print(f"  {label}")
    print("═" * 60)

    spec        = importlib.util.spec_from_file_location("__main__", full_path)
    module      = importlib.util.module_from_spec(spec)
    module.__name__ = "__main__"
    spec.loader.exec_module(module)


if __name__ == "__main__":
    for label, path in MODULES:
        run_module(label, path)
