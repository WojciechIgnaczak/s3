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

getUptime() {
    uptime_info=$(uptime -p) 
    uptime_info="${uptime_info#up }"
    
    if [[ "$uptime_info" == *"minute"* && "$uptime_info" != *"hour"* ]]; then
        echo "Uptime: ${uptime_info}"
    else
        echo "Uptime: $uptime_info"
    fi
}
getKernel() {
    kernel=$(uname -r)
    echo "Kernel: $kernel"
}
getGPU() {
    gpu=$(lspci |grep -i "vga" | cut -d: -f3 | sed 's/^[[:space:]]*//')
    echo "GPU: $gpu"
}
getUser() {
    user=$(whoami)
    echo "User: $user"
}
getShell() {
    shell=$(basename "$SHELL")
    echo "Shell: $shell"
}
getProcesses() {
    echo "Processes: $(ps -eo pid --no-headers | wc -l)"
}
getThreads() {
    echo "Threads: $(ps -eo nlwp --no-headers | awk '{sum+=$1} END {print sum}')"

}
getIP() {
    local ips=$(ip -o -f inet addr show | awk '{print $4}'| tr '\n' ' ')
    echo "IP: $ips"
}

getDNS() {
    local dns=$(grep -E '^nameserver' /etc/resolv.conf | awk '{print $2}')
    echo "DNS: $dns"
}
checkInternet(){
timeout 1 ping -c 1 8.8.8.8 &>/dev/null
    if [[ $? -eq 0 ]]; then
        echo "Internet: OK"
    else
        echo "Internet: Unavailable"
    fi

}

declare -A commands=(
    [cpu]=getCPU
    [memory]=getMemory
    [load]=getLoad
    [uptime]=getUptime
    [kernel]=getKernel
    [gpu]=getGPU
    [user]=getUser
    [shell]=getShell
    [processes]=getProcesses
    [threads]=getThreads
    [ip]=getIP
    [dns]=getDNS
    [internet]=checkInternet
)

if [[ $# -eq 0 ]]; then
    getCPU
    getMemory
    getLoad
    getUptime
    getKernel
    getGPU
    getUser
    getShell
    getProcesses
    getThreads
    getIP
    getDNS
    checkInternet

else
    for arg in "$@"; do
        key=$(echo "$arg" | tr '[:upper:]' '[:lower:]')
        if [[ -n "${commands[$key]}" ]]; then
            ${commands[$key]}
        else
            echo "Invalid argument: $arg"
            exit 1
        fi
    done
fi

exit 0
