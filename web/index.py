#!/usr/bin/env python

from flask import Flask
import os, subprocess

app = Flask('app')

@app.route('/')
def index():
  result = '<a href="/update" data-css-wr5axw="">Update</a><br>'
  result += '<a href="/start" data-css-wr5axw="">Start</a>'

  return result

@app.route('/update')
def UpDate():
  command = 'steamcmd +login ${STEAM_CMD_USER} ${STEAM_CMD_PASSWORD} +force_install_dir /server +app_update 1042420 ${EXTRA_UPDATE_ARGS} +quit'
  try:
      result = subprocess.check_output(command, shell=True)
  except subprocess.CalledProcessError as e:
      return 'An error occurred while trying to fetch task status updates.<br><a href="/" data-css-wr5axw="">Back</a>'

  result += '<br><a href="/" data-css-wr5axw="">Back</a>'
  return result

@app.route('/start')
def Start():
  command = 'cd /server && ./DayZServer -config="serverDZ.cfg" ${EXTRA_START_ARGS}'
  try:
      result = subprocess.check_output(command, shell=True)
  except subprocess.CalledProcessError as e:
      return 'An error occurred while trying to fetch task status updates.<br><a href="/" data-css-wr5axw="">Back</a>'

  return '%s <br><a href="/" data-css-wr5axw="">Back</a>' % (result)

app.run(host='0.0.0.0', port=8080)
