do_subst = sed -e 's|@DATA_DIR[@]|$(datadir)|g'

endlessos.xml.in: endlessos.xml.in.in
	$(AM_V_GEN) $(do_subst) $< > $@

@INTLTOOL_XML_RULE@

default_images = $(datadir)/eos-media/default_images

install-data-hook:
	ln -fs $(default_images)/bg_guatemala_09.jpg $(datadir)/EndlessOS/personality-defaults/desktop-background-default.jpg
	ln -fs $(default_images)/bg_guatemala_09.jpg $(datadir)/EndlessOS/personality-defaults/desktop-background-Guatemala.jpg
	ln -fs $(default_images)/bg_brazil_13.jpg $(datadir)/EndlessOS/personality-defaults/desktop-background-Brazil.jpg

uninstall-hook:
	rm -f $(datadir)/EndlessOS/personality-defaults/desktop-background-default.jpg
	rm -f $(datadir)/EndlessOS/personality-defaults/desktop-background-Guatemala.jpg
	rm -f $(datadir)/EndlessOS/personality-defaults/desktop-background-Brazil.jpg

metadatadir = $(datadir)/gnome-background-properties
metadata_DATA = endlessos.xml

noinst_DATA = endlessos.xml.in
CLEANFILES = endlessos.xml endlessos.xml.in

EXTRA_DIST = endlessos.xml.in.in
