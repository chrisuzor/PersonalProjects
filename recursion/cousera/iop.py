import logging
import os

import pandas as pd
import s3fs
from cachetools.func import ttl_cache

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SOURCE_URL = "https://nyc3.digitaloceanspaces.com"

QUADMIN_FORMAT_PATH = "//recursion/cousera/"
QUADMIN_RAW_PATH = "harvest-data/raw/"

BUDGET_ACTUAL_PATH = QUADMIN_FORMAT_PATH + "another1.parquet"
EMPLOYEE_AVAILABILITY_PATH = (
    QUADMIN_FORMAT_PATH + "employee_availability.parquet"
)  # noqa E501
TASK_HOURS_PATH = QUADMIN_FORMAT_PATH + "task_hours.parquet"
RAW_PROJECTS = "projects.parquet"
RAW_CLIENTS = "clients.parquet"
RAW_USERS = "users.parquet"


def get_digital_ocean_fs():
    return s3fs.S3FileSystem(
        key=os.getenv("DO_API_KEY"),
        secret=os.getenv("DO_API_SECRET"),
        client_kwargs={"endpoint_url": SOURCE_URL},
        skip_instance_cache=True,
    )


def load_quadmin_data(path):
    logger.info(f"Loading data at {path} from Digital Ocean")
    # set up the connection to the database
    fs = get_digital_ocean_fs()
    # get the data
    df = pd.read_parquet(path)
    return df


@ttl_cache(maxsize=1, ttl=60 * 60)
def load_budget_actual():
    """Load the budget_actual weekly data output from scrape_harvest"""
    df = load_quadmin_data(BUDGET_ACTUAL_PATH)
    return df


@ttl_cache(maxsize=1, ttl=60 * 60)
def get_all_employees_active():
    # avoiding circular importing
    from qadmin_pm_apps import util

    return util.get_all_employees_active()


@ttl_cache(maxsize=1, ttl=60 * 60)
def load_employee_availability():

    # get the data
    employee_availability = load_quadmin_data(EMPLOYEE_AVAILABILITY_PATH)

    # filter by active employees
    employees_active = get_all_employees_active()
    employee_availability = employee_availability[
        employee_availability.index.isin(employees_active)
    ]

    employee_availability.index.name = "Employee"
    weekly_capacity = employee_availability.loc[
        :, (slice(None), "Weekly Capacity")
    ]  # noqa E501
    employee_availability.drop(weekly_capacity.columns, axis=1, inplace=True)

    return employee_availability, weekly_capacity


@ttl_cache(maxsize=1, ttl=60 * 60)
def load_task_hours():
    """Load the task level hour data output from scrape_harvest"""
    df = load_quadmin_data(TASK_HOURS_PATH).reset_index()
    return df
