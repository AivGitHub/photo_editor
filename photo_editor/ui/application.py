import os
from pathlib import Path

import wx
import gettext

import settings
from photo_editor.ui.ui import MainFrame


class Application(MainFrame):

    def __init__(self, parent, language='en') -> None:
        """

        TODO: Get settings from saved file.

        :param parent: parent class
        :param language: project language
        """
        super().__init__(parent)

        if not language:
            language = 'en'

        try:
            lang_translations = gettext.translation('base', localedir='locale', languages=[language])
        except FileNotFoundError:
            raise Exception(f'Language \'{language}\' not found!')

        self.current_instrument = {}
        self._project_saved = True
        self._cwd_directory = os.getcwd()
        self._home_directory = str(Path.home())
        self._action_history = []
        self.file_paths = []
        self.language = language
        self._ = lang_translations.gettext
        self.cursor_position = -1

        self.set_locale()
        self._set_instruments()
        self.set_main_menu()

    def set_main_menu(self) -> None:
        if not self._action_history:
            self.main_menubar_edit_undo.Enabled = False
            self.main_menubar_edit_redo.Enabled = False

    def set_instrument(self, event) -> None:

        event_object = event.GetEventObject()
        new_instrument_id = event_object.GetId()
        current_instrument_id = self.current_instrument.get('id')

        if current_instrument_id == new_instrument_id:
            return

        current_instrument = self.FindWindowById(current_instrument_id)
        current_instrument.Enable()
        event_object.Disable()

        self.current_instrument = {
            'id': new_instrument_id,
            'name': event_object.GetName(),
            'label': event_object.GetLabel()
        }

        self.Unbind(wx.EVT_PAINT)

        if self.current_instrument.get('id') == self.instrument_draw_brush.GetId():
            self.Bind(wx.EVT_PAINT, self.image_bitmap_on_paint)

    def _set_instruments(self) -> None:
        if not self.current_instrument:
            # New project
            self.current_instrument = {
                'id': self.instrument_draw_brush.GetId(),
                'name': self.instrument_draw_brush.GetName(),
                'label': self.instrument_draw_brush.GetLabel()
            }
            self.instrument_draw_brush.Disable()

            if self.file_paths:
                self.Bind(wx.EVT_PAINT, self.image_bitmap_on_paint)
        else:
            current_instrument = self.FindWindowById(self.current_instrument.get('id'))
            current_instrument.Disable()

    def set_locale(self) -> None:
        """ Sets locale to initial project

        TODO: set labels

        :return: None
        """
        # self.main_menubar_file.GetMenuItemCount() - 1
        self.main_menubar.SetMenuLabel(0, self._('File'))
        self.main_menubar.SetMenuLabel(1, self._('Edit'))
        self.main_menubar.SetMenuLabel(2, self._('Help'))

        self.main_menubar_file_new_project.SetItemLabel(self._('New project') + '\tCtrl+Shift+N')
        self.main_menubar_help_about.SetItemLabel(self._('About'))
        self.main_menubar_help_language_en.SetItemLabel(self._('English'))
        self.main_menubar_help_quit.SetItemLabel(self._('Quit') + '\tCtrl+Q')

    def set_new_project(self, event) -> None:
        file_dialog = wx.FileDialog(
            self,
            self._('Open image files'),
            self._home_directory,
            wx.EmptyString,
            f'Images file (*.bmp *.gif *.png *.jpg)|*.bmp;*.gif;*.png;*.jpg|'
            f'All files (*.*)|*.*',
            wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
        )

        if file_dialog.ShowModal() == wx.ID_CANCEL:
            return None

        self.file_paths = file_dialog.GetPaths()

        file_dialog.Destroy()
        self.add_image()

    def get_resized_image(self, image=None) -> wx.Image:
        if not image:
            image = wx.Image(self.file_paths[0], wx.BITMAP_TYPE_ANY)

        palette_size: wx.Size = self.panel_palette.GetSize()
        palette_ratio = palette_size.GetWidth() / palette_size.GetHeight()
        image_ratio = image.GetWidth() / image.GetHeight()
        scale_parameter = 0.9

        if palette_ratio > image_ratio:
            image_width = (image.GetWidth() * palette_size.GetHeight()) / image.GetHeight() * scale_parameter
            image_height = palette_size.GetHeight() * scale_parameter
        else:
            image_width = palette_size.GetWidth() * scale_parameter
            image_height = (image.GetHeight() * palette_size.GetWidth()) / image.GetWidth() * scale_parameter

        image = image.Rescale(image_width, image_height)

        return image

    def image_bitmap_on_paint(self, event) -> None:
        dc = wx.PaintDC(self)
        brush = wx.Brush("black")
        dc.SetBackground(brush)
        dc.Clear()

        del dc

    def image_bitmap_on_left_down(self, event) -> None:
        print(self.panel_palette.GetScreenPosition())

    def image_bitmap_on_left_up(self, event) -> None:
        print(self.panel_palette.GetScreenPosition())

    def image_bitmap_on_mouse_wheel(self, event) -> None:
        print(event)

    def panel_palette_resize_palette(self, event) -> None:
        """ Resize palette when window resized.

        TODO: think if image should be resized but not palette.

        :param event: clicked event
        :return: None
        """

        if not self.file_paths:
            return

        image = self.get_resized_image()
        self.image_bitmap.SetBitmap(wx.Bitmap(image))
        # self.panel_palette.Refresh()

        del image

    def add_image(self) -> None:
        """ Method adds image to palette.

        TODO: open all images as layers

        :return: None
        """

        image = wx.Image(self.file_paths[0], wx.BITMAP_TYPE_ANY)
        image = self.get_resized_image(image=image)

        self.image_bitmap.SetBitmap(wx.Bitmap(image))

        del image

    def undo_action(self, event) -> None:
        if not self._action_history:
            event.GetEventObject.Disable()

    def redo_action(self, event) -> None:
        if not self._action_history:
            event.GetEventObject.Disable()

    def show_about(self, event) -> None:
        wx.MessageBox(
            self._(f'Photo editor {settings.PROJECT_NAME}, version: {settings.PROJECT_VERSION}.')
        )

    def quit(self, event) -> None:
        self.on_close(event)

    def on_close(self, event) -> None:

        if wx.MessageBox(self._('Are you sure you want to exit?'), self._('Please confirm'),
                         wx.ICON_QUESTION | wx.YES_NO) != wx.YES:
            return None

        self.Destroy()

        return None
