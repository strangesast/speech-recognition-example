from vosk import Model, KaldiRecognizer, SetLogLevel
from pathlib import Path
import time
import json
import wave
import sys

#SetLogLevel(0)
SetLogLevel(-1)


root_dir = Path.cwd() / 'audio'


def listen(wf):
   
    model = Model('model')
    rec = KaldiRecognizer(model, wf.getframerate())
    
    def g():
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                yield json.loads(rec.Result())
    
    f = lambda: json.loads(rec.FinalResult())

    return (g(), f)
 

for filepath in root_dir.glob('[!._]*.wav'):
    wf = wave.open(str(filepath), 'rb')
    nchannels, sampwidth, framerate, nframes, comptype, compname = wf.getparams()
    if nchannels != 1 or sampwidth != 2 or comptype != 'NONE':
        print(f'unsupported wav file ({filepath.name})')
        continue
    duration = nframes / float(framerate)
    t0 = time.time()
    it, f = listen(wf)
    for segment in it:
        print(f'segment {segment}')

    result = f()
    score = sum(s['conf'] for s in result['result']) / len(result['result'])
    text = result['text']
    execution = time.time() - t0

    r = duration / execution
    print(f'{filepath.name} {duration=:0.2f}s {score=:.3f} {execution=:.2f}s {r=:.3f} {text=}')
