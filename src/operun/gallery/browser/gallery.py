# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api


class GalleryView(BrowserView):

    template = ViewPageTemplateFile('templates/gallery.pt')

    def __call__(self):
        """
        Call template.
        """

        return self.template()
