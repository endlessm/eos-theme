enginedir = $(libdir)/gtk-3.0/$(GTK3_VERSION)/theming-engines
engine_LTLIBRARIES =
engine_LTLIBRARIES += libendlessos.la

libendlessos_la_SOURCES =			\
	endlessos_utils.h			\
	endlessos_utils.c			\
	endlessos_engine.c
libendlessos_la_CFLAGS = $(GTK3_ENGINE_CFLAGS)
libendlessos_la_LDFLAGS = -module -avoid-version -no-undefined
libendlessos_la_LIBADD = $(GTK3_ENGINE_LIBS)

themedir = $(datadir)/themes/EndlessOS/gtk-3.0
theme_DATA = 		\
	gtk.gresource	\
	gtk.css 	\
	gtk-dark.css	\
	endless-widgets.css \
	settings.ini

resource_files = $(shell $(GLIB_COMPILE_RESOURCES) --sourcedir=$(srcdir) --generate-dependencies $(srcdir)/gtk.gresource.xml)
gtk.gresource: gtk.gresource.xml $(resource_files)
	$(AM_V_GEN) $(GLIB_COMPILE_RESOURCES) --target=$@ --sourcedir=$(srcdir)  $<

EXTRA_DIST = \
	$(resource_files) \
	gtk.css \
	gtk-dark.css \
	gtk.gresource.xml \
	endless-widgets.css \
	settings.ini

CLEANFILES = \
	gtk.gresource
