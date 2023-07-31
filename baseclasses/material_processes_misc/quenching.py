#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import numpy as np

from nomad.metainfo import (
    Quantity,
    Section,
    Reference)
from nomad.datamodel.data import ArchiveSection

from ..chemical import Chemical


class Quenching(ArchiveSection):
    pass


class AntiSolventQuenching(Quenching):

    m_def = Section(label_quantity='name')
    name = Quantity(type=str)

    anti_solvent = Quantity(
        type=Reference(Chemical.m_def),
        a_eln=dict(component='ReferenceEditQuantity'))

    anti_solvent_volume = Quantity(
        type=np.dtype(
            np.float64),
        unit=('ml'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='ml',
            props=dict(
                minValue=0)))

    anti_solvent_dropping_time = Quantity(
        type=np.dtype(
            np.float64), unit=('s'), a_eln=dict(
            component='NumberEditQuantity', defaultDisplayUnit='s', props=dict(
                minValue=0)))

    def normalize(self, archive, logger):

        if self.anti_solvent and self.anti_solvent.name:
            if self.anti_solvent_volume:
                self.name = self.anti_solvent.name + \
                    ' ' + str(self.anti_solvent_volume)
            else:
                self.name = self.anti_solvent.name


class SpinCoatingAntiSolvent(AntiSolventQuenching):
    pass


class GasQuenching(Quenching):
    gas = Quantity(
        type=str,
        a_eln=dict(component='StringEditQuantity'))


class AirKnifeGasQuenching(GasQuenching):
    air_knife_pressure = Quantity(
        type=np.dtype(
            np.float64),
        unit=('mbar'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='mbar',
            props=dict(
                minValue=0)))

    air_knife_speed = Quantity(
        type=np.dtype(
            np.float64),
        unit=('mm/s'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='mm/s',
            props=dict(
                minValue=0)))

    air_knife_angle = Quantity(
        type=np.dtype(
            np.float64),
        unit=('degree'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='degree',
            props=dict(
                minValue=0)))

    air_knife_distance_to_thin_film = Quantity(
        type=np.dtype(
            np.float64),
        unit=('um'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='um',
            props=dict(
                minValue=0)))


class SpinCoatingGasQuenching(GasQuenching):
    pass
