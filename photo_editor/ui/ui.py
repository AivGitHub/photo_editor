# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Koldbox", pos = wx.DefaultPosition, size = wx.Size( 600,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		boxsizer_main = wx.BoxSizer( wx.HORIZONTAL )

		self.panel_instruments = wx.Panel( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( 150,-1 ), wx.TAB_TRAVERSAL )
		self.panel_instruments.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.panel_instruments.SetMaxSize( wx.Size( 120,-1 ) )

		boxsizer_panel = wx.BoxSizer( wx.HORIZONTAL )

		self.instrument_draw_brush = wx.Button( self.panel_instruments, wx.ID_ANY, u"Brush", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		boxsizer_panel.Add( self.instrument_draw_brush, 0, wx.ALL, 5 )

		self.instrument_draw_eraser = wx.Button( self.panel_instruments, wx.ID_ANY, u"Eraser", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		boxsizer_panel.Add( self.instrument_draw_eraser, 0, wx.ALL, 5 )


		self.panel_instruments.SetSizer( boxsizer_panel )
		self.panel_instruments.Layout()
		boxsizer_main.Add( self.panel_instruments, 1, wx.EXPAND |wx.ALL, 5 )

		self.panel_palette = wx.Panel( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.DefaultSize, wx.TAB_TRAVERSAL )
		boxsizer_palette = wx.BoxSizer( wx.VERTICAL )

		self.image_bitmap = wx.StaticBitmap( self.panel_palette, wx.ID_ANY, wx.NullBitmap, wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		boxsizer_palette.Add( self.image_bitmap, 0, wx.ALL, 5 )


		self.panel_palette.SetSizer( boxsizer_palette )
		self.panel_palette.Layout()
		boxsizer_palette.Fit( self.panel_palette )
		boxsizer_main.Add( self.panel_palette, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( boxsizer_main )
		self.Layout()
		self.main_menubar = wx.MenuBar( 0 )
		self.main_menubar_file = wx.Menu()
		self.main_menubar_file_new_project = wx.MenuItem( self.main_menubar_file, wx.ID_ANY, u"New project", wx.EmptyString, wx.ITEM_NORMAL )
		self.main_menubar_file.Append( self.main_menubar_file_new_project )

		self.main_menubar.Append( self.main_menubar_file, u"File" )

		self.main_menubar_edit = wx.Menu()
		self.main_menubar_edit_undo = wx.MenuItem( self.main_menubar_edit, wx.ID_ANY, u"Undo"+ u"\t" + u"Ctrl+Z", wx.EmptyString, wx.ITEM_NORMAL )
		self.main_menubar_edit.Append( self.main_menubar_edit_undo )

		self.main_menubar_edit_redo = wx.MenuItem( self.main_menubar_edit, wx.ID_ANY, u"Redo"+ u"\t" + u"Ctrl+Shift+Z", wx.EmptyString, wx.ITEM_NORMAL )
		self.main_menubar_edit.Append( self.main_menubar_edit_redo )

		self.main_menubar.Append( self.main_menubar_edit, u"Edit" )

		self.main_menubar_help = wx.Menu()
		self.main_menubar_help_about = wx.MenuItem( self.main_menubar_help, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.main_menubar_help.Append( self.main_menubar_help_about )

		self.main_menubar_help_language = wx.Menu()
		self.main_menubar_help_language_en = wx.MenuItem( self.main_menubar_help_language, wx.ID_ANY, u"English", wx.EmptyString, wx.ITEM_NORMAL )
		self.main_menubar_help_language.Append( self.main_menubar_help_language_en )
		self.main_menubar_help_language_en.Enable( False )

		self.main_menubar_help.AppendSubMenu( self.main_menubar_help_language, u"Language" )

		self.main_menubar_help_quit = wx.MenuItem( self.main_menubar_help, wx.ID_ANY, u"Quit"+ u"\t" + u"Ctrl+Q", wx.EmptyString, wx.ITEM_NORMAL )
		self.main_menubar_help.Append( self.main_menubar_help_quit )

		self.main_menubar.Append( self.main_menubar_help, u"Help" )

		self.SetMenuBar( self.main_menubar )

		self.main_statusbar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.on_close )
		self.instrument_draw_brush.Bind( wx.EVT_BUTTON, self.set_instrument )
		self.instrument_draw_eraser.Bind( wx.EVT_BUTTON, self.set_instrument )
		self.panel_palette.Bind( wx.EVT_SIZE, self.panel_palette_resize_palette )
		self.image_bitmap.Bind( wx.EVT_LEFT_DOWN, self.image_bitmap_on_left_down )
		self.image_bitmap.Bind( wx.EVT_LEFT_UP, self.image_bitmap_on_left_up )
		self.image_bitmap.Bind( wx.EVT_MOUSEWHEEL, self.image_bitmap_on_mouse_wheel )
		self.image_bitmap.Bind( wx.EVT_PAINT, self.image_bitmap_on_paint )
		self.Bind( wx.EVT_MENU, self.set_new_project, id = self.main_menubar_file_new_project.GetId() )
		self.Bind( wx.EVT_MENU, self.edit_action, id = self.main_menubar_edit_undo.GetId() )
		self.Bind( wx.EVT_MENU, self.redo_action, id = self.main_menubar_edit_redo.GetId() )
		self.Bind( wx.EVT_MENU, self.show_about, id = self.main_menubar_help_about.GetId() )
		self.Bind( wx.EVT_MENU, self.quit, id = self.main_menubar_help_quit.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def on_close( self, event ):
		event.Skip()

	def set_instrument( self, event ):
		event.Skip()


	def panel_palette_resize_palette( self, event ):
		event.Skip()

	def image_bitmap_on_left_down( self, event ):
		event.Skip()

	def image_bitmap_on_left_up( self, event ):
		event.Skip()

	def image_bitmap_on_mouse_wheel( self, event ):
		event.Skip()

	def image_bitmap_on_paint( self, event ):
		event.Skip()

	def set_new_project( self, event ):
		event.Skip()

	def edit_action( self, event ):
		event.Skip()

	def redo_action( self, event ):
		event.Skip()

	def show_about( self, event ):
		event.Skip()

	def quit( self, event ):
		event.Skip()


