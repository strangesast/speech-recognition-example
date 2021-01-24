from subprocess import run, PIPE
from pathlib import Path
import json

from pprint import pprint

cwd = Path.cwd()
model = "models.pbmm"
scorer = "models.scorer"

root_dir = cwd / "audio"
for filepath in root_dir.glob('[!._]*.wav'):
    args = [
            "deepspeech",
            "--model",
            model,
            "--scorer",
            scorer,
            "--audio",
            "{}".format(filepath.resolve()),
            #"'{}'".format(filepath.relative_to(cwd)),
            "--json",
            ]
    p = run(args, stdout=PIPE, stderr=PIPE, cwd=cwd)
    result = json.loads(p.stdout)

    result = result['transcripts']
    result = next(iter(result))
    confidence, words = result['confidence'], result['words']
    text = ' '.join(o['word'] for o in words)

    print(f'{confidence=:.2f} {text=}')
