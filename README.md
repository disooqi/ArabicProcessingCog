# ArabicProcessingCog
A Python package that do stemming, tokenization, sentence breaking, segmentation, normalization, POS tagging for Arabic language.

The library is intended for Python 3

```python
from arabic_processing_cog.normalization import Arabic_normalization as an

import sentence_breaker as SB
import codecs
from normalization import Arabic_normalization as AN
from stemming import Light10stemmer as light10

with codecs.open('docs/68956', encoding='utf-8') as dd:
    with codecs.open('sentences', encoding='utf-8', mode='w') as outf:
        for line in dd:
            sentences = SB.break_into_sentences(line)            
            for sen in sentences:                   
                outf.write(AN.normalize_sentence(sen)+'\n')
        else:
            print 'Done :-)'
```
![TarqeemV5](https://user-images.githubusercontent.com/1148046/111881159-f6f1e300-89b7-11eb-8f4d-b5eeb8ba706b.gif)
