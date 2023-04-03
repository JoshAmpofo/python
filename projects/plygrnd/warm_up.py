#!/usr/bin/env python3
"""Parsing iTunes playlist"""


def findDuplicates(filename):
    """find duplicate tracks"""
    print(f"Finding duplicate tracks in {filename}...")
    # read playlist
    plist = plistlib.readPlist(filename)
    # get tracks from the Tracks dictionary
    tracks = plist['Tracks']
    # create dict for track names
    trackNames = {}
    # iterate through the tracks
    for trackId, track n tracks.items():
        try:
            name = track['Name']
            duration = track['Total Time']
            # look for existing entries
            if name in trackNames:
                # if a name and duratio match, increment count
                # round track length to the nearest second
                if duration // 1000 == trackNames[name][0] // 1000:
                    count = trackNames[name][1]
                    trackNames[name] = (duration, count + 1)
                else:
                    # add dictionary entry as tuple (duration , count)
                    trackNames[name] = (duration, 1)
        except IgnoreError:  # ignore
            pass
