load("@aspect_rules_py//py:defs.bzl", _py_test="py_test")

def py_test(main = Label(":__test__"), **kwargs):
    _py_test(
        main = main,
        **kwargs,
    )
