#!/bin/bash

behave --format=cucumber_json:PrettyCucumberJSONFormatter -o results/cucumber.json  --format=json -o results/behave.json