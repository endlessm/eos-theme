do_subst = sed -e 's|@DATA_DIR[@]|$(datadir)|g'

com.endlessm.gschema.override: com.endlessm.gschema.override.in
	$(AM_V_GEN) $(do_subst) $< > $@

settingsdir = $(DESTDIR)$(datadir)/glib-2.0/schemas
settings_DATA = \
	com.endlessm.gschema.override

CLEANFILES = $(settings_DATA)
EXTRA_DIST = com.endless.gschema.override.in

install-data-hook:
	true #glib-compile-schemas $(datadir)/glib-2.0/schemas

uninstall-hook:
	true #glib-compile-schemas $(datadir)/glib-2.0/schemas
