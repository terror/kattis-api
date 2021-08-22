from bs4 import BeautifulSoup

class Utils:
  @staticmethod
  def html_page(page):
    """
        Returns a BS object from a requests
        page.text

        :param page: request page
        """
    return BeautifulSoup(page.text, "html.parser")
