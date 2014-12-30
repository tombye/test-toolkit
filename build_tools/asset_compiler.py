import os
import sass

class AssetCompiler(object):
  def __init__(self):
    self.repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    self.sass_src_root = os.path.join(self.repo_root, "sass")
    self.sass_dest_root = os.path.join(self.repo_root, "stylesheets")

  def compile_file(self, src_path_abs):
    dest_path_abs = src_path_abs.replace(self.sass_src_root, self.sass_dest_root)
    dest_path_abs = self.__change_extension_to(dest_path_abs, "css")
    result = sass.compile(filename=src_path_abs, output_style="nested")
    open(dest_path_abs, "w+").write(result)

  def compile(self):
    for root, dirs, files in os.walk(self.sass_src_root):
      for dir in dirs:
        dest_dir = os.path.join(self.sass_dest_root, dir)
        if os.path.isdir(dest_dir) is False:
          os.mkdir(dest_dir)

      for file in files:
        self.compile_file(os.path.join(root, file))

  def __change_extension_to(self, file, new_extension):
    filename, extension = os.path.splitext(file)
    return filename + "." + new_extension

if __name__ == "__main__":
  asset_compiler = AssetCompiler()
  asset_compiler.compile()
