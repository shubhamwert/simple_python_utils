	
from multiprocessing import Process
import gi
import pyperclip
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk,Gdk




class Clip(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Clipboard Example")
        self.resize(500, 500)
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
        hbox.set_homogeneous(False)
        self.notes_box=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL ,spacing=10)
        self.notes_box.set_homogeneous(False)
        self.notes=Gtk.Label("hello")
        self.notes.set_text("YOUR COPIED TEXT WILL APPEAR HERE\n")
        hbox.pack_start(self.notes_box, True, True, 0)
        self.notes_box.pack_start(self.notes,True,True,0)
        self.add(hbox)
        button = Gtk.Button.new_with_label("Clear")
        button.connect("clicked", self.clear)
        hbox.pack_start(button, False, False, 0)
        widget = Gtk.DrawingArea()
        widget.show()
        self.add(widget)
        col =Gdk.Color(red=10000,blue=30000,green=40000)
        self.present()
        self.modify_bg(Gtk.StateType.NORMAL, col)
        self.current_text=''
        self.Listener=Process(target=self.wait_for_paste)
        self.Listener.start()
        self.old_text=''
    def clear(self,button):
        self.old_text=''
        self.current_text=''

        self.notes.set_text("TEXT RESET")
        print('done')
    def wait_for_paste(self):
        while True:
            self.current_text=self.current_text+' '+str(Gtk.Clipboard().wait_for_text())
            if self.old_text==self.current_text:
                self.old_text=self.current_text
                
                self.notes.set_text(self.current_text)


win = Clip()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()