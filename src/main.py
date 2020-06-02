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
import csv

if __name__ == '__main__':
    with open("../data/momenta.csv") as csv_file:
        momentum_reader = csv.reader(csv_file)
        pass



