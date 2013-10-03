do_subst = sed -e 's|@DATA_DIR[@]|$(datadir)|g'

endlessos.xml.in: endlessos.xml.in.in
	$(AM_V_GEN) $(do_subst) $< > $@

@INTLTOOL_XML_RULE@

backgroundsdir = $(datadir)/EndlessOS/backgrounds
backgrounds_DATA = \
	$(wildcard *.jpg)

metadatadir = $(datadir)/gnome-background-properties
metadata_DATA = endlessos.xml

noinst_DATA = endlessos.xml.in
CLEANFILES = endlessos.xml endlessos.xml.in

EXTRA_DIST = $(backgrounds_DATA) endlessos.xml.in.in
