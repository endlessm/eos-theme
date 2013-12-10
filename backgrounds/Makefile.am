do_subst = sed -e 's|@DATA_DIR[@]|$(datadir)|g'

endlessos-backgrounds-default.xml.in: endlessos-backgrounds-default.xml.in.in
	$(AM_V_GEN) $(do_subst) $< > $@

@INTLTOOL_XML_RULE@

default_images = $(datadir)/eos-media/default_images

install-data-hook:
	$(mkdir_p) $(DESTDIR)$(datadir)/EndlessOS/personality-defaults
	ln -fs $(default_images)/bg_global_01.jpg $(DESTDIR)$(datadir)/EndlessOS/personality-defaults/desktop-background-default.jpg
	ln -fs $(default_images)/bg_brazil_13.jpg $(DESTDIR)$(datadir)/EndlessOS/personality-defaults/desktop-background-Brazil.jpg
	ln -fs $(default_images)/bg_global_01.jpg $(DESTDIR)$(datadir)/EndlessOS/personality-defaults/desktop-background-Global.jpg
	ln -fs $(default_images)/bg_guatemala_09.jpg $(DESTDIR)$(datadir)/EndlessOS/personality-defaults/desktop-background-Guatemala.jpg

uninstall-hook:
	rm -f $(DESTDIR)$(datadir)/EndlessOS/personality-defaults/desktop-background-default.jpg
	rm -f $(DESTDIR)$(datadir)/EndlessOS/personality-defaults/desktop-background-Brazil.jpg
	rm -f $(DESTDIR)$(datadir)/EndlessOS/personality-defaults/desktop-background-Global.jpg
	rm -f $(DESTDIR)$(datadir)/EndlessOS/personality-defaults/desktop-background-Guatemala.jpg

metadatadir = $(datadir)/gnome-background-properties
metadata_DATA = endlessos-backgrounds-default.xml

noinst_DATA = endlessos-backgrounds-default.xml.in
CLEANFILES = endlessos-backgrounds-default.xml endlessos-backgrounds-default.xml.in

EXTRA_DIST = endlessos-backgrounds-default.xml.in.in
