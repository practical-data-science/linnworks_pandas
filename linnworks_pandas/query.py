"""
Query the Linnworks API

Linnworks has a number of pre-built scripts that can be accessed via their script ID:
https://help.linnworks.com/support/solutions/articles/7000018696-list-of-query-data-script-ids

"""

import requests
import math
import json
import pandas as pd
from linnworks_pandas import auth


def execute_custom_paged_script(script_id, params, page_number=1, entries_per_page=1000, verbose=False):
    """Query the Linnworks ExecuteCustomPagedScript endpoint and return a Pandas dataframe of results.

    Args:
        script_id (str): The ID of the custom script to execute.
        params (str): The parameters to pass to the script.
        page_number (int): The page number to query.
        entries_per_page (int): The number of entries per page to query.
        verbose (bool): Print helpful information on the query.

    Returns:
        Pandas dataframe of results.
    """

    token = auth.authenticate()

    query = {
        "scriptId": script_id,
        "pageNumber": page_number,
        "entriesPerPage": entries_per_page,
        "parameters": params
    }

    try:
        response = requests.post(
            url="https://eu-ext.linnworks.net/api/Dashboards/ExecuteCustomPagedScript",
            data=json.dumps(query),
            headers={
                "Authorization": token
            }
        )

        total_results = response.json()['TotalResults']
        total_pages = total_results / int(entries_per_page)
        total_pages = math.ceil(total_pages)

        if verbose:
            print('Total results: ' + str(total_results))
            print('Total pages: ' + str(total_pages))
            print('Query: ' + str(query))

        df = pd.DataFrame(response.json()['Results'])

        for page in range(2, total_pages + 1):
            query['pageNumber'] = page
            response = requests.post(
                url="https://eu-ext.linnworks.net/api/Dashboards/ExecuteCustomPagedScript",
                data=json.dumps(query),
                headers={
                    "Authorization": token
                }
            )

            df = pd.concat([df, pd.DataFrame(response.json()['Results'])], ignore_index=True)

        if verbose:
            print('Dataframe rows: ' + str(len(df)))

    except Exception as e:
        print('Query failed: ' + str(e))
        exit()

    return df


def get_order_details_between_dates(start_date, end_date, verbose=False):
    """Query the Linnworks ExecuteCustomPagedScript Order Details Between Dates endpoint and return a Pandas dataframe of results.

    Args:
        start_date (str): The start date to query.
        end_date (str): The end date to query.
        verbose (bool): Print helpful information on the query.

    Returns:
        Pandas dataframe of results.
    """

    script_id = '11'
    start_date = start_date + "T00:00:00.000Z"
    end_date = end_date + "T23:59:59.000Z"
    params = """[
        {
            "Type":"Date",
            "Name":"startDate",
            "Description":"Start date",
            "DefaultValue":"",
            "AvailableValues":[],
            "Value":"%s",
            "SortOrder":0
        },
        {
            "Type":"Date",
            "Name":"endDate",
            "Description":"End date",
            "DefaultValue":"",
            "AvailableValues":[],
            "Value":"%s",
            "SortOrder":0
        },
        {
            "Type":"Boolean",
            "Name":"merged",
            "Description":"Exclude merged child orders",
            "DefaultValue":"0",
            "AvailableValues":[],
            "Value":false,
            "SortOrder":0
        }]
    """ % (start_date, end_date)

    df = execute_custom_paged_script(script_id, params, verbose=verbose)
    return df


def get_orders_between_dates(start_date, end_date, verbose=False):
    """Query the Linnworks ExecuteCustomPagedScript Orders Between Dates endpoint and return a Pandas dataframe of results.

    Args:
        start_date (str): The start date to query.
        end_date (str): The end date to query.
        verbose (bool): Print helpful information on the query.

    Returns:
        Pandas dataframe of results.
    """

    script_id = '9'
    start_date = start_date + "T00:00:00.000Z"
    end_date = end_date + "T23:59:59.000Z"
    params = """[
        {
            "Type":"Date",
            "Name":"startDate",
            "Description":"Start date",
            "DefaultValue":"",
            "AvailableValues":[],
            "Value":"%s",
            "SortOrder":0
        },
        {
            "Type":"Date",
            "Name":"endDate",
            "Description":"End date",
            "DefaultValue":"",
            "AvailableValues":[],
            "Value":"%s",
            "SortOrder":0
        }]
    """ % (start_date, end_date)

    df = execute_custom_paged_script(script_id, params, verbose=verbose)
    return df


def get_order_totals_between_dates(start_date, end_date, verbose=False):
    """Query the Linnworks ExecuteCustomPagedScript Order Totals Between Dates endpoint and return a Pandas dataframe of results.

    Args:
        start_date (str): The start date to query.
        end_date (str): The end date to query.
        verbose (bool): Print helpful information on the query.

    Returns:
        Pandas dataframe of results.
    """

    script_id = '10'
    start_date = start_date + "T00:00:00.000Z"
    end_date = end_date + "T23:59:59.000Z"
    params = """[
        {
            "Type":"Date",
            "Name":"startDate",
            "Description":"Start date",
            "DefaultValue":"",
            "AvailableValues":[],
            "Value":"%s",
            "SortOrder":0
        },
        {
            "Type":"Date",
            "Name":"endDate",
            "Description":"End date",
            "DefaultValue":"",
            "AvailableValues":[],
            "Value":"%s",
            "SortOrder":0
        }]
    """ % (start_date, end_date)

    df = execute_custom_paged_script(script_id, params, verbose=verbose)
    return df


def get_stock_items_with_levels(locationName, verbose=False):
    """Query the Linnworks ExecuteCustomPagedScript Stock Items With Levels endpoint and return a Pandas dataframe of results.

    Args:
        locationName (str): The location name to query.
        verbose (bool): Print helpful information on the query.

    Returns:
        Pandas dataframe of results.
    """

    script_id = '8'
    params = """[
        {
            "Type":"Select",
            "Name":"locationName",
            "Value": "%s"
        }]""" % locationName

    df = execute_custom_paged_script(script_id, params, verbose=verbose)
    return df
