from textblob import TextBlob
str = TextBlob('Bonjour')
print(str.detect_language())
print(str.translate(to = "hi"))

# import TextBlob
# from textblob import TextBlob

a = TextBlob("Campk12 is a good compny and alays valule ttheir employeees.")

# using TextBlob.correct() method
a = a.correct()

print(a)


blob = TextBlob("Comment vas-tu?")
 
print(blob.detect_language())
 
print(blob.translate(to='es'))
print(blob.translate(to='en'))
print(blob.translate(to='zh'))