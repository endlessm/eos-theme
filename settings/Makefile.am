do_subst = sed -e 's|@DATA_DIR[@]|$(datadir)|g'

50_eos-theme.gschema.override: com.endlessm.settings.gschema.override.in
	$(AM_V_GEN) $(do_subst) $< > $@

settingsdir = $(datadir)/glib-2.0/schemas
settings_DATA = \
	50_eos-theme.gschema.override

xsessiondir = $(sysconfdir)/X11/Xsession.d
xsession_DATA = 65gtk-overlay-scrolling

EXTRA_DIST = \
	com.endlessm.settings.gschema.override.in \
	$(xsession_DATA)

CLEANFILES = \
	$(settings_DATA)

@GSETTINGS_RULES@
