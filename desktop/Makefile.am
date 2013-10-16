EXTRA_DIST = applications.csv	\
	extras.csv		\
	links.csv		\
	folders.csv		\
	csv_to_desktop.py	\
	eos-exec-localized	\
	eos-select-desktop.in

BUILT_SOURCES = \
	.dot_desktop_files_timestamp

do_subst = sed \
	-e 's|@DATA_DIR[@]|$(datadir)|g' \
	-e 's|@SYSCONF_DIR[@]|$(sysconfdir)|g'

eos-select-desktop: eos-select-desktop.in Makefile
	$(AM_V_GEN) $(do_subst) $< > $@
	chmod +x $@

.dot_desktop_files_timestamp: csv_to_desktop.py applications.csv links.csv folders.csv
	@mkdir -p applications
	@mkdir -p links
	@mkdir -p folders
	$(AM_V_GEN) $(srcdir)/csv_to_desktop.py
	@touch .dot_desktop_files_timestamp

appsdir = $(datadir)/applications
apps_DATA = $(wildcard $(srcdir)/applications/*.desktop)

linksdir = $(datadir)/applications
links_DATA = $(wildcard $(srcdir)/links/*.desktop)

foldersdir = $(datadir)/desktop-directories
folders_DATA = $(wildcard $(srcdir)/folders/*.directory)

desktopsdir = $(datadir)/EndlessOS/desktops
desktops_DATA = $(wildcard settings/com.endlessm.desktop.*.gschema.override)

bin_SCRIPTS = eos-exec-localized eos-select-desktop

CLEANFILES = eos-select-desktop

clean-local:
	rm -rf applications
	rm -rf links
	rm -rf folders
	rm -rf settings
	rm .dot_desktop_files_timestamp
