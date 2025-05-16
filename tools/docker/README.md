# Docker support

Docker is a real challenge for Bazel, because most of what users want to do with
Docker is perform non-reproducible tasks (download and install packages). This
is a huge part of what makes `docker build` "easy" for most applications.

While it is theoretically possible to use
[rules_oci](https://github.com/bazel-contrib/rules_oci) to take a base image,
fetch a number of `.deb` files under Bazel and produce the OCI container tree
resulting from "installing" all those artifacts atop a given base, it's not
reasonable to ask engineers to manage base containers with hundreds of package
dependencies this way.

It's also not viable -- Docker daemons only support 126 or so layers and a
"simple" Ubuntu devcontainer with GCC and G++ weighs some 180 packages or so.

As a compromise, we have to use `docker build`. Specifically, we can use
@thesayyn's implementation of driving `buildx` directly from Bazel.

This package does a three-step.

1. It defines a base image using `buildx` and provides _verbs_ (`base.load`) for loading it into the OCI runtime.
2. It defines a devcontainer image building atop the base image and a `dev.load` verb.
3. It 
