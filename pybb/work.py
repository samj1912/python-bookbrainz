# -*- coding: utf8 -*-

# Copyright (C) 2014-2016 Ben Ockmore, Stanisław Szcześniak

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from entity import Entity
from entity_types import WorkType
from simple_objects import Language


class Work(Entity):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.work_type = None
        self.languages = None

    def fetch_from_json_filled(self, json_data):
        super(self.__class__, self).fetch_from_json(json_data)
        self.work_type = WorkType.from_json(json_data['work_type'])
        self.languages = languages_from_json(json_data['languages'])


def languages_from_json(json_data):
    return [Language.from_json(lang) for lang in json_data]
