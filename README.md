# Pytinker and Pantinker

This repository hosts the source files for both the Pytinker and Pantinker packages.

Author: mizu-bai

## Pytinker

Pytinker provides a means of reading a Tinker log file and return its contents as a dictionary of numpy arrays. Pytinker exposes the following functions:

- `log_to_dict`: returns a dictionary of numpy arrays keyed by the energy type from a given path to a Tinker log file.
- `read_log`: parses an Tinker log file and returns the energy terms in a nested list
- `get_unit_dictionary`: returns a dictionary that holds the units of each energy term found in the Tinker log file.

## Pantinker

Pantinker uses the Pytinkerlog libaray to read a Tinker log file and returns its contents as a pandas dataframe. Pantinker exposes the following functions.

- `log_to_df`: which gets the path to a Tinker log and returns a pandas dataframe.
- `get_unit_dictionary:` returns a dictionary that holds the units of each energy term found in the Tinker log file.

## Example

Using `pytinker`

```python
import pytinker

# read the Tinker log file
path = "npt_eq.log"
dic = pytinker.log_to_dict(path)

# get the unts
unit_dict = pytinker.get_unit_dictionary(path)
```

Using `pantinker`

```python
import pantinker

# read the Tinker log file
path = "npt_eq.log"
df = pantinker.log_to_df(path)

# get the unts
unit_dict = pantinker.get_unit_dictionary(path)
```

## Install

Via `pip`

```shell
$ python3 -m pip install git+https://github.com/mizu-bai/pantinker.git#"subdirectory=pytinker"
$ python3 -m pip install git+https://github.com/mizu-bai/pantinker.git#"subdirectory=pantinker"
```

From source

```shell
$ git clone git@github.com:mizu-bai/pantinker.git
$ cd pantinkerlog
$ pip install ./pytinker ./pantinker
```

## License

BSD-2-Clause License
