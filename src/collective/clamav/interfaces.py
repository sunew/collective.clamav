# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.interface import Interface
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from collective.clamav import MessageFactory as _


class ICollectiveClamavLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


clamdConnectionType = SimpleVocabulary(
    [SimpleTerm(value=u"Unixsocket", title="socket"),
     SimpleTerm(value=u"Network", title="net")]
)


class IAVScannerSettings(Interface):
    """ Schema for the clamav settings
    """


class IAVScanner(Interface):
    def ping():
        pass

    def scanBuffer(buffer):
        pass
