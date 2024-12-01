from flask import Flask, render_template
import webview

from educard.api import API
from educard.server import server
    
def on_start(window):
    ''''''
    #window.toggle_fullscreen() 
    #window.evaluate_js('alert("Nice one!");')
    

class Tester:
    def doSomething(self):
        print('something done')

api=API()
window = webview.create_window('EduCard', server, js_api=api, confirm_close=False)
api._window=window
api.tester = Tester()
webview.start(on_start, window)