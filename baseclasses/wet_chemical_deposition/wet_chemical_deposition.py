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
    Reference,
    SubSection, Section)

from nomad.datamodel.data import ArchiveSection
from ..solution import Solution
from .. import LayerDeposition
from ..material_processes_misc import Annealing, Quenching


class PrecursorSolution(ArchiveSection):

    m_def = Section(label_quantity='name')
    name = Quantity(type=str)

    solution = Quantity(
        type=Reference(Solution.m_def),
        a_eln=dict(component='ReferenceEditQuantity'))

    solution_volume = Quantity(
        type=np.dtype(
            np.float64),
        unit=('ml'),
        a_eln=dict(
            component='NumberEditQuantity',
            defaultDisplayUnit='ml',
            props=dict(
                minValue=0)))

    def normalize(self, archive, logger):

        if self.solution and self.solution.name:
            if self.solution_volume:
                self.name = self.solution.name + \
                    ' ' + str(self.solution_volume)
            else:
                self.name = self.solution.name


class WetChemicalDeposition(LayerDeposition):
    '''Spin Coating'''

    solution = SubSection(
        section_def=PrecursorSolution, repeats=True)

    annealing = SubSection(section_def=Annealing)
    quenching = SubSection(section_def=Quenching)

    def normalize(self, archive, logger):
        super(WetChemicalDeposition, self).normalize(archive, logger)
