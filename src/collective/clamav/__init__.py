# -*- coding: utf-8 -*-
"""Init and utils."""

from zope.i18nmessageid import MessageFactory
from Products.validation import validation
from collective.clamav.validator import clamavValidator


_ = MessageFactory('collective.clamav')


validation.register(clamavValidator('isVirusFree'))
