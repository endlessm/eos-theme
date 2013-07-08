do_subst = sed -e 's|@DATA_DIR[@]|$(datadir)|g'

com.endlessm.settings.gschema.override: com.endlessm.settings.gschema.override.in
	$(AM_V_GEN) $(do_subst) $< > $@
50_eos-theme.gschema.override: com.endlessm.settings.gschema.override $(top_srcdir)/desktop/settings/com.endlessm.desktop.gschema.override
	$(AM_V_GEN) cat com.endlessm.settings.gschema.override $(top_srcdir)/desktop/settings/com.endlessm.desktop.gschema.override > $@

settingsdir = $(datadir)/glib-2.0/schemas
settings_DATA = \
	50_eos-theme.gschema.override

CLEANFILES = \
	$(settings_DATA) \
	com.endlessm.settings.gschema.override

@GSETTINGS_RULES@
