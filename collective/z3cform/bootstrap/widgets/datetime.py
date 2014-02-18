# -*- coding: utf-8 -*-
import string

from z3c.form.browser import widget
from z3c.form.interfaces import IFieldWidget
from z3c.form.widget import FieldWidget
from zope.component import adapter
from zope.schema.interfaces import IDate, IDatetime
from zope.interface import implementer, implements

from collective.z3cform.datetimewidget.widget_date import DateWidget as BaseDateWidget
from collective.z3cform.datetimewidget.widget_datetime import DatetimeWidget as BaseDatetimeWidget
from collective.z3cform.bootstrap.interfaces import IBootstrapLayer


class DateWidget(BaseDateWidget):
    """Widget for Date fields."""

    pickDate = True
    pickTime = False

    klass = 'date-widget'


@adapter(IDate, IBootstrapLayer)
@implementer(IFieldWidget)
def DateFieldWidget(field, request):
    return FieldWidget(field, DateWidget(request))


class DatetimeWidget(BaseDatetimeWidget):
    """Widget for Datetime fields."""

    pickDate = True
    pickTime = True

    klass = 'datetime-widget'


@adapter(IDatetime, IBootstrapLayer)
@implementer(IFieldWidget)
def DatetimeFieldWidget(field, request):
    return FieldWidget(field, DatetimeWidget(request))


