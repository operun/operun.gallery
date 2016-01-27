# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api

from random import choice

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
        folders = self.context.getFolderContents(
            {'portal_type': ('Folder', 'Gallery',)}, full_objects=True)
        images = self.context.getFolderContents(
            {'portal_type': ('Image',)}, full_objects=True)

        items = []

        if folders:
            for obj in folders:
                title = obj.title
                description = obj.description
                url = obj.absolute_url()

                subimages = obj.getFolderContents(
                    {'portal_type': ('Image',)}, full_objects=True)

                if subimages:
                    obj = choice(subimages)

                    if obj.image:
                        images_view = api.content.get_view('images', obj, self.request)  # noqa
                        tag = images_view.tag('image', height=450, width=450, direction='down')  # noqa
                    else:
                        tag = None

                    data = {'title': self.crop(title, 65),
                            'description': self.crop(description, 265),
                            'type': 'folder',
                            'image': tag,
                            'url': url,
                            }

                    items.append(data)

        if images:
            for obj in images:
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
                        'type': 'image',
                        'image': tag,
                        'url': url,
                        }

                items.append(data)

        return items
