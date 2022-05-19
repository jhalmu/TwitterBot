#!/bin/bash

# Start the first process
python favretweet.py &
  
# Start the second process
python followfollowers.py &
  
# Wait for any process to exit
wait -n
  
# Exit with status of process that exited first
exit $?

