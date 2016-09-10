import unicodedata
import sys

# string.translate is a useful method

s = 'pýtĥöň\fis\tawesome\r\n'
print(s)


remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None     # delete it
}

a = s.translate(remap)
print(a)


# remove all combining characters
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a)
print(b)
print(ascii(b))
print(b.translate(cmb_chrs))


# unicode decimal digits to ascii equivalent
digitmap = {
    c: ord('0') + unicodedata.digit(chr(c)) for c in range(sys.maxunicode) if unicodedata.category(chr(c)) == 'Nd'
}

print(len(digitmap))

x = '\u0661\u0662\u0663'    # Arabic digits
print(x.translate(digitmap))


# sanitize with encode and decode
b = unicodedata.normalize('NFD', a)
print(b.encode('ascii', 'ignore'))
print(b.encode('ascii', 'ignore').decode('ascii'))
print(b.encode('utf-8', 'ignore'))
print(b.encode('utf-8', 'ignore').decode('utf-8'))
