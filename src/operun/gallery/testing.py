# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import operun.gallery


class OperunGalleryLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=operun.gallery)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'operun.gallery:default')


OPERUN_GALLERY_FIXTURE = OperunGalleryLayer()


OPERUN_GALLERY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(OPERUN_GALLERY_FIXTURE,),
    name='OperunGalleryLayer:IntegrationTesting'
)


OPERUN_GALLERY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(OPERUN_GALLERY_FIXTURE,),
    name='OperunGalleryLayer:FunctionalTesting'
)


OPERUN_GALLERY_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        OPERUN_GALLERY_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='OperunGalleryLayer:AcceptanceTesting'
)
