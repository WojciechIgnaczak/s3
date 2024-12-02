#!/bin/bash


list_top_cpu() {
    echo -e "\nTop 5 processes by CPU usage:"
    ps aux --sort=-%cpu | head -n 6
}

list_top_memory() {
    echo -e "\nTop 5 processes by memory usage:"
    ps aux --sort=-%mem | head -n 6
}

show_process_tree() {
    echo "Process tree:"
    pstree -p
}

show_process_name_by_pid() {
    read -p "Enter PID: " pid
    if [[ -n "$pid" && "$pid" =~ ^[0-9]+$ ]]; then
        process_name=$(ps -p "$pid" -o comm=)
        if [[ -n "$process_name" ]]; then
            echo "Process name: $process_name"
        else
            echo "No process found with PID $pid."
        fi
    else
        echo "Invalid PID entered."
    fi
}

show_process_pid_by_name() {
    read -p "Enter process name: " pname
    if [[ -n "$pname" ]]; then
        pids=$(pgrep "$pname")
        if [[ -n "$pids" ]]; then
            echo "Process PID(s): $pids"
        else
            echo "No process found with name $pname."
        fi
    else
        echo "Invalid process name entered."
    fi
}

kill_process_by_pid() {
    read -p "Enter PID to kill: " pid
    if [[ -n "$pid" && "$pid" =~ ^[0-9]+$ ]]; then
        kill "$pid" 2>/dev/null
        if [[ $? -eq 0 ]]; then
            echo "Process with PID $pid killed."
        fi
    else
        echo "Invalid PID entered."
    fi
}

kill_process_by_name() {
    read -p "Enter process name to kill: " pname
    if [[ -n "$pname" ]]; then
        pkill "$pname" 2>/dev/null
        if [[ $? -eq 0 ]]; then
            echo "Processes with name $pname killed."
        else
            echo "Failed to kill processes with name $pname. Check permissions or validity."
        fi
    else
        echo "Invalid process name entered."
    fi
}

while true; do
    echo "Process Control:"
    echo "1) List top 5 processes by CPU usage"
    echo "2) List top 5 processes by memory usage"
    echo "3) Show process tree"
    echo "4) Show process name by PID"
    echo "5) Show process PID(s) by name"
    echo "6) Kill process by PID"
    echo "7) Kill process by name"
    echo "q) Exit"
    read -p "Choice: " choice

    case "$choice" in
        1) list_top_cpu ;;
        2) list_top_memory ;;
        3) show_process_tree ;;
        4) show_process_name_by_pid ;;
        5) show_process_pid_by_name ;;
        6) kill_process_by_pid ;;
        7) kill_process_by_name ;;
        q) echo "Exiting..."; break ;;
        *) echo "Invalid choice. Please try again." ;;
    esac
done

exit 0
