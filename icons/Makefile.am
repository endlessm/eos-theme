themedir = $(datadir)/icons/EndlessOS
theme_in_files = index.theme.in.in
theme_DATA = $(theme_in_files:.theme.in.in=.theme)

render_sizes = "24x24" "64x64" "scalable"
THEME_DIRS=$(shell SIZES="$(render_sizes)"; for size in $$SIZES; do for dir in `find $(srcdir)/$$size/* -type d`; do printf "$$dir,"; done; done;)
THEME_FILES=$(shell SIZES="$(render_sizes)"; for size in $$SIZES; do for file in `find $(srcdir)/$$size/* \( -name "*.png" -or -name "*.svg" \)`; do printf "$$file "; done; done;)

EXTRA_DIST = index.theme.in.in $(THEME_FILES)

index.theme.in: index.theme.in.in Makefile
	dirs="`echo $(THEME_DIRS) | sed -e 's#\./##g'`"; \
	sed -e "s|\@THEME_DIRS\@|$$dirs|g" < $< > $@; \
	echo "" >> $@; \
	for dir in `echo $$dirs | sed -e "s/,/ /g"`; do \
		sizefull="`dirname $$dir`"; \
		if test "$$sizefull" = "scalable"; then \
			size="16"; \
		else \
			size="`echo $$sizefull | sed -e 's/x.*$$//g'`"; \
		fi; \
		context="`basename $$dir`"; \
		echo "[$$dir]" >> $@; \
		if test "$$context" = "actions"; then \
			echo "Context=Actions" >> $@; \
		fi; \
		if test "$$context" = "animations"; then \
			echo "Context=Animations" >> $@; \
		fi; \
		if test "$$context" = "apps"; then \
			echo "Context=Applications" >> $@; \
		fi; \
		if test "$$context" = "categories"; then \
			echo "Context=Categories" >> $@; \
		fi; \
		if test "$$context" = "devices"; then \
			echo "Context=Devices" >> $@; \
		fi; \
		if test "$$context" = "emblems"; then \
			echo "Context=Emblems" >> $@; \
		fi; \
		if test "$$context" = "emotes"; then \
			echo "Context=Emotes" >> $@; \
		fi; \
		if test "$$context" = "intl"; then \
			echo "Context=International" >> $@; \
		fi; \
		if test "$$context" = "mimetypes"; then \
			echo "Context=MimeTypes" >> $@; \
		fi; \
		if test "$$context" = "places"; then \
			echo "Context=Places" >> $@; \
		fi; \
		if test "$$context" = "status"; then \
			echo "Context=Status" >> $@; \
		fi; \
		if test "$$context" = "stock"; then \
			echo "Context=Stock" >> $@; \
		fi; \
		echo "Size=$$size" >> $@; \
		if test "$$sizefull" = "scalable"; then \
			echo "MinSize=8" >> $@; \
			echo "MaxSize=512" >> $@; \
			echo "Type=Scalable" >> $@; \
		elif test "$$size" = "256"; then \
			echo "MinSize=56" >> $@; \
			echo "MaxSize=512" >> $@; \
			echo "Type=Scalable" >> $@; \
		elif test "$$context" = "stock"; then \
			echo "Type=Scalable" >> $@; \
		else \
			echo "Type=Fixed" >> $@; \
		fi; \
		echo "" >> $@; \
	done

@INTLTOOL_THEME_RULE@

install-data-local:
	for size in $(render_sizes); do \
		echo -e "Going to copy files for $$size"; \
		for file in `cd $(srcdir)/$$size && find . \( -name "*.png" -or -name "*.svg" \)`; do \
			context="`dirname $$file`"; \
			$(mkdir_p) $(DESTDIR)$(themedir)/$$size/$$context; \
			$(install_sh_DATA) $(srcdir)/$$size/$$file $(DESTDIR)$(themedir)/$$size/$$file; \
		done; \
	done

uninstall-local:
	for size in $(render_sizes); do \
		for file in `cd $(srcdir)/$$size && find . \( -name "*.png" -or -name "*.svg" \)`; do \
			rm -f $(DESTDIR)$(themedir)/$$size/$$file; \
		done; \
	done

install-data-hook:
	if test -z "$(DESTDIR)" ; then \
		$(GTK_UPDATE_ICON_CACHE) -q $(DESTDIR)$(themedir); \
	fi

uninstall-hook:
	@rm -f  $(DESTDIR)$(themedir)/icon-theme.cache

CLEANFILES = index.theme.in index.theme
