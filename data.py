"""
Parses the data files so they can be manipulated within Python.
"""

import csv
from decimal import Decimal
from fractions import Fraction
from pathlib import Path

data_dir = Path(__file__).parent / 'data'


class Approximation:
    """
    Approximations of the form `(ln_base ** ln_exp) / (ld_base ** ld_exp) == (rn / rd) * pi`.
    """
    ln_base: int
    ln_exp: int
    ld_base: int
    ld_exp: int
    rn: int
    rd: int
    
    def __init__(self, ln_base, ln_exp, ld_base, ld_exp, rn, rd):
        self.ln_base = ln_base
        self.ln_exp = ln_exp
        self.ld_base = ld_base
        self.ld_exp = ld_exp
        self.rn = rn
        self.rd = rd

    @property
    def lhs(self) -> Fraction:
        """
        The left-hand side of the approximation.
        """
        return Fraction(ln_base ** ln_exp, ld_base ** ld_exp)

    def rhs_frac(self) -> Fraction:
        """
        The fraction multiple of pi on the right-hand-side (pi excluded).
        """
        return Fraction(rn, rd)

    def __repr__(self):
        return '{}^{} / {}^{} = ({} / {}) * pi'.format(
            self.ln_base,
            self.ln_exp,
            self.ld_base,
            self.ld_exp,
            self.rn,
            self.rd,
        )


with open(data_dir / 'approximations.csv', 'r') as f:
    reader = csv.DictReader(f)
    approximations = [
        Approximation(**{k: int(v) for k, v in row.items()})
        for row in reader
    ]
