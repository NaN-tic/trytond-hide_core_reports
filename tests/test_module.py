
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.tests.test_tryton import ModuleTestCase


class HideCoreReportsTestCase(ModuleTestCase):
    'Test HideCoreReports module'
    module = 'hide_core_reports'


del ModuleTestCase
