do_subst = sed \
	-e 's|@DATADIR[@]|$(datadir)|g' \
	-e 's|@LOCALSTATEDIR[@]|$(localstatedir)|g' \
	$(NULL)

50_eos-theme.gschema.override: com.endlessm.settings.gschema.override.in Makefile
	$(AM_V_GEN) $(do_subst) $< >$@.tmp && mv $@{.tmp,}

user: user.in Makefile
	$(AM_V_GEN) $(do_subst)  $< >$@.tmp && mv $@{.tmp,}

settings: dconf-defaults/settings Makefile
	$(AM_V_GEN) $(DCONF) compile $@ $(dir $<)

dconf_defaultsdir = $(datadir)/eos-default-settings
dconf_defaults_DATA = \
	settings \
	$(NULL)

dconf_profiledir = $(datadir)/dconf/profile
dconf_profile_DATA = \
	user \
	$(NULL)

settingsdir = $(datadir)/glib-2.0/schemas
settings_DATA = \
	50_eos-theme.gschema.override \
	$(NULL)

xsessiondir = $(sysconfdir)/X11/Xsession.d
xsession_DATA = \
	65gtk-overlay-scrolling \
	$(NULL)

chrome_policydir = $(datadir)/eos-chrome-policies
chrome_policy_DATA = \
	safe_search.json \
	$(NULL)

EXTRA_DIST = \
	dconf-defaults/settings \
	com.endlessm.settings.gschema.override.in \
	user.in \
	$(xsession_DATA) \
	$(NULL)

CLEANFILES = \
	$(dconf_defaults_DATA) \
	$(dconf_profile_DATA) \
	$(settings_DATA) \
	$(NULL)

@GSETTINGS_RULES@
