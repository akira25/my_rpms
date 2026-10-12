#!/bin/sh
#
# Manually submit COPR builds for the given packages (in dependency order), the
# same way the CI does. COPR builds the current commit from the repository on
# Codeberg, so it has to be pushed first.
#
# Usage: ./build.sh PACKAGE... | all
#

set -eu

if [ $# -eq 0 ]; then
    echo "Usage: $0 PACKAGE... | all" >&2
    exit 1
fi

if ! git merge-base --is-ancestor HEAD '@{upstream}' 2>/dev/null; then
    echo "HEAD is not pushed yet, COPR could not build it." >&2
    exit 1
fi

PACKAGES="$*" COPR_WAIT=0 exec "$(dirname "$0")/ci/packages.py" ci
