#!/usr/bin/env python
# -*- coding: utf-8 -*-

file = open("language.json", "w")
file.write("{ \n \t \"lang_words\" : [ \n \t\t{ ")
value = input("Kelime girmek istiyormusunuz?(e/E)")
def Function():
    if value == "e" or value == "E":
        devamEt = True
        if (devamEt == True):
            lang_text = input("Language text add please\n")

            file.write("\n\t\t" + "\"alias\" : \"" + lang_text + "\",")
            file.write("\n\t\t" + "\"translations\" : [ \n \t\t\t")
            language_count = int(input("Kaç dilde çevrilecek?"))
            for x in range(language_count):
                lang1 = input("Language write \n")
                lang1 = lang1.replace('"', " ")
                file.write("\n\t\t\t\t{ \"lang_code\" :" + "\"" + lang1 + "\",")
                text1 = input("text write for " + lang1 + "\n")
                text1 = text1.replace('"', " ")
                file.write("\n \t\t\t\t\"text\" : " + "\"" + text1 + "\" \n \t\t\t\t}")
                if language_count > 0:
                    if x <  language_count-1:
                        file.write(",")
                elif language_count == 1:
                    for x in range(language_count):
                        file.write(",")

                else:
                    file.write("\n\t\t\n\t\t\t\n]\n\t\t\t}")
                devamEt = False
            secim = input("Kelime girmek istiyormusunuz?")
            if (secim == "e" or secim == "E"):
                file.write("\n\t\t\t]\n\t\t}\n\t\t,{")
                Function()
            else:
               file.write("\n\t\t\t]\n\t\t}\n\t]\n}")
    else:
        print("Hatalı giris. Yalnızca e veya E girin")


Function()