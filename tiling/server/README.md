# Tiling server

The application code is chatgpt's finest, but what's interesting about this
package is we're using `rules_py`'s `rules_oci` integration to take a Python
binary and integrate it into an OCI container which we can deploy.

Critically, the OCI base container we're using is the
`//tools/docker:base_oci_image` container which we've defined ourselves in this
repo _using a Dockerfile build_.

So this shows using a reproducible/frozen base, applying a Dockerfile build to
it and then composing application code on top of that Dockerfile easily.
