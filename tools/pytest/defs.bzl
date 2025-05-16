load("@aspect_rules_py//py:defs.bzl", _py_test = "py_test")

DEFAULT_DEP = str(Label("//tools/pytest:__test__"))
DEFAULT_MAIN = DEFAULT_DEP + ".py"

def py_pytest_factory(
        deps):
    default_deps = deps

    def _helper(deps = None, **kwargs):
        _py_test(
            pytest_main = True,
            deps = (deps or []) + default_deps,
            **kwargs
        )

    return _helper
