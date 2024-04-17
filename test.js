if (couponNum.substring(0, 4) == prefix) {
    if (couponNum.substring(8, 12) == couponmiddle) {
        if (couponNum.substring(4, 8) == couponfront) {
            if (couponNum.substr(13, 15) == md5hash) {
                if (inputmd5 == md5hash) {
                    return true;
                }
            }
        }
    }
}
0123 4567 891011
Eqst / eSSt / engm / 66
prefix + couponfront + couponmiddle + md5hash
Eqst +                                $('#md5hash').val();
EqsteSSyeo-m
memberid = kmst1234
asciisum = 1369
middle = eo-m
time = 1002

word = 'EqsteSStengm'

for (var i = 65; i < 128; i++) {
    for (var j = 65; j < 128; j++) {
        for (var k = 65; k < 128; k++) {
            var couponNum = 'EqsteSSnengm' + String.fromCharCode(i) + String.fromCharCode(j) + String.fromCharCode(k);
            var inputmd5 = MD5(couponNum.substr(0,13)).substr(0,2);
            if (couponNum.substr(split * 3 + 1, 2) == md5hash) {
                if (inputmd5 == md5hash) {
                    console.log(couponNum)
                }
            }       
         }
    }
}




    var inputmd5 = MD5(couponNum.substr(0,13)).substr(0,2);
    console.log(prefix+couponfront+couponmiddle)
    console.log(md5hash)
    var inputmd5 = MD5(couponNum.substr(0,13)).substr(0,2);
    
    for (var i = 65; i < 128; i++) {
        for (var j = 65; j < 128; j++) {
            for (var k = 65; k < 128; k++) {
                couponNum = prefix+couponfront+couponmiddle + String.fromCharCode(i) + String.fromCharCode(j) + String.fromCharCode(k);
                var split = 4;
    if (couponNum.substring(0, split) == prefix) {
        if (couponNum.substring(split * 2, split * 3) == couponmiddle) {
            if (couponNum.substring(split * 1, split * 2) == couponfront) {
                if (couponNum.substr(split * 3 + 1, 2) == md5hash) {
                    if (inputmd5 == md5hash) {
                        console.log(couponNum)
                    }
                }
            }
        }
    }
            }
        }
    }
    

    const md5hash = '66';
    var memberid = $('#memberid').val();
    var md5hash = $('#md5hash').val();
    var couponNum = $('#couponnum').val();
    var charSet = ["S", "e", "y", "o", "n", "g", "-", "K", "i", "m"];
    var prefix = "Eqst";
    var time = Math.floor(new Date().getTime() / 1000000 % 10000).toString()
    var couponfront = "";
    var couponmiddle = "";
    for (i = 0; i < time.length; i++) {
        couponfront += charSet[Number(time[i])];
    }

    var asciisum = 810;

    for (i = 0; i < memberid.length; i++) {
        asciisum += memberid.charCodeAt(i);
    }

    asciisum = String(asciisum).padStart(4, '0');
    for (i = 0; i < asciisum.length; i++) {
        couponmiddle += charSet[Number(asciisum[i])];
    }

    var charSet = ["S", "e", "y", "o", "n", "g", "-", "K", "i", "m"];
    var asciisum = 810;
    var memberid = 'kmst1234'
    
        for (i = 0; i < memberid.length; i++) {
            asciisum += memberid.charCodeAt(i);
        }
    
        asciisum = String(asciisum).padStart(4, '0');
        for (i = 0; i < asciisum.length; i++) {
            couponmiddle += charSet[Number(asciisum[i])];
        }
    console.log(couponmiddle);
    
    var time = Math.floor(new Date().getTime() / 1000000 % 10000).toString();
    for (i = 0; i < time.length; i++) {
        couponfront += charSet[Number(time[i])];
    }
    console.log(couponfront);
    
    
    var memberid = $('#memberid').val();
    var md5hash = $('#md5hash').val();
    var couponNum = ""
    var charSet = ["S", "e", "y", "o", "n", "g", "-", "K", "i", "m"];
    var prefix = "Eqst";
    var time = Math.floor(new Date().getTime() / 1000000 % 10000).toString()
    var couponfront = "";
    var couponmiddle = "";
    for (i = 0; i < time.length; i++) {
        couponfront += charSet[Number(time[i])];
    }
    
    var asciisum = 810;
    
    for (i = 0; i < memberid.length; i++) {
        asciisum += memberid.charCodeAt(i);
    }
    
    asciisum = String(asciisum).padStart(4, '0');
    for (i = 0; i < asciisum.length; i++) {
        couponmiddle += charSet[Number(asciisum[i])];
    }

for (let i = 65; i < 127; i++) {
    for (let j = 65; j < 127; j++) {
        for (let k = 65; k < 127; k++) {
            let couponNum = 'EqsteSS-engm';
            couponNum += String.fromCharCode(i) + String.fromCharCode(j) + String.fromCharCode(k);
            var inputmd5 = MD5(couponNum.substr(0,13)).substr(0,2);

            var split = 4;
            if (couponNum.substring(0, split) == prefix) {
                if (couponNum.substring(split * 2, split * 3) == couponmiddle) {
                    if (couponNum.substring(split * 1, split * 2) == couponfront) {
                        if (couponNum.substr(split * 3 + 1, 2) == md5hash) {
                            if (inputmd5 == md5hash) {
                                console.log(couponNum)
                            }
                            else console.log("no")
                        }
                    }
                }
            }
        }
    }
}



var memberid = "kmst1234"; 
var md5hash = $('#md5hash').val();
var couponNum = "";
var charSet = ["S", "e", "y", "o", "n", "g", "-", "K", "i", "m"];
var prefix = "Eqst";
var time = Math.floor(new Date().getTime() / 1000000 % 10000).toString();
var couponfront = "";
var couponmiddle = "";
var split = 4;

// couponfront 계산
for (let i = 0; i < time.length; i++) {
    couponfront += charSet[Number(time[i])];
}

// couponmiddle 계산
var asciisum = 810;
for (let i = 0; i < memberid.length; i++) {
    asciisum += memberid.charCodeAt(i);
}
asciisum = String(asciisum).padStart(4, '0');
for (let i = 0; i < asciisum.length; i++) {
    couponmiddle += charSet[Number(asciisum[i])];
}

// couponNum 생성 및 검증
for (let i = 1; i < 128; i++) {
    couponNum = prefix + couponfront + couponmiddle + String.fromCharCode(i) + md5hash;
    var inputmd5 = MD5(couponNum.substr(0, 13)).substr(0, 2);

    if (couponNum.substring(0, split) === prefix &&
        couponNum.substring(split * 2, split * 3) === couponmiddle &&
        couponNum.substring(split, split * 2) === couponfront &&
        couponNum.substr(split * 3 + 1, 2) === md5hash &&
        inputmd5 === md5hash) {
            console.log("yes;")
            console.log(couponNum);
    } else {
        console.log("no");
    }
}
