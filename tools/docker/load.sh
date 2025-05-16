#!/usr/bin/env sh

set -e

DOCKERFILE="$1"
shift
TAG="$1"
shift

buildid=$(uuidgen | tr 'A-Z' 'a-z' | head -c8)

: "${DOCKER:=docker}"

if ! command -v "${DOCKER}" >/dev/null 2>&1; then
    echo "Error: No docker on the \$PATH!" >&2
    exit 1
fi

# Do the build but throw everything on stderr so we can use stdout
"${DOCKER}" build -f $(realpath "$DOCKERFILE") -t "$TAG:$buildid" "$@" . 1>&2

# And produce a rules_oci mock output
echo "Loaded image: $TAG:$buildid"
