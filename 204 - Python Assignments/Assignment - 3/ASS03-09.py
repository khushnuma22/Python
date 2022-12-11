# Q.9. Consider a very small dictionary that contains the translations of English words to Dutch as
# shown below:
# english_dutch = {"last" : "laatst", "week" : "week", "the" : "de", "royal" : "koninklijk",
# "festival" : "feest", "hall" : "hal", "saw" : "zaag", "first" : "eerst", "performance" : "optreden",
# "of" : "van", "a" : "een", "new" : "nieuw", "symphony" : "symphonie", "by" : "bij", "one" : "een",
# "world" : "wereld", "leading" : "leidend", "modern" : "modern", "composer" : "componist",
# "composers" : "componisten", "two" : "twee", "shed" : "schuur", "sheds" : "schuren" }
# Write a program that uses this dictionary to create a word-for-word translation of a sentence to
# be taken as an input from the user. A word for which you cannot find a translation, you can
# leave “as is.” The dictionary is supposed to be used case-insensitively, but your translation may
# consist of all lower-case words. It is nice if you leave punctuation in the translation, but if you
# take it out, that is acceptable (as leaving punctuation in is quite a bit of work and does not really
# have anything to do with dictionaries – besides, leaving punctuation in is much easier to do once
# you have learned about regular expressions).

English_Dutch = {"last" : "laatst", "week" : "week", "the" : "de", "royal" : "koninklijk",
"festival" : "feest", "hall" : "hal", "saw" : "zaag", "first" : "eerst", "performance" : "optreden",
"of" : "van", "a" : "een", "new" : "nieuw", "symphony" : "symphonie", "by" : "bij", "one" : "een",
"world" : "wereld", "leading" : "leidend", "modern" : "modern", "composer" : "componist",
"composers" : "componisten", "two" : "twee", "shed" : "schuur", "sheds" : "schuren" }

while True :
    Data = str(input("Enter a String or 0 for Exit : "))
    if Data == '0' :
        break
    else :
        if Data in English_Dutch :
            Answer = English_Dutch[Data]
            print(Answer)
        else :
            print("Value not found")