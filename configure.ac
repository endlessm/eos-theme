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
AC_PATH_PROG([DCONF],[dconf])

AC_PATH_PROG(GTK_UPDATE_ICON_CACHE, gtk-update-icon-cache)
if test -z "$GTK_UPDATE_ICON_CACHE"; then
    AC_MSG_ERROR([Could not find gtk-update-icon-cache])
fi

AC_PATH_PROG(GTK_ENCODE_SYMBOLIC_SVG, gtk-encode-symbolic-svg)
if test -z "$GTK_ENCODE_SYMBOLIC_SVG"; then
    AC_MSG_ERROR([Could not find gtk-encode-symbolic-svg])
fi

# Workaround to make aclocal get the right flags
AC_SUBST(ACLOCAL_AMFLAGS, "\${ACLOCAL_FLAGS}")

AC_ARG_ENABLE(icontheme,
              [AC_HELP_STRING([--enable-icontheme],
                              [enable icon theme build [default=yes]])],,
              [enable_icontheme="yes"])
AM_CONDITIONAL([BUILD_ICONTHEME],[test "x$enable_icontheme" = "xyes"])

AC_ARG_ENABLE(app_icons,
              [AC_HELP_STRING([--enable-app-icons],
                              [include app icons in theme [default=no]])],
              [enable_app_icons="yes"],)
AM_CONDITIONAL([BUILD_APP_ICONS],[test "x$enable_app_icons" = "xyes"])

AC_ARG_ENABLE(fonts,
              [AC_HELP_STRING([--enable-fonts],
                              [enable fonts build [default=yes]])],,
              [enable_fonts="yes"])
AM_CONDITIONAL([BUILD_FONTS],[test "x$enable_fonts" = "xyes"])

AC_ARG_ENABLE(settings,
              [AC_HELP_STRING([--enable-settings],
                              [enable settings build [default=yes]])],,
              [enable_settings="yes"])
AM_CONDITIONAL([BUILD_SETTINGS],[test "x$enable_settings" = "xyes"])

# allow systemdunitdir to be overridden on the command line so
# that make distcheck doesn't fail when run as a non-root user
m4_define([no_systemdunitdir_error],
          [m4_normalize([Could not get systemdsystemunitdir setting from]
                        [systemd pkg-config file])])
AC_ARG_WITH([systemdunitdir],
            [AS_HELP_STRING([--with-systemdunitdir],
                            [Path to the system directory for systemd units])],
            [systemdunitdir="$withval"],
            [PKG_CHECK_VAR([systemdunitdir], [systemd],
                           [systemdsystemunitdir], [],
                           [AC_MSG_ERROR(no_systemdunitdir_error)])])

AC_CONFIG_FILES([
Makefile
fonts/Makefile
icons/Makefile
safe-defaults/Makefile
settings/Makefile
po/Makefile.in
])

AC_OUTPUT
