import pandas as pd

from pytinker import get_unit_dictionary, read_log


def log_to_df(
    path: str,
) -> pd.DataFrame:
    """Calls `read_log` from ``pytinker`` and packs its return values
    into a ``pandas.DataFrame``.

    Arguments:
        path (str): Path to Tinker log.

    Returns:
        df (pandas.DataFrame): `pandas.DataFrame` object that holds all energy
            terms found in the Tinker log.
    """

    all_energies, all_names, times = read_log(path)
    df = pd.DataFrame(all_energies, columns=all_names, index=times)
    return df
