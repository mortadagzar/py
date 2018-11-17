word=input('أكتب كلمة تريد تشفيرها   : ')
from hashlib import *
x=md5(word.encode()).hexdigest()
print("الكلمة  بعد التشفير هي :",x)
