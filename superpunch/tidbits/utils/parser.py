from lxml import html as lxml_html


class MetaTagParser(object):

    def __init__(self, html, *args, **kwargs):
        self.html = html
        self.tree = lxml_html.fromstring(html)

    def run(self, *args, **kwargs):
        """Returns a parsed meta tags as dict."""

        result = dict()
        result['title'] = self._parse_title()
        result['description'] = self._parse_description()
        result['keywords'] = self._parse_keywords()
        result['image_url'] = self._parse_image_url()

        return result

    def _parse_title(self):
        title_elements = self.tree.cssselect("meta[property='og:title']")

        # If meta[og:title] is not available
        if not title_elements:
            title_elements = self.tree.cssselect('title')
            title_element = title_elements[0]
            title_text = title_element.text

        title_element = title_elements[0]
        title_text = title_element.get('content')

        return title_text or str()

    def _parse_description(self):
        description_elements = self.tree.cssselect("meta[property='og:description']") or\
            self.tree.cssselect("meta[property='description']")
        if description_elements:
            description_element = description_elements[0]
            description_text = description_element.get('content')
            return description_text
        return str()

    def _parse_keywords(self):
        keywords_elements = self.tree.cssselect("meta[property='keywords']")
        if keywords_elements:
            keywords_element = keywords_elements[0]
            keywords_text = keywords_element.get('content')
            return keywords_text
        return str()

    def _parse_image_url(self):
        image_url_elements = self.tree.cssselect("meta[property='og:image']")
        if image_url_elements:
            image_url_element = image_url_elements[0]
            image_url_text = image_url_element.get('content')
            return image_url_text
        return str()
