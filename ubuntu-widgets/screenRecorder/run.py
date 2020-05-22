import models as m
import gi
from multiprocessing import Process
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk,Gdk

class Recorder(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="CRecorder")
        widget = Gtk.DrawingArea()
        widget.show()
        self.add(widget)
        col =Gdk.Color(red=60000,blue=60000,green=60000)
        self.present()
        self.modify_bg(Gtk.StateType.NORMAL, col)
        self.select_Area_bt=Gtk.Button(label="Set Area")
        self.record_bt=Gtk.Button(label="Record")
        self.take_screen_shot=Gtk.Button(label="ScreenShot")
        self.save=Gtk.Button(label='Save')
        grid=Gtk.Grid()
        self.add(grid)
        grid.add(self.record_bt)



def main():
    win=Recorder()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()