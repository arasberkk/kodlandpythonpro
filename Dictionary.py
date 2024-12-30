dictionary_dict = {
    "LMAO": "çok komik",
    "AGGRO": "sinirlenmek",
   }

word = input("bilmediğiniz kelimeyi yazınız")

if kelime in dictionary_dict.keys():
    print(dictionary_dict[kelime])
    
else:
    print("kelime sözlükte bulunmamaktadır")
