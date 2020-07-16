import csv
import sys
from decimal import Decimal
from math import log10

import data
from farey import farey


def iter_count(num, expected):
    i = 1
    for appx in farey(num):
        if appx == expected:
            return i
        elif appx.denominator >= expected.denominator:
            return -1
        i += 1


field_order = ['ln_base', 'ln_exp', 'ld_base', 'ld_exp', 'rn', 'rd', 'iters', 'digits']
writer = csv.DictWriter(sys.stdout, field_order, extrasaction='ignore')
writer.writeheader()
for case in data.approximations:
    lhs_decimal = Decimal(case.lhs.numerator) / Decimal(case.lhs.denominator)
    rhs_decimal = Decimal(case.rhs_frac.numerator) / Decimal(case.rhs_frac.denominator)
    writer.writerow({
        'iters': iter_count(lhs_decimal / data.PI, case.rhs_frac),
        'digits': int(-log10(abs(lhs_decimal / rhs_decimal - data.PI))),
        **case.__dict__,
    })
