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
    
    header="name        compress        decompress      ratio"
    echo -e "$header"
    
    tmp_dir=$(mktemp -d)
    tar_file="$tmp_dir/archive.tar"
    tar -cf "$tar_file" -C "$dir" . # jak -cvf to wyswietla ./ ./5 ./1 ./3 ./2 ./4

    original_size=$(stat --format=%s "$tar_file")

    for compressor in "${compressors[@]}"; do
        compressed_file="$tmp_dir/archive.tar.$compressor"

        case $compressor in
            gzip) cmd_compress="gzip -c -k $tar_file > $compressed_file" ;;
            bzip2) cmd_compress="bzip2 -c -k $tar_file > $compressed_file" ;;
            xz) cmd_compress="xz -c -k $tar_file > $compressed_file" ;;
            zstd) cmd_compress="zstd -c -k $tar_file > $compressed_file" ;;
            lz4) cmd_compress="lz4 -c $tar_file > $compressed_file" ;;
            7z) cmd_compress="7z a -txz $compressed_file $tar_file > /dev/null 2>&1" ;;  # jesli bez 2>&1 to wywala jakies info o 7z
        esac

        case $compressor in
            gzip) cmd_decompress="gzip -d -c -k $compressed_file > /dev/null" ;;
            bzip2) cmd_decompress="bzip2 -d -c -k $compressed_file > /dev/null" ;;
            xz) cmd_decompress="xz -d -c  -k $compressed_file > /dev/null" ;;
            zstd) cmd_decompress="zstd -d -c -k $compressed_file > /dev/null" ;;
            lz4) cmd_decompress="lz4 -d -c -k $compressed_file > /dev/null" ;;
            7z) cmd_decompress="7z x -so $compressed_file > /dev/null 2>&1" ;;
        esac

        avg_compress_time=$(measure_time "$cmd_compress")

        avg_decompress_time=$(measure_time "$cmd_decompress")

        compressed_size=$(stat --format=%s "$compressed_file")

        ratio=$(calculate_ratio "$original_size" "$compressed_size")

        printf "%-10s  %-14s  %-14s  %-12s\n" "$compressor" "$avg_compress_time" "$avg_decompress_time" "$ratio%"

        rm -f "$compressed_file"
    done

    rm -rf "$tmp_dir"
done
