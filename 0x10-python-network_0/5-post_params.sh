#!/bin/bash
# sends post request wi email and subject, then shows body of response
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
