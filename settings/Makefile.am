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

gtk3settingsdir = $(datadir)/gtk-3.0
dist_gtk3settings_DATA = \
	settings.ini \
	$(NULL)

gtk4settingsdir = $(datadir)/gtk-4.0
dist_gtk4settings_DATA = \
	settings.ini \
	$(NULL)

xsessiondir = $(sysconfdir)/X11/Xsession.d
dist_xsession_DATA = \
	65gtk-overlay-scrolling \
	$(NULL)

containers_settingsdir = $(sysconfdir)/containers/registries.conf.d
dist_containers_settings_DATA = \
	00-default-registries.conf \
	$(NULL)

cupspkhelperdir = $(datadir)/polkit-1/rules.d
dist_cupspkhelper_DATA = \
	com.endlessm.Config.Printing.rules \
	$(NULL)

nmconfdir = $(exec_prefix)/lib/NetworkManager/conf.d
dist_nmconf_DATA = \
	endless-connectivity.conf \
	$(NULL)

EXTRA_DIST = \
	dconf-defaults/settings \
	com.endlessm.settings.gschema.override.in \
	user.in \
	$(NULL)

CLEANFILES = \
	$(dconf_defaults_DATA) \
	$(dconf_profile_DATA) \
	$(settings_DATA) \
	$(NULL)

@GSETTINGS_RULES@
