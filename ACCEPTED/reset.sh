#!/bin/bash
find . ! -name 'reset.sh' -type f -exec rm -f {} +
echo 0 > number

