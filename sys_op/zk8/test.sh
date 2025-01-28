#!/bin/bash
getCPU() {
    CPU=$(grep -m 1 "model name" /proc/cpuinfo | awk -F': ' '{print $2}')
    echo "CPU: $CPU"

}
getMemory() { # ile jest zajętej pamięci
    MemTotal=$(grep -m 1 "MemTotal" /proc/meminfo | awk '{print $2}')
    MemFree=$(grep -m 1 "MemFree" /proc/meminfo | awk '{print $2}')
    MemUsed=$((MemTotal - MemFree))
    MemTotalMiB=$((MemTotal / 1024))
    MemUsedMiB=$((MemUsed / 1024))
    percent=$((100 * MemUsed / MemTotal))
    echo "Memory: $MemUsedMiB/$MemTotalMiB MiB ($percent%)"
}

getLoad() {
    load=$(awk '{print $1", "$2", "$3}' /proc/loadavg)
    echo "Load: $load"
}

getUptime(){
    uptime_h=$(uptime -p | awk '{print $2}')
    uptime_m=$(uptime -p | awk '{print $4}')
    echo "Uptime: $uptime_h hour, $uptime_m minutes"
    
}
getKernel() {
    kernel=$(uname -r)
    echo "Kernel: $kernel"
}
getGPU() {
 
}
getGPU
getKernel
getUptime
getLoad
getCPU
getMemory
