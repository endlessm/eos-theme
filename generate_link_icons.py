#!/usr/bin/python

# This script requires installing ImageMagick
# (sudo apt-get install imagemagick)
# for the 'convert' command

# To use this script, first log into eoscms.parafernalia.net.br
# Under "App Store", click on "Generate Package"
# There should be no warnings
# Click on "Click here to download files in zip format"
# Save the downloaded file in this folder as appstore.zip
# Run this script
# Add and commit any changes to git
# Proceed with the normal build process

import os
import shutil
import sys
import zipfile
import json

ZIP_FILENAME = 'appstore.zip'
UNZIP_DIR = 'unzipped'
IGNORE_ERRORS = True
JPEG_QUALITY = 90

# Run the ImageMagick 'convert' application from the command line,
# with specified JPEG quality and all metadata stripped
def convert(source, target, command):
    os.system('convert ' + source + ' ' + command +
              ' -quality ' + str(JPEG_QUALITY) + ' -strip ' + target)

# Return the path to the default designer icon, or None if it doesn't exist
def get_icon_path(linkJSON):
    # If the link object's icon path is just 'icons', there isn't a default designer icon
    if linkJSON['linkIcon'] == 'icons/':
        return None
    return linkJSON['linkIcon']

# Remove the existing unzipped, if they exist
shutil.rmtree(UNZIP_DIR, IGNORE_ERRORS)

# Unzip the file
zfile = zipfile.ZipFile(ZIP_FILENAME)
zfile.extractall(UNZIP_DIR)

# Link icons will be copied/cropped from the zipped dir's links dir
source_dir = os.path.join(UNZIP_DIR, 'links')
target_dir = os.path.join('icons', '64x64', 'apps')

# At the moment, we're only using the spanish content file
links_json = os.path.join(source_dir, 'es-gt.json')

with open(links_json) as links_content:
    link_data = json.load(links_content)
    for category in link_data:
        for link in category['links']:
            icon_path = get_icon_path(link)
            target_file = os.path.join(target_dir, link['linkId'] + '.png')

            if icon_path is None:
                # Generate a new icon based on existing link image
                source_file = os.path.join(source_dir, 'images', link['linkId'] + '.jpg')

                # Path to the mask png which will set the margin/corners of the generated icon.
                # Currently requires that 'generic-link.png' stays put indefinitely
                mask_file = os.path.join(target_dir, 'generic-link.png')

                convert(source_file, target_file,
                        '-resize 64x64^ -gravity center -crop 64x64+0+0 -alpha set \
                        ' + mask_file + ' -compose DstIn -composite')
            else:
                # Simply copy existing icon asset to destination
                source_file = os.path.join(source_dir, icon_path)
                shutil.copy(source_file, target_file)
