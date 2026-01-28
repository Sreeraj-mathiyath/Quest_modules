def ConvertTwoDigitsIntoWords(num):
    ones=["","one","two","three","four","five","six","seven","eight","nine"]
    teens=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens=["","","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
    if 0<num<10:
        return ones[num]
    elif 10<num<20:
        return teens[num-10]
    else:
        t=num//10
        o=num%10
        return tens[t] + ("-"+ones[o] if o>0 else "")
    
print(ConvertTwoDigitsIntoWords(21))