#!/bin/bash
curl -o model.zip -LO https://alphacephei.com/vosk/models/vosk-model-en-us-aspire-0.2.zip
mkdir model && cd model && unzip ../model.zip -d . && cd ..
