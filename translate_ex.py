from translate import Translator
import translators as ts

trs = Translator(to_lang='en', from_lang='vi')

# tr1 = ts.translate_text('Mặt hàng bị lỗi',translator='Google')

trans = trs.translate('Mặt hàng bị lỗi')

print(trans)

