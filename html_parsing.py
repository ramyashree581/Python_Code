from HTMLParser import HTMLParser
# print dir(HTMLParser)

class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):  #overriding the handle_starttag with the args
		print "Start Tag Found :", tag
		for attr in attrs:
			print " attr:", attrs

	def handle_endtag(self, tag):
		print "End Tag Found :", tag
	def handle_data(self, data):
		print "Data found :", data
	def handle_comment(self, data):
		print "Comments are :", data		

parse = MyHTMLParser()
# parse.feed('<html><head><title>Test</title></head>'
            # '<body><h1>Parse me!</h1></body></html>')
parse.feed(""" <html>
<head>Heading</head>
<body attr1='val1'>
    <div class='container'>
        <div id='class'>Something here</div>
        <div>Something else</div>
    </div>
</body>
</html>""")

