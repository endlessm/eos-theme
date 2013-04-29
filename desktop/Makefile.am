SUBDIRS = directories

EXTRA_DIST = applications.csv	\
	links.csv		\
	csv_to_desktop_applications.py	\
	csv_to_desktop_links.py

BUILT_SOURCES = \
	.apps_dot_desktop_files_timestamp \
	.links_dot_desktop_files_timestamp

.apps_dot_desktop_files_timestamp:
	@mkdir -p applications
	$(AM_V_GEN) ./csv_to_desktop_applications.py
	@touch .apps_dot_desktop_files_timestamp

.links_dot_desktop_files_timestamp:
	@mkdir -p links
	$(AM_V_GEN) ./csv_to_desktop_links.py
	@touch .links_dot_desktop_files_timestamp

appsdir = $(datadir)/EndlessOS/applications
apps_DATA = $(wildcard applications/*.desktop)

linksdir = $(datadir)/EndlessOS/links
links_DATA = $(wildcard links/*.desktop)

clean-local:
	rm -rf applications
	rm .apps_dot_desktop_files_timestamp
	rm -rf links
	rm .links_dot_desktop_files_timestamp
