from django.shortcuts import render
from django.http import HttpResponse
from googletrans import Translator
import pyttsx3
import jieba
import ffmpeg
import markovify
import os


translator = Translator()

#以下apiの関数宣言

#英語音声合成→ffmpegで再変換
def TextToSpeech_English_man(ph):
    os.remove('nlp/static/nlp/result/English.mp3')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    engine.setProperty("voice", voices[0].id)
    engine.save_to_file(str(ph), 'nlp/static/nlp/result/result.mp3')
    engine.runAndWait()
    stream = ffmpeg.input("nlp/static/nlp/result/result.mp3")
    stream = ffmpeg.output(stream, "nlp/static/nlp/result/English.mp3")
    ffmpeg.run(stream)

#中国語音声合成→ffmpegで再変換
def TextToSpeech_pyttsx_Chinese_woman(ph):
    os.remove("nlp/static/nlp/result/Chinese.mp3")
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    engine.setProperty("voice", voices[25].id)
    engine.save_to_file(ph, 'nlp/static/nlp/result/result.mp3')
    engine.runAndWait()
    stream = ffmpeg.input('nlp/static/nlp/result/result.mp3')
    stream = ffmpeg.output(stream,"nlp/static/nlp/result/Chinese.mp3")
    ffmpeg.run(stream)
 
#中国語の文字の置換、形態素解析
def split_C(text):
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

#英語の文字の置換(Newlinetesxtで生成できるように)
def split_E(text):
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
   result = text.translate(table)

   splitted_text = ""
   for i in range(len(result)):
      splitted_text += result[i]
      if result[i] == '.' or result[i] == '！' or result[i] == '？':
         splitted_text += '\n'

   return splitted_text

#中国語文章生成
def textGen_Chinese(file):
   f = open(file,'r')
   text = f.read()
   sentence = None
   # テキストを処理できる形に分割
   splitted_text = split_C(text)

   # モデルの生成
   text_model = markovify.NewlineText(splitted_text, state_size=3)

   final=''
   # モデルを基にして文章を生成
   for i in range(7):
      sentence = text_model.make_sentence(tries=100) 
      if sentence is not None:
            final += (''.join(sentence.split()))
      else:
            continue  
        
   
   return final

#英語文章生成
def textGen_English(file):
    f = open(file,'r')
    text = f.read()
    sentence = None
    # テキストを処理できる形に分割
    splitted_text = split_E(text)
   # モデルの生成
    text_model = markovify.NewlineText(splitted_text, state_size=3)
    final = ''

   # モデルを基にして文章を生成
    for i in range(10):
        sentence = text_model.make_sentence(tries=100)
        #noneの対策
        if sentence is not None:
            final += sentence
        else:
            continue
        #.の後に半角スペースを入れて一つのまとまりにする。

    return final

#ここからview.py
#何もなかった時
def home(request):
    if request.method == "GET":
        return render(
        request,
        "nlp/home.html"
        )
    #中国語が選ばれた場合
    elif 'cpipr03' in request.POST:
        Chinese = request.POST['cpipr03']
        if Chinese == 'Chinese_business':
            result = textGen_Chinese('nlp/static/nlp/Chinese/business_C.txt')
            trans_ja = translator.translate(result, src='zh-cn', dest='ja')
            Chinese_list={'genre': '経済', 'result': result, 'trans_ja': trans_ja.text}
            TextToSpeech_pyttsx_Chinese_woman(result)

            return render(
                request,
                "nlp/home.html",
                {'Chinese_list':Chinese_list}
                )
        elif Chinese == 'Chinese_medical':
            result = textGen_Chinese('nlp/static/nlp/Chinese/medical_C.txt')
            trans_ja = translator.translate(result, src='zh-cn', dest='ja')
            Chinese_list={'genre': '医療', 'result': result, 'trans_ja': trans_ja.text}
            TextToSpeech_pyttsx_Chinese_woman(result)
        
            return render(
                request,
                "nlp/home.html",
                {'Chinese_list':Chinese_list}
            )
        elif Chinese == 'Chinese_science':
            result = textGen_Chinese('nlp/static/nlp/Chinese/science_C.txt')
            trans_ja = translator.translate(result, src='zh-cn', dest='ja')
            Chinese_list={'genre': '科学', 'result': result, 'trans_ja': trans_ja.text}
            TextToSpeech_pyttsx_Chinese_woman(result)
        
            return render(
                request,
                "nlp/home.html",
                {'Chinese_list':Chinese_list}
            )
        else:
            return render(
                request,
                "nlp/home.html"
            )
    #英語が選ばれた場合
    elif 'cpipr04' in request.POST:
        English = request.POST['cpipr04']
        if English == 'English_business':
            result = textGen_English('nlp/static/nlp/English/business_E.txt')
            trans_ja = translator.translate(result, src='en', dest='ja')
            English_list={'genre': '経済', 'result': result, 'trans_ja': trans_ja.text}
            TextToSpeech_English_man(result)
        
            return render(
                request,
                "nlp/home.html",
                {'English_list':English_list}
            )
        elif English == 'English_medical':
            result = textGen_English('nlp/static/nlp/English/medical_E.txt')
            trans_ja = translator.translate(result, src='en', dest='ja')
            English_list={'genre': '医療', 'result': result, 'trans_ja': trans_ja.text}
            TextToSpeech_English_man(result)
        
            return render(
                request,
                "nlp/home.html",
                {'English_list':English_list}
            )
        elif English == 'English_science':
            result = textGen_English('nlp/static/nlp/English/science_E.txt')
            trans_ja = translator.translate(result, src='en', dest='ja')
            English_list={'genre': '科学', 'result': result, 'trans_ja': trans_ja.text}
            TextToSpeech_English_man(result)
        
            return render(
                request,
                "nlp/home.html",
                {'English_list':English_list}
            )
        else:
            return render(
                request,
                "nlp/home.html"
            )
    #何も選ばれなかった時
    else:
            return render(
                request,
                "nlp/home.html"
            )

        
    
"""
def trans(request):
    if request.method == "GET":
        return render(
        request,
        "nlp/trans.html"
        )
"""   
    
    








#ここまで関数

