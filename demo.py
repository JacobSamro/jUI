from jUI import *


class DemoApp(Window):

    def __init__(self):
        Window.__init__(self)
        jUI().UiInit(Window,self)

        self.set_decorated(True)
        self.set_border_width(10)


        hbox = Gtk.Box(spacing=6)

        self.add(hbox)

        button = jUI().Button("Hello")
        button.connect("clicked", self.on_click_me_clicked)
        hbox.pack_start(button, True, True, 0)

        button = jUI().ToggleButton("Toggle")
        hbox.pack_start(button, True, True, 0)

        button = jUI().LinkButton("Google","http://google.com")
        button.connect("clicked", self.on_click_me_clicked)
        hbox.pack_start(button, True, True, 0)
        

        self.progressbar = ProgressBar()
        hbox.pack_start(self.progressbar, True, True, 0)

        self.timeout_id = GObject.timeout_add(50, self.on_timeout, None)
        self.activity_mode = False


    def im_pressed(self,button):
        print("I' clicked")


    def on_timeout(self, user_data):

        if self.activity_mode:
            self.progressbar.pulse()
        else:
            new_value = self.progressbar.get_fraction() + 0.01

            if new_value > 1:
                new_value = 0

            self.progressbar.set_fraction(new_value)

        return True

    def on_click_me_clicked(self, button):
        print("\"Click me\" button was clicked")

    def on_open_clicked(self, button):
        print("\"Open\" button was clicked")


win = DemoApp()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()