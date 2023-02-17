#!/usr/bin/env python3

import requests
import subprocess

#variables - find/replace the variable below with the streamer you want to check
Streamer = 'strimmer_name'

#gets channel information
StreamerLiveCheck = requests.get('https://www.twitch.tv/' +Streamer).content.decode('utf-8')

#live check/downloader - replace your folder path
if 'isLiveBroadcast' in StreamerLiveCheck:
    subprocess.Popen('streamlink -o /folder_path_here/ https://www.twitch.tv/strimmer_name 720p60', shell=True)
else:
    exit()
