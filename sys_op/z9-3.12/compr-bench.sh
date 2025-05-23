#!/bin/bash

measure_time() {
    local cmd=$1
    local sum=0
    for i in {1..5}; do
        local start=$(date +%s.%N)
        eval "$cmd"
        local end=$(date +%s.%N)
        local elapsed=$(echo "$end - $start" | bc -l)
        sum=$(echo "$sum + $elapsed" | bc -l)
    done
    echo "scale=10; $sum / 5" | bc -l
}

calculate_ratio() {
    local original_size=$1
    local compressed_size=$2
    echo "scale=2; ($compressed_size / $original_size) * 100" | bc -l
}

compressors=("gzip" "bzip2" "xz" "zstd" "lz4" "7z")

for dir in "$@"; do
    echo -e "$dir"
    header="%-10s  %-14s  %-14s  %-12s\n"
    printf "$header" "name" "compress" "decompress" "ratio"

    tmp_dir=$(mktemp -d)
    tar_file="$tmp_dir/archive.tar"
    tar -cf "$tar_file" -C "$dir" . # jak -cvf to wyswietla ./ ./5 ./1 ./3 ./2 ./4

    original_size=$(wc -c < "$tar_file")

    for compressor in "${compressors[@]}"; do
        compressed_file="$tmp_dir/archive.tar.$compressor"

        case $compressor in
            gzip) cmd_compress="gzip -c $tar_file > $compressed_file" ;;
            bzip2) cmd_compress="bzip2 -c $tar_file > $compressed_file" ;;
            xz) cmd_compress="xz -c $tar_file > $compressed_file" ;;
            zstd) cmd_compress="zstd -c $tar_file > $compressed_file" ;;
            lz4) cmd_compress="lz4 -c $tar_file > $compressed_file" ;;
            7z) cmd_compress="7z a $compressed_file $tar_file > /dev/null 2>&1" ;; # jesli bez 2>&1 to wywala jakies info o 7z
        esac

        case $compressor in
            gzip) cmd_decompress="gzip -d -c $compressed_file > /dev/null" ;;
            bzip2) cmd_decompress="bzip2 -d -c $compressed_file > /dev/null" ;;
            xz) cmd_decompress="xz -d -c $compressed_file > /dev/null" ;;
            zstd) cmd_decompress="zstd -d -c $compressed_file > /dev/null" ;;
            lz4) cmd_decompress="lz4 -d -c $compressed_file > /dev/null" ;;
            7z) cmd_decompress="7z x $compressed_file -so > /dev/null 2>&1" ;;
        esac

        avg_compress_time=$(measure_time "$cmd_compress")
        avg_decompress_time=$(measure_time "$cmd_decompress")

        compressed_size=$(wc -c < "$compressed_file")

        ratio=$(calculate_ratio "$original_size" "$compressed_size")

        printf "%-10s  %-14s  %-14s  %-12s\n" "$compressor" "$avg_compress_time" "$avg_decompress_time" "$ratio%"

        rm -f "$compressed_file"
    done

    rm -rf "$tmp_dir"
done
