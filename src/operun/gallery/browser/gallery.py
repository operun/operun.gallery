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

    def crop(self, text, count):
        """
        Crop given text to given count.
        """
        cropped_text = ' '.join((text[0:count].strip()).split(' ')[:-1])

        strips = ['.', ',', ':', ';']
        for s in strips:
            cropped_text = cropped_text.strip(s)

        if len(text) > count:
            return cropped_text + u'…'
        else:
            return text

    def images(self):
        """
        Check if folder contains images and return images
        """
        brains = api.content.find(portal_type='Image')

        items = []
        for item in brains:
            obj = item.getObject()
            title = obj.title
            description = obj.description
            url = obj.absolute_url()

            if obj.image:
                images_view = api.content.get_view('images', obj, self.request)  # noqa
                tag = images_view.tag('image', height=400, width=400, direction='down')  # noqa
            else:
                tag = None

            data = {'title': self.crop(title, 65),
                    'description': self.crop(description, 265),
                    'image': tag,
                    'url': url,
                    }

            items.append(data)



        return items
