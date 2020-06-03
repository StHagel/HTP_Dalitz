"""
 Copyright © 2020 Stephan Hagel (stephan.hagel@physik.uni-giessen.de)

 This file is part of the HTP_Dalitz project.

 This project is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This project is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import numpy as np
import math
import csv

if __name__ == '__main__':
    # Since the momenta are all given in units of GeV, the masses of the three particles are also in GeV
    m_pi_c = 0.13957018
    m_k_c = 0.493677
    m_pi_0 = 0.1349766
    with open("../data/momenta.csv") as csv_file:
        momentum_reader = csv.reader(csv_file)

        # These variables contain the four-momenta of the decay products
        p4_pi_c = []
        p4_k_c = []
        p4_pi_0 = []

        for row in momentum_reader:
            # The energies are calculated using the standard relativistic dispersion relation
            e_pi_c = math.sqrt(m_pi_c ** 2 + float(row[0]) ** 2 + float(row[1]) ** 2 + float(row[2]) ** 2)
            p4_pi_c.append([e_pi_c, row[0], row[1], row[2]])

            e_k_c = math.sqrt(m_k_c ** 2 + float(row[3]) ** 2 + float(row[4]) ** 2 + float(row[5]) ** 2)
            p4_k_c.append([e_k_c, row[3], row[4], row[5]])

            e_pi_0 = math.sqrt(m_pi_0 ** 2 + float(row[6]) ** 2 + float(row[7]) ** 2 + float(row[8]) ** 2)
            p4_pi_0.append([e_pi_0, row[6], row[7], row[8]])

        print(p4_pi_c[0])
        print(p4_k_c[0])
        print(p4_pi_0[0])
