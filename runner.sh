#!/bin/bash

echo "Started."
python3 automation.py &
python3 collections.py &
wait
echo "Done."