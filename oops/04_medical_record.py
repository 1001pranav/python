"""
=============================================================================
04 — ENCAPSULATION
Public / Protected / Private attributes, name mangling, @property
=============================================================================
"""


class MedicalRecord:
    """
    Access levels in Python:
      public    →  patient_name     (anyone can read/write)
      protected →  _blood_group     (convention: internal/subclass use only)
      private   →  __ssn            (name-mangled → _MedicalRecord__ssn)
    """

    def __init__(self, patient_name: str, blood_group: str, ssn: str) -> None:
        self.patient_name = patient_name        # public
        self._blood_group = blood_group         # protected
        self.__ssn        = ssn                 # private

    # ── Controlled read access ────────────────────────────────────────────
    @property
    def blood_group(self) -> str:
        return self._blood_group

    # ── Controlled write access with validation ───────────────────────────
    @blood_group.setter
    def blood_group(self, value: str) -> None:
        valid = {"A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"}
        if value not in valid:
            raise ValueError(f"Invalid blood group: {value}")
        self._blood_group = value

    # ── Expose only what's needed (partial reveal) ────────────────────────
    def get_ssn_masked(self) -> str:
        return "***-**-" + self.__ssn[-4:]

    def verify_ssn(self, ssn: str) -> bool:
        return self.__ssn == ssn

    def __repr__(self) -> str:
        return f"MedicalRecord(patient={self.patient_name!r}, blood={self._blood_group!r})"


# ── Demo ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    record = MedicalRecord("Pranav", "B+", "123-45-6789")

    print(f"Patient  : {record.patient_name}")       # public — direct access fine
    print(f"Blood    : {record.blood_group}")         # via property
    print(f"SSN      : {record.get_ssn_masked()}")   # controlled reveal
    print(f"Verified : {record.verify_ssn('123-45-6789')}")

    # Update via setter — validation runs automatically
    record.blood_group = "O+"
    print(f"Updated  : {record.blood_group}")

    # Bad update — setter blocks it
    try:
        record.blood_group = "Z+"
    except ValueError as e:
        print(f"Blocked  : {e}")

    # Name mangling — private is ACCESSIBLE but strongly discouraged
    print(f"\nMangled attr: {record._MedicalRecord__ssn}")

    # Direct __ssn access fails (AttributeError) — try it:
    try:
        _ = record.__ssn
    except AttributeError as e:
        print(f"Direct access blocked: {e}")
