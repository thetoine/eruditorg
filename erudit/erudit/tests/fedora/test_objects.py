# -*- coding: utf-8 -*-

import unittest.mock

from django.test import TestCase

from erudit.fedora.objects import ArticleDigitalObject
from erudit.fedora.repository import api


class TestArticleDigitalObject(TestCase):
    @unittest.mock.patch.object(ArticleDigitalObject, 'erudit_xsd300')
    @unittest.mock.patch.object(ArticleDigitalObject, '_get_datastreams')
    def test_can_return_its_xml_content_from_the_ERUDITXSD300_datastrean(
            self, mock_ds, mock_xsd300):
        # Setup
        mock_ds.return_value = ['ERUDITXSD300', ]  # noqa
        mock_xsd300.content = unittest.mock.MagicMock()
        mock_xsd300.content.serialize = unittest.mock.MagicMock(return_value='xml')
        article = ArticleDigitalObject(api, 'test')
        # Run & check
        self.assertEqual(article.xml_content, 'xml')

    @unittest.mock.patch.object(ArticleDigitalObject, 'erudit_xsd201')
    @unittest.mock.patch.object(ArticleDigitalObject, '_get_datastreams')
    def test_can_return_its_xml_content_from_the_ERUDITXSD201_datastrean(
            self, mock_ds, mock_xsd201):
        # Setup
        mock_ds.return_value = ['ERUDITXSD201', ]  # noqa
        mock_xsd201.content = unittest.mock.MagicMock()
        mock_xsd201.content.serialize = unittest.mock.MagicMock(return_value='xml')
        article = ArticleDigitalObject(api, 'test')
        # Run & check
        self.assertEqual(article.xml_content, 'xml')

    @unittest.mock.patch.object(ArticleDigitalObject, 'erudit_xsd300')
    @unittest.mock.patch.object(ArticleDigitalObject, 'erudit_xsd201')
    @unittest.mock.patch.object(ArticleDigitalObject, '_get_datastreams')
    def test_can_return_its_xml_content_using_the_ERUDITXSD300_datastrean_by_default(
            self, mock_ds, mock_xsd201, mock_xsd300):
        # Setup
        mock_ds.return_value = ['ERUDITXSD300', ]  # noqa
        mock_xsd300.content = unittest.mock.MagicMock()
        mock_xsd300.content.serialize = unittest.mock.MagicMock(return_value='xml-300')
        mock_xsd201.content = unittest.mock.MagicMock()
        mock_xsd201.content.serialize = unittest.mock.MagicMock(return_value='xml-201')
        article = ArticleDigitalObject(api, 'test')
        # Run & check
        self.assertEqual(article.xml_content, 'xml-300')
