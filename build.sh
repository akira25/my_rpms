#!/bin/sh

#
# This triggers a new build on copr for the package specified
#

PACKAGE="$1"
SPECFILES=$(find . -name '*.spec' | cut -c 3- | cut -d'.' -f1)

if [ -z "$PACKAGE" ]; then
    echo "Please give a package-name to build"
    exit 1
fi

if ! echo "$SPECFILES" | grep -wq "$PACKAGE"; then
    echo "No package \"$PACKAGE\" found!"
    exit 1
fi

# increment release number for next-packages
case "$PACKAGE" in
  *-next)
        # increment package release number
        echo "Incrementing package release number"
        sed -i -E 's/^(Release:\s*)([0-9]+)/echo "\1$((\2+1))"/e' "$PACKAGE.spec"
        git add "$PACKAGE.spec"
        git commit -m "$PACKAGE: autoincrement package release"
        git push
        ;;
esac

copr buildscm "$PACKAGE" --clone-url https://github.com/akira25/my_rpms.git --spec "$PACKAGE".spec
