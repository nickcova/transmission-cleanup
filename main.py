#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
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

import subprocess

def main():
	
    result = subprocess.check_output(["transmission-remote","--auth=transmission:transmission", "-l"])    
    splitResult = result.split("\n")
    
    # Remove items which are just empty strings
    while True:
        try:
            splitResult.remove("")
        except ValueError:
            break
	
    # Remove first and last items so the list only contains torrent info.
    # If the length of the list is smaller than 2, just exit.
    if len(splitResult) > 2:
        splitResult.pop(0)
        splitResult.pop()
        print(splitResult)
    else:
        return 0
    
    
    return 0

if __name__ == '__main__':
	main()

