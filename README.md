# What is Transmission-Cleanup?

Transmission-Cleanup is a simple and short script written in Python that removes completed torrents from a running instance of *Transmission* (more info at http://www.transmissionbt.com/). 

###Why did I write this script?  

Well, I had two main reasons why I wrote this script:

1)	I have a Raspberry Pi Model B (http://www.raspberrypi.org/) working as an always-on Bit Torrent box and (for some unknown reason) the Transmission daemon has problems executing its “on-complete” script. I decided to write a script that would remove the completed torrents (via transmission-remote) and add it as a Cron task that runs hourly (the RPi is running Raspbian, BTW). 
2)	It’s been a while since I’ve written something in Python, so I felt like practicing a little bit. 

### What do you need to use this script?

In order to use the script you need:
1)	You need to be working on a *Linux* distro.
2)	*transmission-daemon* should be installed, configured and running.
