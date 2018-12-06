#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# HFOS - Hackerfleet Operating System
# ===================================
# Copyright (C) 2011-2018 Heiko 'riot' Weinen <riot@c-base.org> and others.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Heiko 'riot' Weinen"
__license__ = "AGPLv3"

"""


Module: Dashboard
=================


"""

from isomer.component import ConfigurableComponent
from isomer.logger import warn  # , hfoslog, error, critical


# from isomer.database import objectmodels
# from datetime import datetime
# from isomer.events.system import updatesubscriptions, send

class Dashboard(ConfigurableComponent):
    """
    The Dashboard component monitors dashboard changes. It does not do much.
    """
    channel = 'isomer-web'

    configprops = {
    }

    def __init__(self, *args):
        """
        Initialize the Dashboard component.

        :param args:
        """

        super(Dashboard, self).__init__("DASH", *args)

        self.log("Started")

    def dashboardrequest(self, event):
        self.log("Someone interacts with the dashboard! Yay!", event, lvl=warn)

    def objectcreation(self, event):
        if event.schema == 'dashboardconfig':
            self.log("Dashboarconfig was modified: ", event)
