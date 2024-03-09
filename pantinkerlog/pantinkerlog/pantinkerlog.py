import pandas as pd

from pytinkerlog import get_unit_dictionary, read_tinker_log


def tinker_log_to_df(
    path: str,
) -> pd.DataFrame:
    """Calls `read_tinker_log` from ``pytinkerlog`` and packs its return values
    into a ``pandas.DataFrame``.

    Arguments:
        path (str): Path to Tinker log.

    Returns:
        df (pandas.DataFrame): `pandas.DataFrame` object that holds all energy
            terms found in the Tinker log.
    """

    all_energies, all_names, times = read_tinker_log(path)
    df = pd.DataFrame(all_energies, columns=all_names, index=times)
    return df
