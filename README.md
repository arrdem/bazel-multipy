# Monorepo example - multi pip

This repo provides an example of a trio of applications across a pair of
projects, where each project uses a different virtualenv. The intent is to
provide an example of current Bazel x Python ecosystem patterns.

Highlights:
- `rules_uv` used to implement requirements lock management (`:requirements.update`)
- `rules_python` used to fetch a hermetic Python toolchain and Pip deps; see `MODULE.bazel` for details.
- `aspect_rules_py` used to provide familiar Pytest flows
- `//tools/docker` implements building a "base" and "dev" image
- `//tools/dazel:dazel` implements builds under Docker with a persistent devcontainer defined using `rules_oci`
- `bazel_env` + `direnv` puts `dazel` on the `$PATH` for convenience

Key features:
- Changes to `Dockerfile-base` or `Dockerfile-dev` will cause image rebuilds automatically
- Changes to the `dazel` devcontainer configuration (including invalidation of the image target!) will cause a restart
- The `dazel` devcontainer makes its outputs available natively in the host filesystem (`dazel-bin`, etc)

Possible refinements:
- The `dazel` tool is quick work and could use refinement
- The `dazel` tool could try to mount the Docker socket through to the dev container for DIND shenanigans
- The `:*.digest` rules being uncacheable is proof against Docker engine cleans, but a bit slow.
  Slightly risky operationally but would be faster to allow the loaded digests to cache so that Dazel can hit the cache.

## License

This code is of educational value only and is provided under the terms of the WTFPBL.
Use at your own risk.
