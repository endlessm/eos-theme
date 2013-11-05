#!/usr/bin/env python

import os
import errno
import re
import collections
import json

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

class DesktopWriter:

    CONFIGS = {
        'apps': {
            'csv_path': 'applications.csv',
            'desktop_dir': 'applications',
            'prefix': 'eos-app-',
            'suffix': '.desktop',
            'desktop_type': 'Application',
            'locale_keys': ['Name', 'Comment', 'TryExec', 'Exec', 'Icon', 'SplashScreen', 'Categories'],
            'in_app_store': True },
        'links': {
            'csv_path': 'links.csv',
            'desktop_dir': 'links',
            'prefix': 'eos-link-',
            'suffix': '.desktop',
            'desktop_type': 'Application',
            'locale_keys': ['Name', 'Comment', 'URL', 'Icon', 'Categories'],
            'in_app_store': True },
        'folders': {
            'csv_path': 'folders.csv',
            'desktop_dir': 'folders',
            'prefix': 'eos-folder-',
            'suffix': '.directory',
            'desktop_type': 'Directory',
            'locale_keys': ['Name', 'Icon'],
            'in_app_store': False },
        'extras': {
            'csv_path': 'extras.csv',
            'desktop_dir': None,
            'prefix': '',
            'suffix': '.desktop',
            'desktop_type': 'Application',
            'locale_keys': [],
            'in_app_store': False } }

    def __init__(self, asset_type):
        self._asset_type = asset_type
        self._config = self.CONFIGS[self._asset_type]
        self._csv_path = self._config['csv_path']
        self._desktop_dir = self._config['desktop_dir']
        self._prefix = self._config['prefix']
        self._suffix = self._config['suffix']
        self._desktop_type = self._config['desktop_type']
        self._locale_keys = self._config['locale_keys']
        self._in_app_store = self._config['in_app_store']

        if self._desktop_dir:
            make_sure_path_exists(self._desktop_dir)

    def locale_string(self, locale):
        if locale == 'default':
            return ''
        else:
            return '[' + locale + ']'

    def url_to_exec(self, url):
        exec_string = 'chromium-browser %s' % url
        return exec_string

    def _write_key(self, desktop_file, fields, key):
        # Write a line for each localized version of the key
        for locale in self._locales:
            field = fields[self._indexes[key][locale]]
            # Other than the default, omit blank values
            if field or locale == 'default':
                if key == 'Icon' and self._asset_type == 'folders':
                    field = field + '-symbolic'
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

        if 'TryExec' in self._locale_keys:
            field = fields[self._indexes['TryExec']['default']]
            if field:
                desktop_file.write("%s=%s\n" % ('TryExec', field))

        if 'URL' in self._locale_keys:
            self._write_exec(desktop_file, fields, 'URL')

        self._write_key(desktop_file, fields, 'Icon')

        if 'Categories' in self._locale_keys:
            # Note: Categories is not localized
            desktop_file.write('Categories=%s\n' %
                               fields[self._indexes['Categories']['default']])

        disable_splash = False
        splash_file = ''
        if self._asset_type == 'links':
            # Since we currently open web links as a new tab in the browser,
            # it is not appropriate to show the launch splash screen
            disable_splash = True
        elif 'SplashScreen' in self._locale_keys:
            # Note: SplashScreen is not localized
            field = fields[self._indexes['SplashScreen']['default']]
            if field == 'none':
                disable_splash = True
            else :
                splash_file = field
        if disable_splash:
            desktop_file.write('X-Endless-Splash-Screen=false\n')
        else :
            desktop_file.write('X-Endless-Splash-Screen=true\n')
            desktop_file.write('X-Endless-launch-background=' + splash_file + '\n')

        if self._in_app_store:
            show_in_app_store = True
            if 'AppStore' in self._indexes:
                field = fields[self._indexes['AppStore']['default']]
                if not field:
                    show_in_app_store = False

            desktop_file.write('X-Endless-ShowInAppStore=%s\n' % str(show_in_app_store).lower())

        desktop_file.close()

    def _add_index(self, key, qualifier, index):
        try:
            inner_dict = self._indexes[key]
        except:
            inner_dict = {}
        
        inner_dict[qualifier] = index
        self._indexes[key] = inner_dict

    def _add_locale_index(self, key, locale, index):
        self._locales.add(locale)
        self._add_index(key, locale, index)

    def _add_personality_index(self, key, personality, index):
        self._personalities.add(personality)
        self._add_index(key, personality, index)

    def _parse_header(self, header):
        # Set of all personalities
        self._personalities = set()

        # Set of all locales
        self._locales = set()

        # Dictionary that relates keys and locales to indexes
        self._indexes = {}

        # Find all the personalities and locales specified in the header
        index = 0

        # For each field in the header
        fields = header.split(',')
        for field in fields:

            # Check if this is a personalized field
            for key in ['Desktop', 'AppStore']:
                if field.startswith(key):
                    if field == key:
                        # Non-personalized field
                        personality = 'default'
                    else:
                        # Personalized field
                        regex = '^' + key + '\[(.+)\]$'
                        match_result = re.match(regex, field)
                        if match_result:
                            personality = match_result.group(1)
                        else:
                            print 'Invalid personalized field header:', field
                            exit(1)
                    self._add_personality_index(key, personality, index)

            # Check if this is a localized field
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
                    self._add_locale_index(key, locale, index)

            index += 1

    def _add_to_layout(self, fields, desktop_layout):
        # Note: for now, we don't do anything with the AppStore column
        
        for personality in self._personalities:
            index = self._indexes['Desktop'][personality]
            position = fields[index]
            if position:
                id = fields[0]
                item = self._prefix + id + self._suffix 
                desktop_layout.add_item(personality, item, position)

    def process_all(self, desktop_layout):
        # CSV files must live in the same directory
        # as the python script file
        csv_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(csv_dir, self._csv_path)
        csv_file = open(csv_path, 'r')

        # Parse the first line header
        header = csv_file.readline().rstrip()
        self._parse_header(header)

        # For each remaining line after the header
        for line in csv_file:
            fields = line.rstrip().split(',')
            self._add_to_layout(fields, desktop_layout)
            if (self._desktop_dir):
                self._write_desktop_file(fields)

        csv_file.close()

class DesktopLayout:

    def __init__(self):
        self._layouts  = {}

    def add_item(self, personality, item, position):
        if personality not in self._layouts:
            self._layouts[personality] = { 'desktop': {}, 'folders': {} }
        layout = self._layouts[personality]
        desktop = layout['desktop']
        folders = layout['folders']

        if ':' in position:
            # Add to a folder
            [name, index] = position.split(':')
            folder = 'eos-folder-' + name + '.directory'
            if folder not in folders:
                folders[folder] = {}
            if index in folders[folder]:
                print 'Duplicate entry adding ' + item + ' to ' + position + \
                    '; conflicts with ' + folders[folder][index]
                exit(1)
            folders[folder][index] = item
        else:
            # Add to desktop
            if position in desktop:
                print 'Duplicate entry adding ' + item + ' to ' + position + \
                    '; conflicts with ' + desktop[position]
                exit(1)
            desktop[position] = item

    def write_settings(self):
        settings_dir = 'settings'
        prefix = 'icon-grid-'
        suffix = '.json'
        make_sure_path_exists(settings_dir)
        for [personality, layout] in self._layouts.items():
            settings_path = os.path.join(settings_dir,
                                         prefix + personality + suffix)
            settings_dict = collections.OrderedDict()

            desktop = layout['desktop']
            sorted_desktop = sorted(desktop, key = lambda val: int(val))
            settings_dict['desktop'] = []
            for item in sorted_desktop:
                settings_dict['desktop'].append(desktop[item])

            # Process the folders in the order that they appear on the desktop
            folders = layout['folders']
            for item in sorted_desktop:
                folder = desktop[item]
                if folder in folders:
                    settings_dict[folder] = []
                    entries = folders[folder]
                    sorted_entries = sorted(entries, key = lambda val: int(val))
                    first_entry = True
                    for entry in sorted_entries:
                        settings_dict[folder].append(entries[entry])
                
            settings_file = open(settings_path, 'w')
            json.dump(settings_dict, settings_file)
            settings_file.close()

if __name__ == '__main__':
    desktop_layout = DesktopLayout()
    for asset_type in ['apps', 'links', 'folders', 'extras']:
        desktop_writer = DesktopWriter(asset_type)
        desktop_writer.process_all(desktop_layout)

    desktop_layout.write_settings()

