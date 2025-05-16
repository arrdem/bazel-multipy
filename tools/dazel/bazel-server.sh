#!/bin/bash

set -eu -o pipefail

bazel info

bazel_pid=$(bazel info server_pid)
bazel_logfile=$(bazel info server_log)

exec tail --pid="${bazel_pid}" -f "${bazel_logfile}"
