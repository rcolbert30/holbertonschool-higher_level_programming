#!/bin/bash
# takes in a url and displays all HTTP methods the server accepts
curl -sI "$1" | grep -w "Allow:" | cut -d' ' -f2
