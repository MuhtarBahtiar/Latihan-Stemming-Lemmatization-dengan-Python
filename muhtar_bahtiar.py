import ntlk
#Author : Muhtar Bahtiar
from ntlk.steam import PorterSteamer 
porter = PorterSteamer()

tokens = ['study','studying','studies','studied']

for token in tokens:
    print(token + " : " + porter.stem(token))
study : studi
studying : studi
studies : studi
studied : studi

 #Jadi untuk Belajar Stemming & Lemmatization di maksudkan untuk memangkas awalan atau akhiran dari suatu kalimat
 #Dan hasilnya tidak harus ada selalu dalam kamus intinya hanya menyeragamkan.
 #ini biasa kita jumpai saat mengetik di browser yang suka menarankan suatu kata yang kita ketik


 #CONTOH LAINNYA :
In :

#word tokenization
def word_tokenization(s):
    tokens = word_tokenize(s)

    return tokens
    
text_data = "Saya suka belajar. Karena ingin menjadi pintar. Selain itu, saya ingin membuat bahagia kedua orang tua."
word_tokenization(text_data)

Out:

['Saya',
 'suka',
 'belajar',
 '.',
 'Karena',
 'ingin',
 'menjadi',
 'pintar',
 '.',
 'Selain',
 'itu',
 ',',
 'saya',
 'ingin',
 'membuat',
 'bahagia',
 'kedua',
 'orang',
 'tua',
 '.']


