#!/bin/bash
# sends a request to a URL returns response
curl -sw "%{http_code}" -s -o /dev/null $1
