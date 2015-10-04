#!/usr/bin/env python

# jUI.py
#
# Copyright (C) 2015 Jacob Samro, Dhinakaran, JJ & Bagla
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


from gi.repository import Gtk, Gdk, GObject, Gio

Window      =   Gtk.Window
Box         =   Gtk.Box
ProgressBar =   Gtk.ProgressBar
Spinner     =   Gtk.Spinner



class jUI:    
    __Window    =   ""
    __Self      =   ""

    def __init__(self):
        pass
        css = Gtk.CssProvider()
        css.load_from_path('core/styleLib/jUIStyleLibrary.css')
        screen = Gdk.Screen.get_default()
        styleContext = Gtk.StyleContext()
        styleContext.add_provider_for_screen(screen, css,
                                             Gtk.STYLE_PROVIDER_PRIORITY_USER)


    def Button(self,label):
        return Gtk.Button.new_with_label(label)

    def ToggleButton(self,label):
        return Gtk.ToggleButton(label)

    def LinkButton(self,label,link):
        return Gtk.LinkButton(link, label)

    def UiInit(self,win,s):
        self.__Window   = win
        self.__Self     = s
        hb = Gtk.HeaderBar()
        hb.set_show_close_button(False)
        hb.props.title = win.get_title(s)
        s.set_titlebar(hb)

        buttonMin = Gtk.Button()
        #buttonMin.connect("clicked", self.minimize)
        image = Gtk.Image()
        image.set_from_file("core/icons/minimize.png")
        buttonMin.add(image)
        hb.pack_end(buttonMin)

        buttonMax = Gtk.Button()
        buttonMax.connect("clicked", self.maximize)
        image = Gtk.Image()
        image.set_from_file("core/icons/maximize.png")
        buttonMax.add(image)
        hb.pack_end(buttonMax)

        buttonClose = Gtk.Button()
        buttonClose.connect("clicked", Gtk.main_quit)
        image = Gtk.Image()
        image.set_from_file("core/icons/close.png")
        buttonClose.add(image)
        hb.pack_end(buttonClose)
        

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")

        hb.pack_start(box)

    def getWindow(self):
        return self.__Window

    def getSelf(self):
        return self.__Self

    def getSelfOrigin(self):
        return self;

    def maximize(ins,win):
        print(ins)
        print(win)
        win.connect('window-state-event', win.maximize)
        ins.getWindow().maximize(ins.getSelf())
        

    def maxMinHandler(self,win,event):
        print 'connected'
        if event.changed_mask & Gtk.gdk.WINDOW_STATE_ICONIFIED:
            if event.new_window_state & Gtk.gdk.WINDOW_STATE_ICONIFIED:
                print 'Window was minimized!'
            else:
                print 'Window was unminimized!'




