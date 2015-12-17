# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from operun.gallery.testing import OPERUN_GALLERY_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that operun.gallery is properly installed."""

    layer = OPERUN_GALLERY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if operun.gallery is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'operun.gallery'))

    def test_browserlayer(self):
        """Test that IOperunGalleryLayer is registered."""
        from operun.gallery.interfaces import (
            IOperunGalleryLayer)
        from plone.browserlayer import utils
        self.assertIn(IOperunGalleryLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = OPERUN_GALLERY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['operun.gallery'])

    def test_product_uninstalled(self):
        """Test if operun.gallery is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'operun.gallery'))

    def test_browserlayer_removed(self):
        """Test that IOperunGalleryLayer is removed."""
        from operun.gallery.interfaces import IOperunGalleryLayer
        from plone.browserlayer import utils
        self.assertNotIn(IOperunGalleryLayer, utils.registered_layers())
