# *****************************************************************************************
# *    Copyright 2024 by the_grandson and Google Gemini.                                  *
# *    You may use, edit, run or distribute this file                                     *
# *    as long as the above copyright notice remains                                      *
# * THIS SOFTWARE IS PROVIDED "AS IS".  NO WARRANTIES, WHETHER EXPRESS, IMPLIED           *
# * OR STATUTORY, INCLUDING, BUT NOT LIMITED TO, IMPLIED WARRANTIES OF                    *
# * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE APPLY TO THIS SOFTWARE.          *
# * the_grandson and Google Gemini SHALL NOT, IN ANY CIRCUMSTANCES, BE LIABLE FOR SPECIAL,*
# * INCIDENTAL, OR CONSEQUENTIAL DAMAGES, FOR ANY REASON WHATSOEVER.                      *
# * For more information visit: https://digi2.fe.up.pt                                    *
# *****************************************************************************************

import requests
from bs4 import BeautifulSoup
import datetime
from prettytable import PrettyTable
from prettytable import MARKDOWN, MSWORD_FRIENDLY, PLAIN_COLUMNS, ORGMODE
import json

def check_table_dates(url):
  """
  Fetches webpage content, searches for tables with class="dados",
  and returns a JSON object containing table data and matching dates.

  Args:
    url: The URL of the webpage to scrape.

  Returns:
    A JSON object containing all scraped table data or None if an error occurs.
  """
  # Fetch webpage content
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise error for bad status codes
  except requests.exceptions.RequestException as e:
    print(f"Error fetching webpage content: {e}")
    return [f"Error fetching webpage content: {e}"]

  # Parse HTML content
  soup = BeautifulSoup(response.content, 'html.parser')

  # Find all tables with class="dados"
  tables = soup.find_all('table', class_='dados')

  # Get today's date in desired format
  today = datetime.date.today().strftime('%d-%m-%Y')

  # Initialize empty list to store table data
  scraped_data = []
  pretty_tables = []

  # Loop through each table
  for table in tables:
    table_data = {}  # Dictionary to store data for current table
    table_title = table.find_previous_sibling('h2').text.strip()  # Extract table title
    matching_data = []  # List to store matching row data

    # Extract table headers from the first tr (adjusting for header structure)
    table_headers = [th.text.strip() for th in table.find('tr').find_all('th')]

    # Find all rows within the table (excluding the first header row)
    for row in table.find_all('tr')[1:]:  # Start from the second row
      row_data = []  # List to store data for current row
      for cell in row.find_all('td'):
        cell_text = cell.text.strip()
        if cell_text == today:
          # Matching date found, store all data in current row
          matching_data = [td.text.strip() for td in row.find_all('td')]
          break  # Move to the next table after a match
        row_data.append(cell_text)

      # Add row data to table data dictionary
      if row_data:
        table_data["row_data"] = row_data

    if(len(matching_data) > 0):
      # Add table title, headers, and matching data to scraped data
      table_headers.insert(0, "Dia")
      table_data["table_title"] = table_title
      table_data["table_headers"] = table_headers
      table_data["matching_data"] = matching_data
      
      # Append table data to scraped_data list
      scraped_data.append(table_data)

  for rest in scraped_data:
    pt = PrettyTable()
    pt.padding_width = 1
    pt.field_names = rest["table_headers"]
    max_width = {}
    for header in rest["table_headers"]:
       max_width[header] = 25
    pt._max_width = max_width
    pt.title = rest["table_title"]
    pt.add_row(rest["matching_data"])

    #pt.set_style(MARKDOWN)
    pretty_tables.append(pt.get_string())

  # Return JSON object with all scraped data
  # return json.dumps(scraped_data, indent=2)  # Indent for better readability
  return pretty_tables

# Example usage
# url = "https://sigarra.up.pt/feup/pt/cantina.ementashow"  # Replace with your target URL
# tables = check_table_dates(url)
# for table in tables:
#    print(table)