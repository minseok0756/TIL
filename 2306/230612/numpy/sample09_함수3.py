import numpy as np

'''
    * 문자열 범용 함수(중요)

   1) 문법

       np.char.문자열함수

      https://numpy.org/devdocs/reference/routines.char.html#module-numpy.char

   2) 종류

      - np.char.add
      - np.char.multiply
      - np.char.capitalize
      - np.char.lower
      - np.char.swapcase
      - np.char.center
      - np.char.ljust
      - np.char.rjust
      - np.char.encode
      - np.char.decode
      - np.char.join
      - np.char.strip
      - np.char.split
      - np.char.replace
      - np.char.find
      - np.char.count
      - np.char.startswith
      - np.char.endswith
      - np.char.equal
      - np.char.isdigit
      - np.char.islower
      - np.char.isupper
      - np.char.rjust
      - np.char.ljust
'''
# 1. np.char.add
x1 = np.array(['Hello', 'Say'], dtype=str)
x2 = np.array([' world', ' something'], dtype=str)
out = np.char.add(x1, x2)
print("1. np.char.add(x1,x2):", out) # ['Hello world' 'Say something']

# 2. np.char.multiply
x = np.array(['Hello ', 'Say '], dtype=str)
out = np.char.multiply(x, 3)
print("2. np.char.multiply(x, 3):", out) # ['Hello Hello Hello ' 'Say Say Say ']

# 2. np.char.함수
x = np.array(['heLLo woRLd', 'Say sOmething'], dtype=str)
capitalized = np.char.capitalize(x)
lowered = np.char.lower(x)
uppered = np.char.upper(x)
swapcased = np.char.swapcase(x)
titlecased = np.char.title(x)
print("3. capitalized =", capitalized) # ['Hello world' 'Say something']
print("4. lowered =", lowered) # ['hello world' 'say something']
print("5. uppered =", uppered) #  ['HELLO WORLD' 'SAY SOMETHING']
print("6. swapcased =", swapcased) # ['HEllO WOrlD' 'sAY SoMETHING']
print("7. titlecased =", titlecased) # ['Hello World' 'Say Something']

# 3. np.char.center,  np.char.ljust, np.char.rjust
x = np.array(['hello world', 'say something'], dtype=str)
centered = np.char.center(x, 20, fillchar='_')
left = np.char.ljust(x, 20, fillchar='_')
right = np.char.rjust(x, 20, fillchar='_')

print("8. centered =", centered) # ['____hello world_____' '___say something____']
print("9. left =", left)       # ['hello world_________' 'say something_______']
print("10. right =", right)    # ['_________hello world' '_______say something']

# 4. np.char.encode,  np.char.decode
x = np.array(['hello world', 'say something'], dtype=str)
encoded = np.char.encode(x, 'cp500')
decoded = np.char.decode(encoded,'cp500')
print("11. encoded =", encoded) # b'\x88\x85\x93\x93\x96@\xa6\x96\x99\x93\x84'
print("12. decoded =", decoded) # ['hello world' 'say something']

# 5. np.char.join
x = np.array(['hello world', 'say something'], dtype=str)
out = np.char.join(",", x)
print("13. join =", out)  # ['h,e,l,l,o, ,w,o,r,l,d' 's,a,y, ,s,o,m,e,t,h,i,n,g']

x = np.array("hello", dtype=str)
out = np.char.join(",", x)
print("13. join =", out) # h,e,l,l,o

x = np.array([1,2,3], dtype=str)
out = np.char.join(",", x)
print("13. join =", out) # ['1' '2' '3']

# 5. np.char.strip => 기본은 공백제거
x = np.array(['   hello world   ', '\tsay something\n'], dtype=str)
stripped = np.char.strip(x)
lstripped = np.char.lstrip(x)
rstripped = np.char.rstrip(x)
print("14. stripped =", stripped) # ['hello world' 'say something']
print("15. lstripped =", lstripped) # ['hello world   ' 'say something\n']
print("16. rstripped =", rstripped) # ['   hello world' '\tsay something']

x =np.array(['aAaAaA', '  aA  ', 'abBABba'])
print("16. ", np.char.strip(x, 'a')) # ['AaAaA' '  aA  ' 'bBABb']
print("16. ", np.char.lstrip(x, 'a')) # ['AaAaA' '  aA  ' 'bBABba']
print("16. ", np.char.rstrip(x, 'a')) # ['aAaAaA' '  aA  ' 'abBABb']

# 6. np.char.split ==> 기본은 공백으로 분리
x = np.array(['Hello my name is John'], dtype=str)
out = np.char.split(x)
print("17. split =", out, out.ndim, out[0][0]) # [list(['Hello', 'my', 'name', 'is', 'John'])] 1 Hello

x = np.array(['He/llo/m/ynameisJ/ohn'], dtype=str)
out = np.char.split(x, '/')
print("17. split =", out, out.ndim, out[0][0]) # [list(['He', 'llo', 'm', 'ynameisJ', 'ohn'])] 1 He

# 7. np.char.replace ==> 기본적으로 모두 변경됨. count지정하여 변경갯수 설정가능
x = np.array(['John Hello my name is John'], dtype=str)
out = np.char.replace(x, "John", "Jim", count=1)
print("18. replace =", out) # ['Jim Hello my name is John']
print()

# 8. np.char.find
x = np.array(['hello world', 'say something'], dtype=str)
out = np.char.find(x, 'e')  # 'e' 문자의 인덱스 값 반환
print("19. find =", out) # [1 7]

# 9. np.char.count
x = np.array(['Hello', 'my', 'name', 'is', 'Lily'], dtype=str)
out = np.char.count(x, "l")
print("20. count =", out) # [2 0 0 0 1]

# 10. np.char.startswith
x = np.array(['he', 'his', 'him', 'his'], dtype=str)
out = np.char.startswith(x, "hi")
print("21. startswith =", out) # [False  True  True  True]

# 11. np.char.endswith
x = np.array(['he', 'his', 'him', 'his'], dtype=str)
out = np.char.endswith(x, "s")
print("22. endswith =", out) # [False  True False  True]

# 12. np.char.equal , np.char.not_equal
x1 = np.array(['Hello', 'my', 'name', 'is', 'John'], dtype=str)
x2 = np.array(['Hello', 'my', 'name', 'is', 'Jim'], dtype=str)
out = np.char.equal(x1, x2)
print(out)  # [ True  True  True  True False]

x1 = np.array(['Hello', 'my', 'name', 'is', 'John'], dtype=str)
x2 = np.array(['Hello', 'my', 'name', 'is', 'Jim'], dtype=str)
out = np.char.not_equal(x1, x2)
print(out)  # [False False False False  True]

#  13. isdigit, islower, isupper, isalpha
x = np.array(['Hello', 'I', 'am', '20', 'years', 'old'], dtype=np.str_)
out1 = np.char.isdigit(x)
out2 = np.char.islower(x)
out3 = np.char.isupper(x)
out4 = np.char.isalpha(x)
print("Digits only =", out1) # [False False False  True False False]
print("Lower cases only =", out2)  # [False False  True False  True  True]
print("Upper cases only =", out3)  # [False  True False False False False]
print("Alpha cases only =", out4) # [ True  True  True False  True  True]
