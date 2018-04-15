import sublime
import sublime_plugin

import os

class AtCoderFriendsCommand(sublime_plugin.WindowCommand):
  def run_af_on_file(self, af_cmd):
    if self.window.active_view() and self.window.active_view().file_name():
      path = self.window.active_view().file_name()
    else:
      sublime.error_message('AtCoderFriends: No file is opened')
      return
    self.run_af(af_cmd, path)

  def run_af(self, af_cmd, path, work_dir=None):
    args = ['at_coder_friends', af_cmd, path]
    if not work_dir:
      work_dir =  os.path.dirname(path)
    self.window.run_command('exec', {
      'cmd': ' '.join(args),
      'working_dir': work_dir,
      'shell': True
    })


class AtCoderFriendsSetupCommand(AtCoderFriendsCommand):
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
    self.run_af('setup', path, work_dir=self.dir)

class AtCoderFriendsTestOneCommand(AtCoderFriendsCommand):
  def run(self):
    self.run_af_on_file('test-one')

class AtCoderFriendsTestAllCommand(AtCoderFriendsCommand):
  def run(self):
    self.run_af_on_file('test-all')

class AtCoderFriendsSubmitCommand(AtCoderFriendsCommand):
  def run(self):
    self.run_af_on_file('submit')
