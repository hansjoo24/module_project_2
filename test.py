import hashlib
def get_couponNum():
    md5hash='66'
    charSet = ["S", "e", "y", "o", "n", "g", "-", "K", "i", "m"]
    prefix = "Eqst"
    time = '1006'
    couponfront = ""
    couponmiddle = ""
    memberid = 'kmst1234'

    for char in time:
        couponfront += charSet[int(char)]

    asciisum = 810
    for char in memberid:
        asciisum += ord(char)

    asciisum = str(asciisum).zfill(4)
    for char in asciisum:
        couponmiddle += charSet[int(char)]

    #print(prefix+couponfront+couponmiddle)
    return prefix+couponfront+couponmiddle


    
    

def couponValidation():
    md5hash='66'
    

    for i in range(65,127):
        for j in range(65,127):
            for k in range(65,127):
                couponNum='EqsteSS-engm'
                couponNum = couponNum + chr(i) + chr(j) + chr(k)
                inputmd5 = hashlib.md5(couponNum[:13].encode()).hexdigest()[:2]
                split = 4
                if (couponNum[:split] == prefix and
                    couponNum[split * 2:split * 3] == couponmiddle and
                    couponNum[split:split * 2] == couponfront and
                    couponNum[split * 3 + 1:split * 3 + 3] == md5hash and
                    inputmd5 == md5hash):
                    print(couponNum)
                    exit()
                
                else:
                    print("no")

    


    

couponValidation()

md5hash='66'
    
    for i in range(65,127):
        for j in range(65,127):
            for k in range(65,127):
                couponNum='EqsteSS-engm'
                couponNum = couponNum + chr(i) + chr(j) + chr(k)
                inputmd5 = hashlib.md5(couponNum[:13].encode()).hexdigest()[:2]
                split = 4
                if (couponNum[:split] == prefix and
                    couponNum[split * 2:split * 3] == couponmiddle and
                    couponNum[split:split * 2] == couponfront and
                    couponNum[split * 3 + 1:split * 3 + 3] == md5hash and
                    inputmd5 == md5hash):
                    print(couponNum)
                    exit()
                
                else:
                    print("no")
