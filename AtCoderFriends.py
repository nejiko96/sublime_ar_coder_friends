import sublime
import sublime_plugin
from functools import partial
import os
import subprocess

class AtCoderCommand(sublime_plugin.WindowCommand):
  def get_file(self):
    return self.window.active_view().file_name()


class AtCoderFriendsSetupCommand(sublime_plugin.WindowCommand):
  def run(self):
    if self.window.folders():
      dir = self.window.folders()[0]
    else:
      sublime.error_message('AtCoderFriends: No folder for the new contest')
      return False
    self.window.show_input_panel(
      'Contest Name:', '', partial(self.on_done, dir), None, None
    )

  def on_done(self, dir, contest):
    if contest == "":
      return False
    path = os.path.join(dir, contest)
    args = ['at_coder_friends', 'setup', path]
    # print(args)
    subprocess.call(args)


class AtCoderFriendsTestOneCommand(AtCoderCommand):
  def run(self):
    print(self.get_file())


class AtCoderFriendsTestAllCommand(AtCoderCommand):
  def run(self):
    print(self.paths[0])


class AtCoderFriendsSubmitCommand(AtCoderCommand):
  def run(self, paths=[], parameters=None):
    print(self.paths[0])
