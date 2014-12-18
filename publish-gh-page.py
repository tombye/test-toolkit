import os
import pystache
from template_handler import TemplateHandler 

class Styleguide_publisher(object):
  "publish a styleguide for the toolkit"

  GIT_URL = "git@github.com:tombye/test-toolkit.git"

  pages = []

  def __init__(self):
    self.repo_root_rel = os.path.dirname(__file__)
    self.repo_root_abs = os.path.dirname(__file__)
    self.pages_dirname = "data"
    self.pages_dir = os.path.join(self.repo_root_rel, self.pages_dirname)
    self.template_dir = self.get_template_folder()
    self.template_view = self.get_template_view()
    self.render_pages()

  def get_template_folder(self):
    template_handler = TemplateHandler()
    if template_handler.needs_update():
      template_handler.update_template()
    return template_handler.get_folder()

  def get_template_view(self):
    return open(os.path.join(self.template_dir, "views/layouts/govuk_template.html"), "r").read()
    
  def render_pages(self):
    for root, dirs, files in os.walk(self.pages_dir):
      for dir in dirs:
        pages_dir = self.__get_pages_dir(dir)
        if os.path.isdir(pages_dir) is False:
          os.mkdir(pages_dir)

      for file in files:
        if self.__is_html(file):
          self.render_page(os.path.join(root, file))

  def render_page(self, filename):
    partial = open(filename, "r").read()
    page_render = pystache.render(self.template_view, { "content" : partial })
    page_filename = os.path.join(self.repo_root_abs, filename.replace(self.pages_dirname + "/", ""))
    print "creating " + page_filename + " file"
    open(page_filename, "w+").write(page_render)

  def __get_pages_dir(self, file):
    return file.replace(self.pages_dirname + "/", "")

  def __is_html(self, file):
    filename, extension = os.path.splitext(file)
    return extension == ".html"

if __name__ == "__main__":
  styleguide_publisher = Styleguide_publisher()
