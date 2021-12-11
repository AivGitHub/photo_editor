import argparse

import wx

from photo_editor.ui.application import Application


def run():
    parser = argparse.ArgumentParser(description='Personal information')
    parser.add_argument('--language', dest='language', type=str, help='Language of the project')
    args = parser.parse_args()

    app = wx.App(False)
    frame = Application(None, language=args.language)
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    run()
