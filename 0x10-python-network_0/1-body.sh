#!/bin/bash
# takes in url, shows body of response (only 200)
curl -sLX GET "$1"
