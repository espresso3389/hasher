import string
import sublime
import sublime_plugin
import hashlib
import urllib
import time
import base64

# test

class Md5Command(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():
			if s.empty():
				s = self.view.word(s)

			selected = self.view.substr(s)
			m = hashlib.md5()
			m.update(selected)
			txt = m.hexdigest()
			self.view.replace(edit, s, txt)

class Sha1Command(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():
			if s.empty():
				s = self.view.word(s)

			selected = self.view.substr(s)
			m = hashlib.sha1()
			m.update(selected)
			txt = m.hexdigest()
			self.view.replace(edit, s, txt)

class Base64EncodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():
			if s.empty():
				s = self.view.word(s)

			selected = self.view.substr(s)
			txt = base64.b64encode(selected)
			self.view.replace(edit, s, txt)
			
class Base64DecodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():
			if s.empty():
				s = self.view.word(s)

			selected = self.view.substr(s)
			txt = base64.b64decode(selected)
			self.view.replace(edit, s, txt)

class UrlEncodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():
			if s.empty():
				s = self.view.word(s)

			selected = self.view.substr(s)
			txt = urllib.quote(selected.encode('utf8'))
			self.view.replace(edit, s, txt)

class UrlDecodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():
			if s.empty():
				s = self.view.word(s)

			selected = self.view.substr(s)
			txt = urllib.unquote(selected.encode('utf8'))
			txt = unicode(txt.decode('utf8'));
			self.view.replace(edit, s, txt);

class CurrentUnixTimestamp(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():

			txt = time.asctime(time.gmtime())
			txt = time.ctime()
			txt = "%.0f" % round(time.time(), 3)
			self.view.replace(edit, s, txt)