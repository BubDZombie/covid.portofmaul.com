#!/usr/bin/env python

import csv
import json
import sys

series = [
  {
    'name': 'New Cases',
    'data': []
  }, {
    'name': 'Deaths',
    'data': []
  }
]

def get_window_average(window):
  '''Given a list of accumulating integers, take the average of deltas.
  '''
  deltas = []
  for i in range(1, len(window)):
    deltas.append(window[i] - window[i-1])
  try:
    return(sum(deltas) / len(deltas))
  except ZeroDivisionError:
    return(0)

cases_window = []
deaths_window = []
with open(sys.argv[1], 'r') as csv_file:
  csv_reader = csv.reader(csv_file)
  for row in csv_reader:
    if(row[1] == 'Bergen' and row[2] == 'New Jersey'):
      date = row[0]
      cases_window.append(int(row[4]))
      deaths_window.append(int(row[5]))

      if(len(cases_window) > 5): cases_window.pop(0)
      if(len(deaths_window) > 5): deaths_window.pop(0)

      series[0]['data'].append([date, get_window_average(cases_window)])
      series[1]['data'].append([date, get_window_average(deaths_window)])

print('var series = ' + json.dumps(series))
