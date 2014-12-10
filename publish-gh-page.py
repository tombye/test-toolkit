import os

class StyleguidePublisher():
  "publish a styleguide for the toolkit"

  GIT_URL = "git@github.com:tombye/test-toolkit.git"

  def __init__(self):
    self["version"] = self.getVersion()
    self["repo_root"] = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

  def getVersion():
    version_file = os.path.join(self["repo_root"], "VERSION.txt")
    version = open(version_file, 'r')
    return version
