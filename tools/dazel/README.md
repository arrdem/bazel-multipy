# Dazel

> Bazel + Docker = Dazel

With credit to https://github.com/nadirizr/dazel, which this has a lot of notional similarity to.

This Dazel refines on the original in a few key respects.

1. The BASH implementation is more straightforwards and hackable
2. This Dazel provides a better 0conf experience
3. This Dazel uses Bazel to fetch loaded images, allowing Bazel to serve as the image source of truth
4. This Dazel does a better job of providing automated container restarts on config changes
5. This Dazel can be used as a `tools/bazel` script for full transparency, although there are some oddities with doing so

Notionally it consists of two parts -- a client known as `dazel` and the server
script which runs inside a dev container and serves mostly as a busy loop.

Because of Bazel's server-oriented model, efficiency demands persistent build
server processes. Otherwise cold server starts are extremely expensive. Bazel
doesn't have a way to launch a server in the foreground, so we have to fake it
by using `bazel info` to create a server and then busy-looping while that server
lives.

As long as a container exists, the client can just proxy commands to `docker
exec <container>` which needs no help to provide the expected behaviors.
