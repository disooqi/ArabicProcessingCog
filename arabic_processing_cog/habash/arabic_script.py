
# Arabic, Persian, Kurdish, Urdu and Pashtokurd


#Nizar Habash, Abdelhadi Soudi, and Tim Buckwalter. On Arabic Transliteration. In
#A. van den Bosch and A. Soudi, editors, Arabic Computational Morphology: Knowledge-based
#and Empirical Methods. Springer, 2007. 4, 21, 27, 31
habash_soudi_buckwalter_transliteration_scheme = dict()

def orthographic_transliteration():
    pass

def orthographic_normalization():
    pass

def handwriting_recognition():
    pass

def automatic_diacritization():
    pass

cursive_style = u'محمد إبراهيم'


letter_form = '' # dfd رسم dfd
letter_mark = '' # ddd إعجام ddd
consonantal_diacritics = letter_mark  # three types: dots/points, short kaf, and Hamza (This includes Madda)

LETTER_FORM_COUNT = 19


diacrtic = None # this term has another meaning among OCR researchers as the "consonantal diacritic"

grapheme = u'حرف الهاء' # also called character  (font and encoding design terminology)
allographs =['ه', 'هـ', 'ـه', 'ـهـ'] # also called glyphs
# a grapheme has multiple allographs
# the context-based selection of letter shape is called "graphotactics"