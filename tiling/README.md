# Land mapping & navigation

This group of components uses a conventional requirements + constraints flow to define a Python lock environment (`requirements_lock.txt`) which is loaded into Bazel as the `@land_pip` hub workspace.

The requirement lock is defined in this Bazel package by the `:requirements` rule.

Every package listed in the lockfile is available according to the locked configuration as `@land_pip//<package>`, for instance `requests` is `@land_pip//requests`. These external `py_library` rules form a full dependency graph according to the package dependencies. Depending on one will make any transitive dependencies it may have available.


