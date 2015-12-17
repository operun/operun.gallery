# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from operun.gallery.testing import OPERUN_GALLERY_INTEGRATION_TESTING  # noqa
from operun.gallery.interfaces import IGallery

import unittest2 as unittest


class GalleryIntegrationTest(unittest.TestCase):

    layer = OPERUN_GALLERY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Gallery')
        schema = fti.lookupSchema()
        self.assertEqual(IGallery, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Gallery')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Gallery')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IGallery.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('Gallery', 'Gallery')
        self.assertTrue(
            IGallery.providedBy(self.portal['Gallery'])
        )
