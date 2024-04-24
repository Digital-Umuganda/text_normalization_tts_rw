## Kinyarwanda text normalization
This is a kinyarwanda text normalization package, it is an open source project designed to create a normilization package capable of converting numbers, time, symbols and abbreviations into words and vice versa, it can be used in various NLP tools for example in Text To Speech (TTS) applications where it can normalize a text it is send to the TTS model. We have released the code including the package and the code necessary to recreate the far files who are in charge of normalization. 
## Script usage example

```
python text_normalization.py -t "byatangiye 12:02 haje abantu 2000"
```
## To install and use the python package

```
pip install kinya_tn
```
To import it in python run the following:
```
from kinya_tn import text_normalization

text_normalization.normalize("abantu 2000 baje kure ikiganiro cya covid cyatangiye 12:40")
```
## Who can contribute
- This is a community project and we encourage everyone to contribute, if you want to contribute send a PR request and it shall be review ASAP
## Limitations
- The installation works for linux distro, it is not supported on windows (we are yet to test it on mac)
- Currently the numbers supported are up to 10,000
- When there is an error, it returns the original text
- We do not cover symbols such as dollars
- Time format supported is up to 12 hours
- The numbers do not follow the class markers of the previous word
