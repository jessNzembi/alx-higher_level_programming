#!/bin/bash
# Send request to URL and return the status code
curl -so /dev/null -w "%{http_code}" "$1"