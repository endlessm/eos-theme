#!/bin/sh
libtoolize && intltoolize && aclocal && automake --add-missing && autoconf
