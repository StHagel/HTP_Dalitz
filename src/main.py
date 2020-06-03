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

import math
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statistics as stat


def invariant_mass(p1, p2):
    """
    Given two four-momenta, this function calculates the invariant mass squared, i.e. the Mandlestam variable s.
    :param p1: The first four-momentum (list of length 4).
    :param p2: The second four-momentum (list of length 4).
    :return: The invariant mass squared (float).
    """
    return (p1[0] + p2[0]) ** 2 - ((p1[1] + p2[1]) ** 2 + (p1[2] + p2[2]) ** 2 + (p1[3] + p2[3]) ** 2)


def mother_particle_mass(p1, p2, p3):
    """
    Calculates the mean total energy of three particles and the variance.
    From this we can get the mother particle's mass.
    :param p1: List of four momenta of particle 1.
    :param p2: List of four momenta of particle 2.
    :param p3: List of four momenta of particle 3.
    :return: A list of mother particle masses.
    """

    total_energies = []

    for j, entry in enumerate(p1):
        energy = entry[0] + p2[j][0] + p3[j][0]
        total_energies.append(energy)

    return total_energies


def draw_dalitz_plot(_df):
    """
    Draws a Dalitz plot from two given sets of invariant masses.
    :param _df: A pandas dataframe containing the invariant masses of the decay products.
    :return:
    """

    sns.pairplot(df, corner=True, diag_kind="kde", markers="+")
    plt.show()


def plot_mass(data):
    mean = stat.mean(data)
    sigma = stat.stdev(data)

    plt.figure()
    plt.plot(data, "x", markersize=2)
    plt.title("Mother particle mass")
    plt.xlabel("Event number")
    plt.ylabel(r"$m$[GeV]")
    plt.grid(True)
    plt.plot([mean for k in range(len(data))], "red",
             label=r"$m=(" + "%.4f" % mean + "\pm" + "%.4f" % sigma + ")\;$GeV")
    plt.legend()
    plt.plot([(mean + sigma) for k in range(len(data))], "r:",)
    plt.plot([(mean - sigma) for k in range(len(data))], "r:",)
    plt.show()


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

        # These variables hold the actual invariant masses
        m_pi_c_k_c = []
        m_pi_c_pi_0 = []
        m_k_c_pi_0 = []

        for i, row in enumerate(momentum_reader):
            # The energies are calculated using the standard relativistic dispersion relation
            e_pi_c = math.sqrt(m_pi_c ** 2 + float(row[0]) ** 2 + float(row[1]) ** 2 + float(row[2]) ** 2)
            p4_pi_c.append([e_pi_c, float(row[0]), float(row[1]), float(row[2])])

            e_k_c = math.sqrt(m_k_c ** 2 + float(row[3]) ** 2 + float(row[4]) ** 2 + float(row[5]) ** 2)
            p4_k_c.append([e_k_c, float(row[3]), float(row[4]), float(row[5])])

            e_pi_0 = math.sqrt(m_pi_0 ** 2 + float(row[6]) ** 2 + float(row[7]) ** 2 + float(row[8]) ** 2)
            p4_pi_0.append([e_pi_0, float(row[6]), float(row[7]), float(row[8])])

            # The invariant masses are calculated using the invariant_mass function defined above
            m_pi_c_k_c.append(invariant_mass(p4_pi_c[i], p4_k_c[i]))
            m_pi_c_pi_0.append(invariant_mass(p4_pi_c[i], p4_pi_0[i]))
            m_k_c_pi_0.append(invariant_mass(p4_k_c[i], p4_pi_0[i]))

        masses = {
            "m12": m_pi_c_k_c,
            "m23": m_k_c_pi_0,
            "m13": m_pi_c_pi_0
        }
        df = pd.DataFrame(masses)

        draw_dalitz_plot(df)

        m_mother_list = mother_particle_mass(p4_pi_c, p4_k_c, p4_pi_0)

        plot_mass(m_mother_list)
