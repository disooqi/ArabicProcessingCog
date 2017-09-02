# -*- coding:utf8 -*-
import codecs


'''
Table 2.1: Arabic encodings contrasted: letters
'''
class ArabicChar:
    representations = ('unicode','HSB', 'bw_base', 'bw_xml', 'bw_safe', 'parkinson')
#     def __init__(self, code_point, HSB, buckwalter_base, buckwalter_xml, buckwalter_safe, parkinson=None):
#         self.codepoint  = code_point
#
#         # self.utf8       = self.codepoint.encode('utf8')
#         # self.wins       = self.codepoint.encode('windows-1256')
#         # self.iso        = self.codepoint.encode('ISO-8859-6')
#
#         self.HSB        = HSB
#         self.bw_base    = buckwalter_base
#         self.bw_xml     = buckwalter_xml
#         self.bw_safe    = buckwalter_safe
#         self.parkinson = parkinson
#
#         self.dic = {'unicode':self.codepoint, 'HSB':self.HSB, 'bw_base':self.bw_base, 'bw_xml':self.bw_xml, 'bw_safe':self.bw_safe,
#                     'parkinson':self.parkinson}

class Letter:
    'Optional class documentation string'
    def __init__(self, code_point, HSB, buckwalter_base, buckwalter_xml, buckwalter_safe, parkinson=None):
        self.codepoint  = code_point

        # self.utf8       = self.codepoint.encode('utf8')
        # self.wins       = self.codepoint.encode('windows-1256')
        # self.iso        = self.codepoint.encode('ISO-8859-6')

        self.HSB        = HSB
        self.bw_base    = buckwalter_base
        self.bw_xml     = buckwalter_xml
        self.bw_safe    = buckwalter_safe
        self.parkinson = parkinson

        self.dic = {'unicode':self.codepoint, 'HSB':self.HSB, 'bw_base':self.bw_base, 'bw_xml':self.bw_xml, 'bw_safe':self.bw_safe,
                    'parkinson':self.parkinson}

    def change_representation(self, target_repr):
        pass

class Diacrtic:
    def __init__(self, code_point, HSB, buckwalter_base, buckwalter_xml, buckwalter_safe, parkinson=None):
        self.codepoint  = code_point

        self.HSB        = HSB
        self.bw_base    = buckwalter_base
        self.bw_xml     = buckwalter_xml
        self.bw_safe    = buckwalter_safe
        self.parkinson = parkinson

        self.dic = {'unicode':self.codepoint, 'HSB':self.HSB, 'bw_base':self.bw_base, 'bw_xml':self.bw_xml, 'bw_safe':self.bw_safe,
                    'parkinson':self.parkinson}




class ArabicScript:
    # look at cp1256.py in python 3 module to learn how mapping really done

    HAMZA            = Letter(u'\u0621', u'\u0027', u'\u0027', u'\u0027', u'C', u'C')
    ALEF_MADDA       = Letter(u'\u0622', u'\u0100', u'\u007c', u'\u007c', u'M', u'M')
    ALEF_HAMZA_ABOVE = Letter(u'\u0623', u'\u00C2', u'\u003e', u'O', u'O', u'L')
    WAW_HAMZA        = Letter(u'\u0624', u'\u0175', u'\u0026', u'W', u'W', u'W')
    ALEF_HAMZA_BELOW = Letter(u'\u0625', u'\u01cd', u'\u003c', u'I', u'I', u'E')
    YEH_HAMZA        = Letter(u'\u0626', u'\u0177', u'\u007d', u'\x7d', u'Q', u'Y')

    ALEF             = Letter(u'\u0627', u'\u0041', u'\u0041', u'\u0041', u'\u0041', u'\u0041')
    BEH              = Letter(u'\u0628', u'\u0062', u'\u0062', u'\u0062', u'\u0062', u'\u0062')

    TEH_MARBUTA      = Letter(u'\u0629', u'\u0127', u'p', u'p', u'p', u'Q')

    TEH              = Letter(u'\u062a', u'\u0074', u'\u0074', u'\u0074', u'\u0074', u'\u0074')
    THEH             = Letter(u'\u062b', u'\u03b8', u'v', u'v', u'v', u'V')
    JEEM             = Letter(u'\u062c', u'\u006A', u'\u006A', u'\u006A', u'\u006A', u'\u006A')
    HAH              = Letter(u'\u062d', u'\u0048', u'\u0048', u'\u0048', u'\u0048', u'\u0048')
    KHAH             = Letter(u'\u062e', u'\u0078', u'\u0078', u'\u0078', u'\u0078', u'\u0078')
    DAL              = Letter(u'\u062f', u'\u0064', u'\u0064', u'\u0064', u'\u0064', u'\u0064')
    THAL             = Letter(u'\u0630', u'\u00F0', u'\u002a', u'\u002a', u'V', u'v')
    REH              = Letter(u'\u0631', u'\u0072', u'\u0072', u'\u0072', u'\u0072', u'\u0072')
    ZAIN             = Letter(u'\u0632', u'\u007A', u'\u007A', u'\u007A', u'\u007A', u'\u007A')
    SEEN             = Letter(u'\u0633', u'\u0073', u'\u0073', u'\u0073', u'\u0073', u'\u0073')
    SHEEN            = Letter(u'\u0634', u'\u0161', u'\u0024', u'\u0024', u'c', u'p')
    SAD              = Letter(u'\u0635', u'\u0053', u'\u0053', u'\u0053', u'\u0053', u'\u0053')
    DAD              = Letter(u'\u0636', u'\u0044', u'\u0044', u'\u0044', u'\u0044', u'\u0044')
    TAH              = Letter(u'\u0637', u'\u0054', u'\u0054', u'\u0054', u'\u0054', u'\u0054')
    ZAH              = Letter(u'\u0638', u'\u010E', u'Z', u'Z', u'Z', u'Z')
    AIN              = Letter(u'\u0639', u'\u03C2', u'E', u'E', u'E', u'c')
    GHAIN            = Letter(u'\u063a', u'\u03B3', u'g', u'g', u'g', u'g')
    FEH              = Letter(u'\u0641', u'\u0066', u'\u0066', u'\u0066', u'\u0066', u'\u0066')
    QAF              = Letter(u'\u0642', u'\u0071', u'\u0071', u'\u0071', u'\u0071', u'\u0071')
    KAF              = Letter(u'\u0643', u'\u006B', u'\u006B', u'\u006B', u'\u006B', u'\u006B')
    LAM              = Letter(u'\u0644', u'\u006C', u'\u006C', u'\u006C', u'\u006C', u'\u006C')
    MEEM             = Letter(u'\u0645', u'\u006D', u'\u006D', u'\u006D', u'\u006D', u'\u006D')
    NOON             = Letter(u'\u0646', u'\u006E', u'\u006E', u'\u006E', u'\u006E', u'\u006E')
    HEH              = Letter(u'\u0647', u'\u0068', u'\u0068', u'\u0068', u'\u0068', u'\u0068')
    WAW              = Letter(u'\u0648', u'\u0077', u'\u0077', u'\u0077', u'\u0077', u'\u0077')
    ALEF_MAKSURA     = Letter(u'\u0649', u'\u00FD', u'Y', u'Y', u'Y', u'e')
    YEH              = Letter(u'\u064a', u'\u0079', u'\u0079', u'\u0079', u'\u0079', u'\u0079')

    #Ligatures
    LAM_ALEF                    =Letter(u'\ufefb', u'', u'', u'', u'', u'')
    LAM_ALEF_HAMZA_ABOVE        =Letter(u'\ufef7', u'', u'', u'', u'', u'')
    LAM_ALEF_HAMZA_BELOW        =Letter(u'\ufef9', u'', u'', u'', u'', u'')
    LAM_ALEF_MADDA_ABOVE        =Letter(u'\ufef5', u'', u'', u'', u'', u'')

    basic_letters = {ALEF,BEH,TEH,THEH,JEEM, HAH,KHAH,DAL,THAL,REH,ZAIN,SEEN,SHEEN,SAD,DAD,TAH,ZAH,AIN,GHAIN,
                     FEH,QAF,KAF,LAM,MEEM,NOON,HEH,WAW,YEH}

    basic_letters_and_hamza = {HAMZA,ALEF,BEH,TEH,THEH,JEEM,HAH,KHAH,DAL,THAL,REH,ZAIN,SEEN,SHEEN,SAD,DAD,TAH,
                              ZAH,AIN,GHAIN,FEH,QAF,KAF,LAM,MEEM,NOON,HEH,WAW,YEH}

    common_letters = {HAMZA,ALEF_MADDA,ALEF_HAMZA_ABOVE,WAW_HAMZA,ALEF_HAMZA_BELOW,YEH_HAMZA,ALEF,BEH,TEH_MARBUTA,TEH,THEH,JEEM,
               HAH,KHAH,DAL,THAL,REH,ZAIN,SEEN,SHEEN,SAD,DAD,TAH,ZAH,AIN,GHAIN,FEH,QAF,KAF,LAM,MEEM,NOON,HEH,WAW,
               ALEF_MAKSURA,YEH}

    full_letters = {HAMZA,ALEF_MADDA,ALEF_HAMZA_ABOVE,WAW_HAMZA,ALEF_HAMZA_BELOW,YEH_HAMZA,ALEF,BEH,TEH_MARBUTA,TEH,THEH,JEEM,
               HAH,KHAH,DAL,THAL,REH,ZAIN,SEEN,SHEEN,SAD,DAD,TAH,ZAH,AIN,GHAIN,FEH,QAF,KAF,LAM,MEEM,NOON,HEH,WAW,
               ALEF_MAKSURA,YEH, LAM_ALEF, LAM_ALEF_HAMZA_ABOVE, LAM_ALEF_HAMZA_BELOW, LAM_ALEF_MADDA_ABOVE}

    lam_alif_ligatures = {LAM_ALEF, LAM_ALEF_HAMZA_ABOVE, LAM_ALEF_HAMZA_BELOW, LAM_ALEF_MADDA_ABOVE}

    # FATHATAN = Diacrtic(u'\u064b', u'')
    # DAMMATAN = Diacrtic(u'\u064c')
    # KASRATAN = Diacrtic(u'\u064d')
    # FATHA = Diacrtic(u'\u064e')
    # DAMMA = Diacrtic(u'\u064f')
    # KASRA = Diacrtic(u'\u0650')
    # SHADDA = Diacrtic(u'\u0651')
    # SUKUN = Diacrtic(u'\u0652')
    # DAGGER_ALEF = Diacrtic(u'\u0670')
    # ALEF_WASLA = Diacrtic(u'\u0671')

    def __init__(self):
        pass

    @classmethod
    def convert_to(cls, text, source_repr, target_repr):
        pass
        # check if 'text' is Arabic first
        # if source_repr or target_repr not in cls.representations:
        #     # should throw exception
        #     return

class ArabicText:
    def __init__(self, text, representation):
        'this method takes only unicode '
        if representation not in ArabicChar.representations:
            # should throw exception
            return
        else:
            self.repr = representation

        self.text = text

        letters = [letter.dic[self.repr] for letter in ArabicScript.common_letters]
        letters.append(u' ')

        arabic_chars = list()
        arabic_chars.extend(letters)

        for ch in text:
            if ch not in arabic_chars:
                self.is_arabic = False
                self.repr = None
                break
        else:
            self.is_arabic = True

    @classmethod
    def detect_presentation(cls, text):
        '''
        The function returns empty list if does not fined a representation
        '''
        possible_repr = list()
        for rep in ArabicChar.representations:
            letters = [letter.dic[rep] for letter in ArabicScript.common_letters]
            letters.append(u' ')

            for ch in text:
                if ch not in letters:
                    break
            else:
                possible_repr.append(rep)
        else:
            return possible_repr


    def convert_to(self, representation, mode='strict', source_repr=None):
        '''
        modes: strict, char, word
        source_repr: Although it makes sense that the source representation should be known in advance however some
        times we need to loose this condtion and force the source token to be in specific repr and this work only in
        the 'char' mode
        strict mode means if the character not there don't accept the word for conversion and give an error

        '''
        if representation not in ArabicChar.representations:
            # should throw exception
            return
        if mode=='word' and not self.is_arabic:
            # throw exception 'cannot change representation of non-arabic text'
            return self.text

        if self.repr == representation:
            return self.text
        elif self.repr:
            letters_map = {letter.dic[self.repr]:letter.dic[representation] for letter in ArabicScript.common_letters}
            new_repr = list()
            for ch in self.text:
                if mode=='strict':
                    new_repr.append(letters_map[ch])
                elif mode=='char':
                    new_repr.append(letters_map.get(ch, ch))
                elif mode=='word':
                    new_repr.append(letters_map.get(ch, ch))
            else:
                return ''.join(new_repr)
        elif mode=='char' and source_repr:
            letters_map = {letter.dic[source_repr]:letter.dic[representation] for letter in ArabicScript.common_letters}
            new_repr = list()
            for ch in self.text:
                new_repr.append(letters_map.get(ch, ch))
            else:
                return ''.join(new_repr)
        elif mode=='char' and not source_repr:
                pass  # should pass an error
        else:
            pass # no char mode no self,repr ... what do u want????

    def transliterate_parkinson(self):
        self.text = self.convert_to('parkinson')
        self.repr = 'parkinson'

    def transliterate_HSB(self):
        # https://api.metacpan.org/source/SMRZ/Encode-Arabic-14.2
        # https://metacpan.org/release/Encode-Arabic
        # https://github.com/otakar-smrz/encode-arabic
        # http://quest.ms.mff.cuni.cz/cgi-bin/encode/index.fcgi
        self.text = self.convert_to('HSB')
        self.repr = 'HSB'

    def transliterate_buckwalter(self, mode='base'):
        if mode == 'base':
            self.text = self.convert_to('bw_base')
            self.repr = 'bw_base'
        elif mode == 'xml':
            self.text = self.convert_to('bw_xml')
            self.repr = 'bw_xml'
        elif mode == 'safe':
            self.text = self.convert_to('bw_safe')
            self.repr = 'bw_safe'
        else:
            return 'Throw Exception: Argument Error'

    def untransliterate(self):
        if self.is_arabic and self.repr=='unicode':
            pass

        if not self.is_arabic:
            pass

        self.text = self.convert_to('unicode')
        self.repr = 'unicode'

    def to_string(self):
        return self.text

    def __unicode__(self):
        return self.text

    def __str__(self):
        return self.text.encode('utf8')
        #return self.convert_to('unicode')

#print len(ArabicScript.common_letters)
abdelali_test_path = r'/home/disooqi/qcri/egy_seg/abdelali/test_bkw.txt'
abdelali_train_path = r'/home/disooqi/qcri/egy_seg/abdelali/train_bkw.txt'

train = list()
test = list()

with codecs.open(abdelali_test_path, encoding='utf-8') as fobj:
    for line in fobj:
        token = line.strip()
        #print ArabicText.detect_presentation(token.replace('+', '')), token
        txt = ArabicText(token, 'bw_safe')
        utf8 = txt.convert_to('unicode', mode='char', source_repr='bw_safe')
        train.append(utf8)

with codecs.open(r'/home/disooqi/qcri/egy_seg/abdelali/test_utf8.txt', encoding='utf-8', mode='w') as fobj:
    for token in train:
        fobj.write(token)
        fobj.write('\n')


# HSB =      u'\u005F\u00C2\u0175\u01CD\u002C\u003B\u003F\u0027\u0100\u0177\u0041\u0062\u0127\u0074\u03B8\u006A\u0048\u0078\u0064\u00F0\u0072\u007A\u0073\u0161\u0053\u0044\u0054\u010E\u03C2\u03B3\u0066\u0071\u006B\u006C\u006D\u006E\u0068\u0077\u00FD\u0079\u0070\u0063\u017E\u0076\u0067'
# HSB_cor =  u'\u0640\u0623\u0624\u0625\u060C\u061B\u061F\u0621\u0622\u0626\u0627\u0628\u0629\u062a\u062b\u062c\u062d\u062e\u062f\u0630\u0631\u0632\u0633\u0634\u0635\u0636\u0637\u0638\u0639\u063a\u0641\u0642\u0643\u0644\u0645\u0646\u0647\u0648\u0649\u064a\u067E\u0686\u0698\u06A4\u06AF'
# p = '_LWE,;?CMYAbQtVjHxdvrzspSDTZcgfqklmnhwey'

# HAMZA            = u'\u0621'
# ALEF_MADDA       = u'\u0622'
# ALEF_HAMZA_ABOVE = u'\u0623'
# WAW_HAMZA        = u'\u0624'
# ALEF_HAMZA_BELOW = u'\u0625'
# YEH_HAMZA        = u'\u0626'
# ALEF             = u'\u0627'
# BEH              = u'\u0628'
# TEH_MARBUTA      = u'\u0629'
# TEH              = u'\u062a'
# THEH             = u'\u062b'
# JEEM             = u'\u062c'
# HAH              = u'\u062d'
# KHAH             = u'\u062e'
# DAL              = u'\u062f'
# THAL             = u'\u0630'
# REH              = u'\u0631'
# ZAIN             = u'\u0632'
# SEEN             = u'\u0633'
# SHEEN            = u'\u0634'
# SAD              = u'\u0635'
# DAD              = u'\u0636'
# TAH              = u'\u0637'
# ZAH              = u'\u0638'
# AIN              = u'\u0639'
# GHAIN            = u'\u063a'
# FEH              = u'\u0641'
# QAF              = u'\u0642'
# KAF              = u'\u0643'
# LAM              = u'\u0644'
# MEEM             = u'\u0645'
# NOON             = u'\u0646'
# HEH              = u'\u0647'
# WAW              = u'\u0648'
# ALEF_MAKSURA     = u'\u0649'
# YEH              = u'\u064a'