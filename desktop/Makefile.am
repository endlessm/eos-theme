EXTRA_DIST = applications.csv	\
	links.csv		\
	folders.csv		\
	csv_to_desktop_applications.py	\
	csv_to_desktop_links.py \
	csv_to_desktop_folders.py

BUILT_SOURCES = \
	.apps_dot_desktop_files_timestamp \
	.links_dot_desktop_files_timestamp \
	.folders_dot_directory_files_timestamp

.apps_dot_desktop_files_timestamp: csv_to_desktop_applications.py applications.csv
	@mkdir -p applications
	$(AM_V_GEN) ./csv_to_desktop_applications.py
	@touch .apps_dot_desktop_files_timestamp

.links_dot_desktop_files_timestamp: csv_to_desktop_links.py links.csv
	@mkdir -p links
	$(AM_V_GEN) ./csv_to_desktop_links.py
	@touch .links_dot_desktop_files_timestamp

.folders_dot_directory_files_timestamp: csv_to_desktop_folders.py folders.csv
	@mkdir -p links
	$(AM_V_GEN) ./csv_to_desktop_folders.py
	@touch .folders_dot_directory_files_timestamp

appsdir = $(datadir)/applications
apps_DATA = $(wildcard applications/*.desktop)

linksdir = $(datadir)/applications
links_DATA = $(wildcard links/*.desktop)

foldersdir = $(datadir)/desktop-directories
folders_DATA = $(wildcard folders/*.directory)

autostartdir = $(sysconfdir)/xdg/autostart
autostart_DATA = applications/eos-app-epiphany.desktop

clean-local:
	rm -rf applications
	rm .apps_dot_desktop_files_timestamp
	rm -rf links
	rm .links_dot_desktop_files_timestamp
	rm -rf folders
	rm .folders_dot_directory_files_timestamp
