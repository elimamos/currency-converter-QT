import gi
import urllib.request
import json
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

currencies = []


class Handler:
        def onDestroy(self, *args):
            Gtk.main_quit()

        def onButtonPressed(self, button):
            print("Hello World!")


builder = Gtk.Builder()
builder.add_from_file("mainwindow.glade")
builder.connect_signals(Handler())

window = builder.get_object("MainWindow")
window.show_all()

Gtk.main()