# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api

import logging

logger = logging.getLogger(__name__)


class GalleryView(BrowserView):

    template = ViewPageTemplateFile('templates/gallery.pt')

    def __call__(self):
        """
        Call template.
        """

        return self.template()

    def crop(self, text="", count=0):
        """
        Crop given text to given count.
        """
        if text:
            cropped_text = ' '.join((text[0:count].strip()).split(' ')[:-1])
            strips = ['.', ',', ':', ';']
            for s in strips:
                cropped_text = cropped_text.strip(s)
            if len(text) > count:
                return cropped_text + u'…'
            else:
                return text
        else:
            return ''

    def images(self):
        """
        Check if folder contains images and return images
        """
        brains = api.content.find(
            context=self.context, portal_type='Image', depth=1)

        items = []
        for item in brains:
            obj = item.getObject()
            title = obj.title
            description = obj.description
            url = obj.absolute_url()

            if obj.image:
                images_view = api.content.get_view('images', obj, self.request)  # noqa
                tag = images_view.tag('image', height=450, width=450, direction='down')  # noqa
            else:
                tag = None

            data = {'title': self.crop(title, 65),
                    'description': self.crop(description, 265),
                    'image': tag,
                    'url': url,
                    }
            items.append(data)

        return items
