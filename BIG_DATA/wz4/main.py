# 1. podial na mniejsze pliki
# 2. sortowanie tych plików
# 3. łączenie tych plików w pary i te pary też w pary itd aż do momentu otrzymania 1 pliku

import os
import random
from timeit import default_timer as timer

def generate_data(file_path,size,max_value):
    with open(file_path,"w") as file_out:
        for _ in range(size-1):
            number=random.randint(0,max_value)
            file_out.write(str(number)+",z"+str(random.randint(0,100))+"\n")
            if _%100_000 ==0:
                print(f"{_} of {size}")
        number=random.randint(0,max_value)
        file_out.write(str(number)+",z"+str(number))

def divide_file(file_path,size,working_directory):
    with open(file_path,"r") as file_data:
        file_number=1
        end=False

        while not end:
            file_out_name=f"data_{file_number}.dat"
            file_out_path=os.path.join(working_directory,file_out_name)
            file_number+=1
            counter=0
            line=file_data.readline().strip()
            if not line:
                break
            with open(file_out_path,'w') as file_out:
                file_out.write(line)
                counter+=1

                while counter<size:
                    line=file_data.readline().strip()
                    if not line:
                        break
                        end=true
                    file_out.write("\n"+line)
                    counter+=1
            if file_number%10 ==0:
                print(f"{file_number} of {size}")


def get_all_files_in_directory(working_directory):
    files=[]
    for file in os.listdir(working_directory):
        file_path=os.path.join(working_directory,file)
        if not os.path.isdir(file_path):
            files.append(file)
    return files
        

def sort_data_in_directory(working_directory):
    files=get_all_files_in_directory(working_directory)
    c=1
    number_of_files=len(files)
    for file in files:
        file_path=os.path.join(working_directory,file)
        data=[]
        with open(file_path,'r') as source_file:
            for line in source_file:
                data_p=line.split(",",1)
                data_p[0]=int(data_p[0])
                data_p[1]=str(data_p[1].strip())
                data.append(data_p)
            
           # data=[[int(line.split(",",1))] for line in source_file]
        data.sort()
        with open(file_path,'w') as result_file:
            for i in range(len(data)-1):
                result_file.write(str(data[i][0])+","+str(data[i][1])+"\n")
            result_file.write(str(data[-1][0])+","+data[-1][1])            

        if c%10 ==0:
            print(f"{c} of {number_of_files}")
        c += 1
    
def merge_two_file(working_directory,file_in_1_name,file_in_2_name,file_out_name):
    file_in_1_path=os.path.join(working_directory,file_in_1_name)
    file_in_2_path=os.path.join(working_directory,file_in_2_name)
    file_out_path=os.path.join(working_directory,file_out_name)

    with open(file_in_1_path,'r') as file_in_1:
        with open (file_in_2_path,"r")as file_in_2:
            with open(file_out_path,"w")as file_out:
                line_1=file_in_1.readline().strip()
                line_2=file_in_2.readline().strip()

                while True:
                    if line_1 and line_2:
                        l1=line_1.split(",",1)
                        l2=line_2.split(",",1)
                        v1=int(l1[0])
                        v2=int(l2[0])
                        if v1<v2:
                            file_out.write(line_1)
                            line_1=file_in_1.readline().strip()
                        else:
                            file_out.write(line_2)
                            line_2=file_in_2.readline().strip()
                    elif line_1 and not line_2:
                        file_out.write(line_1)
                        line_1=file_in_1.readline().strip()
                    elif not line_1 and line_2:
                        file_out.write(line_2)
                        line_2=file_in_2.readline().strip()
                    else:
                        break
                    if line_1 or line_2:
                        file_out.write("\n")

def merge_one_iteration(working_directory,files,iteration,remove_source_files=True):
    dim=2
    list_of_pairs=[files[i:i+2]for i in range(0,len(files),dim)]
    
    p=1

    for pair in list_of_pairs:
        if len(pair)==dim:
            file_in_1_name=pair[0]
            file_in_2_name=pair[1]
            file_out_name=f"{iteration}_{p}.dat"
            merge_two_file(working_directory,file_in_1_name,file_in_2_name,file_out_name)
        else: 
           path_current=os.path.join(working_directory,pair[0]) 
           path_new=os.path.join(working_directory,f"{iteration}_{p}.dat")
           os.rename(path_current,path_new)
        p+=1
    
    if remove_source_files:
        for file in files:
            file_path=os.path.join(working_directory,file)
            if not os.path.isdir(file_path):
                if os.path.exists(file_path):
                    os.remove(file_path)

def merge_all_files(working_directory):
    files=get_all_files_in_directory(working_directory)
    number_of_files=len(files)
    iteration=1
    safe=10000000
    while number_of_files>1 and safe>0:
        safe-=1
        merge_one_iteration(working_directory,files,iteration,True)
        files=get_all_files_in_directory(working_directory)
        number_of_files=len(files)
        iteration+=1



def check_numbers(original_file, working_directory):
    sorted_file = get_all_files_in_directory(working_directory)
    if len(sorted_file) != 1:
        raise NameError("Zły katalog")

    sorted_file_path = os.path.join(working_directory, sorted_file[0])
    numbers={}
    with open(sorted_file_path, 'r') as file_sort:
        for line in file_sort:
            number=line.strip().split(",",1)
            number=int(number[0])
            if not number in numbers:
                numbers[number]=0
            numbers[number]+=1
        
    with open(original_file, 'r') as file_original:
        for line in file_original:
            number=line.strip().split(",",1)
            number=int(number[0])
            if not number in numbers:
                numbers[number]=0
            numbers[number]-=1
    
    for number in numbers.values():
        if number!=0:
            return False
    return True
    
def is_sorted(working_directory):
    sorted_file = get_all_files_in_directory(working_directory)
    if len(sorted_file) != 1:
        raise NameError("Zły katalog")

    sorted_file_path = os.path.join(working_directory, sorted_file[0])

    with open(sorted_file_path, 'r') as file_sort:
        x=file_sort.readline().strip().split(",",1)
        x=int(x[0])
        for line in file_sort:
            number=line.strip().split(",",1)
            number=int(number[0])
            if number < x:
                return False
            x=number

        return True

def check_correct(original_file,working_directory):
    return  is_sorted(working_directory) and check_numbers(original_file,working_directory)

def clear_directory(working_directory):
    files = get_all_files_in_directory(working_directory)

    for file in files:
        file_path = os.path.join(working_directory, file)
        if not os.path.isdir(file_path):
            if os.path.exists(file_path):
                os.remove(file_path)

def main():
    clear_directory("work")
    begin=timer()
    generate_data("data.dat",200_000,25_000)
    end=timer()
    print(f"Generate Time: {end-begin} s.")
    
    begin=timer()
    divide_file("data.dat",5000,"work")
    end=timer()
    print(f"Divide time: {end-begin} s.")
    begin=timer()
    sort_data_in_directory("work")
    end=timer()
    print(f"Sort Time: {end-begin} s.")
    begin=timer()
    merge_all_files("work")
    end=timer()
    print(f"Merge time: {end-begin} s.")
    begin=timer()
    print(check_correct("data.dat","work"))
    end=timer()
    print(f"Check time: {end-begin} s.")
if __name__=='__main__':
    main()


# sprawdz czy sa posortowane
# zlicz czy elemetow jest tyle samo

# aby dzialalo na pliku:
# 1,11
# 5,555
# 12,1323232
# 7,444
# 9,32323