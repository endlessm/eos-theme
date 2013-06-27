#!/usr/bin/env python

import os
import errno
import re

class DesktopWriter:

    CONFIGS = {
        'apps': {
            'csv_path': 'applications.csv',
            'desktop_dir': 'applications',
            'prefix': 'eos-app-',
            'suffix': '.desktop',
            'desktop_type': 'Application',
            'locale_keys': ['Name', 'Comment', 'Exec', 'Icon', 'Categories'] },
        'links': {
            'csv_path': 'links.csv',
            'desktop_dir': 'links',
            'prefix': 'eos-link-',
            'suffix': '.desktop',
            'desktop_type': 'Application',
            'locale_keys': ['Name', 'Comment', 'URL', 'Icon'] },
        'folders': {
            'csv_path': 'folders.csv',
            'desktop_dir': 'folders',
            'prefix': 'eos-folder-',
            'suffix': '.directory',
            'desktop_type': 'Directory',
            'locale_keys': ['Name', 'Icon'] } }

    def __init__(self, asset_type):
        self._asset_type = asset_type
        self._config = self.CONFIGS[self._asset_type]
        self._csv_path = self._config['csv_path']
        self._desktop_dir = self._config['desktop_dir']
        self._prefix = self._config['prefix']
        self._suffix = self._config['suffix']
        self._desktop_type = self._config['desktop_type']
        self._locale_keys = self._config['locale_keys']
        self.make_sure_path_exists(self._desktop_dir)

    def make_sure_path_exists(self, path):
        try:
            os.makedirs(path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

    def locale_string(self, locale):
        if locale == 'default':
            return ''
        else:
            return '[' + locale + ']'

    def url_to_exec(self, url):
        exec_string = 'epiphany-browser %s' % url
        return exec_string

    def _write_key(self, desktop_file, fields, key):
        # Write a line for each localized version of the key
        for locale in self._locales:
            field = fields[self._indexes[key][locale]]
            # Other than the default, omit blank values
            if field or locale == 'default':
                line = '%s%s=%s\n' % (key, self.locale_string(locale), field)
                desktop_file.write(line)

    def _have_localized(self, fields, key):
        have_localized = False
        for locale in self._locales:
            index = self._indexes[key][locale]
            localized_field = fields[index]
            if localized_field and locale != 'default':
                have_localized = True
                break
        return have_localized

    def _write_exec(self, desktop_file, fields, field):
        have_localized = self._have_localized(fields, field)
        if have_localized:
            exec_string = 'eos-exec-localized'
            index = self._indexes[field]['default']
            if field == 'URL':
                url = fields[index]
                default_exec = self.url_to_exec(url)
            else:
                default_exec = fields[index]
            exec_string += " '" + default_exec + "'"
            for locale in self._locales:
                index = self._indexes[field][locale]
                localized_field = fields[index]
                if localized_field and locale != 'default':
                    if field == 'URL':
                        localized_exec = self.url_to_exec(localized_field)
                    else:
                        localized_exec = localized_field
                    exec_string += " " + locale + ":'" + localized_exec + "'"
        else:
            index = self._indexes[field]['default']
            if field == 'URL':
                url = fields[index]
                exec_string = self.url_to_exec(url)
            else:
                exec_string = fields[index]

        desktop_file.write('Exec=%s\n' % exec_string)

    def _write_desktop_file(self, fields):
        desktop_id = fields[0]
        desktop_path = os.path.join(self._desktop_dir,
                                    self._prefix + desktop_id + self._suffix)
        desktop_file = open(desktop_path, 'w')
        desktop_file.write('[Desktop Entry]\n')
        desktop_file.write('Version=1.0\n')
        self._write_key(desktop_file, fields, 'Name')

        if 'Comment' in self._locale_keys:
            self._write_key(desktop_file, fields, 'Comment')

        desktop_file.write('Type=%s\n' % self._desktop_type)

        if 'Exec' in self._locale_keys:
            self._write_exec(desktop_file, fields, 'Exec')

        if 'URL' in self._locale_keys:
            self._write_exec(desktop_file, fields, 'URL')

        self._write_key(desktop_file, fields, 'Icon')

        if 'Categories' in self._locale_keys:
            # Note: Categories is not localized
            desktop_file.write('Categories=%s\n' %
                               fields[self._indexes['Categories']['default']])

    def _add_index(self, key, locale, index):
        self._locales.add(locale)

        try:
            inner_dict = self._indexes[key]
        except:
            inner_dict = {}
        
        inner_dict[locale] = index
        self._indexes[key] = inner_dict

    def _parse_header(self, header):
        # Note: for now, the Desktop and AppStore columns are ignored
        # They will be used later to specify what is available by default
        # on the desktop and in the app store for each user personality

        # Set of all locales
        self._locales = set()

        # Dictionary that relates keys and locales to indexes
        self._indexes = {}

        # Find all the locales specified in the header
        index = 0

        # For each field in the header
        fields = header.split(',')
        for field in fields:
            for key in self._locale_keys:
                if field.startswith(key):
                    if field == key:
                        # Non-localized field
                        locale = 'default'
                    else:
                        # Localized field
                        regex = '^' + key + '\[(.+)\]$'
                        match_result = re.match(regex, field)
                        if match_result:
                            locale = match_result.group(1)
                        else:
                            print 'Invalid localized field header:', field
                            exit(1)
                    self._add_index(key, locale, index)
            index += 1

    def write_desktop_files(self):
        csv_file = open(self._csv_path, 'r')

        # Parse the first line header
        header = csv_file.readline().rstrip()
        self._parse_header(header)

        # For each remaining line after the header
        for line in csv_file:
            fields = line.rstrip().split(',')
            self._write_desktop_file(fields)

        csv_file.close()

if __name__ == '__main__':
    for asset_type in ['apps', 'links', 'folders']:
        desktop_writer = DesktopWriter(asset_type)
        desktop_writer.write_desktop_files()
