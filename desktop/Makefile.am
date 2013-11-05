EXTRA_DIST = applications.csv	\
	extras.csv		\
	links.csv		\
	folders.csv		\
	csv_to_desktop.py	\
	eos-exec-localized	\
	eos-select-personality.in

BUILT_SOURCES = \
	.dot_desktop_files_timestamp

do_subst = sed \
	-e 's|@DATA_DIR[@]|$(datadir)|g' \
	-e 's|@SYSCONF_DIR[@]|$(sysconfdir)|g'

eos-select-personality: eos-select-personality.in Makefile
	$(AM_V_GEN) $(do_subst) $< > $@
	chmod +x $@

.dot_desktop_files_timestamp: csv_to_desktop.py applications.csv links.csv folders.csv
	@mkdir -p applications
	@mkdir -p links
	@mkdir -p folders
	$(AM_V_GEN) $(srcdir)/csv_to_desktop.py --basedir $(datadir)/EndlessOS
	@touch .dot_desktop_files_timestamp

appsdir = $(datadir)/applications
apps_DATA = $(wildcard $(srcdir)/applications/*.desktop)

linksdir = $(datadir)/applications
links_DATA = $(wildcard $(srcdir)/links/*.desktop)

foldersdir = $(datadir)/desktop-directories
folders_DATA = $(wildcard $(srcdir)/folders/*.directory)

desktopsdir = $(datadir)/EndlessOS/personality-defaults
desktops_DATA = $(wildcard settings/icon-grid-*.json)

bin_SCRIPTS = eos-exec-localized eos-select-personality

CLEANFILES = eos-select-personality

clean-local:
	rm -rf applications
	rm -rf links
	rm -rf folders
	rm -rf settings
	rm .dot_desktop_files_timestamp
