EXTRA_DIST = applications.csv	\
	links.csv		\
	folders.csv		\
	csv_to_desktop.py

BUILT_SOURCES = \
	.dot_desktop_files_timestamp

.dot_desktop_files_timestamp: csv_to_desktop.py applications.csv links.csv folders.csv
	@mkdir -p applications
	@mkdir -p links
	@mkdir -p folders
	$(AM_V_GEN) ./csv_to_desktop.py
	@touch .dot_desktop_files_timestamp

appsdir = $(datadir)/applications
apps_DATA = $(wildcard applications/*.desktop)

linksdir = $(datadir)/applications
links_DATA = $(wildcard links/*.desktop)

foldersdir = $(datadir)/desktop-directories
folders_DATA = $(wildcard folders/*.directory)

settingsdir = $(datadir)/glib-2.0/schemas
settings_DATA = settings/com.endlessm.desktop.gschema.override

desktopsdir = $(datadir)/EndlessOS/desktops
desktops_DATA = $(wildcard settings/com.endlessm.desktop.*.gschema.override)

autostartdir = $(sysconfdir)/xdg/autostart
autostart_DATA = applications/eos-app-epiphany.desktop

bin_SCRIPTS = eos-exec-localized

@GSETTINGS_RULES@

clean-local:
	rm -rf applications
	rm -rf links
	rm -rf folders
	rm -rf settings
	rm .dot_desktop_files_timestamp
