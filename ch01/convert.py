ones=["","one","two","three","four","five","six","seven","eight","nine","ten",
     "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen",
     "eighteen","nineteen"]

tens=["","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]

def numToWords(n, s):
    
    str=""

    if n > 19:
        str+=tens[n//10]+ones[n%10]
    else:
        str+=ones[n]
    if n:
        str+=s

    return str


def convertTowords(n):

    out=""

    out+=numToWords((n//10000000),"crore")

    out+=numToWords(((n//100000)%100),"lakh")

    out+=numToWords(((n//1000)%100),"thousand")

    out+=numToWords(((n//100)%10),"hundred")

    if n>100 and n%100:
        out+="and"

    out+=numToWords((n%100),"")

    return out


n=int(input("Enter a number:"))
print(convertTowords(n))             
