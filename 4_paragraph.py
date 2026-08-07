para =  input("enter paragraph:-")

words = para.split()

print("total word :", len(words))
print("unique word :", len(words))
print("longest word :", max(words, key=len))
print("shortest word :", min(words, key=len))

print("words appearing more then once")
for w in set(words):
    if words.count(w) > 1:
        print(w,":",words.count(w))
