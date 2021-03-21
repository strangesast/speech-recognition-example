#!/bin/bash

if [ ! -f youtube-dl ]; then
  curl -L https://yt-dl.org/downloads/latest/youtube-dl -o ./youtube-dl
  chmod +x ./youtube-dl
fi
URL=https://www.youtube.com/watch?v=hK8kk_3WA7w
./youtube-dl $URL -o 'video'
ffmpeg -y -i video.mkv -ss 00:01:00 -t 00:01:00 -acodec pcm_s16le -ac 1 audio.wav 
