__all__ = ['sympy']

import sympy

# Future monkey patches should be imported here, each offering a `patch`
# function that modifies the sympy module passed to it.
import \
        issue_11099

issue_11099.patch(sympy)
