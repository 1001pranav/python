"""
=============================================================================
05 — ABSTRACTION
Abstract Base Classes (ABC), @abstractmethod, template method pattern
=============================================================================
"""

from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    """
    Abstract contract — defines WHAT must be done, not HOW.
    Any concrete gateway MUST implement connect(), charge(), refund().
    Attempting to instantiate this class directly raises TypeError.
    """

    @abstractmethod
    def connect(self) -> bool: ...

    @abstractmethod
    def charge(self, amount: float) -> dict: ...

    @abstractmethod
    def refund(self, transaction_id: str) -> bool: ...

    # ── Template method — concrete shared behaviour ───────────────────────
    # Subclasses don't override this; they only fill in the abstract pieces.
    def process_payment(self, amount: float) -> dict:
        if not self.connect():
            return {"status": "error", "msg": "Connection failed"}
        result = self.charge(amount)
        print(f"[{self.__class__.__name__}] Processed ₹{amount} → {result['status']}")
        return result


# ── Concrete implementations ──────────────────────────────────────────────
class RazorpayGateway(PaymentGateway):
    def connect(self) -> bool:
        print("  Razorpay: connected via API key")
        return True

    def charge(self, amount: float) -> dict:
        return {"status": "success", "txn_id": "RPY_001", "amount": amount}

    def refund(self, transaction_id: str) -> bool:
        print(f"  Razorpay: refunded {transaction_id}")
        return True


class StripeGateway(PaymentGateway):
    def connect(self) -> bool:
        print("  Stripe: connected via secret key")
        return True

    def charge(self, amount: float) -> dict:
        return {"status": "success", "txn_id": "STR_001", "amount": amount}

    def refund(self, transaction_id: str) -> bool:
        print(f"  Stripe: refunded {transaction_id}")
        return True


class FailingGateway(PaymentGateway):
    """Simulates a gateway that can't connect."""
    def connect(self) -> bool:
        return False

    def charge(self, amount: float) -> dict:
        return {}

    def refund(self, transaction_id: str) -> bool:
        return False


# ── Demo ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Cannot instantiate the abstract class
    try:
        g = PaymentGateway()
    except TypeError as e:
        print(f"Cannot instantiate ABC → {e}\n")

    gateways = [RazorpayGateway(), StripeGateway(), FailingGateway()]
    for gw in gateways:
        result = gw.process_payment(999.00)
        if result["status"] == "error":
            print(f"  [{gw.__class__.__name__}] Failed: {result['msg']}")
        print()
