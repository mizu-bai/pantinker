# Pytinkerlog and Pantinkerlog

This repository hosts the source files for both the Pytinkerlog and Pantinkerlog packages.

Author: mizu-bai

## Pytinkerlog

Pytinkerlog provides a means of reading a Tinker log file and return its contents as a dictionary of numpy arrays. Pytinkerlog exposes the following functions:

- `tinker_log_to_dict`: returns a dictionary of numpy arrays keyed by the energy type from a given path to a Tinker log file.
- `read_tinker_log`: parses an Tinker log file and returns the energy terms in a nested list
- `get_unit_dictionary`: returns a dictionary that holds the units of each energy term found in the Tinker log file.

## Pantinkerlog

Pantinkerlog uses the Pytinkerlog libaray to read a Tinker log file and returns its contents as a pandas dataframe. Pantinkerlog exposes the following functions.

- `tinker_log_to_df`: which gets the path to a Tinker log and returns a pandas dataframe.
- `get_unit_dictionary:` returns a dictionary that holds the units of each energy term found in the Tinker log file.

## Example

Using `pytinkerlog`

```python
import pytinkerlog

# read the Tinker log file
path = "npt_eq.log"
dic = pytinkerlog.tinker_log_to_dict(path)

# get the unts
unit_dict = pytinkerlog.get_unit_dictionary(path)
```

Using `pantinkerlog`

```python
import pantinkerlog

# read the Tinker log file
path = "npt_eq.log"
df = pantinkerlog.tinker_log_to_df(path)

# get the unts
unit_dict = pantinkerlog.get_unit_dictionary(path)
```

## Install

Via `pip`

```shell
$ python3 -m pip install git+https://github.com/mizu-bai/pantinkerlog.git#"subdirectory=pytinkerlog"
$ python3 -m pip install git+https://github.com/mizu-bai/pantinkerlog.git#"subdirectory=pantinkerlog"
```

From source

```shell
$ git clone git@github.com:mizu-bai/pantinkerlog.git
$ cd pantinkerlog
$ pip install ./pytinkerlog ./pantinkerlog
```

## License

BSD-2-Clause License
