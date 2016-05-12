### fix for issue #11099 | pull request #11100 (merged)

def patch(sympy_mod):
    def _min_max_base_evalf_fix(self, prec=None, **options):
        return self.func(*[a.evalf(prec, **options) for a in self.args])
    sympy_mod.functions.elementary.miscellaneous.MinMaxBase.evalf = \
            _min_max_base_evalf_fix
