#!/usr/bin/env python3

import requests
import subprocess

#variables
Streamer = 'moonmoon' #replace with channel name you want to check
Quality = '720p60' #reference https://streamlink.github.io/cli.html#cmdoption-arg-STREAM for quality options
Location = '/home/ubuntu/testing/{author}/{id}.ts' #reference https://streamlink.github.io/cli.html#cmdoption-o for location options
StartRecording = f"streamlink -o {Location} https://twitch.tv/{Streamer} {Quality}"

#gets channel information
StreamerLiveCheck = requests.get('https://www.twitch.tv/' +Streamer).content.decode('utf-8')

#live check/downloader
if 'isLiveBroadcast' in StreamerLiveCheck:
    subprocess.run(StartRecording, shell=True)
else:
    exit()
