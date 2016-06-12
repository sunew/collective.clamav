# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.interface import Interface
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from collective.clamav import MessageFactory as _


clamdConnectionType = SimpleVocabulary(
    [SimpleTerm(value=u"Local UNIX Socket", title=_(u"socket")),
     SimpleTerm(value=u"Network", title=_(u"net"))]
     )

class ICollectiveClamavLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IAVScannerSettings(Interface):
    """ Schema for the clamav settings
    """
    clamav_connection = schema.Choice(
        title=_(u"Connection type to clamd"),
        description=_(u"Choose whether clamd is accessible through local "
                      u"UNIX sockets or network."),
        vocabulary=clamdConnectionType)

    clamav_socket = schema.ASCIILine(
        title=_(u"Clamd local socket file"),
        description=_(u"If connected to clamd through local UNIX sockets, "
                      u"the path to the local socket file."),
        default='/var/run/clamd',
        required=True)

    clamav_host = schema.ASCIILine(title=_(u"Scanner host"),
                                   description=_(u"If connected to clamd through the network, "
                                                 u"the host running clamd."),
                                   default='localhost',
                                   required=True)

    clamav_port = schema.Int(title=_(u"Scanner port"),
                             description=_(u"If connected to clamd through the network, "
                                           u"the port on which clamd listens."),
                             default=3310,
                             required=True)

    clamav_timeout = schema.Int(title=_(u"Timeout"),
                                description=_(u"The timeout in seconds for communication with "
                                              u"clamd."),
                                default=120,
                                required=True)


class IAVScanner(Interface):
    def ping():
        pass

    def scanBuffer(buffer):
        pass
