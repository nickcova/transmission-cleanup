#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Transmission Cleanup
#  (main.py)
#  
#  Copyright 2014 Nicolas Cova <nicolas.cova.work@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import time
import subprocess

def main():

    try:
        commandResult = subprocess.check_output(["transmission-remote","--auth", "transmission:transmission", "-l"])
    except CalledProcessError:
        dateAndTime = time.strftime("%H:%M:%S") + " " + time.strftime("%d/%m/%Y")
        print(dateAndTime + " ERROR: something went wrong checking the torrents listing.") 
        return -1
        
    splitResult = commandResult.split("\n")

    # Remove items which are just empty strings
    while True:
        try:
            splitResult.remove("")
        except ValueError:
            # Insert error message here
            break

    # Remove first and last items so the list only contains torrent info.
    # If the length of the list is smaller than 2, just exit.
    if len(splitResult) > 2:
        splitResult.pop(0)
        splitResult.pop()
    else:
        return 0

    # For the remaining items, check if any of them contains '100%' and
    # add them to a completed torrents list.
    completedTorrents = []
    for item in splitResult:
        if "100%" in item:
            torrentId = item.lstrip().split()[0].rstrip("*")
            torrentName = item[item.rfind("      "):len(item)].lstrip()
            completedTorrents.append((torrentId,torrentName))

    # For each torrentId in the completed Torrents list, remove the
    # trailing spaces and execute the shell command to remove the torrent
    emailMessage = "The following torrents were removed: \n"
    torrentsRemoved = False
    
    try:
        for item in completedTorrents:
            commandResult = subprocess.check_output(["transmission-remote","--auth", "transmission:transmission", "-t", item[0], "--remove"])
            emailMessage += commandResult.rstrip() + ", Id = "  + item[0] + ", Torrent Name = " + item[1] + "\n"    
            if "success" in commandResult:
                torrentsRemoved = True

        if torrentsRemoved == True:
            ps = subprocess.Popen(('echo', emailMessage), stdout=subprocess.PIPE)
            output = subprocess.check_output(('mail', '-s', 'Torrents Removed', "email@email.com"), stdin=ps.stdout)
            ps.wait()
    except CalledProcessError:
        dateAndTime = time.strftime("%H:%M:%S") + " " + time.strftime("%d/%m/%Y")
        print(dateAndTime + " ERROR: something went wrong with 'check_output'. " + commandResult)
        return -1
    except OSError:
        dateAndTime = time.strftime("%H:%M:%S") + " " + time.strftime("%d/%m/%Y")
        print(dateAndTime + " ERROR: something went wrong with 'mail'. " + output)
        return -1
        
    return 0

if __name__ == '__main__':
    main()

