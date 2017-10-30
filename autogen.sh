#!/bin/sh

test -n "$srcdir" || srcdir=`dirname "$0"`
test -n "$srcdir" || srcdir=.

olddir=`pwd`
cd "$srcdir"

INTLTOOLIZE=`which intltoolize`
if test -z $INTLTOOLIZE; then
        echo "*** Unable to find intltoolize; you must install intltool ***"
        exit 1
fi

AUTORECONF=`which autoreconf`
if test -z $AUTORECONF; then
        echo "*** Unable to find autoreconf; you must install Autotools ***"
        exit 1
fi

${INTLTOOLIZE} || exit $?
${AUTORECONF} -f -v -i || exit $?

cd "$olddir"

test -n "$NOCONFIGURE" || "$srcdir/configure" "$@"
