from typing import Dict, List, Tuple

import numpy as np

all_energies_type = List[List[float]]
all_names_type = List[str]
times_type = List[float]
read_tinker_log_return_type = Tuple[
    all_energies_type,
    all_names_type,
    times_type,
]


def read_tinker_log(
    path: str,
) -> read_tinker_log_return_type:
    """Parse Tinker log and make contents available in Python.

    Arguments:
        path (str): Path to Tinker log.

    Returns:
        all_energies (List[List[float]]): A nested containing the energy values
            for each frame found in the Tinker log.
        all_names (List[str]): A list containing the names of the energy terms
            found in the file.
        times (List[float]): A list containing the time of each step/frame.
    """

    times = []
    total = []
    potential = []
    kinetic = []
    temperature = []
    pressure = []
    density = []

    with open(path, "r") as f:
        while line := f.readline():
            if "Simulation Time" in line:
                arr = line.split()
                times.append(float(arr[2]))
            elif "Total Energy" in line:
                arr = line.split()
                total.append(float(arr[2]) * 4.184)  # kcal/mol -> kJ/mol
            elif "Potential Energy" in line:
                arr = line.split()
                potential.append(float(arr[2]) * 4.184)  # kcal/mol -> kJ/mol
            elif "Kinetic Energy" in line:
                arr = line.split()
                kinetic.append(float(arr[2]) * 4.184)  # kcal/mol -> kJ/mol
            elif "Temperature" in line:
                arr = line.split()
                temperature.append(float(arr[1]))  # K
            elif "Pressure" in line:
                arr = line.split()
                pressure.append(float(arr[1]) * 1.01325)  # atm -> bar
            elif "Density" in line:
                arr = line.split()
                density.append(float(arr[1]) * 1.0e+03)  # g/cm^3 -> kg/m^3

    all_energies = list(
        zip(*[
            times, total, potential, kinetic,
            temperature, pressure, density,
        ])
    )

    all_names = [
        "Time", "Total Energy", "Potential", "Kinetic En.",
        "Temperature", "Pressure", "Density",
    ]

    return (all_energies, all_names, times)


def get_unit_dictionary(
    path: str,
) -> Dict[str, str]:
    """Reads the names and units of a Tinker log and returns as a
    dictionary mapping column names (str) to unit names (str).

    Arguments:
        path (str): Path to Tinker log.

    Returns:
        unit_dict (Dict[str, str]): A dictionary mapping the term names to
            their units.
    """

    unit_dict = {
        "Time": "ps",
        "Total Energy": "kJ/mol",
        "Potential": "kJ/mol",
        "Kinetic En.": "kJ/mol",
        "Temperature": "K",
        "Pressure": "bar",
        "Density": "kg/m^3",
    }

    return unit_dict


def tinker_log_to_dict(
    path: str,
) -> Dict[str, np.array]:
    """Calls `read_tinker_log` and packs its return values into a dictionary.

    Arguments:
        path (str): Path to Tinker log.

    Returns:
        energy_dict (Dict[str, np.ndarray]): Dictionary that holds all energy
            terms found in the Tinker log.
    """

    all_energies, all_names, times = read_tinker_log(path)

    energy_dict = {}

    for (idx, name) in enumerate(all_names):
        energy_dict[name] = np.array(
            [all_energies[frame][idx] for frame in range(len(times))]
        )

    return energy_dict


if __name__ == "__main__":
    import sys

    print(tinker_log_to_dict(sys.argv[1]))
