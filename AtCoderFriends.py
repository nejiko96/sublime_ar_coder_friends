import sublime
import sublime_plugin

import os

class AtCoderCommand(sublime_plugin.WindowCommand):
  def run_on_file(self, af_cmd):
    if self.window.active_view() and self.window.active_view().file_name():
      path = self.window.active_view().file_name()
    else:
      sublime.error_message('AtCoderFriends: No file is opened')
      return
    args = ['at_coder_friends', af_cmd, path]
    self.window.run_command('exec', {
      'cmd': args,
      'shell': True
    })

class AtCoderFriendsSetupCommand(sublime_plugin.WindowCommand):
  def run(self):
    if self.window.folders():
      self.dir = self.window.folders()[0]
    else:
      sublime.error_message('AtCoderFriends: No folder is opened')
      return
    self.window.show_input_panel(
      'Contest Name:', '', self.on_done, None, None
    )

  def on_done(self, contest):
    if contest == '':
      return
    path = os.path.join(self.dir, contest)
    args = ['at_coder_friends', 'setup', path]
    self.window.run_command('exec', {
      'cmd': args,
      'shell': True
    })

class AtCoderFriendsTestOneCommand(AtCoderCommand):
  def run(self):
    self.run_on_file('test-one')

class AtCoderFriendsTestAllCommand(AtCoderCommand):
  def run(self):
    self.run_on_file('test-all')

class AtCoderFriendsSubmitCommand(AtCoderCommand):
  def run(self):
    self.run_on_file('submit')
