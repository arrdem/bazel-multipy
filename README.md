# Monorepo example - multi pip

This repo provides an example of a trio of applications across a pair of
projects, where each project uses a different virtualenv. The intent is to
provide an example of current Bazel x Python ecosystem patterns.

Highlights:
- `rules_uv` used to implement requirements lock management (`:requirements.update`)
- `rules_python` used to fetch a hermetic Python toolchain and Pip deps; see `MODULE.bazel` for details.
- `aspect_rules_py` used to provide familiar Pytest flows
- `//tools/docker` implements building a "base" and "dev" image
- `//tools/dazel:dazel` implements builds under Docker with a persistent devcontainer defined by `//tools/docker`
- `bazel_env` + `direnv` puts `dazel` on the `$PATH` for convenience

Key features:
- Changes to `Dockerfile-base` or `Dockerfile-dev` will cause image rebuilds automatically
- Changes to the `dazel` devcontainer configuration (including invalidation of the image target!) will cause a restart
- The `dazel` devcontainer makes its outputs available natively in the host filesystem (`dazel-bin`, etc)

Possible refinements:
- The `dazel` tool is quick work and could use refinement
- The `//tools/docker` flow using `genrule` is ... unidiomatic.
- While the `:dev.label` and `:dev.digest` targets are cute and highly effective, Docker image cleanups could invalidate them silently.
  It would be better albeit slower to create an explicit post-build export/import phase which would allow Bazel to persist the image definition.
