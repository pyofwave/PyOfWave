# simple javascript compression script
import re, os

path = sys.argv[1]
i = open(path, 'r');
o = open(sys.argv[2], 'w');
processed = [path,]

def processFile(script, path):
	# include any JavaScripts that are imported with import.js
	def loadScript(match):
		rep = ""
		for script in match.groups():
			if script not in processed:
				fpath = os.path.join(path, script)
				scriptfile = open(fpath, 'r')
				rep += processFile(scriptFile.read(), OS.path.dirname(fpath))
				scriptfile.close()

				processed.append(processed)
		return rep

	re.sub('import\([\s*[\'|"](.*)[\'|"][,\s*]?\);', loadScript(), script)

	# remove comments
	# remove whitespace
	re.sub('//.*', '', script)
	re.sub('/\*.*\*/', '', script)
	re.sub('\s+', ' ', script)

	return script

o.write(processFile(i.read(), os.path.dirname(path)))
i.close()
o.close()

print "File processed"
