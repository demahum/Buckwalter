# -*- coding: utf-8 -*-

import re
import codecs

t1 = {ord(u'ا'):u'A',
      ord(u'ب'):u'b',
      ord(u'ت'):u't',
      ord(u'ث'):u'v',
      ord(u'ج'):u'j',
      ord(u'ح'):u'H',
      ord(u'خ'):u'x',
      ord(u'د'):u'd',
      ord(u'ذ'):u'*',
      ord(u'ر'):u'r',
      ord(u'ز'):u'z',
      ord(u'س'):u's',
      ord(u'ش'):u'$',
      ord(u'ص'):u'S',
      ord(u'ض'):u'D',
      ord(u'ط'):u'T',
      ord(u'ظ'):u'Z',
      ord(u'ع'):u'E',
      ord(u'غ'):u'g',
      ord(u'ف'):u'f',
      ord(u'ق'):u'q',
      ord(u'ك'):u'k',
      ord(u'ل'):u'l',
      ord(u'م'):u'm',
      ord(u'ن'):u'n',
      ord(u'ه'):u'h',
      ord(u'و'):u'w',
	    ord(u'ي'):u'y'}
	  
def subst(word):    
        return word.translate(t1)

f = codecs.open('arabic', encoding='utf-8') # "arabic" is the name of input file you want to read from (file with arabic text)
q = f.read()
o = re.sub(ur'(\S+)', lambda m: subst(m.group(1)), q)
f.close()

b = codecs.open('new', 'w', encoding = 'utf-8') # "new" is the name of output file you'll get after running this script (file with transliterated text)
b.write(o)
b.close()
