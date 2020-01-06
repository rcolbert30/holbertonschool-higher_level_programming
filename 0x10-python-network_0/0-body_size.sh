#!/bin/bash
# gets the body size of a request
curl -I "$1" | grep -w 'Content-Length' | cut -f2 -d' '
