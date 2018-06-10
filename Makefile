default: public/index.html public/dubliners.css public/dubliners.js public/vendor/jquery-2.1.4.min.js

valid:
	xmllint --dtdvalid schema/tei_all.dtd --xinclude header.xml --noout

chars.txt:
	ag --nofilename -o "(?<=<said who=\")[\w\'\. ]*" *.xml | sort | uniq > $@

public/index.html: stylesheets/dubliners.xsl header.xml
	xsltproc --xinclude $^ > $@

public/dubliners.css:
		cp stylesheets/dubliners.css $@

public/dubliners.js:
	cp dubliners.js $@

public/vendor/jquery-2.1.4.min.js:
	cp vendor/jquery-2.1.4.min.js $@
