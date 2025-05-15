# Monorepo example - multi pip

This repo provides an example of a trio of applications across a pair of
projects, where each project uses a different virtualenv. The intent is to
provide an example of current Bazel x Python ecosystem patterns.

Highlights:
- `rules_uv` used to implement requirements lock management (`:requirements.update`)
- `rules_python` used to fetch a hermetic Python toolchain and Pip deps
- `aspect_rules_py` used to provide familiar Pytest flows
- `bazel_env` + `multitool` used to make consuming 3rdparty tools convenient
- `aspect_rules_lint` used for linting/formatting integrations
- `rules_oci` used in conjunction with `docker build` to provide builds container building
- `tools/bazel` used to provide local builds under Docker
