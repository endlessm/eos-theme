dnl Process this file with autoconf to produce a configure script.
AC_PREREQ(2.53)

AC_INIT([eos-theme], [1.5.0],
        [http://www.endlessm.com])

AM_INIT_AUTOMAKE([1.9 tar-ustar foreign dist-xz no-dist-gzip])
m4_ifdef([AM_SILENT_RULES],[AM_SILENT_RULES([yes])])

PKG_PROG_PKG_CONFIG([0.19])

AC_PROG_SED
AC_PROG_CC
AC_PROG_INSTALL
AC_PROG_MAKE_SET
AM_PATH_GLIB_2_0

dnl Initialize libtool
AM_DISABLE_STATIC
AC_LIBTOOL_WIN32_DLL
AM_PROG_LIBTOOL

dnl Initialize intltool
IT_PROG_INTLTOOL([0.40.0])

GETTEXT_PACKAGE="${PACKAGE}"
AC_SUBST(GETTEXT_PACKAGE)

GLIB_GSETTINGS

AC_ARG_ENABLE([gtk2-engine],
              AC_HELP_STRING([--disable-gtk2-engine],
                             [Disable Gtk+-2 engine [default=no]]),
              enable_gtk2_engine=$enableval,
              enable_gtk2_engine=yes)
AC_MSG_CHECKING([building gtk2 engine])
AM_CONDITIONAL(GTK2_ENGINE, test "x$enable_gtk2_engine" = "xyes")
AC_MSG_RESULT([$enable_gtk2_engine])

GTK2_VERSION_REQUIRED=2.24.15
if test "x$enable_gtk2_engine" = "xyes"; then
  PKG_CHECK_MODULES([GTK2_ENGINE], [gtk+-2.0 >= $GTK2_VERSION_REQUIRED gdk-2.0 >= $GTK2_VERSION_REQUIRED])
fi

GTK2_VERSION=`$PKG_CONFIG --variable=gtk_binary_version gtk+-2.0`
AC_SUBST(GTK2_VERSION)

GLIB_COMPILE_RESOURCES=`$PKG_CONFIG --variable glib_compile_resources gio-2.0`
AC_SUBST(GLIB_COMPILE_RESOURCES)

AC_PATH_PROG(GTK_UPDATE_ICON_CACHE, gtk-update-icon-cache)
if test -z "$GTK_UPDATE_ICON_CACHE"; then
    AC_MSG_ERROR([Could not find gtk-update-icon-cache])
fi

# Workaround to make aclocal get the right flags
AC_SUBST(ACLOCAL_AMFLAGS, "\${ACLOCAL_FLAGS}")

AC_CONFIG_FILES([
Makefile
fonts/Makefile
backgrounds/Makefile
icons/Makefile
settings/Makefile
themes/Makefile
themes/EndlessOS/Makefile
themes/EndlessOS/gtk-2.0/Makefile
themes/EndlessOS/metacity-1/Makefile
po/Makefile.in
])

AC_OUTPUT
