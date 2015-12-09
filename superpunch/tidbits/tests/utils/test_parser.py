from django.test import TestCase

from tidbits.utils.parser import MetaTagParser

import requests


class MetaTagParserTestCase(TestCase):

    def setUp(self):
        # FIXME: Should refactor with Mock.
        # Tests with a article published on PPSS.

        response = requests.get("http://ppss.kr/archives/55616")
        self.parser = MetaTagParser(response.text)

    def test_parse_title(self):
        parsed_title = self.parser._parse_title()

        self.assertTrue(self.parser._parse_title())
        self.assertEqual(
            parsed_title,
            "읽지 않겠는가? ㅍㅍㅅㅅ 8월 BEST",
        )

    def test_parse_description(self):
        parsed_description = self.parser._parse_description()

        self.assertTrue(parsed_description)
        self.assertIn(
            "1. 가장 많이 본 기사",
            parsed_description,
        )

    def test_parse_keywords(self):
        parsed_keywords = self.parser._parse_keywords()

        # self.assertTrue(parsed_keywords)
        self.assertEqual(
            parsed_keywords,
            "",
        )

    def test_parse_image_url(self):
        parsed_image_url = self.parser._parse_image_url()

        self.assertTrue(parsed_image_url)
        self.assertEqual(
            parsed_image_url,
            "http://ppss.kr/wp-content/uploads/2015/07/TITLE_BEST.jpg",
        )
