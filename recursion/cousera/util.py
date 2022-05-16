import datetime as dt
from pathlib import Path

import pandas as pd
from qadmin_pm_apps import io, load_budget_actual


def get_now(tzone):
    return dt.datetime.now(tzone)


def get_latest_raw_folder(client, source):
    """Get the folder on DO of the most recent raw data

    Parameters
    ----------
    client: s3fs.S3FileSystem
        Connection client to Digital Ocean
    source: str
        data source, 'harvest' or 'forecast'

    Returns
    -------
    String with folder path to the most recent data,
    e.g. 'harvest-data/raw/forecast/2020-11-03_17:36:11'
    """
    source_path = Path(io.QUADMIN_RAW_PATH) / source
    # it assumes that the result from client.ls is already
    # sorted in ascending order
    return client.ls(str(source_path))[-1]


def get_raw_path(filename):
    most_recent = get_latest_raw_folder(io.get_digital_ocean_fs(), "harvest")
    return f"{most_recent}/{filename}"


def monday_this_week(tzone=dt.timezone.utc):
    """Utility to get the date of Monday of this week

    Parameters
    ----------
    tzone: dt.timezone
        (Optional) Timezone requested, defaults to UTC

    Returns
    -------
    monday_date: dt.datetime
        Datetime object of Monday of this week
    """
    # get today's date
    today = get_now(tzone)
    # get the day of the week
    today_weekday = today.weekday()
    # get the date of monday of this week
    monday_date = today - dt.timedelta(days=today_weekday)
    # cleanup extraneous timing
    monday_date = monday_date.replace(
        hour=0, minute=0, second=0, microsecond=0
    )  # noqa E501

    return monday_date


def get_all_projects_timeless():
    """Get an alphabetized list of all projects ever started in the form of
    `client_name - project_name`
    """
    # get the raw-ish data
    df = load_budget_actual()
    # extract the client_project index
    level = df.index.get_level_values("client_project")
    # convert to list, remove duplicates
    client_project = list(set(level))
    # sort alphabetically
    client_project.sort()

    return client_project


def get_all_projects_active():
    """
    Get an alphabetized list of all projects active
    in the form of `client_name - project_name`.
    """
    df_project = io.load_quadmin_data(get_raw_path(io.RAW_PROJECTS))
    df_project = df_project[df_project.is_active == 1][["client_id", "name"]]

    df_client = io.load_quadmin_data(get_raw_path(io.RAW_CLIENTS))
    df_client = df_client[["id", "name"]]

    df_project = df_project.merge(
        df_client, left_on="client_id", right_on="id", suffixes=("_project", "_client")
    )

    client_project_active = df_project.apply(
        lambda v: f"{v.name_client} - {v.name_project}", axis=1
    ).to_list()

    client_project_active.sort()
    return client_project_active


def get_all_projects_in_lookback(lookback_period=6, tzone=None):
    """Get an alphabetized list of all projects in the lookback period
    in the form of `client_name - project_name`
    """
    # if no timezone passed, assume UTC
    if not tzone:
        tzone = dt.timezone.utc

    # get the raw-ish data
    df = load_budget_actual()

    # subtract one to include this week
    lookback_period = lookback_period - 1
    # get the date of today
    today = get_now(tzone)
    # get the date of monday
    monday_date = monday_this_week()
    # get the date 6 weeks back
    start_date = monday_date - dt.timedelta(days=lookback_period * 7)

    # reset the index as date
    reindexed = df.reset_index(["client_project", "name"])
    # sort by date
    reindexed.sort_index(inplace=True)
    # slice to get the lookback period
    lookback_df = reindexed.loc[start_date:today]

    # convert to list, remove duplicates
    client_project = list(set(lookback_df.client_project.tolist()))
    # sort alphabetically
    client_project.sort()

    return client_project


def get_all_projects_active_in_lookback(lookback_period=6, tzone=None):
    """Get an alphabetized list of all projects active in the lookback period
    in the form of `client_name - project_name`
    """
    projects_lookback = get_all_projects_in_lookback(
        lookback_period=lookback_period, tzone=tzone
    )
    projects_active = get_all_projects_active()

    result = list(set(projects_lookback) & set(projects_active))
    result.sort()
    return result


def get_all_employees():
    """Get a list of all employees from Harvest, sorted
    alphabetically
    """
    # get the harvest data
    df = load_budget_actual()
    # extract the name index
    level = df.index.get_level_values("name")
    # convert to list, remove duplicates
    name_list = list(set(level))
    # sort alphabetically
    name_list.sort()

    return name_list


def get_all_employees_active():
    """Get a list of all employees from Harvest, sorted
    alphabetically
    """
    # get the harvest data
    df = load_budget_actual()

    df_people = io.load_quadmin_data(get_raw_path(io.RAW_USERS))
    df_people = df_people[df_people.is_active == True]  # noqa: E712
    df_people["name"] = (
        df_people["first_name"] + " " + df_people["last_name"]
    ).str.strip()

    # extract the name index
    level = df.index.get_level_values("name")
    # convert to list, remove duplicates
    name_list = list(set(level) & set(df_people.name.unique()))
    # sort alphabetically
    name_list.sort()

    return name_list


def get_managed_employees(manager):
    """placeholder to get the bamboo managed employees

    Parameters
    ----------
    manager: str
        Name of manager
    Returns
    -------
    employee_list: list
        List of employees under this manager
    """
    return []


def datetime_to_fiscal_quarter(date):
    """Convert datetimes to fiscal quarter and date

    Parameters
    ----------
    date : Union(pd._libs.tslibs.timestamps.Timestamp,
                 pd.core.series.Series,
                 pd.core.indexes.datetimes.DatetimeIndex)
        [description]

    Returns
    -------
    tuple(int, int)
        Returns fiscal quarter and year

    Note: Quansight's 1st quarter begins February 1
    """
    fiscal_yr, fiscal_qtr = None, None
    adjusted_date = date - pd.DateOffset(months=1)

    if isinstance(date, pd._libs.tslibs.timestamps.Timestamp):
        fiscal_yr, fiscal_qtr = adjusted_date.year, adjusted_date.quarter
    elif isinstance(date, pd.core.series.Series):
        fiscal_yr, fiscal_qtr = adjusted_date.dt.year, adjusted_date.dt.quarter
    elif isinstance(date, pd.core.indexes.datetimes.DatetimeIndex):
        fiscal_yr, fiscal_qtr = adjusted_date.year, adjusted_date.quarter
    return fiscal_qtr, fiscal_yr


def fiscal_quarter_start_date(qtr, yr):
    """Returns the start date of a particular quarter

    Parameters
    ----------
    qtr : int
        quarter, possible values: {1,2,3,4}
    yr : int
        year, e.g. 2020

    Returns
    -------
    pd.Timestamp
    """
    month = 3 * qtr - 1
    return pd.Timestamp(year=yr, month=month, day=1)


def fiscal_quarter_end_date(qtr, yr):
    """Returns the end date of a particular quarter

    Parameters
    ----------
    qtr : int
        quarter, possible values: {1,2,3,4}
    yr : int
        year, e.g. 2020

    Returns
    -------
    pd.Timestamp
    """
    start = fiscal_quarter_start_date(qtr, yr)
    return start + pd.DateOffset(months=3)
