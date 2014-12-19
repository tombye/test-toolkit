import sass

class AssetCompiler(object):
  def __init__(self):
    self.repo_root = os.path.abspath(os.path.dirname(__file__))
    self.sass_src = os.path.join(self.repo_root, "/assets/sass")
    self.sass_dest = os.path.join(self.repo_root, "/assets/stylesheets")

  def compile(self):
    
