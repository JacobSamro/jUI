#!/usr/bin/env python

# jUI.py
#
# Copyright (C) 2015 Jacob Samro, Dhinakaran
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from gi.repository import Gtk,Gdk

class jUI():

    def __init__(self):
        css = Gtk.CssProvider()
        css.load_from_path('jUIStyleLibrary.css')
        screen = Gdk.Screen.get_default()
        styleContext = Gtk.StyleContext()
        styleContext.add_provider_for_screen(screen, css,
                                             Gtk.STYLE_PROVIDER_PRIORITY_USER)

    def Button(self,label):

        button = Gtk.Button.new_with_label(label)
        return button

    def ToggleButton(self,label):
        return Gtk.ToggleButton(label)

    def LinkButton(self,label,link):
        return Gtk.LinkButton(link, label)

class Button():
    """Button"""
    def __init__(self, label):
        css = Gtk.CssProvider()
        css.load_from_path('jUIStyleLibrary.css')
        screen = Gdk.Screen.get_default()
        styleContext = Gtk.StyleContext()
        styleContext.add_provider_for_screen(screen, css,
                                             Gtk.STYLE_PROVIDER_PRIORITY_USER)
        button = Gtk.Button.new_with_label(label)
        
