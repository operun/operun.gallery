# -*- coding: utf-8 -*-

from plone.app.textfield import RichText
from plone.dexterity.content import Container
from operun.gallery import _
from zope import schema
from zope.interface import Interface
from plone.namedfile.field import NamedBlobImage


class IGallery(Interface):

    text = RichText(
        title=_(u'gallery_text_title', default=u'Text'),
        description=_(u'gallery_text_description', default=u'Add an image description.'),  # noqa
        required=False,
        )

    image = NamedBlobImage(
        title=_(u'gallery_image_title', default='Image'),
        description=_(u'gallery_image_description', default=u'Upload a gallery image.'),  # noqa
        required=True,
    )


class Gallery(Container):
    """
    Gallery class
    """
