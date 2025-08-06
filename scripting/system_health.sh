#!/bin/bash

# 1. Log Running Processes
logfile="process_log_$(date +%F).log"
ps aux > "$logfile"

# 2. Check for High Memory Usage (Without --sort)
high_mem_file="high_mem_processes.log"
high_mem_count=$(ps aux | awk '$4+0 > 30.0 {print}' | tee -a "$high_mem_file" | wc -l)

if [ "$high_mem_count" -gt 0 ]; then
  echo "  Warning: High memory usage processes detected!"
fi

# 3. Check Disk Space on /c/ (Windows C Drive)
disk_usage=$(df /c/ | awk 'NR==2 {print $5}' | sed 's/%//')

if [ "$disk_usage" -gt 80 ]; then
  echo "  Warning: Disk usage on C: is above 80%!"
fi

# 4. Display Summary
total_processes=$(ps aux | wc -l)
echo
echo "===== Summary ====="
echo "Total running processes         : $total_processes"
echo "Processes >30% memory           : $high_mem_count"
echo "Disk usage on C:                : ${disk_usage}%"
