load("@aspect_rules_py//py:defs.bzl", _py_test="py_test")

def py_test(main = Label(":__test__"), **kwargs):
    """
    aspect_rules_py's py_test wrapped with a reasonable default main.
    """

    _py_test(
        main = main,
        **kwargs,
    )
