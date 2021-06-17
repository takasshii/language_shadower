from django.test import TestCase
'''
def TextToSpeech_pyttsx_Chinese_woman(ph):
    
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[25].id)
    engine.save_to_file(ph, 'nlp/static/nlp/result/result.mp3')
    engine.runAndWait()
# Create your tests here.

from googletrans import Translator
import pyttsx3


def TextToSpeech_pyttsx_Chinese_woman(ph):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[25].id)
    result = open('nlp/static/nlp/result/result.mp3', 'wb')
    engine.save_to_file(ph, 'nlp/static/nlp/result/result.mp3', name='result.mp3')
    result.write()
    result.close()

    engine.runAndWait()

translator = Translator()

Chinese='こんにちは'
trans_zh = translator.translate(Chinese, src='ja', dest='zh-cn')
print(trans_zh)

TextToSpeech_pyttsx_Chinese_woman(trans_zh.text)
'''
'''
import markovify

# Get raw text as string.
with open('nlp/text.txt','r') as f:
   text = f.read()
# Build the model.
text_model = markovify.Text(text)
for i in range(10):
   print(text_model.make_sentence())
'''
'''
def TextToSpeech_English_man(ph):
    
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[0].id)
    engine.save_to_file(ph, 'nlp/static/nlp/result/result.mp3')
    engine.runAndWait()
'''
'''
import jieba
import markovify
import pyttsx3

def split(text):
    # 改行、スペース、問題を起こす文字の置換
   table = str.maketrans({
      '\n': '',
      '\r': '',
      '(': '（',
      ')': '）',
      '[': '［',
      ']': '］',
      '"':'”',
      "'":"’",
   })
   text = text.translate(table)

   result = list(jieba.cut(text))

   splitted_text = ""
   for i in range(len(result)):
      splitted_text += result[i]
      if result[i] != '。' and result[i] != '！' and result[i] != '？':
         splitted_text += ' '
      if result[i] == '。' or result[i] == '！' or result[i] == '？':
         splitted_text += '\n'

   return splitted_text
'''
'''
def textGen(file):
   f = open('nlp/Chinese.txt','r')
   text = f.read()
   sentence = None
# 素材によってはNoneが返ることがあるので、その対策したい
   # テキストを処理できる形に分割
   splitted_text = split(text)

   # モデルの生成
   text_model = markovify.NewlineText(splitted_text, state_size=3)

   # モデルを基にして文章を生成
   for i in range(10):
      sentence = text_model.make_sentence(tries=100)   
      final = ( ''.join(sentence.split()))
      print(final)
   
   return final
'''
    # 結合された一連の文字列として返す

'''
textGen('nlp/Chinese.txt')                
TextToSpeech_pyttsx_Chinese_woman(textGen('nlp/Chinese.txt'))
'''
'''
def textGen_Chinese(file):
    f = open(file, 'r', encoding="utf-8")
    text = f.read()
    sentence = None
    while sentence == None: # 素材によってはNoneが返ることがあるので、その対策
        # テキストを処理できる形に分割
        splitted_text = split(text)

        # モデルの生成
        text_model = markovify.NewlineText(splitted_text, state_size=3)

        # モデルを基にして文章を生成
        sentence = text_model.make_sentence()   
'''

'''
def textGen_English(file):
   f = open('nlp/English.txt','r')
   text = f.read()
   sentence = None
# 素材によってはNoneが返ることがあるので、その対策したい

   # モデルの生成
   text_model = markovify.NewlineText(text, state_size=3)

   # モデルを基にして文章を生成
   for i in range(10):
      sentence = text_model.make_sentence(tries=100)   
      final = ( ''.join(sentence.split()))
      print(final)
   
   return final

textGen_English('nlp/English.txt')
'''