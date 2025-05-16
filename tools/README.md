# //tools

This package is best understood as providing Bazel support.

`//tools/build_rules` is a subpackage that Bazel has magical knowledge of.

`//tools:bazel` as a script is something both Bazel and Bazelisk have magical knowledge of.

Of particular interest in this package is the use of
[rules_multitool](https://github.com/theoremlp/rules_multitool/) to allow Bazel
to fetch a ton of general utilities.

Also of note is the usage of [bazel_env](github.com/buildbuddy-io/bazel_env.bzl)
to integrate the Bazel-defined tools with [direnv](https://direnv.net/). Of
particular note is that we're configuring both the `//tools:format` and
`//tools/dazel:dazel` targets to be presented on the `$PATH`.
