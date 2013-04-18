settingsdir = $(datadir)/glib-2.0/schemas
settings_DATA = \
	com.endlessm.gschema.override

install-data-hook:
	glib-compile-schemas $(datadir)/glib-2.0/schemas

uninstall-hook:
	glib-compile-schemas $(datadir)/glib-2.0/schemas
