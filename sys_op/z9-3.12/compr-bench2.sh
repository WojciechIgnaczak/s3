#!/bin/bash
mktemp -d tymczas


for arg in "$@"; do
        tar -cvf $arg /tymczas
done

for file in /tymczas/*.tar; do
    for ((i = 0 ; i < 6 ; i++ ));do
        start=`date +%s.%N`
            gzip -k $file /tymczas
        end=`date +%s.%N`
        result_comp_gzip=$(echo "$end - $start" | bc -l)

        start=`date +%s.%N`
            gzip -d -k $file /tymczas
        end=`date +%s.%N`
        result_dcomp_gzip=$(echo "$end - $start" | bc -l)

    
        start=`date +%s.%N`
                bzip2 -k $file /tymczas
        end=`date +%s.%N`
        result_comp_bzip2=$(echo "$end - $start" | bc -l)

        start=`date +%s.%N`
                bzip2 -d -k $file /tymczas
        end=`date +%s.%N`
        result_dcomp_bzip2=$(echo "$end - $start" | bc -l)
        


        start=`date +%s.%N`
            xz -k $file /tymczas
        end=`date +%s.%N`
        result_comp_xz=$(echo "$end - $start" | bc -l)

        start=`date +%s.%N`
            xz -d -k $file /tymczas
        end=`date +%s.%N`
        result_dcomp_xz=$(echo "$end - $start" | bc -l)

        start=`date +%s.%N`
            zstd -k $file /tymczas
        end=`date +%s.%N`
        result_comp_zstd=$(echo "$end - $start" | bc -l)

        start=`date +%s.%N`
            zstd -d -k $file /tymczas
        end=`date +%s.%N`
        result_dcomp_zstd=$(echo "$end - $start" | bc -l)

        start=`date +%s.%N`
            lz4 -k $file /tymczas
        end=`date +%s.%N`
        result_comp_lz4=$(echo "$end - $start" | bc -l)

        start=`date +%s.%N`
            lz4 -d -k $file /tymczas
        end=`date +%s.%N`
        result_dcomp_lz4=$(echo "$end - $start" | bc -l)
    

        start=`date +%s.%N`
            7z $file /tymczas
        end=`date +%s.%N`
        result_comp_7z=$(echo "$end - $start" | bc -l)

        start=`date +%s.%N`
            7z e $file /tymczas
        end=`date +%s.%N`
        result_dcomp_7z=$(echo "$end - $start" | bc -l)
    done

done

rm -rf tymczas
exit 0


start=`date +%s.%N`

end=`date +%s.%N`
result=$(echo "$end - $start" | bc -l)