# coding:utf-8

import json
import re

import execjs

from util.app_util import timestamp
from util.net_util import api

js_url = 'https://kyfw.12306.cn/otn/HttpZF/GetJS'
advice_url = "https://kyfw.12306.cn/otn/HttpZF/logdevice?algID={}&hashCode={}{}&timestamp={}"

params = {
    'FMQw': '0',  # adblock
    'q4f3': 'en-US',  # browserLanguage
    'VPIf': '1',  # cookieEnabled
    'custID': '133',  # custID
    'VEek': 'unknown',  # doNotTrack
    'dzuS': '0',  # flashVersion
    'yD16': '0',  # javaEnabled
    'EOQP': 'f58b1186770646318a429cb33977d8c',  # jsFonts
    'jp76': '52d67b2a5aa5e031084733d5006cc664',  # mimeTypes
    'hAqN': 'Win32',  # os
    'platform': 'WEB',  # platform
    'ks0Q': 'd22ca0b81584fbea62237b14bd04c866',  # plugins
    'TeRS': '1040x1920',  # scrAvailSize
    'tOHY': '24xx1080x1920',  # srcScreenSize
    'Fvje': 'i1l1o1s1',  # storeDb
    'q5aJ': '-8',  # timeZone
    'wNLf': '99115dfb07133750ba677d055874de87',  # touchSupport
    '0aew': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWeb…L, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    # userAgent
    'E3gR': 'fb25305a718e8032038c5a2905f60536',  # webSmartID
}


def generate_advice():
    res = api.single_get(js_url).text
    alg_id = re.findall(r'\\x3d\w*\\x26', res)[0][4:-4]
    if alg_id == 'vAxaJJ4MXM':
        ctx = execjs.compile("""
                function Ya(a){return 0|4294967296*(a-(0|a))}function l(a,b){this.key=a,this.value=b}function launch(){var d,e,f,b="",c="";for(a=[],a.push(new l("adblock","0")),a.push(new l("browserLanguage","en-US")),a.push(new l("cookieEnabled","1")),a.push(new l("custID","133")),a.push(new l("doNotTrack","unknown")),a.push(new l("flashVersion",0)),a.push(new l("javaEnabled","0")),a.push(new l("jsFonts","8f58b1186770646318a429cb33977d8c")),a.push(new l("mimeTypes","52d67b2a5aa5e031084733d5006cc664")),a.push(new l("os","Win32")),a.push(new l("platform","WEB")),a.push(new l("plugins","d22ca0b81584fbea62237b14bd04c866")),a.push(new l("scrAvailSize","1040x1920")),a.push(new l("srcScreenSize","24xx1080x1920")),a.push(new l("storeDb","i1l1o1s1")),a.push(new l("timeZone",-8)),a.push(new l("touchSupport","99115dfb07133750ba677d055874de87")),a.push(new l("userAgent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")),a.push(new l("webSmartID","fb25305a718e8032038c5a2905f60536")),a.sort(function(a,b){var c,d;if("object"==typeof a&&"object"==typeof b&&a&&b)return c=a.key,d=b.key,c===d?0:typeof c==typeof d?d>c?-1:1:typeof d>typeof c?-1:1;throw"error"}),d=0;d<a.length;d++)e=a[d].key.replace(RegExp("%","gm"),""),f="",f="string"==typeof a[d].value?a[d].value.replace(RegExp("%","gm"),""):a[d].value,""!==f&&(c+=e+f,b+="&"+(void 0==hb[e]?e:hb[e])+"="+f);for(a=c,c=a.length,d=0==c%3?parseInt(c/3):parseInt(c/3)+1,3>c||(e=a.substring(0,1*d),f=a.substring(1*d,2*d),a=a.substring(2*d,c)+e+f),c=a.length,d="",a=d=0==a.length%2?a.substring(c/2,c)+a.substring(0,c/2):a.substring(c/2+1,c)+a.charAt(c/2)+a.substring(0,c/2),c="",d=a.length,e=0;d>e;e++)f=a.charAt(e).charCodeAt(0),c=127===f?c+String.fromCharCode(0):c+String.fromCharCode(f+1);for(a=c,c="",d=a.length-1;d>=0;d--)c+=a.charAt(d);return d=c,e=d.length,f=0==e%3?parseInt(e/3):parseInt(e/3)+1,3>e?c=d:(a=d.substring(0,1*f),c=d.substring(1*f,2*f),d=d.substring(2*f,e),c=c+d+a),c=ca.SHA256(c).toString(Base64),new l(b,c)}var wb,ca,sa,ta,R,xb,ua,db,eb,va,ga,W,yb,La,S,fb,zb,res,hb={online:"9vyE",appcodeName:"qT7b",browserLanguage:"q4f3",flashVersion:"dzuS",historyList:"kU5z",localStorage:"XM7l",systemLanguage:"e6OK",scrDeviceXDPI:"3jCe",cookieCode:"VySQ",scrWidth:"ssI5",browserVersion:"d435",hasLiedBrowser:"2xC5",cookieEnabled:"VPIf",indexedDb:"3sw-",scrHeight:"5Jwy",adblock:"FMQw",javaEnabled:"yD16",os:"hAqN",srcScreenSize:"tOHY",scrAvailSize:"TeRS",scrAvailWidth:"E-lJ",webSmartID:"E3gR",hasLiedResolution:"3neK",touchSupport:"wNLf",cpuClass:"Md7A",browserName:"-UVA",mimeTypes:"jp76",userLanguage:"hLzX",openDatabase:"V8vl",scrAvailHeight:"88tV",localCode:"lEnu",plugins:"ks0Q",userAgent:"0aew",storeDb:"Fvje",appMinorVersion:"qBVW",hasLiedOs:"ci5c",doNotTrack:"VEek",jsFonts:"EOQP",scrColorDepth:"qmyu",hasLiedLanguages:"j5po",sessionStorage:"HVia",timeZone:"q5aJ"},da=Math,qa={},ra=qa.lib={},ab=function(){},ea=ra.Base={init:function(){},create:function(){var a=this.extend();return a.init.apply(a,arguments),a},extend:function(a){ab.prototype=this;var b=new ab;return a&&b.mixIn(a),b.hasOwnProperty("init")||(b.init=function(){b.$super.init.apply(this,arguments)}),b.init.prototype=b,b.$super=this,b},mixIn:function(a){for(var b in a)a.hasOwnProperty(b)&&(this[b]=a[b]);a.hasOwnProperty("toString")&&(this.toString=a.toString)},clone:function(){return this.init.prototype.extend(this)}},fa=ra.WordArray=ea.extend({toString:function(a){return(a||ub).stringify(this)},clamp:function(){var a=this.words,b=this.sigBytes;a[b>>>2]&=4294967295<<32-8*(b%4),a.length=da.ceil(b/4)},clone:function(){var a=ea.clone.call(this);return a.words=this.words.slice(0),a},concat:function(a){var e,b=this.words,c=a.words,d=this.sigBytes;if(a=a.sigBytes,this.clamp(),d%4)for(e=0;a>e;e++)b[d+e>>>2]|=(255&c[e>>>2]>>>24-8*(e%4))<<24-8*((d+e)%4);else if(65535<c.length)for(e=0;a>e;e+=4)b[d+e>>>2]=c[e>>>2];else b.push.apply(b,c);return this.sigBytes+=a,this},init:function(a,b){a=this.words=a||[],this.sigBytes=void 0!=b?b:4*a.length},random:function(a){for(var b=[],c=0;a>c;c+=4)b.push(0|4294967296*da.random());return new fa.init(b,a)}}),Ka=qa.enc={},ub=Ka.Hex={parse:function(a){for(var b=a.length,c=[],d=0;b>d;d+=2)c[d>>>3]|=parseInt(a.substr(d,2),16)<<24-4*(d%8);return new fa.init(c,b/2)},stringify:function(a){var c,d,e,b=a.words;for(a=a.sigBytes,c=[],d=0;a>d;d++)e=255&b[d>>>2]>>>24-8*(d%4),c.push((e>>>4).toString(16)),c.push((15&e).toString(16));return c.join("")}},bb=Ka.Latin1={stringify:function(a){var c,d,b=a.words;for(a=a.sigBytes,c=[],d=0;a>d;d++)c.push(String.fromCharCode(255&b[d>>>2]>>>24-8*(d%4)));return c.join("")},parse:function(a){for(var b=a.length,c=[],d=0;b>d;d++)c[d>>>2]|=(255&a.charCodeAt(d))<<24-8*(d%4);return new fa.init(c,b)}},vb=Ka.Utf8={parse:function(a){return bb.parse(unescape(encodeURIComponent(a)))},stringify:function(a){try{return decodeURIComponent(escape(bb.stringify(a)))}catch(b){throw Error("Malformed UTF-8 data")}}},cb=ra.BufferedBlockAlgorithm=ea.extend({_append:function(a){"string"==typeof a&&(a=vb.parse(a)),this._data.concat(a),this._nDataBytes+=a.sigBytes},reset:function(){this._data=new fa.init,this._nDataBytes=0},_process:function(a){var g,b=this._data,c=b.words,d=b.sigBytes,e=this.blockSize,f=d/(4*e);if(f=a?da.ceil(f):da.max((0|f)-this._minBufferSize,0),a=f*e,d=da.min(4*a,d),a){for(g=0;a>g;g+=e)this._doProcessBlock(c,g);g=c.splice(0,a),b.sigBytes-=d}return new fa.init(g,d)},clone:function(){var a=ea.clone.call(this);return a._data=this._data.clone(),a},_minBufferSize:0});for(ra.Hasher=cb.extend({init:function(a){this.cfg=this.cfg.extend(a),this.reset()},finalize:function(a){return a&&this._append(a),this._doFinalize()},_createHelper:function(a){return function(b,c){return new a.init(c).finalize(b)}},cfg:ea.extend(),blockSize:16,update:function(a){return this._append(a),this._process(),this},reset:function(){cb.reset.call(this),this._doReset()},_createHmacHelper:function(a){return function(b,c){return new wb.HMAC.init(a,c).finalize(b)}}}),wb=qa.algo={},Ja=qa,ca=Ja,sa=Math,ta=ca,R=ta.lib,xb=R.WordArray,ua=R.Hasher,R=ta.algo,db=[],eb=[],va=2,ga=0;64>ga;){a:{for(W=va,yb=sa.sqrt(W),La=2;yb>=La;La++)if(!(W%La)){W=!1;break a}W=!0}W&&(8>ga&&(db[ga]=Ya(sa.pow(va,.5))),eb[ga]=Ya(sa.pow(va,1/3)),ga++),va++}S=[],R=R.SHA256=ua.extend({_doFinalize:function(){var a=this._data,b=a.words,c=8*this._nDataBytes,d=8*a.sigBytes;return b[d>>>5]|=128<<24-d%32,b[(d+64>>>9<<4)+14]=sa.floor(c/4294967296),b[(d+64>>>9<<4)+15]=c,a.sigBytes=4*b.length,this._process(),this._hash},_doReset:function(){this._hash=new xb.init(db.slice(0))},_doProcessBlock:function(a,b){var c,d,e,f,g,h,i,j,k,l,m,n;for(c=this._hash.words,d=c[0],e=c[1],f=c[2],g=c[3],h=c[4],i=c[5],j=c[6],k=c[7],l=0;64>l;l++)16>l?S[l]=0|a[b+l]:(m=S[l-15],n=S[l-2],S[l]=((m<<25|m>>>7)^(m<<14|m>>>18)^m>>>3)+S[l-7]+((n<<15|n>>>17)^(n<<13|n>>>19)^n>>>10)+S[l-16]),m=k+((h<<26|h>>>6)^(h<<21|h>>>11)^(h<<7|h>>>25))+(h&i^~h&j)+eb[l]+S[l],n=((d<<30|d>>>2)^(d<<19|d>>>13)^(d<<10|d>>>22))+(d&e^d&f^e&f),k=j,j=i,i=h,h=0|g+m,g=f,f=e,e=d,d=0|m+n;c[0]=0|c[0]+d,c[1]=0|c[1]+e,c[2]=0|c[2]+f,c[3]=0|c[3]+g,c[4]=0|c[4]+h,c[5]=0|c[5]+i,c[6]=0|c[6]+j,c[7]=0|c[7]+k},clone:function(){var a=ua.clone.call(this);return a._hash=this._hash.clone(),a}}),ta.SHA256=ua._createHelper(R),ta.HmacSHA256=ua._createHmacHelper(R),fb=ca,zb=fb.lib.WordArray,Base64={stringify:function(a){var e,f,g,b=a.words,c=a.sigBytes,d=this._map;for(a.clamp(),a=[],e=0;c>e;e+=3)for(f=(255&b[e>>>2]>>>24-8*(e%4))<<16|(255&b[e+1>>>2]>>>24-8*((e+1)%4))<<8|255&b[e+2>>>2]>>>24-8*((e+2)%4),g=0;4>g&&c>e+.75*g;g++)a.push(d.charAt(63&f>>>6*(3-g)));if(b=d.charAt(64))for(;a.length%4;)a.push(b);return a.join("")},_map:"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_",parse:function(a){var e,f,g,h,b=a.length,c=this._map,d=c.charAt(64);for(d&&(d=a.indexOf(d),-1!=d&&(b=d)),d=[],e=0,f=0;b>f;f++)f%4&&(g=c.indexOf(a.charAt(f-1))<<2*(f%4),h=c.indexOf(a.charAt(f))>>>6-2*(f%4),d[e>>>2]|=(g|h)<<24-8*(e%4),e++);return zb.create(d,e)}},res=launch(),console.log(res.key),console.log(res.value);
                """)

    elif alg_id == 'rnFP89sRGr':
        ctx = execjs.compile("""
                var hb={online:"9vyE",appcodeName:"qT7b",browserLanguage:"q4f3",flashVersion:"dzuS",historyList:"kU5z",localStorage:"XM7l",systemLanguage:"e6OK",scrDeviceXDPI:"3jCe",cookieCode:"VySQ",scrWidth:"ssI5",browserVersion:"d435",hasLiedBrowser:"2xC5",cookieEnabled:"VPIf",indexedDb:"3sw-",scrHeight:"5Jwy",adblock:"FMQw",javaEnabled:"yD16",os:"hAqN",srcScreenSize:"tOHY",scrAvailSize:"TeRS",scrAvailWidth:"E-lJ",webSmartID:"E3gR",hasLiedResolution:"3neK",touchSupport:"wNLf",cpuClass:"Md7A",browserName:"-UVA",mimeTypes:"jp76",userLanguage:"hLzX",openDatabase:"V8vl",scrAvailHeight:"88tV",localCode:"lEnu",plugins:"ks0Q",userAgent:"0aew",storeDb:"Fvje",appMinorVersion:"qBVW",hasLiedOs:"ci5c",doNotTrack:"VEek",jsFonts:"EOQP",scrColorDepth:"qmyu",hasLiedLanguages:"j5po",sessionStorage:"HVia",timeZone:"q5aJ"};function ya(a){return Y.SHA256(a).toString(Y.enc.Base64)}function Ya(a){return 4294967296*(a-(a|0))|0}var da=Math,pa={},qa=pa.lib={},ab=function(){},ea=qa.Base={clone:function(){return this.init.prototype.extend(this)},mixIn:function(a){for(var b in a){a.hasOwnProperty(b)&&(this[b]=a[b])}a.hasOwnProperty("toString")&&(this.toString=a.toString)},create:function(){var a=this.extend();a.init.apply(a,arguments);return a},extend:function(a){ab.prototype=this;var b=new ab;a&&b.mixIn(a);b.hasOwnProperty("init")||(b.init=function(){b.$super.init.apply(this,arguments)});b.init.prototype=b;b.$super=this;return b},init:function(){}},fa=qa.WordArray=ea.extend({init:function(a,b){a=this.words=a||[];this.sigBytes=void 0!=b?b:4*a.length},random:function(a){for(var b=[],c=0;c<a;c+=4){b.push(4294967296*da.random()|0)}return new fa.init(b,a)},toString:function(a){return(a||vb).stringify(this)},concat:function(a){var b=this.words,c=a.words,d=this.sigBytes;a=a.sigBytes;this.clamp();if(d%4){for(var e=0;e<a;e++){b[d+e>>>2]|=(c[e>>>2]>>>24-e%4*8&255)<<24-(d+e)%4*8}}else{if(65535<c.length){for(e=0;e<a;e+=4){b[d+e>>>2]=c[e>>>2]}}else{b.push.apply(b,c)}}this.sigBytes+=a;return this},clone:function(){var a=ea.clone.call(this);a.words=this.words.slice(0);return a},clamp:function(){var a=this.words,b=this.sigBytes;a[b>>>2]&=4294967295<<32-b%4*8;a.length=da.ceil(b/4)}}),Ka=pa.enc={},vb=Ka.Hex={stringify:function(a){var b=a.words;a=a.sigBytes;for(var c=[],d=0;d<a;d++){var e=b[d>>>2]>>>24-d%4*8&255;c.push((e>>>4).toString(16));c.push((e&15).toString(16))}return c.join("")},parse:function(a){for(var b=a.length,c=[],d=0;d<b;d+=2){c[d>>>3]|=parseInt(a.substr(d,2),16)<<24-d%8*4}return new fa.init(c,b/2)}},bb=Ka.Latin1={stringify:function(a){var b=a.words;a=a.sigBytes;for(var c=[],d=0;d<a;d++){c.push(String.fromCharCode(b[d>>>2]>>>24-d%4*8&255))}return c.join("")},parse:function(a){for(var b=a.length,c=[],d=0;d<b;d++){c[d>>>2]|=(a.charCodeAt(d)&255)<<24-d%4*8}return new fa.init(c,b)}},wb=Ka.Utf8={stringify:function(a){try{return decodeURIComponent(escape(bb.stringify(a)))}catch(b){throw Error("Malformed UTF-8 data")}},parse:function(a){return bb.parse(unescape(encodeURIComponent(a)))}},cb=qa.BufferedBlockAlgorithm=ea.extend({_append:function(a){"string"==typeof a&&(a=wb.parse(a));this._data.concat(a);this._nDataBytes+=a.sigBytes},clone:function(){var a=ea.clone.call(this);a._data=this._data.clone();return a},_minBufferSize:0,reset:function(){this._data=new fa.init;this._nDataBytes=0},_process:function(a){var b=this._data,c=b.words,d=b.sigBytes,e=this.blockSize,f=d/(4*e),f=a?da.ceil(f):da.max((f|0)-this._minBufferSize,0);a=f*e;d=da.min(4*a,d);if(a){for(var h=0;h<a;h+=e){this._doProcessBlock(c,h)}h=c.splice(0,a);b.sigBytes-=d}return new fa.init(h,d)}});qa.Hasher=cb.extend({reset:function(){cb.reset.call(this);this._doReset()},_createHmacHelper:function(a){return function(b,c){return(new xb.HMAC.init(a,c)).finalize(b)}},cfg:ea.extend(),blockSize:16,update:function(a){this._append(a);this._process();return this},_createHelper:function(a){return function(b,c){return(new a.init(c)).finalize(b)}},init:function(a){this.cfg=this.cfg.extend(a);this.reset()},finalize:function(a){a&&this._append(a);return this._doFinalize()}});var xb=pa.algo={};Ja=pa;for(var Y=Ja,ra=Math,sa=Y,R=sa.lib,yb=R.WordArray,ta=R.Hasher,R=sa.algo,db=[],eb=[],ua=2,ga=0;64>ga;){var W;a:{W=ua;for(var zb=ra.sqrt(W),La=2;La<=zb;La++){if(!(W%La)){W=!1;break a}}W=!0}W&&(8>ga&&(db[ga]=Ya(ra.pow(ua,0.5))),eb[ga]=Ya(ra.pow(ua,1/3)),ga++);ua++}var S=[],R=R.SHA256=ta.extend({clone:function(){var a=ta.clone.call(this);a._hash=this._hash.clone();return a},_doReset:function(){this._hash=new yb.init(db.slice(0))},_doFinalize:function(){var a=this._data,b=a.words,c=8*this._nDataBytes,d=8*a.sigBytes;b[d>>>5]|=128<<24-d%32;b[(d+64>>>9<<4)+14]=ra.floor(c/4294967296);b[(d+64>>>9<<4)+15]=c;a.sigBytes=4*b.length;this._process();return this._hash},_doProcessBlock:function(a,b){for(var c=this._hash.words,d=c[0],e=c[1],f=c[2],h=c[3],p=c[4],g=c[5],m=c[6],K=c[7],k=0;64>k;k++){if(16>k){S[k]=a[b+k]|0}else{var n=S[k-15],l=S[k-2];S[k]=((n<<25|n>>>7)^(n<<14|n>>>18)^n>>>3)+S[k-7]+((l<<15|l>>>17)^(l<<13|l>>>19)^l>>>10)+S[k-16]}n=K+((p<<26|p>>>6)^(p<<21|p>>>11)^(p<<7|p>>>25))+(p&g^~p&m)+eb[k]+S[k];l=((d<<30|d>>>2)^(d<<19|d>>>13)^(d<<10|d>>>22))+(d&e^d&f^e&f);K=m;m=g;g=p;p=h+n|0;h=f;f=e;e=d;d=n+l|0}c[0]=c[0]+d|0;c[1]=c[1]+e|0;c[2]=c[2]+f|0;c[3]=c[3]+h|0;c[4]=c[4]+p|0;c[5]=c[5]+g|0;c[6]=c[6]+m|0;c[7]=c[7]+K|0}});sa.SHA256=ta._createHelper(R);sa.HmacSHA256=ta._createHmacHelper(R);var fb=Y,Ab=fb.lib.WordArray;fb.enc.Base64={parse:function(a){var b=a.length,c=this._map,d=c.charAt(64);d&&(d=a.indexOf(d),-1!=d&&(b=d));for(var d=[],e=0,f=0;f<b;f++){if(f%4){var h=c.indexOf(a.charAt(f-1))<<f%4*2,p=c.indexOf(a.charAt(f))>>>6-f%4*2;d[e>>>2]|=(h|p)<<24-e%4*8;e++}}return Ab.create(d,e)},_map:"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_",stringify:function(a){var b=a.words,c=a.sigBytes,d=this._map;a.clamp();a=[];for(var e=0;e<c;e+=3){for(var f=(b[e>>>2]>>>24-e%4*8&255)<<16|(b[e+1>>>2]>>>24-(e+1)%4*8&255)<<8|b[e+2>>>2]>>>24-(e+2)%4*8&255,h=0;4>h&&e+0.75*h<c;h++){a.push(d.charAt(f>>>6*(3-h)&63))}}if(b=d.charAt(64)){for(;a.length%4;){a.push(b)}}return a.join("")}};function l(a,b){this.key=a;this.value=b}function launch(){var b="";var c="";a=[];a.push(new l("adblock","0"));a.push(new l("browserLanguage","en-US"));a.push(new l("cookieEnabled","1"));a.push(new l("custID","133"));a.push(new l("doNotTrack","unknown"));a.push(new l("flashVersion",0));a.push(new l("javaEnabled","0"));a.push(new l("jsFonts","8f58b1186770646318a429cb33977d8c"));a.push(new l("mimeTypes","52d67b2a5aa5e031084733d5006cc664"));a.push(new l("os","Win32"));a.push(new l("platform","WEB"));a.push(new l("plugins","d22ca0b81584fbea62237b14bd04c866"));a.push(new l("scrAvailSize","1040x1920"));a.push(new l("srcScreenSize","24xx1080x1920"));a.push(new l("storeDb","i1l1o1s1"));a.push(new l("timeZone",-8));a.push(new l("touchSupport","99115dfb07133750ba677d055874de87"));a.push(new l("userAgent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"));a.push(new l("webSmartID","fb25305a718e8032038c5a2905f60536"));a.sort(function(a,b){var c,d;if("object"===typeof a&&"object"===typeof b&&a&&b)return c=a.key,d=b.key,c===d?0:typeof c===typeof d?c<d?-1:1:typeof c<typeof d?-1:1;throw"error";});for(var d=0;d<a.length;d++){var e=a[d].key.replace(RegExp("%","gm"),""),f="",f="string"==typeof a[d].value?a[d].value.replace(RegExp("%","gm"),""):a[d].value;""!==f&&(c+=e+f,b+="\x26"+(void 0==hb[e]?e:hb[e])+"\x3d"+f)}a=ya(c);c=a.length;d="";a=d=0==a.length%2?a.substring(c/2,c)+a.substring(0,c/2):a.substring(c/2+1,c)+a.charAt(c/2)+a.substring(0,c/2);c="";for(d=a.length-1;0<=d;d--)c+=a.charAt(d);a=c;c=a.length;d=a.split("");for(e=0;e<parseInt(c/2);e++)0==e%2&&(f=a.charAt(e),d[e]=d[c-1-e],d[c-1-e]=f);a=d.join("");c=ya(a);c=ya(c);return new l(b,c)};
                """)
    else:
        ctx = execjs.compile("""
                var hb={online:"9vyE",appcodeName:"qT7b",browserLanguage:"q4f3",flashVersion:"dzuS",historyList:"kU5z",localStorage:"XM7l",systemLanguage:"e6OK",scrDeviceXDPI:"3jCe",cookieCode:"VySQ",scrWidth:"ssI5",browserVersion:"d435",hasLiedBrowser:"2xC5",cookieEnabled:"VPIf",indexedDb:"3sw-",scrHeight:"5Jwy",adblock:"FMQw",javaEnabled:"yD16",os:"hAqN",srcScreenSize:"tOHY",scrAvailSize:"TeRS",scrAvailWidth:"E-lJ",webSmartID:"E3gR",hasLiedResolution:"3neK",touchSupport:"wNLf",cpuClass:"Md7A",browserName:"-UVA",mimeTypes:"jp76",userLanguage:"hLzX",openDatabase:"V8vl",scrAvailHeight:"88tV",localCode:"lEnu",plugins:"ks0Q",userAgent:"0aew",storeDb:"Fvje",appMinorVersion:"qBVW",hasLiedOs:"ci5c",doNotTrack:"VEek",jsFonts:"EOQP",scrColorDepth:"qmyu",hasLiedLanguages:"j5po",sessionStorage:"HVia",timeZone:"q5aJ"};function ya(a){return Y.SHA256(a).toString(Y.enc.Base64)}function Ya(a){return 4294967296*(a-(a|0))|0}var da=Math,pa={},qa=pa.lib={},ab=function(){},ea=qa.Base={clone:function(){return this.init.prototype.extend(this)},mixIn:function(a){for(var b in a){a.hasOwnProperty(b)&&(this[b]=a[b])}a.hasOwnProperty("toString")&&(this.toString=a.toString)},create:function(){var a=this.extend();a.init.apply(a,arguments);return a},extend:function(a){ab.prototype=this;var b=new ab;a&&b.mixIn(a);b.hasOwnProperty("init")||(b.init=function(){b.$super.init.apply(this,arguments)});b.init.prototype=b;b.$super=this;return b},init:function(){}},fa=qa.WordArray=ea.extend({init:function(a,b){a=this.words=a||[];this.sigBytes=void 0!=b?b:4*a.length},random:function(a){for(var b=[],c=0;c<a;c+=4){b.push(4294967296*da.random()|0)}return new fa.init(b,a)},toString:function(a){return(a||vb).stringify(this)},concat:function(a){var b=this.words,c=a.words,d=this.sigBytes;a=a.sigBytes;this.clamp();if(d%4){for(var e=0;e<a;e++){b[d+e>>>2]|=(c[e>>>2]>>>24-e%4*8&255)<<24-(d+e)%4*8}}else{if(65535<c.length){for(e=0;e<a;e+=4){b[d+e>>>2]=c[e>>>2]}}else{b.push.apply(b,c)}}this.sigBytes+=a;return this},clone:function(){var a=ea.clone.call(this);a.words=this.words.slice(0);return a},clamp:function(){var a=this.words,b=this.sigBytes;a[b>>>2]&=4294967295<<32-b%4*8;a.length=da.ceil(b/4)}}),Ka=pa.enc={},vb=Ka.Hex={stringify:function(a){var b=a.words;a=a.sigBytes;for(var c=[],d=0;d<a;d++){var e=b[d>>>2]>>>24-d%4*8&255;c.push((e>>>4).toString(16));c.push((e&15).toString(16))}return c.join("")},parse:function(a){for(var b=a.length,c=[],d=0;d<b;d+=2){c[d>>>3]|=parseInt(a.substr(d,2),16)<<24-d%8*4}return new fa.init(c,b/2)}},bb=Ka.Latin1={stringify:function(a){var b=a.words;a=a.sigBytes;for(var c=[],d=0;d<a;d++){c.push(String.fromCharCode(b[d>>>2]>>>24-d%4*8&255))}return c.join("")},parse:function(a){for(var b=a.length,c=[],d=0;d<b;d++){c[d>>>2]|=(a.charCodeAt(d)&255)<<24-d%4*8}return new fa.init(c,b)}},wb=Ka.Utf8={stringify:function(a){try{return decodeURIComponent(escape(bb.stringify(a)))}catch(b){throw Error("Malformed UTF-8 data")}},parse:function(a){return bb.parse(unescape(encodeURIComponent(a)))}},cb=qa.BufferedBlockAlgorithm=ea.extend({_append:function(a){"string"==typeof a&&(a=wb.parse(a));this._data.concat(a);this._nDataBytes+=a.sigBytes},clone:function(){var a=ea.clone.call(this);a._data=this._data.clone();return a},_minBufferSize:0,reset:function(){this._data=new fa.init;this._nDataBytes=0},_process:function(a){var b=this._data,c=b.words,d=b.sigBytes,e=this.blockSize,f=d/(4*e),f=a?da.ceil(f):da.max((f|0)-this._minBufferSize,0);a=f*e;d=da.min(4*a,d);if(a){for(var h=0;h<a;h+=e){this._doProcessBlock(c,h)}h=c.splice(0,a);b.sigBytes-=d}return new fa.init(h,d)}});qa.Hasher=cb.extend({reset:function(){cb.reset.call(this);this._doReset()},_createHmacHelper:function(a){return function(b,c){return(new xb.HMAC.init(a,c)).finalize(b)}},cfg:ea.extend(),blockSize:16,update:function(a){this._append(a);this._process();return this},_createHelper:function(a){return function(b,c){return(new a.init(c)).finalize(b)}},init:function(a){this.cfg=this.cfg.extend(a);this.reset()},finalize:function(a){a&&this._append(a);return this._doFinalize()}});var xb=pa.algo={};Ja=pa;for(var Y=Ja,ra=Math,sa=Y,R=sa.lib,yb=R.WordArray,ta=R.Hasher,R=sa.algo,db=[],eb=[],ua=2,ga=0;64>ga;){var W;a:{W=ua;for(var zb=ra.sqrt(W),La=2;La<=zb;La++){if(!(W%La)){W=!1;break a}}W=!0}W&&(8>ga&&(db[ga]=Ya(ra.pow(ua,0.5))),eb[ga]=Ya(ra.pow(ua,1/3)),ga++);ua++}var S=[],R=R.SHA256=ta.extend({clone:function(){var a=ta.clone.call(this);a._hash=this._hash.clone();return a},_doReset:function(){this._hash=new yb.init(db.slice(0))},_doFinalize:function(){var a=this._data,b=a.words,c=8*this._nDataBytes,d=8*a.sigBytes;b[d>>>5]|=128<<24-d%32;b[(d+64>>>9<<4)+14]=ra.floor(c/4294967296);b[(d+64>>>9<<4)+15]=c;a.sigBytes=4*b.length;this._process();return this._hash},_doProcessBlock:function(a,b){for(var c=this._hash.words,d=c[0],e=c[1],f=c[2],h=c[3],p=c[4],g=c[5],m=c[6],K=c[7],k=0;64>k;k++){if(16>k){S[k]=a[b+k]|0}else{var n=S[k-15],l=S[k-2];S[k]=((n<<25|n>>>7)^(n<<14|n>>>18)^n>>>3)+S[k-7]+((l<<15|l>>>17)^(l<<13|l>>>19)^l>>>10)+S[k-16]}n=K+((p<<26|p>>>6)^(p<<21|p>>>11)^(p<<7|p>>>25))+(p&g^~p&m)+eb[k]+S[k];l=((d<<30|d>>>2)^(d<<19|d>>>13)^(d<<10|d>>>22))+(d&e^d&f^e&f);K=m;m=g;g=p;p=h+n|0;h=f;f=e;e=d;d=n+l|0}c[0]=c[0]+d|0;c[1]=c[1]+e|0;c[2]=c[2]+f|0;c[3]=c[3]+h|0;c[4]=c[4]+p|0;c[5]=c[5]+g|0;c[6]=c[6]+m|0;c[7]=c[7]+K|0}});sa.SHA256=ta._createHelper(R);sa.HmacSHA256=ta._createHmacHelper(R);var fb=Y,Ab=fb.lib.WordArray;fb.enc.Base64={parse:function(a){var b=a.length,c=this._map,d=c.charAt(64);d&&(d=a.indexOf(d),-1!=d&&(b=d));for(var d=[],e=0,f=0;f<b;f++){if(f%4){var h=c.indexOf(a.charAt(f-1))<<f%4*2,p=c.indexOf(a.charAt(f))>>>6-f%4*2;d[e>>>2]|=(h|p)<<24-e%4*8;e++}}return Ab.create(d,e)},_map:"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_",stringify:function(a){var b=a.words,c=a.sigBytes,d=this._map;a.clamp();a=[];for(var e=0;e<c;e+=3){for(var f=(b[e>>>2]>>>24-e%4*8&255)<<16|(b[e+1>>>2]>>>24-(e+1)%4*8&255)<<8|b[e+2>>>2]>>>24-(e+2)%4*8&255,h=0;4>h&&e+0.75*h<c;h++){a.push(d.charAt(f>>>6*(3-h)&63))}}if(b=d.charAt(64)){for(;a.length%4;){a.push(b)}}return a.join("")}};function l(a,b){this.key=a;this.value=b}function launch(){var b="";var c="";a=[];a.push(new l("adblock","0"));a.push(new l("browserLanguage","en-US"));a.push(new l("cookieEnabled","1"));a.push(new l("custID","133"));a.push(new l("doNotTrack","unknown"));a.push(new l("flashVersion",0));a.push(new l("javaEnabled","0"));a.push(new l("jsFonts","8f58b1186770646318a429cb33977d8c"));a.push(new l("mimeTypes","52d67b2a5aa5e031084733d5006cc664"));a.push(new l("os","Win32"));a.push(new l("platform","WEB"));a.push(new l("plugins","d22ca0b81584fbea62237b14bd04c866"));a.push(new l("scrAvailSize","1040x1920"));a.push(new l("srcScreenSize","24xx1080x1920"));a.push(new l("storeDb","i1l1o1s1"));a.push(new l("timeZone",-8));a.push(new l("touchSupport","99115dfb07133750ba677d055874de87"));a.push(new l("userAgent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"));a.push(new l("webSmartID","fb25305a718e8032038c5a2905f60536"));a.sort(function(a,b){var c,d;if("object"===typeof a&&"object"===typeof b&&a&&b)return c=a.key,d=b.key,c===d?0:typeof c===typeof d?c<d?-1:1:typeof c<typeof d?-1:1;throw"error";});for(var d=0;d<a.length;d++){var e=a[d].key.replace(RegExp("%","gm"),""),f="",f="string"==typeof a[d].value?a[d].value.replace(RegExp("%","gm"),""):a[d].value;""!==f&&(c+=e+f,b+="\x26"+(void 0==hb[e]?e:hb[e])+"\x3d"+f)}a=ya(c);c=a.length;d="";a=d=0==a.length%2?a.substring(c/2,c)+a.substring(0,c/2):a.substring(c/2+1,c)+a.charAt(c/2)+a.substring(0,c/2);c="";for(d=a.length-1;0<=d;d--)c+=a.charAt(d);a=c;c=a.length;d=a.split("");for(e=0;e<parseInt(c/2);e++)0==e%2&&(f=a.charAt(e),d[e]=d[c-1-e],d[c-1-e]=f);a=d.join("");c=ya(a);c=ya(c);return new l(b,c)};
                """)
        alg_id = 'rnFP89sRGr'

    res = ctx.call("launch")
    global advice_url
    advice_url = advice_url.format(alg_id, res['value'], res['key'], timestamp()).replace(' ', '%20')
    res = api.single_get(advice_url).text
    return json.loads(res[18:-2])


if __name__ == '__main__':
    print(generate_advice())
