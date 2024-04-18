#!/bin/bash

echo "Started."
python3 automation.py &
PID1=$!

python3 collections.py &
PID2=$!

wait $PID1
wait $PID2
echo "Done."