from jUI import *


class DemoApp(Window):

    def __init__(self):

        Window.__init__(self, title="Button Demo")
        self.set_border_width(10)

        hbox = Box(spacing=6)
        self.add(hbox)

        button = jUI().Button("Hello")
        button.connect("clicked", self.on_click_me_clicked)
        hbox.pack_start(button, True, True, 0)

        button = jUI().ToggleButton("Toggle")
        hbox.pack_start(button, True, True, 0)

        button = jUI().LinkButton("Google","http://google.com")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)

        

        self.progressbar = ProgressBar()
        hbox.pack_start(self.progressbar, True, True, 0)

        self.timeout_id = GObject.timeout_add(50, self.on_timeout, None)
        self.activity_mode = False

    def on_show_text_toggled(self, button):
        show_text = button.get_active()
        if show_text:
            text = "some text"
        else:
            text = None
        self.progressbar.set_text(text)
        self.progressbar.set_show_text(show_text)

    def on_activity_mode_toggled(self, button):
        self.activity_mode = button.get_active()
        if self.activity_mode:
            self.progressbar.pulse()
        else:
            self.progressbar.set_fraction(0.0)

    def on_right_to_left_toggled(self, button):
        value = button.get_active()
        self.progressbar.set_inverted(value)

    def on_timeout(self, user_data):
        """
        Update value on the progress bar
        """
        if self.activity_mode:
            self.progressbar.pulse()
        else:
            new_value = self.progressbar.get_fraction() + 0.01

            if new_value > 1:
                new_value = 0

            self.progressbar.set_fraction(new_value)

        # As this is a timeout function, return True so that it
        # continues to get called
        return True

    def on_click_me_clicked(self, button):
        print("\"Click me\" button was clicked")

    def on_open_clicked(self, button):
        print("\"Open\" button was clicked")

    def on_close_clicked(self, button):
        print("Closing application")
        Gtk.main_quit()

win = DemoApp()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()