do_subst = sed -e 's|@DATA_DIR[@]|$(datadir)|g'

endlessos-backgrounds-default.xml.in: endlessos-backgrounds-default.xml.in.in
	$(AM_V_GEN) $(do_subst) $< > $@

@INTLTOOL_XML_RULE@

metadatadir = $(datadir)/gnome-background-properties
metadata_DATA = endlessos-backgrounds-default.xml

noinst_DATA = endlessos-backgrounds-default.xml.in
CLEANFILES = endlessos-backgrounds-default.xml endlessos-backgrounds-default.xml.in

EXTRA_DIST = endlessos-backgrounds-default.xml.in.in
