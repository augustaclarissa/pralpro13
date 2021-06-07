#Augusta Clarissa Silvy Pascalin
#Universitas Kristen Duta Wacana
#Topic : Regular Expressions

'''Rissa adalah orang yang suka menulis sesuatu di dalam diarynya. Karena takut orang lain membaca rahasianya,
ia menggunakan inisial nama untuk subjek dalam diarynya, kemudian huruf selanjutnya diganti dengan simbol *
seolah - olah disensor dengan syarat menambahkan panggilan Si di depan nama'''

#input : txt diary
#proses : import re, melakukan compile untuk panggilan Si dengan regex (\w)\w*, melakukan sub untuk mengubah nama 
#menjadi inisial diikuti simbol * butuh 2 argumen string pengganti dan string yang ingin diganti
#output : inisial nama diikuti simbol ****

import re

txt = input("Tulis cerita hari ini : ")
secret = re.compile(r'(Si|Pak|Bu) (\w)\w*')
secret = secret.sub(r'\1****', txt)
print(secret)