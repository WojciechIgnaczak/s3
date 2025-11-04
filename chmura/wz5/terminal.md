u334535@user-Precision-3460:~$ uname -r
6.14.0-34-generic
u334535@user-Precision-3460:~$ groups
u334535 adm cdrom sudo dip plugdev users lpadmin wireshark
u334535@user-Precision-3460:~$ df -h
System plików  rozm. użyte dost. %uż. zamont. na
tmpfs           1,6G  2,6M  1,6G   1% /run
/dev/sda2       219G  151G   57G  73% /
tmpfs           7,7G   19M  7,7G   1% /dev/shm
tmpfs           5,0M   12K  5,0M   1% /run/lock
efivarfs        438K  248K  186K  58% /sys/firmware/efi/efivars
/dev/sda1      1022M   47M  976M   5% /boot/efi
tmpfs           1,6G  2,5M  1,6G   1% /run/user/1001
u334535@user-Precision-3460:~$ sudo apt update
[sudo] hasło użytkownika u334535: 
Stary:1 https://packages.microsoft.com/repos/azure-cli noble InRelease
Pobieranie:2 https://packages.microsoft.com/repos/code stable InRelease [3 590 B]                  
Pobieranie:3 https://dl.google.com/linux/chrome/deb stable InRelease [1 825 B]                     
Stary:4 https://apt.postgresql.org/pub/repos/apt noble-pgdg InRelease                              
Pobieranie:5 https://packages.microsoft.com/repos/code stable/main amd64 Packages [20,1 kB]        
Stary:6 https://ppa.launchpadcontent.net/kicad/kicad-9.0-releases/ubuntu noble InRelease           
Pobieranie:7 https://dl.google.com/linux/chrome/deb stable/main amd64 Packages [1 209 B]           
Pobieranie:8 http://security.ubuntu.com/ubuntu noble-security InRelease [126 kB]                   
Stary:9 http://archive.ubuntu.com/ubuntu noble InRelease                             
Pobieranie:10 http://archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]                    
Pobieranie:11 http://archive.ubuntu.com/ubuntu noble-backports InRelease [126 kB]                  
Pobieranie:12 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 Packages [1 581 kB]        
Pobieranie:13 http://archive.ubuntu.com/ubuntu noble-updates/main Translation-en [298 kB]          
Pobieranie:14 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 Components [175 kB]        
Pobieranie:15 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 c-n-f Metadata [15,4 kB]   
Pobieranie:16 http://archive.ubuntu.com/ubuntu noble-updates/restricted amd64 Packages [2 240 kB]  
Pobieranie:17 http://archive.ubuntu.com/ubuntu noble-updates/restricted Translation-en [508 kB]    
Pobieranie:18 http://archive.ubuntu.com/ubuntu noble-updates/restricted amd64 Components [212 B]   
Pobieranie:19 http://security.ubuntu.com/ubuntu noble-security/main amd64 Packages [1 298 kB]      
Pobieranie:20 http://security.ubuntu.com/ubuntu noble-security/main Translation-en [213 kB]        
Pobieranie:21 http://security.ubuntu.com/ubuntu noble-security/main amd64 Components [21,6 kB]     
Pobieranie:22 http://security.ubuntu.com/ubuntu noble-security/main amd64 c-n-f Metadata [9 012 B] 
Pobieranie:23 http://security.ubuntu.com/ubuntu noble-security/restricted amd64 Packages [2 131 kB]
Pobieranie:24 http://security.ubuntu.com/ubuntu noble-security/restricted Translation-en [483 kB]  
Pobieranie:25 http://security.ubuntu.com/ubuntu noble-security/restricted amd64 Components [212 B] 
Pobieranie:26 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Packages [906 kB]    
Pobieranie:27 http://security.ubuntu.com/ubuntu noble-security/universe Translation-en [203 kB]    
Pobieranie:28 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Components [52,3 kB] 
Pobieranie:29 http://security.ubuntu.com/ubuntu noble-security/multiverse amd64 Components [208 B] 
Zign:30 http://archive.ubuntu.com/ubuntu noble-updates/universe amd64 Components                   
Pobieranie:31 http://archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 Components [940 B]
Pobieranie:32 http://archive.ubuntu.com/ubuntu noble-backports/main amd64 Components [7 132 B]
Pobieranie:33 http://archive.ubuntu.com/ubuntu noble-backports/restricted amd64 Components [212 B]
Pobieranie:34 http://archive.ubuntu.com/ubuntu noble-backports/universe amd64 Components [11,0 kB]
Pobieranie:35 http://archive.ubuntu.com/ubuntu noble-backports/multiverse amd64 Components [212 B]
Pobieranie:30 http://archive.ubuntu.com/ubuntu noble-updates/universe amd64 Components [378 kB]    
Pobrano 10,9 MB w 1min 2s (177 kB/s)                                                               
Czytanie list pakietów... Gotowe
Budowanie drzewa zależności... Gotowe
Odczyt informacji o stanie... Gotowe   
6 pakietów może być zaktualizowanych. Można je zobaczyć wykonując 'apt list --upgradable'.
u334535@user-Precision-3460:~$ sudo apt upgrade -y
Czytanie list pakietów... Gotowe
Budowanie drzewa zależności... Gotowe
Odczyt informacji o stanie... Gotowe   
Obliczanie aktualizacji... Gotowe
Get more security updates through Ubuntu Pro with 'esm-apps' enabled:
  libmagickcore-6.q16-7t64 libzvbi-common imagemagick
  libmagickcore-6.q16-7-extra libcjson1 libpostproc57 libavcodec60
  libgstreamer-plugins-bad1.0-0 libzvbi0t64 libgraphicsmagick++-q16-12t64
  libavutil58 imagemagick-6.q16 libswscale7 libswresample4
  imagemagick-6-common 7zip libavformat60 libgraphicsmagick-q16-3t64
  libavfilter9 libmagickwand-6.q16-7t64
Learn more about Ubuntu Pro at https://ubuntu.com/pro
Zostaną zainstalowane następujące NOWE pakiety:
  linux-headers-6.14.0-35-generic linux-hwe-6.14-headers-6.14.0-35 linux-hwe-6.14-tools-6.14.0-35
  linux-image-6.14.0-35-generic linux-modules-6.14.0-35-generic
  linux-modules-extra-6.14.0-35-generic linux-modules-nvidia-580-6.14.0-35-generic
  linux-objects-nvidia-580-6.14.0-35-generic linux-signatures-nvidia-6.14.0-35-generic
  linux-tools-6.14.0-35-generic
Następujące pakiety zostały zatrzymane:
  linux-signatures-nvidia-6.14.0-33-generic
Następujące pakiety zostaną zaktualizowane:
  linux-generic-hwe-24.04 linux-headers-generic-hwe-24.04 linux-image-generic-hwe-24.04
  linux-modules-nvidia-550-generic-hwe-24.04 linux-modules-nvidia-580-generic-hwe-24.04
5 aktualizowanych, 10 nowo instalowanych, 0 usuwanych i 1 nieaktualizowanych.
Konieczne pobranie 292 MB archiwów.
Po tej operacji zostanie dodatkowo użyte 494 MB miejsca na dysku.
Pobieranie:1 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 linux-modules-6.14.0-35-generic amd64 6.14.0-35.35~24.04.1 [40,7 MB]
Pobieranie:2 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 linux-image-6.14.0-35-generic amd64 6.14.0-35.35~24.04.1 [15,3 MB]
Pobieranie:3 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 linux-modules-extra-6.14.0-35-generic amd64 6.14.0-35.35~24.04.1 [119 MB]
Pobieranie:4 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 linux-generic-hwe-24.04 amd64 6.14.0-35.35~24.04.1 [1 728 B]
Pobieranie:5 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 linux-image-generic-hwe-24.04 amd64 6.14.0-35.35~24.04.1 [2 486 B]
Pobieranie:6 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 linux-hwe-6.14-headers-6.14.0-35 all 6.14.0-35.35~24.04.1 [14,1 MB]
Pobieranie:7 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 linux-headers-6.14.0-35-generic amd64 6.14.0-35.35~24.04.1 [3 739 kB]
Zign:8 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 linux-headers-generic-hwe-24.04 amd64 6.14.0-35.35~24.04.1
Pobieranie:9 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 linux-hwe-6.14-tools-6.14.0-35 amd64 6.14.0-35.35~24.04.1 [1 178 kB]
Pobieranie:10 http://archive.ubuntu.com/ubuntu noble-updates/restricted amd64 linux-signatures-nvidia-6.14.0-35-generic amd64 6.14.0-35.35~24.04.1+1 [22,9 kB]
Pobieranie:11 http://archive.ubuntu.com/ubuntu noble-updates/restricted amd64 linux-objects-nvidia-580-6.14.0-35-generic amd64 6.14.0-35.35~24.04.1+1 [97,9 MB]
Zign:11 http://archive.ubuntu.com/ubuntu noble-updates/restricted amd64 linux-objects-nvidia-580-6.14.0-35-generic amd64 6.14.0-35.35~24.04.1+1
Pobieranie:12 http://archive.ubuntu.com/ubuntu noble-updates/restricted amd64 linux-modules-nvidia-580-6.14.0-35-generic amd64 6.14.0-35.35~24.04.1+1 [8 382 B]
Pobieranie:13 http://archive.ubuntu.com/ubuntu noble-updates/restricted amd64 linux-modules-nvidia-580-generic-hwe-24.04 amd64 6.14.0-35.35~24.04.1+1 [6 702 B]
Pobieranie:14 http://archive.ubuntu.com/ubuntu noble-updates/restricted amd64 linux-modules-nvidia-550-generic-hwe-24.04 amd64 6.14.0-35.35~24.04.1+1 [6 634 B]
Pobieranie:15 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 linux-tools-6.14.0-35-generic amd64 6.14.0-35.35~24.04.1 [1 636 B]
Pobieranie:8 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 linux-headers-generic-hwe-24.04 amd64 6.14.0-35.35~24.04.1 [2 328 B]
Pobieranie:11 http://archive.ubuntu.com/ubuntu noble-updates/restricted amd64 linux-objects-nvidia-580-6.14.0-35-generic amd64 6.14.0-35.35~24.04.1+1 [97,9 MB]
Pobrano 213 MB w 7min 55s (449 kB/s)                                                               
Prekonfiguracja pakietów ...
Wybieranie wcześniej niewybranego pakietu linux-modules-6.14.0-35-generic.
(Odczytywanie bazy danych ... 573840 plików i katalogów obecnie zainstalowanych.)
Przygotowywanie do rozpakowania pakietu .../00-linux-modules-6.14.0-35-generic_6.14.0-35.35~24.04.1_
amd64.deb ...
Rozpakowywanie pakietu linux-modules-6.14.0-35-generic (6.14.0-35.35~24.04.1) ...
Wybieranie wcześniej niewybranego pakietu linux-image-6.14.0-35-generic.
Przygotowywanie do rozpakowania pakietu .../01-linux-image-6.14.0-35-generic_6.14.0-35.35~24.04.1_am
d64.deb ...
Rozpakowywanie pakietu linux-image-6.14.0-35-generic (6.14.0-35.35~24.04.1) ...
Wybieranie wcześniej niewybranego pakietu linux-modules-extra-6.14.0-35-generic.
Przygotowywanie do rozpakowania pakietu .../02-linux-modules-extra-6.14.0-35-generic_6.14.0-35.35~24
.04.1_amd64.deb ...
Rozpakowywanie pakietu linux-modules-extra-6.14.0-35-generic (6.14.0-35.35~24.04.1) ...
Przygotowywanie do rozpakowania pakietu .../03-linux-generic-hwe-24.04_6.14.0-35.35~24.04.1_amd64.de
b ...
Rozpakowywanie pakietu linux-generic-hwe-24.04 (6.14.0-35.35~24.04.1) nad (6.14.0-34.34~24.04.1) ...
Przygotowywanie do rozpakowania pakietu .../04-linux-image-generic-hwe-24.04_6.14.0-35.35~24.04.1_am
d64.deb ...
Rozpakowywanie pakietu linux-image-generic-hwe-24.04 (6.14.0-35.35~24.04.1) nad (6.14.0-34.34~24.04.
1) ...
Wybieranie wcześniej niewybranego pakietu linux-hwe-6.14-headers-6.14.0-35.
Przygotowywanie do rozpakowania pakietu .../05-linux-hwe-6.14-headers-6.14.0-35_6.14.0-35.35~24.04.1
_all.deb ...
Rozpakowywanie pakietu linux-hwe-6.14-headers-6.14.0-35 (6.14.0-35.35~24.04.1) ...
Wybieranie wcześniej niewybranego pakietu linux-headers-6.14.0-35-generic.
Przygotowywanie do rozpakowania pakietu .../06-linux-headers-6.14.0-35-generic_6.14.0-35.35~24.04.1_
amd64.deb ...
Rozpakowywanie pakietu linux-headers-6.14.0-35-generic (6.14.0-35.35~24.04.1) ...
Przygotowywanie do rozpakowania pakietu .../07-linux-headers-generic-hwe-24.04_6.14.0-35.35~24.04.1_
amd64.deb ...
Rozpakowywanie pakietu linux-headers-generic-hwe-24.04 (6.14.0-35.35~24.04.1) nad (6.14.0-34.34~24.0
4.1) ...
Wybieranie wcześniej niewybranego pakietu linux-hwe-6.14-tools-6.14.0-35.
Przygotowywanie do rozpakowania pakietu .../08-linux-hwe-6.14-tools-6.14.0-35_6.14.0-35.35~24.04.1_a
md64.deb ...
Rozpakowywanie pakietu linux-hwe-6.14-tools-6.14.0-35 (6.14.0-35.35~24.04.1) ...
Wybieranie wcześniej niewybranego pakietu linux-signatures-nvidia-6.14.0-35-generic.
Przygotowywanie do rozpakowania pakietu .../09-linux-signatures-nvidia-6.14.0-35-generic_6.14.0-35.3
5~24.04.1+1_amd64.deb ...
Rozpakowywanie pakietu linux-signatures-nvidia-6.14.0-35-generic (6.14.0-35.35~24.04.1+1) ...
Wybieranie wcześniej niewybranego pakietu linux-objects-nvidia-580-6.14.0-35-generic.
Przygotowywanie do rozpakowania pakietu .../10-linux-objects-nvidia-580-6.14.0-35-generic_6.14.0-35.
35~24.04.1+1_amd64.deb ...
Rozpakowywanie pakietu linux-objects-nvidia-580-6.14.0-35-generic (6.14.0-35.35~24.04.1+1) ...
Wybieranie wcześniej niewybranego pakietu linux-modules-nvidia-580-6.14.0-35-generic.
Przygotowywanie do rozpakowania pakietu .../11-linux-modules-nvidia-580-6.14.0-35-generic_6.14.0-35.
35~24.04.1+1_amd64.deb ...
Rozpakowywanie pakietu linux-modules-nvidia-580-6.14.0-35-generic (6.14.0-35.35~24.04.1+1) ...
Przygotowywanie do rozpakowania pakietu .../12-linux-modules-nvidia-580-generic-hwe-24.04_6.14.0-35.
35~24.04.1+1_amd64.deb ...
Rozpakowywanie pakietu linux-modules-nvidia-580-generic-hwe-24.04 (6.14.0-35.35~24.04.1+1) nad (6.14
.0-34.34~24.04.1+1) ...
Przygotowywanie do rozpakowania pakietu .../13-linux-modules-nvidia-550-generic-hwe-24.04_6.14.0-35.
35~24.04.1+1_amd64.deb ...
Rozpakowywanie pakietu linux-modules-nvidia-550-generic-hwe-24.04 (6.14.0-35.35~24.04.1+1) nad (6.14
.0-34.34~24.04.1+1) ...
Wybieranie wcześniej niewybranego pakietu linux-tools-6.14.0-35-generic.
Przygotowywanie do rozpakowania pakietu .../14-linux-tools-6.14.0-35-generic_6.14.0-35.35~24.04.1_am
d64.deb ...
Rozpakowywanie pakietu linux-tools-6.14.0-35-generic (6.14.0-35.35~24.04.1) ...
Konfigurowanie pakietu linux-hwe-6.14-headers-6.14.0-35 (6.14.0-35.35~24.04.1) ...
Konfigurowanie pakietu linux-objects-nvidia-580-6.14.0-35-generic (6.14.0-35.35~24.04.1+1) ...
Konfigurowanie pakietu linux-modules-6.14.0-35-generic (6.14.0-35.35~24.04.1) ...
Konfigurowanie pakietu linux-hwe-6.14-tools-6.14.0-35 (6.14.0-35.35~24.04.1) ...
Konfigurowanie pakietu linux-image-6.14.0-35-generic (6.14.0-35.35~24.04.1) ...
I: /boot/vmlinuz.old is now a symlink to vmlinuz-6.14.0-34-generic
I: /boot/initrd.img.old is now a symlink to initrd.img-6.14.0-34-generic
I: /boot/vmlinuz is now a symlink to vmlinuz-6.14.0-35-generic
I: /boot/initrd.img is now a symlink to initrd.img-6.14.0-35-generic
Konfigurowanie pakietu linux-modules-extra-6.14.0-35-generic (6.14.0-35.35~24.04.1) ...
Konfigurowanie pakietu linux-headers-6.14.0-35-generic (6.14.0-35.35~24.04.1) ...
/etc/kernel/header_postinst.d/dkms:
 * dkms: running auto installation service for kernel 6.14.0-35-generic
Sign command: /usr/bin/kmodsign
Signing key: /var/lib/shim-signed/mok/MOK.priv
Public certificate (MOK): /var/lib/shim-signed/mok/MOK.der

Building module:
Cleaning build area...
unset ARCH; [ ! -h /usr/bin/cc ] && export CC=/usr/bin/gcc; env NV_VERBOSE=1 'make' -j12 NV_EXCLUDE_
BUILD_MODULES='' KERNEL_UNAME=6.14.0-35-generic IGNORE_XEN_PRESENCE=1 IGNORE_CC_MISMATCH=1 SYSSRC=/l
ib/modules/6.14.0-35-generic/build LD=/usr/bin/ld.bfd CONFIG_X86_KERNEL_IBT= modules...........
Signing module /var/lib/dkms/nvidia/580.95.05/build/nvidia.ko
Signing module /var/lib/dkms/nvidia/580.95.05/build/nvidia-modeset.ko
Signing module /var/lib/dkms/nvidia/580.95.05/build/nvidia-drm.ko
Signing module /var/lib/dkms/nvidia/580.95.05/build/nvidia-uvm.ko
Signing module /var/lib/dkms/nvidia/580.95.05/build/nvidia-peermem.ko
Cleaning build area...

nvidia.ko.zst:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/6.14.0-35-generic/updates/dkms/

nvidia-modeset.ko.zst:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/6.14.0-35-generic/updates/dkms/

nvidia-drm.ko.zst:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/6.14.0-35-generic/updates/dkms/

nvidia-uvm.ko.zst:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/6.14.0-35-generic/updates/dkms/

nvidia-peermem.ko.zst:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/6.14.0-35-generic/updates/dkms/
depmod...
dkms autoinstall on 6.14.0-35-generic/x86_64 succeeded for nvidia
 * dkms: autoinstall for kernel 6.14.0-35-generic
   ...done.
Konfigurowanie pakietu linux-tools-6.14.0-35-generic (6.14.0-35.35~24.04.1) ...
Konfigurowanie pakietu linux-signatures-nvidia-6.14.0-35-generic (6.14.0-35.35~24.04.1+1) ...
Konfigurowanie pakietu linux-image-generic-hwe-24.04 (6.14.0-35.35~24.04.1) ...
Konfigurowanie pakietu linux-headers-generic-hwe-24.04 (6.14.0-35.35~24.04.1) ...
Konfigurowanie pakietu linux-modules-nvidia-580-6.14.0-35-generic (6.14.0-35.35~24.04.1+1) ...
linux-image-nvidia-6.14.0-35-generic: constructing .ko files
/usr/bin/ld.bfd: warning: --package-metadata is empty, ignoring
/usr/bin/ld.bfd: warning: --package-metadata is empty, ignoring
/usr/bin/ld.bfd: warning: --package-metadata is empty, ignoring
/usr/bin/ld.bfd: warning: --package-metadata is empty, ignoring
/usr/bin/ld.bfd: warning: --package-metadata is empty, ignoring
/usr/bin/ld.bfd: warning: --package-metadata is empty, ignoring
/usr/bin/ld.bfd: warning: --package-metadata is empty, ignoring
/usr/bin/ld.bfd: warning: --package-metadata is empty, ignoring
/usr/bin/ld.bfd: warning: --package-metadata is empty, ignoring
/usr/bin/ld.bfd: warning: --package-metadata is empty, ignoring
/usr/bin/ld.bfd: warning: --package-metadata is empty, ignoring
/usr/bin/ld.bfd: warning: --package-metadata is empty, ignoring
nvidia-drm.ko: DOBRZE
nvidia-modeset.ko: DOBRZE
nvidia-peermem.ko: DOBRZE
nvidia-uvm.ko: DOBRZE
nvidia.ko: DOBRZE
Konfigurowanie pakietu linux-generic-hwe-24.04 (6.14.0-35.35~24.04.1) ...
Konfigurowanie pakietu linux-modules-nvidia-580-generic-hwe-24.04 (6.14.0-35.35~24.04.1+1) ...
Konfigurowanie pakietu linux-modules-nvidia-550-generic-hwe-24.04 (6.14.0-35.35~24.04.1+1) ...
Przetwarzanie wyzwalaczy pakietu linux-image-6.14.0-35-generic (6.14.0-35.35~24.04.1)...
/etc/kernel/postinst.d/dkms:
 * dkms: running auto installation service for kernel 6.14.0-35-generic
 * dkms: autoinstall for kernel 6.14.0-35-generic
   ...done.
/etc/kernel/postinst.d/initramfs-tools:
update-initramfs: Generating /boot/initrd.img-6.14.0-35-generic
/etc/kernel/postinst.d/zz-update-grub:
Sourcing file `/etc/default/grub'
Generating grub configuration file ...
Found linux image: /boot/vmlinuz-6.14.0-35-generic
Found initrd image: /boot/initrd.img-6.14.0-35-generic
Found linux image: /boot/vmlinuz-6.14.0-34-generic
Found initrd image: /boot/initrd.img-6.14.0-34-generic
Found linux image: /boot/vmlinuz-6.14.0-33-generic
Found initrd image: /boot/initrd.img-6.14.0-33-generic
Found linux image: /boot/vmlinuz-6.11.0-21-generic
Found initrd image: /boot/initrd.img-6.11.0-21-generic
Found linux image: /boot/vmlinuz-6.8.0-47-generic
Found initrd image: /boot/initrd.img-6.8.0-47-generic
Found memtest86+ 64bit EFI image: /boot/memtest86+x64.efi
Warning: os-prober will be executed to detect other bootable partitions.
Its output will be used to detect bootable binaries on them and create new boot entries.
Found Windows Boot Manager on /dev/nvme0n1p1@/efi/Microsoft/Boot/bootmgfw.efi
Adding boot menu entry for UEFI Firmware Settings ...
Found grml-rescueboot ISO image: /boot/grml/kali-linux-2025.1a-live-amd64.iso
done
u334535@user-Precision-3460:~$ sudo apt-get install -y \
ca-certificates \
curl gnupg \
lsb-relase
Czytanie list pakietów... Gotowe
Budowanie drzewa zależności... Gotowe
Odczyt informacji o stanie... Gotowe   
E: Nie udało się odnaleźć pakietu lsb-relase
u334535@user-Precision-3460:~$ sudo apt-get install -y \
ca-certificates \
curl gnupg \
lsb-release
Czytanie list pakietów... Gotowe
Budowanie drzewa zależności... Gotowe
Odczyt informacji o stanie... Gotowe   
ca-certificates jest już w najnowszej wersji (20240203).
curl jest już w najnowszej wersji (8.5.0-2ubuntu10.6).
gnupg jest już w najnowszej wersji (2.4.4-2ubuntu17.3).
lsb-release jest już w najnowszej wersji (12.0-2).
Następujące pakiety zostały zainstalowane automatycznie i nie są już więcej wymagane:
  linux-headers-6.14.0-33-generic linux-hwe-6.14-headers-6.14.0-33 linux-hwe-6.14-tools-6.14.0-33
  linux-image-6.14.0-33-generic linux-modules-6.14.0-33-generic
  linux-modules-extra-6.14.0-33-generic linux-modules-nvidia-550-6.14.0-33-generic
  linux-objects-nvidia-550-6.14.0-33-generic linux-objects-nvidia-580-6.14.0-33-generic
  linux-signatures-nvidia-6.14.0-33-generic linux-tools-6.14.0-33-generic nvidia-kernel-common-550
Aby je usunąć należy użyć "sudo apt autoremove".
0 aktualizowanych, 0 nowo instalowanych, 0 usuwanych i 1 nieaktualizowanych.
u334535@user-Precision-3460:~$ ^[[200~sudo mkdir -p /etc/apt/keyrings
sudo: nie znaleziono polecenia
u334535@user-Precision-3460:~$ sudo mkdir -p /etc/apt/keyrings
u334535@user-Precision-3460:~$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
u334535@user-Precision-3460:~$ echo \
"deb [arch=amd64 signed-by=/etc/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list >/dev/null
u334535@user-Precision-3460:~$ docker
Polecenie 'docker' nie zostało znalezione, ale można je zainstalować za pomocą:
sudo snap install docker         # version 28.4.0, or
sudo snap install docker         # version 28.1.1+1
sudo apt  install docker.io      # version 28.2.2-0ubuntu1~24.04.1
sudo apt  install podman-docker  # version 4.9.3+ds1-1ubuntu0.2
Zobacz 'snap info <nazwasnapa>' dla dodatkowych wersji.
u334535@user-Precision-3460:~$ sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
Pobieranie:1 https://download.docker.com/linux/ubuntu noble InRelease [48,5 kB]
Stary:2 https://packages.microsoft.com/repos/azure-cli noble InRelease                             
Stary:3 https://packages.microsoft.com/repos/code stable InRelease                                 
Stary:4 https://apt.postgresql.org/pub/repos/apt noble-pgdg InRelease                              
Błąd:1 https://download.docker.com/linux/ubuntu noble InRelease                                    
  Następujące podpisy nie mogły zostać zweryfikowane z powodu braku klucza publicznego: NO_PUBKEY 7EA0A9C3F273FCD8
Stary:5 https://dl.google.com/linux/chrome/deb stable InRelease                                    
Stary:6 https://ppa.launchpadcontent.net/kicad/kicad-9.0-releases/ubuntu noble InRelease           
Stary:7 http://security.ubuntu.com/ubuntu noble-security InRelease                                 
Stary:8 http://archive.ubuntu.com/ubuntu noble InRelease                          
Stary:9 http://archive.ubuntu.com/ubuntu noble-updates InRelease
Stary:10 http://archive.ubuntu.com/ubuntu noble-backports InRelease
Czytanie list pakietów... Gotowe
W: Błąd GPG: https://download.docker.com/linux/ubuntu noble InRelease: Następujące podpisy nie mogły zostać zweryfikowane z powodu braku klucza publicznego: NO_PUBKEY 7EA0A9C3F273FCD8
E: Repozytorium "https://download.docker.com/linux/ubuntu noble InRelease" nie jest podpisane.
N: Aktualizacja z takiego repozytorium nie może być bezpiecznie wykonana, zatem jest domyślnie wyłączona.
N: Więcej informacji o tworzeniu repozytorium i szczegółach konfiguracji użytkownika znajduje się w podręczniku apt-secure(8).
Czytanie list pakietów... Gotowe
Budowanie drzewa zależności... Gotowe
Odczyt informacji o stanie... Gotowe   
ca-certificates jest już w najnowszej wersji (20240203).
curl jest już w najnowszej wersji (8.5.0-2ubuntu10.6).
Następujące pakiety zostały zainstalowane automatycznie i nie są już więcej wymagane:
  linux-headers-6.14.0-33-generic linux-hwe-6.14-headers-6.14.0-33 linux-hwe-6.14-tools-6.14.0-33
  linux-image-6.14.0-33-generic linux-modules-6.14.0-33-generic
  linux-modules-extra-6.14.0-33-generic linux-modules-nvidia-550-6.14.0-33-generic
  linux-objects-nvidia-550-6.14.0-33-generic linux-objects-nvidia-580-6.14.0-33-generic
  linux-signatures-nvidia-6.14.0-33-generic linux-tools-6.14.0-33-generic nvidia-kernel-common-550
Aby je usunąć należy użyć "sudo apt autoremove".
0 aktualizowanych, 0 nowo instalowanych, 0 usuwanych i 1 nieaktualizowanych.
Pobieranie:1 https://download.docker.com/linux/ubuntu noble InRelease [48,5 kB]
Stary:2 https://dl.google.com/linux/chrome/deb stable InRelease                                    
Stary:3 https://apt.postgresql.org/pub/repos/apt noble-pgdg InRelease                              
Stary:4 https://packages.microsoft.com/repos/azure-cli noble InRelease                             
Stary:5 https://packages.microsoft.com/repos/code stable InRelease                                 
Pobieranie:6 https://download.docker.com/linux/ubuntu noble/stable amd64 Packages [33,5 kB]        
Stary:7 https://ppa.launchpadcontent.net/kicad/kicad-9.0-releases/ubuntu noble InRelease           
Stary:8 http://security.ubuntu.com/ubuntu noble-security InRelease                                 
Stary:9 http://archive.ubuntu.com/ubuntu noble InRelease                         
Pobieranie:10 http://archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]
Stary:11 http://archive.ubuntu.com/ubuntu noble-backports InRelease                                
Pobrano 208 kB w 6s (33,2 kB/s)                                                                    
Czytanie list pakietów... Gotowe
u334535@user-Precision-3460:~$ sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && ec^C
u334535@user-Precision-3460:~$  sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
Czytanie list pakietów... Gotowe
Budowanie drzewa zależności... Gotowe
Odczyt informacji o stanie... Gotowe   
Następujące pakiety zostały zainstalowane automatycznie i nie są już więcej wymagane:
  linux-headers-6.14.0-33-generic linux-hwe-6.14-headers-6.14.0-33 linux-hwe-6.14-tools-6.14.0-33
  linux-image-6.14.0-33-generic linux-modules-6.14.0-33-generic
  linux-modules-extra-6.14.0-33-generic linux-modules-nvidia-550-6.14.0-33-generic
  linux-objects-nvidia-550-6.14.0-33-generic linux-objects-nvidia-580-6.14.0-33-generic
  linux-signatures-nvidia-6.14.0-33-generic linux-tools-6.14.0-33-generic nvidia-kernel-common-550
Aby je usunąć należy użyć "sudo apt autoremove".
Zostaną zainstalowane następujące dodatkowe pakiety:
  docker-ce-rootless-extras libslirp0 pigz slirp4netns
Sugerowane pakiety:
  cgroupfs-mount | cgroup-lite docker-model-plugin
Zostaną zainstalowane następujące NOWE pakiety:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli docker-ce-rootless-extras
  docker-compose-plugin libslirp0 pigz slirp4netns
0 aktualizowanych, 9 nowo instalowanych, 0 usuwanych i 1 nieaktualizowanych.
Konieczne pobranie 105 MB archiwów.
Po tej operacji zostanie dodatkowo użyte 437 MB miejsca na dysku.
Kontynuować? [T/n] t
Pobieranie:1 https://download.docker.com/linux/ubuntu noble/stable amd64 containerd.io amd64 1.7.28-1~ubuntu.24.04~noble [31,9 MB]
Pobieranie:2 http://archive.ubuntu.com/ubuntu noble/universe amd64 pigz amd64 2.8-1 [65,6 kB]
Pobieranie:3 https://download.docker.com/linux/ubuntu noble/stable amd64 docker-ce-cli amd64 5:28.5.1-1~ubuntu.24.04~noble [16,5 MB]
Pobieranie:4 https://download.docker.com/linux/ubuntu noble/stable amd64 docker-ce amd64 5:28.5.1-1~ubuntu.24.04~noble [19,7 MB]
Pobieranie:5 https://download.docker.com/linux/ubuntu noble/stable amd64 docker-buildx-plugin amd64 0.29.1-1~ubuntu.24.04~noble [15,9 MB]
Pobieranie:6 https://download.docker.com/linux/ubuntu noble/stable amd64 docker-ce-rootless-extras amd64 5:28.5.1-1~ubuntu.24.04~noble [6 481 kB]
Pobieranie:7 https://download.docker.com/linux/ubuntu noble/stable amd64 docker-compose-plugin amd64 2.40.3-1~ubuntu.24.04~noble [14,3 MB]
Pobieranie:8 http://archive.ubuntu.com/ubuntu noble/main amd64 libslirp0 amd64 4.7.0-1ubuntu3 [63,8 kB]
Pobieranie:9 http://archive.ubuntu.com/ubuntu noble/universe amd64 slirp4netns amd64 1.2.1-1build2 [34,9 kB]
Pobrano 105 MB w 2s (63,7 MB/s)                                                           
Wybieranie wcześniej niewybranego pakietu containerd.io.
(Odczytywanie bazy danych ... 613384 pliki i katalogi obecnie zainstalowane.)
Przygotowywanie do rozpakowania pakietu .../0-containerd.io_1.7.28-1~ubuntu.24.04~noble_amd64.deb ...
Rozpakowywanie pakietu containerd.io (1.7.28-1~ubuntu.24.04~noble) ...
Wybieranie wcześniej niewybranego pakietu docker-ce-cli.
Przygotowywanie do rozpakowania pakietu .../1-docker-ce-cli_5%3a28.5.1-1~ubuntu.24.04~noble_amd64.deb ...
Rozpakowywanie pakietu docker-ce-cli (5:28.5.1-1~ubuntu.24.04~noble) ...
Wybieranie wcześniej niewybranego pakietu docker-ce.
Przygotowywanie do rozpakowania pakietu .../2-docker-ce_5%3a28.5.1-1~ubuntu.24.04~noble_amd64.deb ...
Rozpakowywanie pakietu docker-ce (5:28.5.1-1~ubuntu.24.04~noble) ...
Wybieranie wcześniej niewybranego pakietu pigz.
Przygotowywanie do rozpakowania pakietu .../3-pigz_2.8-1_amd64.deb ...
Rozpakowywanie pakietu pigz (2.8-1) ...
Wybieranie wcześniej niewybranego pakietu docker-buildx-plugin.
Przygotowywanie do rozpakowania pakietu .../4-docker-buildx-plugin_0.29.1-1~ubuntu.24.04~noble_amd64.deb ...
Rozpakowywanie pakietu docker-buildx-plugin (0.29.1-1~ubuntu.24.04~noble) ...
Wybieranie wcześniej niewybranego pakietu docker-ce-rootless-extras.
Przygotowywanie do rozpakowania pakietu .../5-docker-ce-rootless-extras_5%3a28.5.1-1~ubuntu.24.04~noble_amd64.deb ...
Rozpakowywanie pakietu docker-ce-rootless-extras (5:28.5.1-1~ubuntu.24.04~noble) ...
Wybieranie wcześniej niewybranego pakietu docker-compose-plugin.
Przygotowywanie do rozpakowania pakietu .../6-docker-compose-plugin_2.40.3-1~ubuntu.24.04~noble_amd64.deb ...
Rozpakowywanie pakietu docker-compose-plugin (2.40.3-1~ubuntu.24.04~noble) ...
Wybieranie wcześniej niewybranego pakietu libslirp0:amd64.
Przygotowywanie do rozpakowania pakietu .../7-libslirp0_4.7.0-1ubuntu3_amd64.deb ...
Rozpakowywanie pakietu libslirp0:amd64 (4.7.0-1ubuntu3) ...
Wybieranie wcześniej niewybranego pakietu slirp4netns.
Przygotowywanie do rozpakowania pakietu .../8-slirp4netns_1.2.1-1build2_amd64.deb ...
Rozpakowywanie pakietu slirp4netns (1.2.1-1build2) ...
Konfigurowanie pakietu docker-buildx-plugin (0.29.1-1~ubuntu.24.04~noble) ...
Konfigurowanie pakietu containerd.io (1.7.28-1~ubuntu.24.04~noble) ...
Created symlink /etc/systemd/system/multi-user.target.wants/containerd.service → /usr/lib/systemd/system/containerd.service.
Konfigurowanie pakietu docker-compose-plugin (2.40.3-1~ubuntu.24.04~noble) ...
Konfigurowanie pakietu docker-ce-cli (5:28.5.1-1~ubuntu.24.04~noble) ...
Konfigurowanie pakietu libslirp0:amd64 (4.7.0-1ubuntu3) ...
Konfigurowanie pakietu pigz (2.8-1) ...
Konfigurowanie pakietu docker-ce-rootless-extras (5:28.5.1-1~ubuntu.24.04~noble) ...
Konfigurowanie pakietu slirp4netns (1.2.1-1build2) ...
Konfigurowanie pakietu docker-ce (5:28.5.1-1~ubuntu.24.04~noble) ...
Created symlink /etc/systemd/system/multi-user.target.wants/docker.service → /usr/lib/systemd/system/docker.service.
Created symlink /etc/systemd/system/sockets.target.wants/docker.socket → /usr/lib/systemd/system/docker.socket.
Przetwarzanie wyzwalaczy pakietu man-db (2.12.0-4build2)...
Przetwarzanie wyzwalaczy pakietu libc-bin (2.39-0ubuntu8.6)...
u334535@user-Precision-3460:~$  sudo systemctl status docker
● docker.service - Docker Application Container Engine
     Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; preset: enabled)
     Active: active (running) since Tue 2025-11-04 09:21:23 GMT; 20s ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 29079 (dockerd)
      Tasks: 17
     Memory: 24.8M (peak: 27.2M)
        CPU: 211ms
     CGroup: /system.slice/docker.service
             └─29079 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock

lis 04 09:21:22 user-Precision-3460 dockerd[29079]: time="2025-11-04T09:21:22.535563501Z" level=inf>
lis 04 09:21:22 user-Precision-3460 dockerd[29079]: time="2025-11-04T09:21:22.556537499Z" level=inf>
lis 04 09:21:22 user-Precision-3460 dockerd[29079]: time="2025-11-04T09:21:22.787763666Z" level=inf>
lis 04 09:21:23 user-Precision-3460 dockerd[29079]: time="2025-11-04T09:21:23.029141923Z" level=inf>
lis 04 09:21:23 user-Precision-3460 dockerd[29079]: time="2025-11-04T09:21:23.040666148Z" level=inf>
lis 04 09:21:23 user-Precision-3460 dockerd[29079]: time="2025-11-04T09:21:23.040729789Z" level=inf>
lis 04 09:21:23 user-Precision-3460 dockerd[29079]: time="2025-11-04T09:21:23.054157919Z" level=inf>
lis 04 09:21:23 user-Precision-3460 dockerd[29079]: time="2025-11-04T09:21:23.057431130Z" level=inf>
lis 04 09:21:23 user-Precision-3460 dockerd[29079]: time="2025-11-04T09:21:23.057456905Z" level=inf>
lis 04 09:21:23 user-Precision-3460 systemd[1]: Started docker.service - Docker Application Contain>
u334535@user-Precision-3460:~$ docker
Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Common Commands:
  run         Create and run a new container from an image
  exec        Execute a command in a running container
  ps          List containers
  build       Build an image from a Dockerfile
  bake        Build from a file
  pull        Download an image from a registry
  push        Upload an image to a registry
  images      List images
  login       Authenticate to a registry
  logout      Log out from a registry
  search      Search Docker Hub for images
  version     Show the Docker version information
  info        Display system-wide information

Management Commands:
  builder     Manage builds
  buildx*     Docker Buildx
  checkpoint  Manage checkpoints
  compose*    Docker Compose
  container   Manage containers
  context     Manage contexts
  image       Manage images
  manifest    Manage Docker image manifests and manifest lists
  network     Manage networks
  plugin      Manage plugins
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Swarm Commands:
  config      Manage Swarm configs
  node        Manage Swarm nodes
  secret      Manage Swarm secrets
  service     Manage Swarm services
  stack       Manage Swarm stacks
  swarm       Manage Swarm

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  import      Import the contents from a tarball to create a filesystem image
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  wait        Block until one or more containers stop, then print their exit codes

Global Options:
      --config string      Location of client config files (default "/home/u334535/.docker")
  -c, --context string     Name of the context to use to connect to the daemon (overrides
                           DOCKER_HOST env var and default context set with "docker context use")
  -D, --debug              Enable debug mode
  -H, --host string        Daemon socket to connect to
  -l, --log-level string   Set the logging level ("debug", "info", "warn", "error", "fatal")
                           (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default
                           "/home/u334535/.docker/ca.pem")
      --tlscert string     Path to TLS certificate file (default "/home/u334535/.docker/cert.pem")
      --tlskey string      Path to TLS key file (default "/home/u334535/.docker/key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Run 'docker COMMAND --help' for more information on a command.

For more help on how to use Docker, head to https://docs.docker.com/go/guides/
u334535@user-Precision-3460:~$ docker --version
Docker version 28.5.1, build e180ab8
u334535@user-Precision-3460:~$ docker info
Client: Docker Engine - Community
 Version:    28.5.1
 Context:    default
 Debug Mode: false
 Plugins:
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.29.1
    Path:     /usr/libexec/docker/cli-plugins/docker-buildx
  compose: Docker Compose (Docker Inc.)
    Version:  v2.40.3
    Path:     /usr/libexec/docker/cli-plugins/docker-compose

Server:
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.51/info": dial unix /var/run/docker.sock: connect: permission denied
u334535@user-Precision-3460:~$ sudo docker info
Client: Docker Engine - Community
 Version:    28.5.1
 Context:    default
 Debug Mode: false
 Plugins:
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.29.1
    Path:     /usr/libexec/docker/cli-plugins/docker-buildx
  compose: Docker Compose (Docker Inc.)
    Version:  v2.40.3
    Path:     /usr/libexec/docker/cli-plugins/docker-compose

Server:
 Containers: 0
  Running: 0
  Paused: 0
  Stopped: 0
 Images: 0
 Server Version: 28.5.1
 Storage Driver: overlay2
  Backing Filesystem: extfs
  Supports d_type: true
  Using metacopy: false
  Native Overlay Diff: true
  userxattr: false
 Logging Driver: json-file
 Cgroup Driver: systemd
 Cgroup Version: 2
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local splunk syslog
 CDI spec directories:
  /etc/cdi
  /var/run/cdi
 Swarm: inactive
 Runtimes: io.containerd.runc.v2 runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: b98a3aace656320842a23f4a392a33f46af97866
 runc version: v1.3.0-0-g4ca628d1
 init version: de40ad0
 Security Options:
  apparmor
  seccomp
   Profile: builtin
  cgroupns
 Kernel Version: 6.14.0-34-generic
 Operating System: Ubuntu 24.04.3 LTS
 OSType: linux
 Architecture: x86_64
 CPUs: 12
 Total Memory: 15.31GiB
 Name: user-Precision-3460
 ID: cd2db5ed-8c27-4a37-83c3-440d70275150
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Experimental: false
 Insecure Registries:
  ::1/128
  127.0.0.0/8
 Live Restore Enabled: false

u334535@user-Precision-3460:~$  sudo docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
17eec7bbc9d7: Pull complete 
Digest: sha256:56433a6be3fda188089fb548eae3d91df3ed0d6589f7c2656121b911198df065
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

u334535@user-Precision-3460:~$ sudo docekr ps
sudo: docekr: nie znaleziono polecenia
u334535@user-Precision-3460:~$ ^[[200~sudo usermod -aG docker $USER
sudo: nie znaleziono polecenia
u334535@user-Precision-3460:~$ sudo usermod -aG docker $USER
u334535@user-Precision-3460:~$ newgrp docker
u334535@user-Precision-3460:~$ docker run hello-word
Unable to find image 'hello-word:latest' locally
docker: Error response from daemon: pull access denied for hello-word, repository does not exist or may require 'docker login': denied: requested access to the resource is denied

Run 'docker run --help' for more information
u334535@user-Precision-3460:~$ sudo groupadd docker
groupadd: group 'docker' already exists
u334535@user-Precision-3460:~$ sudo usermod -aG docker $USER
u334535@user-Precision-3460:~$ newgrp docker
u334535@user-Precision-3460:~$ docekr run hello-world
Nie znaleziono polecenia 'docekr', czy chodziło o:
  polecenie 'docker' ze snapa docker (28.4.0)
  polecenie 'docker' ze snapa docker (28.1.1+1)
  polecenie 'docker' z pakietu deb docker.io (28.2.2-0ubuntu1~24.04.1)
  polecenie 'docker' z pakietu deb podman-docker (4.9.3+ds1-1ubuntu0.2)
Zobacz 'snap info <nazwasnapa>' dla dodatkowych wersji.
u334535@user-Precision-3460:~$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

u334535@user-Precision-3460:~$ docker run -it ubuntu bash
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
4b3ffd8ccb52: Pull complete 
Digest: sha256:66460d557b25769b102175144d538d88219c077c678a49af4afca6fbfc1b5252
Status: Downloaded newer image for ubuntu:latest
root@8ec89171ca40:/# whoami
root
root@8ec89171ca40:/# exit
exit
u334535@user-Precision-3460:~$ docker run -it ubuntu bash
root@2be2496cc9e5:/# exit
exit
u334535@user-Precision-3460:~$ docker pull alpine:latest
latest: Pulling from library/alpine
2d35ebdb57d9: Pull complete 
Digest: sha256:4b7ce07002c69e8f3d704a9c5d6fd3053be500b7f1c69fc0d80990c2ad8dd412
Status: Downloaded newer image for alpine:latest
docker.io/library/alpine:latest
u334535@user-Precision-3460:~$ docker images
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
alpine        latest    706db57fb206   3 weeks ago    8.32MB
ubuntu        latest    97bed23a3497   4 weeks ago    78.1MB
hello-world   latest    1b44b5a3e06a   2 months ago   10.1kB
u334535@user-Precision-3460:~$ docker run -it alpine sh
/ # exit
u334535@user-Precision-3460:~$ docker run -it alpine sh
/ # cat /plik.txt
cat: can't open '/plik.txt': No such file or directory
/ # exit
u334535@user-Precision-3460:~$ sudo docker run -d --name web-test \
> -p 8080:80 \
> -v ~/docker-test:/usr/share/nginx/html \
> ngnx:alpine
[sudo] hasło użytkownika u334535: 
Unable to find image '8080:80' locally
docker: Error response from daemon: pull access denied for 8080, repository does not exist or may require 'docker login': denied: requested access to the resource is denied

Run 'docker run --help' for more information
u334535@user-Precision-3460:~$ sudo docker run -d --name web-test > -p 8080:80 > -v ~/docker-test:/usr/share/nginx/html > nginx:alpine
Unable to find image '8080:80' locally
docker: Error response from daemon: pull access denied for 8080, repository does not exist or may require 'docker login': denied: requested access to the resource is denied

Run 'docker run --help' for more information
u334535@user-Precision-3460:~$ sudo docker run -d --name web-test > -p 8080:80 > -v ~/docker-test:/usr/share/nginx/html > nginx:alpine
Unable to find image '8080:80' locally
docker: Error response from daemon: pull access denied for 8080, repository does not exist or may require 'docker login': denied: requested access to the resource is denied

Run 'docker run --help' for more information
u334535@user-Precision-3460:~$ sudo docker run -d --name web-test -p 8080:80 -v ~/docker-test:/usr/share/nginx/html nginx:alpine
Unable to find image 'nginx:alpine' locally
alpine: Pulling from library/nginx
2d35ebdb57d9: Already exists 
8f6a6833e95d: Pull complete 
194fa24e147d: Pull complete 
3eaba6cd10a3: Pull complete 
df413d6ebdc8: Pull complete 
d9a55dab5954: Pull complete 
ff8a36d5502a: Pull complete 
bdabb0d44271: Pull complete 
Digest: sha256:b3c656d55d7ad751196f21b7fd2e8d4da9cb430e32f646adcf92441b72f82b14
Status: Downloaded newer image for nginx:alpine
4c836c4fabc7443c9b9f797f2681507e29c1b2760ff50d0eab2fc4755ef8e92e
u334535@user-Precision-3460:~$ ls
Android                docker-test  Downloads  Muzyka        ngnx:alpine  -p       postgres:15-alpine  Pulpit  Szablony  Wideo
AndroidStudioProjects  Dokumenty    -e         nginx:alpine  Obrazy       Pobrane  Publiczny           snap    -v
u334535@user-Precision-3460:~$ cd docker-test/
u334535@user-Precision-3460:~/docker-test$ ls
index.html
u334535@user-Precision-3460:~/docker-test$ echo "<h3>Update from Host</h3>" >>index.html
u334535@user-Precision-3460:~/docker-test$ sudo docker volume ls
DRIVER    VOLUME NAME
local     3bdc22614ce9c45379eca6684cc9d8688a87cfbf8a7da7871d326b515a80595f
local     ac8838120d03f3e945c85702dfa7b8f439e23db1d8b062fed8e3a3117e779da4
u334535@user-Precision-3460:~/docker-test$ sudo docker stop web-test
web-test
u334535@user-Precision-3460:~/docker-test$ sudo docker rm web-test
web-test
u334535@user-Precision-3460:~/docker-test$ docker ls
docker: unknown command: docker ls

Run 'docker --help' for more information
u334535@user-Precision-3460:~/docker-test$ docker ps
CONTAINER ID   IMAGE                COMMAND                  CREATED          STATUS          PORTS      NAMES
f884f9498e47   postgres:15-alpine   "docker-entrypoint.s…"   25 minutes ago   Up 25 minutes   5432/tcp   db-test
u334535@user-Precision-3460:~/docker-test$ sudo docker stop db-test
db-test
u334535@user-Precision-3460:~/docker-test$ sudo docker rm db-test
db-test
u334535@user-Precision-3460:~/docker-test$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
u334535@user-Precision-3460:~/docker-test$ ^C
u334535@user-Precision-3460:~/docker-test$ 













u334535@user-Precision-3460:~$ docker ps
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.51/containers/json": dial unix /var/run/docker.sock: connect: permission denied
u334535@user-Precision-3460:~$ sudo docker ps
[sudo] hasło użytkownika u334535: 
CONTAINER ID   IMAGE     COMMAND   CREATED              STATUS              PORTS     NAMES
8ec89171ca40   ubuntu    "bash"    About a minute ago   Up About a minute             frosty_newton
u334535@user-Precision-3460:~$ docker logs 8ec89171ca40
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.51/containers/8ec89171ca40/json": dial unix /var/run/docker.sock: connect: permission denied
u334535@user-Precision-3460:~$ sudo docker logs 8ec89171ca40
root@8ec89171ca40:/# whoami
root
u334535@user-Precision-3460:~$ sudo docker logs 8ec89171ca40
root@8ec89171ca40:/# whoami
root
root@8ec89171ca40:/# exit
exit
u334535@user-Precision-3460:~$ docker info
Client: Docker Engine - Community
 Version:    28.5.1
 Context:    default
 Debug Mode: false
 Plugins:
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.29.1
    Path:     /usr/libexec/docker/cli-plugins/docker-buildx
  compose: Docker Compose (Docker Inc.)
    Version:  v2.40.3
    Path:     /usr/libexec/docker/cli-plugins/docker-compose

Server:
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.51/info": dial unix /var/run/docker.sock: connect: permission denied
u334535@user-Precision-3460:~$ sudo docker info
Client: Docker Engine - Community
 Version:    28.5.1
 Context:    default
 Debug Mode: false
 Plugins:
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.29.1
    Path:     /usr/libexec/docker/cli-plugins/docker-buildx
  compose: Docker Compose (Docker Inc.)
    Version:  v2.40.3
    Path:     /usr/libexec/docker/cli-plugins/docker-compose

Server:
 Containers: 5
  Running: 1
  Paused: 0
  Stopped: 4
 Images: 3
 Server Version: 28.5.1
 Storage Driver: overlay2
  Backing Filesystem: extfs
  Supports d_type: true
  Using metacopy: false
  Native Overlay Diff: true
  userxattr: false
 Logging Driver: json-file
 Cgroup Driver: systemd
 Cgroup Version: 2
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local splunk syslog
 CDI spec directories:
  /etc/cdi
  /var/run/cdi
 Swarm: inactive
 Runtimes: io.containerd.runc.v2 runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: b98a3aace656320842a23f4a392a33f46af97866
 runc version: v1.3.0-0-g4ca628d1
 init version: de40ad0
 Security Options:
  apparmor
  seccomp
   Profile: builtin
  cgroupns
 Kernel Version: 6.14.0-34-generic
 Operating System: Ubuntu 24.04.3 LTS
 OSType: linux
 Architecture: x86_64
 CPUs: 12
 Total Memory: 15.31GiB
 Name: user-Precision-3460
 ID: cd2db5ed-8c27-4a37-83c3-440d70275150
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Experimental: false
 Insecure Registries:
  ::1/128
  127.0.0.0/8
 Live Restore Enabled: false

u334535@user-Precision-3460:~$ docker ps
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.51/containers/json": dial unix /var/run/docker.sock: connect: permission denied
u334535@user-Precision-3460:~$ sudo docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED          STATUS          PORTS     NAMES
c3a0ff690e72   alpine    "sh"      34 seconds ago   Up 34 seconds             kind_matsumoto
u334535@user-Precision-3460:~$ sudo docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED         STATUS         PORTS     NAMES
cc5567ee9cf9   alpine    "sh"      4 seconds ago   Up 4 seconds             kontener1
c3a0ff690e72   alpine    "sh"      2 minutes ago   Up 2 minutes             kind_matsumoto
u334535@user-Precision-3460:~$ sudo docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED          STATUS          PORTS     NAMES
611cefaaccae   alpine    "sh"      19 seconds ago   Up 18 seconds             kontener2
c3a0ff690e72   alpine    "sh"      3 minutes ago    Up 3 minutes              kind_matsumoto
u334535@user-Precision-3460:~$ sudo docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED              STATUS              PORTS     NAMES
a230b8996909   alpine    "sh"      About a minute ago   Up About a minute             serene_mclaren
611cefaaccae   alpine    "sh"      2 minutes ago        Up 28 seconds                 kontener2
u334535@user-Precision-3460:~$ sudo docker image history ngix:latest
Error response from daemon: No such image: ngix:latest
u334535@user-Precision-3460:~$ sudo docker pull nginx:latest
latest: Pulling from library/nginx
38513bd72563: Pull complete 
a0a6ab141558: Pull complete 
0e86847a3920: Pull complete 
1bace2083289: Pull complete 
89df300a082a: Pull complete 
35fb9ffa6621: Pull complete 
5545b08f9d26: Pull complete 
Digest: sha256:f547e3d0d5d02f7009737b284abc87d808e4252b42dceea361811e9fc606287f
Status: Downloaded newer image for nginx:latest
docker.io/library/nginx:latest
u334535@user-Precision-3460:~$ sudo docker image history nginx:latest
IMAGE          CREATED       CREATED BY                                      SIZE      COMMENT
9d0e6f6199dc   6 days ago    CMD ["nginx" "-g" "daemon off;"]                0B        buildkit.dockerfile.v0
<missing>      6 days ago    STOPSIGNAL SIGQUIT                              0B        buildkit.dockerfile.v0
<missing>      6 days ago    EXPOSE map[80/tcp:{}]                           0B        buildkit.dockerfile.v0
<missing>      6 days ago    ENTRYPOINT ["/docker-entrypoint.sh"]            0B        buildkit.dockerfile.v0
<missing>      6 days ago    COPY 30-tune-worker-processes.sh /docker-ent…   4.62kB    buildkit.dockerfile.v0
<missing>      6 days ago    COPY 20-envsubst-on-templates.sh /docker-ent…   3.02kB    buildkit.dockerfile.v0
<missing>      6 days ago    COPY 15-local-resolvers.envsh /docker-entryp…   389B      buildkit.dockerfile.v0
<missing>      6 days ago    COPY 10-listen-on-ipv6-by-default.sh /docker…   2.12kB    buildkit.dockerfile.v0
<missing>      6 days ago    COPY docker-entrypoint.sh / # buildkit          1.62kB    buildkit.dockerfile.v0
<missing>      6 days ago    RUN /bin/sh -c set -x     && groupadd --syst…   73.2MB    buildkit.dockerfile.v0
<missing>      6 days ago    ENV DYNPKG_RELEASE=1~trixie                     0B        buildkit.dockerfile.v0
<missing>      6 days ago    ENV PKG_RELEASE=1~trixie                        0B        buildkit.dockerfile.v0
<missing>      6 days ago    ENV NJS_RELEASE=1~trixie                        0B        buildkit.dockerfile.v0
<missing>      6 days ago    ENV NJS_VERSION=0.9.4                           0B        buildkit.dockerfile.v0
<missing>      6 days ago    ENV NGINX_VERSION=1.29.3                        0B        buildkit.dockerfile.v0
<missing>      6 days ago    LABEL maintainer=NGINX Docker Maintainers <d…   0B        buildkit.dockerfile.v0
<missing>      2 weeks ago   # debian.sh --arch 'amd64' out/ 'trixie' '@1…   78.6MB    debuerreotype 0.16
u334535@user-Precision-3460:~$ sudo docker images
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
nginx         latest    9d0e6f6199dc   6 days ago     152MB
alpine        latest    706db57fb206   3 weeks ago    8.32MB
ubuntu        latest    97bed23a3497   4 weeks ago    78.1MB
hello-world   latest    1b44b5a3e06a   2 months ago   10.1kB
u334535@user-Precision-3460:~$ sudo docker run -d --name db-test \
> -e PoSTGRES_PASSWORD=secret \
> postgres:15-alpine
Unable to find image 'postgres:15-alpine' locally
15-alpine: Pulling from library/postgres
2d35ebdb57d9: Already exists 
d7cf304fb91a: Pull complete 
01a8e1e8a6d3: Pull complete 
c8d6a201b2ea: Pull complete 
665050181beb: Pull complete 
e7d8b5a29e19: Pull complete 
b7a5b6d84454: Pull complete 
8e7af31e0abd: Pull complete 
0a297d5cb757: Pull complete 
78753f2bcd40: Pull complete 
9229d0c336e2: Pull complete 
Digest: sha256:64583b3cb4f2010277bdd9749456de78e5c36f8956466ba14b0b96922e510950
Status: Downloaded newer image for postgres:15-alpine
523605f6dd0a9e3717192bd8df86efcd3ad99eec3d4e71c6e9080ed7b7a8eef1
u334535@user-Precision-3460:~$ sudo docker images
REPOSITORY    TAG         IMAGE ID       CREATED        SIZE
nginx         latest      9d0e6f6199dc   6 days ago     152MB
postgres      15-alpine   ba05c11fe977   2 weeks ago    273MB
alpine        latest      706db57fb206   3 weeks ago    8.32MB
ubuntu        latest      97bed23a3497   4 weeks ago    78.1MB
hello-world   latest      1b44b5a3e06a   2 months ago   10.1kB
u334535@user-Precision-3460:~$ sudo docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
u334535@user-Precision-3460:~$ sudo docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
u334535@user-Precision-3460:~$ sudo docker run -d --name db-test \
> -e POSTGRES_PASSWORD=secret \
> postgres:15-alpine
docker: invalid reference format: repository name (library/POSTGRES_PASSWORD=secret) must be lowercase

Run 'docker run --help' for more information
u334535@user-Precision-3460:~$ sudo docker run -d --name db-test -e POSTGRES_PASSWORD=secret postgres:15-alpine
docker: Error response from daemon: Conflict. The container name "/db-test" is already in use by container "523605f6dd0a9e3717192bd8df86efcd3ad99eec3d4e71c6e9080ed7b7a8eef1". You have to remove (or rename) that container to be able to reuse that name.

Run 'docker run --help' for more information
u334535@user-Precision-3460:~$ sudo docker exec -it db-test psql -U postgres
Error response from daemon: container 523605f6dd0a9e3717192bd8df86efcd3ad99eec3d4e71c6e9080ed7b7a8eef1 is not running
u334535@user-Precision-3460:~$ docker rm db-test
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Delete "http://%2Fvar%2Frun%2Fdocker.sock/v1.51/containers/db-test": dial unix /var/run/docker.sock: connect: permission denied
u334535@user-Precision-3460:~$ sudo docker rm db-test
db-test
u334535@user-Precision-3460:~$ sudo docker run -d --name db-test -e POSTGRES_PASSWORD=secret postgres:15-alpine
f884f9498e47fb79d96c93bd084591b5d210c183f1c6ba3ecf6af1239c41ee1d
u334535@user-Precision-3460:~$ sudo docker exec -it db-test psql -U postgres
psql (15.14)
Type "help" for help.

postgres=# \q
u334535@user-Precision-3460:~$ sudo docker volume create postgres-data
postgres-data
u334535@user-Precision-3460:~$ sudo docker ps
CONTAINER ID   IMAGE                COMMAND                  CREATED              STATUS              PORTS      NAMES
f884f9498e47   postgres:15-alpine   "docker-entrypoint.s…"   About a minute ago   Up About a minute   5432/tcp   db-test
u334535@user-Precision-3460:~$ sudo docker start db-test
db-test
u334535@user-Precision-3460:~$ sudo docker exec -it db-test sh
/ # psql -U postgres
psql (15.14)
Type "help" for help.

postgres=# SHOW config_file;
               config_file                
------------------------------------------
 /var/lib/postgresql/data/postgresql.conf
(1 row)

postgres=# \q
/ # cat /var/lib/postgresql/data/postgresql.conf
# -----------------------------
# PostgreSQL configuration file
# -----------------------------
#
# This file consists of lines of the form:
#
#   name = value
#
# (The "=" is optional.)  Whitespace may be used.  Comments are introduced with
# "#" anywhere on a line.  The complete list of parameter names and allowed
# values can be found in the PostgreSQL documentation.
#
# The commented-out settings shown in this file represent the default values.
# Re-commenting a setting is NOT sufficient to revert it to the default value;
# you need to reload the server.
#
# This file is read on server startup and when the server receives a SIGHUP
# signal.  If you edit the file on a running system, you have to SIGHUP the
# server for the changes to take effect, run "pg_ctl reload", or execute
# "SELECT pg_reload_conf()".  Some parameters, which are marked below,
# require a server shutdown and restart to take effect.
#
# Any parameter can also be given as a command-line option to the server, e.g.,
# "postgres -c log_connections=on".  Some parameters can be changed at run time
# with the "SET" SQL command.
#
# Memory units:  B  = bytes            Time units:  us  = microseconds
#                kB = kilobytes                     ms  = milliseconds
#                MB = megabytes                     s   = seconds
#                GB = gigabytes                     min = minutes
#                TB = terabytes                     h   = hours
#                                                   d   = days


#------------------------------------------------------------------------------
# FILE LOCATIONS
#------------------------------------------------------------------------------

# The default values of these variables are driven from the -D command-line
# option or PGDATA environment variable, represented here as ConfigDir.

#data_directory = 'ConfigDir'		# use data in another directory
					# (change requires restart)
#hba_file = 'ConfigDir/pg_hba.conf'	# host-based authentication file
					# (change requires restart)
#ident_file = 'ConfigDir/pg_ident.conf'	# ident configuration file
					# (change requires restart)

# If external_pid_file is not explicitly set, no extra PID file is written.
#external_pid_file = ''			# write an extra PID file
					# (change requires restart)


#------------------------------------------------------------------------------
# CONNECTIONS AND AUTHENTICATION
#------------------------------------------------------------------------------

# - Connection Settings -

listen_addresses = '*'
					# comma-separated list of addresses;
					# defaults to 'localhost'; use '*' for all
					# (change requires restart)
#port = 5432				# (change requires restart)
max_connections = 100			# (change requires restart)
#superuser_reserved_connections = 3	# (change requires restart)
#unix_socket_directories = '/var/run/postgresql'	# comma-separated list of directories
					# (change requires restart)
#unix_socket_group = ''			# (change requires restart)
#unix_socket_permissions = 0777		# begin with 0 to use octal notation
					# (change requires restart)
#bonjour = off				# advertise server via Bonjour
					# (change requires restart)
#bonjour_name = ''			# defaults to the computer name
					# (change requires restart)

# - TCP settings -
# see "man tcp" for details

#tcp_keepalives_idle = 0		# TCP_KEEPIDLE, in seconds;
					# 0 selects the system default
#tcp_keepalives_interval = 0		# TCP_KEEPINTVL, in seconds;
					# 0 selects the system default
#tcp_keepalives_count = 0		# TCP_KEEPCNT;
					# 0 selects the system default
#tcp_user_timeout = 0			# TCP_USER_TIMEOUT, in milliseconds;
					# 0 selects the system default

#client_connection_check_interval = 0	# time between checks for client
					# disconnection while running queries;
					# 0 for never

# - Authentication -

#authentication_timeout = 1min		# 1s-600s
#password_encryption = scram-sha-256	# scram-sha-256 or md5
#db_user_namespace = off

# GSSAPI using Kerberos
#krb_server_keyfile = 'FILE:${sysconfdir}/krb5.keytab'
#krb_caseins_users = off

# - SSL -

#ssl = off
#ssl_ca_file = ''
#ssl_cert_file = 'server.crt'
#ssl_crl_file = ''
#ssl_crl_dir = ''
#ssl_key_file = 'server.key'
#ssl_ciphers = 'HIGH:MEDIUM:+3DES:!aNULL' # allowed SSL ciphers
#ssl_prefer_server_ciphers = on
#ssl_ecdh_curve = 'prime256v1'
#ssl_min_protocol_version = 'TLSv1.2'
#ssl_max_protocol_version = ''
#ssl_dh_params_file = ''
#ssl_passphrase_command = ''
#ssl_passphrase_command_supports_reload = off


#------------------------------------------------------------------------------
# RESOURCE USAGE (except WAL)
#------------------------------------------------------------------------------

# - Memory -

shared_buffers = 128MB			# min 128kB
					# (change requires restart)
#huge_pages = try			# on, off, or try
					# (change requires restart)
#huge_page_size = 0			# zero for system default
					# (change requires restart)
#temp_buffers = 8MB			# min 800kB
#max_prepared_transactions = 0		# zero disables the feature
					# (change requires restart)
# Caution: it is not advisable to set max_prepared_transactions nonzero unless
# you actively intend to use prepared transactions.
#work_mem = 4MB				# min 64kB
#hash_mem_multiplier = 2.0		# 1-1000.0 multiplier on hash table work_mem
#maintenance_work_mem = 64MB		# min 1MB
#autovacuum_work_mem = -1		# min 1MB, or -1 to use maintenance_work_mem
#logical_decoding_work_mem = 64MB	# min 64kB
#max_stack_depth = 2MB			# min 100kB
#shared_memory_type = mmap		# the default is the first option
					# supported by the operating system:
					#   mmap
					#   sysv
					#   windows
					# (change requires restart)
dynamic_shared_memory_type = posix	# the default is usually the first option
					# supported by the operating system:
					#   posix
					#   sysv
					#   windows
					#   mmap
					# (change requires restart)
#min_dynamic_shared_memory = 0MB	# (change requires restart)

# - Disk -

#temp_file_limit = -1			# limits per-process temp file space
					# in kilobytes, or -1 for no limit

# - Kernel Resources -

#max_files_per_process = 1000		# min 64
					# (change requires restart)

# - Cost-Based Vacuum Delay -

#vacuum_cost_delay = 0			# 0-100 milliseconds (0 disables)
#vacuum_cost_page_hit = 1		# 0-10000 credits
#vacuum_cost_page_miss = 2		# 0-10000 credits
#vacuum_cost_page_dirty = 20		# 0-10000 credits
#vacuum_cost_limit = 200		# 1-10000 credits

# - Background Writer -

#bgwriter_delay = 200ms			# 10-10000ms between rounds
#bgwriter_lru_maxpages = 100		# max buffers written/round, 0 disables
#bgwriter_lru_multiplier = 2.0		# 0-10.0 multiplier on buffers scanned/round
#bgwriter_flush_after = 512kB		# measured in pages, 0 disables

# - Asynchronous Behavior -

#backend_flush_after = 0		# measured in pages, 0 disables
#effective_io_concurrency = 1		# 1-1000; 0 disables prefetching
#maintenance_io_concurrency = 10	# 1-1000; 0 disables prefetching
#max_worker_processes = 8		# (change requires restart)
#max_parallel_workers_per_gather = 2	# limited by max_parallel_workers
#max_parallel_maintenance_workers = 2	# limited by max_parallel_workers
#max_parallel_workers = 8		# number of max_worker_processes that
					# can be used in parallel operations
#parallel_leader_participation = on
#old_snapshot_threshold = -1		# 1min-60d; -1 disables; 0 is immediate
					# (change requires restart)


#------------------------------------------------------------------------------
# WRITE-AHEAD LOG
#------------------------------------------------------------------------------

# - Settings -

#wal_level = replica			# minimal, replica, or logical
					# (change requires restart)
#fsync = on				# flush data to disk for crash safety
					# (turning this off can cause
					# unrecoverable data corruption)
#synchronous_commit = on		# synchronization level;
					# off, local, remote_write, remote_apply, or on
#wal_sync_method = fsync		# the default is the first option
					# supported by the operating system:
					#   open_datasync
					#   fdatasync (default on Linux and FreeBSD)
					#   fsync
					#   fsync_writethrough
					#   open_sync
#full_page_writes = on			# recover from partial page writes
#wal_log_hints = off			# also do full page writes of non-critical updates
					# (change requires restart)
#wal_compression = off			# enables compression of full-page writes;
					# off, pglz, lz4, zstd, or on
#wal_init_zero = on			# zero-fill new WAL files
#wal_recycle = on			# recycle WAL files
#wal_buffers = -1			# min 32kB, -1 sets based on shared_buffers
					# (change requires restart)
#wal_writer_delay = 200ms		# 1-10000 milliseconds
#wal_writer_flush_after = 1MB		# measured in pages, 0 disables
#wal_skip_threshold = 2MB

#commit_delay = 0			# range 0-100000, in microseconds
#commit_siblings = 5			# range 1-1000

# - Checkpoints -

#checkpoint_timeout = 5min		# range 30s-1d
#checkpoint_completion_target = 0.9	# checkpoint target duration, 0.0 - 1.0
#checkpoint_flush_after = 256kB		# measured in pages, 0 disables
#checkpoint_warning = 30s		# 0 disables
max_wal_size = 1GB
min_wal_size = 80MB

# - Prefetching during recovery -

#recovery_prefetch = try		# prefetch pages referenced in the WAL?
#wal_decode_buffer_size = 512kB		# lookahead window used for prefetching
					# (change requires restart)

# - Archiving -

#archive_mode = off		# enables archiving; off, on, or always
				# (change requires restart)
#archive_library = ''		# library to use to archive a logfile segment
				# (empty string indicates archive_command should
				# be used)
#archive_command = ''		# command to use to archive a logfile segment
				# placeholders: %p = path of file to archive
				#               %f = file name only
				# e.g. 'test ! -f /mnt/server/archivedir/%f && cp %p /mnt/server/archivedir/%f'
#archive_timeout = 0		# force a logfile segment switch after this
				# number of seconds; 0 disables

# - Archive Recovery -

# These are only used in recovery mode.

#restore_command = ''		# command to use to restore an archived logfile segment
				# placeholders: %p = path of file to restore
				#               %f = file name only
				# e.g. 'cp /mnt/server/archivedir/%f %p'
#archive_cleanup_command = ''	# command to execute at every restartpoint
#recovery_end_command = ''	# command to execute at completion of recovery

# - Recovery Target -

# Set these only when performing a targeted recovery.

#recovery_target = ''		# 'immediate' to end recovery as soon as a
                                # consistent state is reached
				# (change requires restart)
#recovery_target_name = ''	# the named restore point to which recovery will proceed
				# (change requires restart)
#recovery_target_time = ''	# the time stamp up to which recovery will proceed
				# (change requires restart)
#recovery_target_xid = ''	# the transaction ID up to which recovery will proceed
				# (change requires restart)
#recovery_target_lsn = ''	# the WAL LSN up to which recovery will proceed
				# (change requires restart)
#recovery_target_inclusive = on # Specifies whether to stop:
				# just after the specified recovery target (on)
				# just before the recovery target (off)
				# (change requires restart)
#recovery_target_timeline = 'latest'	# 'current', 'latest', or timeline ID
				# (change requires restart)
#recovery_target_action = 'pause'	# 'pause', 'promote', 'shutdown'
				# (change requires restart)


#------------------------------------------------------------------------------
# REPLICATION
#------------------------------------------------------------------------------

# - Sending Servers -

# Set these on the primary and on any standby that will send replication data.

#max_wal_senders = 10		# max number of walsender processes
				# (change requires restart)
#max_replication_slots = 10	# max number of replication slots
				# (change requires restart)
#wal_keep_size = 0		# in megabytes; 0 disables
#max_slot_wal_keep_size = -1	# in megabytes; -1 disables
#wal_sender_timeout = 60s	# in milliseconds; 0 disables
#track_commit_timestamp = off	# collect timestamp of transaction commit
				# (change requires restart)

# - Primary Server -

# These settings are ignored on a standby server.

#synchronous_standby_names = ''	# standby servers that provide sync rep
				# method to choose sync standbys, number of sync standbys,
				# and comma-separated list of application_name
				# from standby(s); '*' = all
#vacuum_defer_cleanup_age = 0	# number of xacts by which cleanup is delayed

# - Standby Servers -

# These settings are ignored on a primary server.

#primary_conninfo = ''			# connection string to sending server
#primary_slot_name = ''			# replication slot on sending server
#promote_trigger_file = ''		# file name whose presence ends recovery
#hot_standby = on			# "off" disallows queries during recovery
					# (change requires restart)
#max_standby_archive_delay = 30s	# max delay before canceling queries
					# when reading WAL from archive;
					# -1 allows indefinite delay
#max_standby_streaming_delay = 30s	# max delay before canceling queries
					# when reading streaming WAL;
					# -1 allows indefinite delay
#wal_receiver_create_temp_slot = off	# create temp slot if primary_slot_name
					# is not set
#wal_receiver_status_interval = 10s	# send replies at least this often
					# 0 disables
#hot_standby_feedback = off		# send info from standby to prevent
					# query conflicts
#wal_receiver_timeout = 60s		# time that receiver waits for
					# communication from primary
					# in milliseconds; 0 disables
#wal_retrieve_retry_interval = 5s	# time to wait before retrying to
					# retrieve WAL after a failed attempt
#recovery_min_apply_delay = 0		# minimum delay for applying changes during recovery

# - Subscribers -

# These settings are ignored on a publisher.

#max_logical_replication_workers = 4	# taken from max_worker_processes
					# (change requires restart)
#max_sync_workers_per_subscription = 2	# taken from max_logical_replication_workers


#------------------------------------------------------------------------------
# QUERY TUNING
#------------------------------------------------------------------------------

# - Planner Method Configuration -

#enable_async_append = on
#enable_bitmapscan = on
#enable_gathermerge = on
#enable_hashagg = on
#enable_hashjoin = on
#enable_incremental_sort = on
#enable_indexscan = on
#enable_indexonlyscan = on
#enable_material = on
#enable_memoize = on
#enable_mergejoin = on
#enable_nestloop = on
#enable_parallel_append = on
#enable_parallel_hash = on
#enable_partition_pruning = on
#enable_partitionwise_join = off
#enable_partitionwise_aggregate = off
#enable_seqscan = on
#enable_sort = on
#enable_tidscan = on

# - Planner Cost Constants -

#seq_page_cost = 1.0			# measured on an arbitrary scale
#random_page_cost = 4.0			# same scale as above
#cpu_tuple_cost = 0.01			# same scale as above
#cpu_index_tuple_cost = 0.005		# same scale as above
#cpu_operator_cost = 0.0025		# same scale as above
#parallel_setup_cost = 1000.0	# same scale as above
#parallel_tuple_cost = 0.1		# same scale as above
#min_parallel_table_scan_size = 8MB
#min_parallel_index_scan_size = 512kB
#effective_cache_size = 4GB

#jit_above_cost = 100000		# perform JIT compilation if available
					# and query more expensive than this;
					# -1 disables
#jit_inline_above_cost = 500000		# inline small functions if query is
					# more expensive than this; -1 disables
#jit_optimize_above_cost = 500000	# use expensive JIT optimizations if
					# query is more expensive than this;
					# -1 disables

# - Genetic Query Optimizer -

#geqo = on
#geqo_threshold = 12
#geqo_effort = 5			# range 1-10
#geqo_pool_size = 0			# selects default based on effort
#geqo_generations = 0			# selects default based on effort
#geqo_selection_bias = 2.0		# range 1.5-2.0
#geqo_seed = 0.0			# range 0.0-1.0

# - Other Planner Options -

#default_statistics_target = 100	# range 1-10000
#constraint_exclusion = partition	# on, off, or partition
#cursor_tuple_fraction = 0.1		# range 0.0-1.0
#from_collapse_limit = 8
#jit = on				# allow JIT compilation
#join_collapse_limit = 8		# 1 disables collapsing of explicit
					# JOIN clauses
#plan_cache_mode = auto			# auto, force_generic_plan or
					# force_custom_plan
#recursive_worktable_factor = 10.0	# range 0.001-1000000


#------------------------------------------------------------------------------
# REPORTING AND LOGGING
#------------------------------------------------------------------------------

# - Where to Log -

#log_destination = 'stderr'		# Valid values are combinations of
					# stderr, csvlog, jsonlog, syslog, and
					# eventlog, depending on platform.
					# csvlog and jsonlog require
					# logging_collector to be on.

# This is used when logging to stderr:
#logging_collector = off		# Enable capturing of stderr, jsonlog,
					# and csvlog into log files. Required
					# to be on for csvlogs and jsonlogs.
					# (change requires restart)

# These are only used if logging_collector is on:
#log_directory = 'log'			# directory where log files are written,
					# can be absolute or relative to PGDATA
#log_filename = 'postgresql-%Y-%m-%d_%H%M%S.log'	# log file name pattern,
					# can include strftime() escapes
#log_file_mode = 0600			# creation mode for log files,
					# begin with 0 to use octal notation
#log_rotation_age = 1d			# Automatic rotation of logfiles will
					# happen after that time.  0 disables.
#log_rotation_size = 10MB		# Automatic rotation of logfiles will
					# happen after that much log output.
					# 0 disables.
#log_truncate_on_rotation = off		# If on, an existing log file with the
					# same name as the new log file will be
					# truncated rather than appended to.
					# But such truncation only occurs on
					# time-driven rotation, not on restarts
					# or size-driven rotation.  Default is
					# off, meaning append to existing files
					# in all cases.

# These are relevant when logging to syslog:
#syslog_facility = 'LOCAL0'
#syslog_ident = 'postgres'
#syslog_sequence_numbers = on
#syslog_split_messages = on

# This is only relevant when logging to eventlog (Windows):
# (change requires restart)
#event_source = 'PostgreSQL'

# - When to Log -

#log_min_messages = warning		# values in order of decreasing detail:
					#   debug5
					#   debug4
					#   debug3
					#   debug2
					#   debug1
					#   info
					#   notice
					#   warning
					#   error
					#   log
					#   fatal
					#   panic

#log_min_error_statement = error	# values in order of decreasing detail:
					#   debug5
					#   debug4
					#   debug3
					#   debug2
					#   debug1
					#   info
					#   notice
					#   warning
					#   error
					#   log
					#   fatal
					#   panic (effectively off)

#log_min_duration_statement = -1	# -1 is disabled, 0 logs all statements
					# and their durations, > 0 logs only
					# statements running at least this number
					# of milliseconds

#log_min_duration_sample = -1		# -1 is disabled, 0 logs a sample of statements
					# and their durations, > 0 logs only a sample of
					# statements running at least this number
					# of milliseconds;
					# sample fraction is determined by log_statement_sample_rate

#log_statement_sample_rate = 1.0	# fraction of logged statements exceeding
					# log_min_duration_sample to be logged;
					# 1.0 logs all such statements, 0.0 never logs


#log_transaction_sample_rate = 0.0	# fraction of transactions whose statements
					# are logged regardless of their duration; 1.0 logs all
					# statements from all transactions, 0.0 never logs

#log_startup_progress_interval = 10s	# Time between progress updates for
					# long-running startup operations.
					# 0 disables the feature, > 0 indicates
					# the interval in milliseconds.

# - What to Log -

#debug_print_parse = off
#debug_print_rewritten = off
#debug_print_plan = off
#debug_pretty_print = on
#log_autovacuum_min_duration = 10min	# log autovacuum activity;
					# -1 disables, 0 logs all actions and
					# their durations, > 0 logs only
					# actions running at least this number
					# of milliseconds.
#log_checkpoints = on
#log_connections = off
#log_disconnections = off
#log_duration = off
#log_error_verbosity = default		# terse, default, or verbose messages
#log_hostname = off
#log_line_prefix = '%m [%p] '		# special values:
					#   %a = application name
					#   %u = user name
					#   %d = database name
					#   %r = remote host and port
					#   %h = remote host
					#   %b = backend type
					#   %p = process ID
					#   %P = process ID of parallel group leader
					#   %t = timestamp without milliseconds
					#   %m = timestamp with milliseconds
					#   %n = timestamp with milliseconds (as a Unix epoch)
					#   %Q = query ID (0 if none or not computed)
					#   %i = command tag
					#   %e = SQL state
					#   %c = session ID
					#   %l = session line number
					#   %s = session start timestamp
					#   %v = virtual transaction ID
					#   %x = transaction ID (0 if none)
					#   %q = stop here in non-session
					#        processes
					#   %% = '%'
					# e.g. '<%u%%%d> '
#log_lock_waits = off			# log lock waits >= deadlock_timeout
#log_recovery_conflict_waits = off	# log standby recovery conflict waits
					# >= deadlock_timeout
#log_parameter_max_length = -1		# when logging statements, limit logged
					# bind-parameter values to N bytes;
					# -1 means print in full, 0 disables
#log_parameter_max_length_on_error = 0	# when logging an error, limit logged
					# bind-parameter values to N bytes;
					# -1 means print in full, 0 disables
#log_statement = 'none'			# none, ddl, mod, all
#log_replication_commands = off
#log_temp_files = -1			# log temporary files equal or larger
					# than the specified size in kilobytes;
					# -1 disables, 0 logs all temp files
log_timezone = 'UTC'


#------------------------------------------------------------------------------
# PROCESS TITLE
#------------------------------------------------------------------------------

#cluster_name = ''			# added to process titles if nonempty
					# (change requires restart)
#update_process_title = on


#------------------------------------------------------------------------------
# STATISTICS
#------------------------------------------------------------------------------

# - Cumulative Query and Index Statistics -

#track_activities = on
#track_activity_query_size = 1024	# (change requires restart)
#track_counts = on
#track_io_timing = off
#track_wal_io_timing = off
#track_functions = none			# none, pl, all
#stats_fetch_consistency = cache


# - Monitoring -

#compute_query_id = auto
#log_statement_stats = off
#log_parser_stats = off
#log_planner_stats = off
#log_executor_stats = off


#------------------------------------------------------------------------------
# AUTOVACUUM
#------------------------------------------------------------------------------

#autovacuum = on			# Enable autovacuum subprocess?  'on'
					# requires track_counts to also be on.
#autovacuum_max_workers = 3		# max number of autovacuum subprocesses
					# (change requires restart)
#autovacuum_naptime = 1min		# time between autovacuum runs
#autovacuum_vacuum_threshold = 50	# min number of row updates before
					# vacuum
#autovacuum_vacuum_insert_threshold = 1000	# min number of row inserts
					# before vacuum; -1 disables insert
					# vacuums
#autovacuum_analyze_threshold = 50	# min number of row updates before
					# analyze
#autovacuum_vacuum_scale_factor = 0.2	# fraction of table size before vacuum
#autovacuum_vacuum_insert_scale_factor = 0.2	# fraction of inserts over table
					# size before insert vacuum
#autovacuum_analyze_scale_factor = 0.1	# fraction of table size before analyze
#autovacuum_freeze_max_age = 200000000	# maximum XID age before forced vacuum
					# (change requires restart)
#autovacuum_multixact_freeze_max_age = 400000000	# maximum multixact age
					# before forced vacuum
					# (change requires restart)
#autovacuum_vacuum_cost_delay = 2ms	# default vacuum cost delay for
					# autovacuum, in milliseconds;
					# -1 means use vacuum_cost_delay
#autovacuum_vacuum_cost_limit = -1	# default vacuum cost limit for
					# autovacuum, -1 means use
					# vacuum_cost_limit


#------------------------------------------------------------------------------
# CLIENT CONNECTION DEFAULTS
#------------------------------------------------------------------------------

# - Statement Behavior -

#client_min_messages = notice		# values in order of decreasing detail:
					#   debug5
					#   debug4
					#   debug3
					#   debug2
					#   debug1
					#   log
					#   notice
					#   warning
					#   error
#search_path = '"$user", public'	# schema names
#row_security = on
#default_table_access_method = 'heap'
#default_tablespace = ''		# a tablespace name, '' uses the default
#default_toast_compression = 'pglz'	# 'pglz' or 'lz4'
#temp_tablespaces = ''			# a list of tablespace names, '' uses
					# only default tablespace
#check_function_bodies = on
#default_transaction_isolation = 'read committed'
#default_transaction_read_only = off
#default_transaction_deferrable = off
#session_replication_role = 'origin'
#statement_timeout = 0			# in milliseconds, 0 is disabled
#lock_timeout = 0			# in milliseconds, 0 is disabled
#idle_in_transaction_session_timeout = 0	# in milliseconds, 0 is disabled
#idle_session_timeout = 0		# in milliseconds, 0 is disabled
#vacuum_freeze_table_age = 150000000
#vacuum_freeze_min_age = 50000000
#vacuum_failsafe_age = 1600000000
#vacuum_multixact_freeze_table_age = 150000000
#vacuum_multixact_freeze_min_age = 5000000
#vacuum_multixact_failsafe_age = 1600000000
#bytea_output = 'hex'			# hex, escape
#xmlbinary = 'base64'
#xmloption = 'content'
#gin_pending_list_limit = 4MB

# - Locale and Formatting -

datestyle = 'iso, mdy'
#intervalstyle = 'postgres'
timezone = 'UTC'
#timezone_abbreviations = 'Default'     # Select the set of available time zone
					# abbreviations.  Currently, there are
					#   Default
					#   Australia (historical usage)
					#   India
					# You can create your own file in
					# share/timezonesets/.
#extra_float_digits = 1			# min -15, max 3; any value >0 actually
					# selects precise output mode
#client_encoding = sql_ascii		# actually, defaults to database
					# encoding

# These settings are initialized by initdb, but they can be changed.
lc_messages = 'en_US.utf8'			# locale for system error message
					# strings
lc_monetary = 'en_US.utf8'			# locale for monetary formatting
lc_numeric = 'en_US.utf8'			# locale for number formatting
lc_time = 'en_US.utf8'				# locale for time formatting

# default configuration for text search
default_text_search_config = 'pg_catalog.english'

# - Shared Library Preloading -

#local_preload_libraries = ''
#session_preload_libraries = ''
#shared_preload_libraries = ''	# (change requires restart)
#jit_provider = 'llvmjit'		# JIT library to use

# - Other Defaults -

#dynamic_library_path = '$libdir'
#gin_fuzzy_search_limit = 0


#------------------------------------------------------------------------------
# LOCK MANAGEMENT
#------------------------------------------------------------------------------

#deadlock_timeout = 1s
#max_locks_per_transaction = 64		# min 10
					# (change requires restart)
#max_pred_locks_per_transaction = 64	# min 10
					# (change requires restart)
#max_pred_locks_per_relation = -2	# negative values mean
					# (max_pred_locks_per_transaction
					#  / -max_pred_locks_per_relation) - 1
#max_pred_locks_per_page = 2            # min 0


#------------------------------------------------------------------------------
# VERSION AND PLATFORM COMPATIBILITY
#------------------------------------------------------------------------------

# - Previous PostgreSQL Versions -

#array_nulls = on
#backslash_quote = safe_encoding	# on, off, or safe_encoding
#escape_string_warning = on
#lo_compat_privileges = off
#quote_all_identifiers = off
#standard_conforming_strings = on
#synchronize_seqscans = on

# - Other Platforms and Clients -

#transform_null_equals = off


#------------------------------------------------------------------------------
# ERROR HANDLING
#------------------------------------------------------------------------------

#exit_on_error = off			# terminate session on any error?
#restart_after_crash = on		# reinitialize after backend crash?
#data_sync_retry = off			# retry or panic on failure to fsync
					# data?
					# (change requires restart)
#recovery_init_sync_method = fsync	# fsync, syncfs (Linux 5.8+)


#------------------------------------------------------------------------------
# CONFIG FILE INCLUDES
#------------------------------------------------------------------------------

# These options allow settings to be loaded from files other than the
# default postgresql.conf.  Note that these are directives, not variable
# assignments, so they can usefully be given more than once.

#include_dir = '...'			# include files ending in '.conf' from
					# a directory, e.g., 'conf.d'
#include_if_exists = '...'		# include file only if it exists
#include = '...'			# include file


#------------------------------------------------------------------------------
# CUSTOMIZED OPTIONS
#------------------------------------------------------------------------------

# Add settings for extensions here
/ # ls -ls /var/lib/postgresql/data
total 128
     4 -rw-------    1 postgres postgres         3 Nov  4 10:03 PG_VERSION
     4 drwx------    5 postgres postgres      4096 Nov  4 10:03 base
     4 drwx------    2 postgres postgres      4096 Nov  4 10:06 global
     4 drwx------    2 postgres postgres      4096 Nov  4 10:03 pg_commit_ts
     4 drwx------    2 postgres postgres      4096 Nov  4 10:03 pg_dynshmem
     8 -rw-------    1 postgres postgres      4821 Nov  4 10:03 pg_hba.conf
     4 -rw-------    1 postgres postgres      1636 Nov  4 10:03 pg_ident.conf
     4 drwx------    4 postgres postgres      4096 Nov  4 10:08 pg_logical
     4 drwx------    4 postgres postgres      4096 Nov  4 10:03 pg_multixact
     4 drwx------    2 postgres postgres      4096 Nov  4 10:03 pg_notify
     4 drwx------    2 postgres postgres      4096 Nov  4 10:03 pg_replslot
     4 drwx------    2 postgres postgres      4096 Nov  4 10:03 pg_serial
     4 drwx------    2 postgres postgres      4096 Nov  4 10:03 pg_snapshots
     4 drwx------    2 postgres postgres      4096 Nov  4 10:03 pg_stat
     4 drwx------    2 postgres postgres      4096 Nov  4 10:03 pg_stat_tmp
     4 drwx------    2 postgres postgres      4096 Nov  4 10:03 pg_subtrans
     4 drwx------    2 postgres postgres      4096 Nov  4 10:03 pg_tblspc
     4 drwx------    2 postgres postgres      4096 Nov  4 10:03 pg_twophase
     4 drwx------    3 postgres postgres      4096 Nov  4 10:03 pg_wal
     4 drwx------    2 postgres postgres      4096 Nov  4 10:03 pg_xact
     4 -rw-------    1 postgres postgres        88 Nov  4 10:03 postgresql.auto.conf
    32 -rw-------    1 postgres postgres     29400 Nov  4 10:03 postgresql.conf
     4 -rw-------    1 postgres postgres        24 Nov  4 10:03 postmaster.opts
     4 -rw-------    1 postgres postgres        94 Nov  4 10:03 postmaster.pid
/ # exit
u334535@user-Precision-3460:~$ sudo docker run -d --name db-persistent -e POSTGRES_PASSWORD=secret -v postgres-data:/var/lib/postgresql/data postgres:15-alpine
cc54f10428841fdbd230bc191af0013638aa17b9138919dbf65ee8cc6d6f8db0
u334535@user-Precision-3460:~$ sudo docker ps
CONTAINER ID   IMAGE                COMMAND                  CREATED          STATUS          PORTS      NAMES
cc54f1042884   postgres:15-alpine   "docker-entrypoint.s…"   16 seconds ago   Up 16 seconds   5432/tcp   db-persistent
f884f9498e47   postgres:15-alpine   "docker-entrypoint.s…"   9 minutes ago    Up 9 minutes    5432/tcp   db-test
u334535@user-Precision-3460:~$ sudo docker volume ls
DRIVER    VOLUME NAME
local     3bdc22614ce9c45379eca6684cc9d8688a87cfbf8a7da7871d326b515a80595f
local     ac8838120d03f3e945c85702dfa7b8f439e23db1d8b062fed8e3a3117e779da4
local     postgres-data
u334535@user-Precision-3460:~$ sudo docekr exec -it db-persistent psql -U postgres
sudo: docekr: nie znaleziono polecenia
u334535@user-Precision-3460:~$ sudo docker exec -it db-persistent psql -U postgres
psql (15.14)
Type "help" for help.

postgres=# CREATE TABLE users (id INT, name VARCHAR(50));
CREATE TABLE
postgres=# INSERT INTO users VALUES (1,'Alicja'),(2,'Krzysztof');
INSERT 0 2
postgres=# SELECT * FROM users
postgres-# ;
 id |   name    
----+-----------
  1 | Alicja
  2 | Krzysztof
(2 rows)

postgres=# \q
u334535@user-Precision-3460:~$ sudo docker stop db-persistent
db-persistent
u334535@user-Precision-3460:~$ sudo docker rm db-persistent
db-persistent
u334535@user-Precision-3460:~$ sudo docker run -d --name db-persistent -e POSTGRES_PASSWORD=secret -v postgres-data:/var/lib/postgresql/data postgres:15-alpine
6699faab20246d364ea8883773a3f6a770b5447ea65f859292c1651fa843ae12
u334535@user-Precision-3460:~$ sudo docker exec -it db-persistent psql -U postgres
psql (15.14)
Type "help" for help.

postgres=# SELECT * FROM usersl
postgres-# SELECT * FROM users;
ERROR:  syntax error at or near "SELECT"
LINE 2: SELECT * FROM users;
        ^
postgres=# SELECT * FROM usersl
SELECT * FROM users;
ERROR:  syntax error at or near "SELECT"
LINE 2: SELECT * FROM users;
        ^
postgres=# ;
postgres=# SELECT * FROM users;
 id |   name    
----+-----------
  1 | Alicja
  2 | Krzysztof
(2 rows)

postgres=# \q
u334535@user-Precision-3460:~$ sudo docker volume ls
DRIVER    VOLUME NAME
local     3bdc22614ce9c45379eca6684cc9d8688a87cfbf8a7da7871d326b515a80595f
local     ac8838120d03f3e945c85702dfa7b8f439e23db1d8b062fed8e3a3117e779da4
local     postgres-data
u334535@user-Precision-3460:~$ sudo docker volume inspect postgres-data
[
    {
        "CreatedAt": "2025-11-04T10:04:52Z",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/postgres-data/_data",
        "Name": "postgres-data",
        "Options": null,
        "Scope": "local"
    }
]
u334535@user-Precision-3460:~$ sudo docker volume rm postgres-data
Error response from daemon: remove postgres-data: volume is in use - [6699faab20246d364ea8883773a3f6a770b5447ea65f859292c1651fa843ae12]
u334535@user-Precision-3460:~$ sudo docker stop db-persistent
db-persistent
u334535@user-Precision-3460:~$ sudo rm db-persistent
rm: nie można usunąć 'db-persistent': Nie ma takiego pliku ani katalogu
u334535@user-Precision-3460:~$ sudo docker rm db-persistent
db-persistent
u334535@user-Precision-3460:~$ sudo docker volume rm postgres-data
postgres-data
u334535@user-Precision-3460:~$ pwd
/home/u334535
u334535@user-Precision-3460:~$ mkdir docker-test
u334535@user-Precision-3460:~$ echo"<h1>Hello from host</h1>" >docker-test/index.html
bash: echo<h1>Hello from host</h1>: Nie ma takiego pliku ani katalogu
u334535@user-Precision-3460:~$ echo"<h1>Hello from host</h1>" > docker-test/index.html
bash: echo<h1>Hello from host</h1>: Nie ma takiego pliku ani katalogu
u334535@user-Precision-3460:~$ echo "<h1>Hello from host</h1>" > docker-test/index.html
u334535@user-Precision-3460:~$ cat docker-test/index.html 
<h1>Hello from host</h1>
u334535@user-Precision-3460:~$ sudo docker run -d --name web-test \
> -p 8080:80 \
> -v ~/docker-test:/usr/share/nginx/html \
> ngnx:alpine
Unable to find image 'ngnx:alpine' locally
docker: Error response from daemon: pull access denied for ngnx, repository does not exist or may require 'docker login': denied: requested access to the resource is denied

Run 'docker run --help' for more information
u334535@user-Precision-3460:~$ 


















u334535@user-Precision-3460:~$ sudo docker run -it --name kontener2 alpine sh
[sudo] hasło użytkownika u334535: 
/ # echo "Hello from kontener2" >/plik.txt
/ # cat /plik.txt
Hello from kontener2
/ # exit
u334535@user-Precision-3460:~$ sudo docker start kontener2
kontener2
u334535@user-Precision-3460:~$ sudo docker attach kontener2
/ # cat /plik.txt
Hello from kontener2
/ # exit
u334535@user-Precision-3460:~$ 
































u334535@user-Precision-3460:~/docker-test$ docker network create blognet
963e5a97308ac00903f225b54b78f56e1ab8790004ee8b3a862902bf180c5aab
u334535@user-Precision-3460:~/docker-test$ ^C
u334535@user-Precision-3460:~/docker-test$ docker volume create blog-data
blog-data
u334535@user-Precision-3460:~/docker-test$ docker run -d \
> --name blog-db \
> --network blognet \
> -v blog-data:/var/lib/postgresql/data \
> -e POSTGRES_PASSWORD=secret123 \
> -e POSTGRES_DB=blogdb \
> -e POSTGRES_USER=blogger \
> postgres:15-alpine
67163f716d55abad262873a2ded1e28f073e6251eb28380c34b23dabbb532b12
u334535@user-Precision-3460:~/docker-test$ docker run -d \
> --name blog-app \
> --network blognet \
> -p 8080:80 \
> -e WORDPRESS_DB_HOST=blog-db:5432 \
> -e WORDPRESS_DB_USER=blogger \
> -e WORDPRESS_DB_PASSWORD=secret123 \
> -e WORDPRESS_DB_NAME=blogdb \
> wordpress:latest
Unable to find image 'wordpress:latest' locally
latest: Pulling from library/wordpress
38513bd72563: Already exists 
7c587c536410: Pull complete 
3262e3d480fc: Pull complete 
96dfba1a7aa9: Pull complete 
38a62f60c0ae: Pull complete 
0c7f7dbf73bd: Pull complete 
095e60baea1c: Pull complete 
5d7ef5dedb8e: Pull complete 
978f9bcbf3eb: Pull complete 
705807c02638: Pull complete 
3c631ec4c979: Pull complete 
061dd099b2ba: Pull complete 
cc4c6a09928c: Pull complete 
75c3bd976576: Pull complete 
4f4fb700ef54: Pull complete 
dee1bf57e253: Pull complete 
0eb92cc49677: Pull complete 
74d8a97bb60c: Pull complete 
5e59b25b0c46: Pull complete 
bda09bffbbd8: Pull complete 
803d8813d4c6: Pull complete 
d183a52dadcf: Pull complete 
7e2a3357b4fb: Pull complete 
28fc03424957: Pull complete 
Digest: sha256:3b89ab18542e90b63e4c150e24d5b590a21c1200c6cebe626a6015e99f498721
Status: Downloaded newer image for wordpress:latest
99db444f6c63f4010024ab350620376f76665198fae0aa6aba726bd85f6a37b3
u334535@user-Precision-3460:~/docker-test$ docker ps
CONTAINER ID   IMAGE                COMMAND                  CREATED         STATUS         PORTS                                     NAMES
99db444f6c63   wordpress:latest     "docker-entrypoint.s…"   8 seconds ago   Up 5 seconds   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   blog-app
67163f716d55   postgres:15-alpine   "docker-entrypoint.s…"   5 minutes ago   Up 5 minutes   5432/tcp                                  blog-db
u334535@user-Precision-3460:~/docker-test$ docker logs blog-app
WordPress not found in /var/www/html - copying now...
Complete! WordPress has been successfully copied to /var/www/html
No 'wp-config.php' found in /var/www/html, but 'WORDPRESS_...' variables supplied; copying 'wp-config-docker.php' (WORDPRESS_DB_HOST WORDPRESS_DB_NAME WORDPRESS_DB_PASSWORD WORDPRESS_DB_USER)
AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.18.0.3. Set the 'ServerName' directive globally to suppress this message
AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.18.0.3. Set the 'ServerName' directive globally to suppress this message
[Tue Nov 04 11:02:10.023639 2025] [mpm_prefork:notice] [pid 1:tid 1] AH00163: Apache/2.4.65 (Debian) PHP/8.3.27 configured -- resuming normal operations
[Tue Nov 04 11:02:10.023656 2025] [core:notice] [pid 1:tid 1] AH00094: Command line: 'apache2 -D FOREGROUND'
u334535@user-Precision-3460:~/docker-test$ docker run -d \
> ^C
u334535@user-Precision-3460:~/docker-test$ docker ps
CONTAINER ID   IMAGE                COMMAND                  CREATED         STATUS         PORTS                                     NAMES
99db444f6c63   wordpress:latest     "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   blog-app
67163f716d55   postgres:15-alpine   "docker-entrypoint.s…"   8 minutes ago   Up 8 minutes   5432/tcp                                  blog-db
u334535@user-Precision-3460:~/docker-test$ docker stop blog-db
blog-db
u334535@user-Precision-3460:~/docker-test$ docker rm blog-db
blog-db
u334535@user-Precision-3460:~/docker-test$ docker run -d \
> --name blog-db
docker: 'docker run' requires at least 1 argument

Usage:  docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

See 'docker run --help' for more information
u334535@user-Precision-3460:~/docker-test$ docker run -d --name blog-db \
> --network blognet \
> -v blog-data:/var/lib/mysql \
> -e MYSQL_ROOT_PASSWORD=rootpass \
> -e MYSQL_DATABASE=blogdb \
> -e MYSQL_USER=blogger \
> -e MYSQL_PASSWORD=secret123 \
> mysql:8.0
Unable to find image 'mysql:8.0' locally
8.0: Pulling from library/mysql
023a182c62a0: Pull complete 
4f78e34adfad: Pull complete 
a2ed1082d9e2: Pull complete 
c9ecfb07ed08: Pull complete 
4f94eaa123bf: Pull complete 
2a2d53254403: Pull complete 
48ec49971d94: Pull complete 
fdca9f583d44: Pull complete 
abcf302dead6: Pull complete 
37bd516ff765: Pull complete 
d68710a4a4e9: Pull complete 
Digest: sha256:f37951fc3753a6a22d6c7bf6978c5e5fefcf6f31814d98c582524f98eae52b21
Status: Downloaded newer image for mysql:8.0
1a464869dd872a4e94ccc9724c4d8fa2422f5b01349fc49d90e1cd04c68781d9
u334535@user-Precision-3460:~/docker-test$ docker ps
CONTAINER ID   IMAGE              COMMAND                  CREATED         STATUS         PORTS                                     NAMES
99db444f6c63   wordpress:latest   "docker-entrypoint.s…"   6 minutes ago   Up 6 minutes   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   blog-app
u334535@user-Precision-3460:~/docker-test$ docker volume rm blog-data
Error response from daemon: remove blog-data: volume is in use - [1a464869dd872a4e94ccc9724c4d8fa2422f5b01349fc49d90e1cd04c68781d9]
u334535@user-Precision-3460:~/docker-test$ docker ps
CONTAINER ID   IMAGE              COMMAND                  CREATED         STATUS         PORTS                                     NAMES
99db444f6c63   wordpress:latest   "docker-entrypoint.s…"   6 minutes ago   Up 6 minutes   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   blog-app
u334535@user-Precision-3460:~/docker-test$ docker stop blog-app
blog-app
u334535@user-Precision-3460:~/docker-test$ docker rm blog-app
blog-app
u334535@user-Precision-3460:~/docker-test$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
u334535@user-Precision-3460:~/docker-test$ docker volume rm blog-data
Error response from daemon: remove blog-data: volume is in use - [1a464869dd872a4e94ccc9724c4d8fa2422f5b01349fc49d90e1cd04c68781d9]
u334535@user-Precision-3460:~/docker-test$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
u334535@user-Precision-3460:~/docker-test$ ps
    PID TTY          TIME CMD
   7249 pts/1    00:00:00 bash
  30984 pts/1    00:00:00 bash
  31048 pts/1    00:00:00 bash
  41083 pts/1    00:00:00 ps
u334535@user-Precision-3460:~/docker-test$ docker ps -a
CONTAINER ID   IMAGE         COMMAND                  CREATED             STATUS                          PORTS     NAMES
1a464869dd87   mysql:8.0     "docker-entrypoint.s…"   2 minutes ago       Exited (1) About a minute ago             blog-db
a230b8996909   alpine        "sh"                     About an hour ago   Exited (1) About an hour ago              serene_mclaren
611cefaaccae   alpine        "sh"                     About an hour ago   Exited (0) About an hour ago              kontener2
cc5567ee9cf9   alpine        "sh"                     About an hour ago   Exited (0) About an hour ago              kontener1
c3a0ff690e72   alpine        "sh"                     2 hours ago         Exited (0) About an hour ago              kind_matsumoto
2be2496cc9e5   ubuntu        "bash"                   2 hours ago         Exited (0) 2 hours ago                    peaceful_zhukovsky
8ec89171ca40   ubuntu        "bash"                   2 hours ago         Exited (0) 2 hours ago                    frosty_newton
115ca1734802   hello-world   "/hello"                 2 hours ago         Exited (0) 2 hours ago                    trusting_swartz
76d049775ae2   hello-world   "/hello"                 2 hours ago         Exited (0) 2 hours ago                    angry_sinoussi
u334535@user-Precision-3460:~/docker-test$ docker rm blog-db
blog-db
u334535@user-Precision-3460:~/docker-test$ docker ps -a
CONTAINER ID   IMAGE         COMMAND    CREATED             STATUS                         PORTS     NAMES
a230b8996909   alpine        "sh"       About an hour ago   Exited (1) About an hour ago             serene_mclaren
611cefaaccae   alpine        "sh"       About an hour ago   Exited (0) About an hour ago             kontener2
cc5567ee9cf9   alpine        "sh"       About an hour ago   Exited (0) About an hour ago             kontener1
c3a0ff690e72   alpine        "sh"       2 hours ago         Exited (0) About an hour ago             kind_matsumoto
2be2496cc9e5   ubuntu        "bash"     2 hours ago         Exited (0) 2 hours ago                   peaceful_zhukovsky
8ec89171ca40   ubuntu        "bash"     2 hours ago         Exited (0) 2 hours ago                   frosty_newton
115ca1734802   hello-world   "/hello"   2 hours ago         Exited (0) 2 hours ago                   trusting_swartz
76d049775ae2   hello-world   "/hello"   2 hours ago         Exited (0) 2 hours ago                   angry_sinoussi
u334535@user-Precision-3460:~/docker-test$ docker volume create blog-data
blog-data
u334535@user-Precision-3460:~/docker-test$ docker run -d --name blog-db --network blognet -v blog-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=rootpass -e MYSQL_DATABASE=blogdb -e MYSQL_USER=blogger -e MYSQL_PASSWORD=secret123 mysql:8.0
acc697f9cff559c245515b75a42adfb2874fb5cbd9649352b87704b94da89768
u334535@user-Precision-3460:~/docker-test$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
u334535@user-Precision-3460:~/docker-test$ docker ps -aa
CONTAINER ID   IMAGE         COMMAND                  CREATED              STATUS                          PORTS     NAMES
acc697f9cff5   mysql:8.0     "docker-entrypoint.s…"   About a minute ago   Exited (1) About a minute ago             blog-db
a230b8996909   alpine        "sh"                     About an hour ago    Exited (1) About an hour ago              serene_mclaren
611cefaaccae   alpine        "sh"                     About an hour ago    Exited (0) About an hour ago              kontener2
cc5567ee9cf9   alpine        "sh"                     2 hours ago          Exited (0) 2 hours ago                    kontener1
c3a0ff690e72   alpine        "sh"                     2 hours ago          Exited (0) About an hour ago              kind_matsumoto
2be2496cc9e5   ubuntu        "bash"                   2 hours ago          Exited (0) 2 hours ago                    peaceful_zhukovsky
8ec89171ca40   ubuntu        "bash"                   2 hours ago          Exited (0) 2 hours ago                    frosty_newton
115ca1734802   hello-world   "/hello"                 2 hours ago          Exited (0) 2 hours ago                    trusting_swartz
76d049775ae2   hello-world   "/hello"                 2 hours ago          Exited (0) 2 hours ago                    angry_sinoussi
u334535@user-Precision-3460:~/docker-test$ docker rm blog-db
blog-db
u334535@user-Precision-3460:~/docker-test$ docker run -d --name blog-db --network blognet -v blog-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=rootpass -e MYSQL_DATABASE=blogdb -e MYSQL_USER=blogger -e MYSQL_PASSWORD=secret123 mysql:latest
Unable to find image 'mysql:latest' locally
latest: Pulling from library/mysql
023a182c62a0: Already exists 
f5f78fcd9ccb: Pull complete 
494c372d15c3: Pull complete 
dcee80f7340c: Pull complete 
480d01bd7a6a: Pull complete 
834e15e3ed24: Pull complete 
c276de9b5571: Pull complete 
0cd145fbb449: Pull complete 
5a3f7744d0e7: Pull complete 
21aa606d8d58: Pull complete 
Digest: sha256:569c4128dfa625ac2ac62cdd8af588a3a6a60a049d1a8d8f0fac95880ecdbbe5
Status: Downloaded newer image for mysql:latest
2f0b7e04d5145b9ceda490d810a29df7d12c9c3b00100b9d1808a4a79279a9ae
u334535@user-Precision-3460:~/docker-test$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
u334535@user-Precision-3460:~/docker-test$ docker rm blog-db
blog-db
u334535@user-Precision-3460:~/docker-test$ docker run -d --name blog-db --network blognet -e MYSQL_ROOT_PASSWORD=rootpass -e MYSQL_DATABASE=blogdb -e MYSQL_USER=blogger -e MYSQL_PASSWORD=secret123 mysql:latest
43720d7cfe448d3235de828f591bd26651460ef650f19799403b558b2a7b589c
u334535@user-Precision-3460:~/docker-test$ docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                 NAMES
43720d7cfe44   mysql:latest   "docker-entrypoint.s…"   3 seconds ago   Up 3 seconds   3306/tcp, 33060/tcp   blog-db
u334535@user-Precision-3460:~/docker-test$ docker run -d --name blog-app --network blognet -p 8080:80 -e WORDPRESS_DB_HOST=blog-db:5432 -e WORDPRESS_DB_USER=blogger -e WORDPRESS_DB_PASSWORD=secret123 -e WORDPRESS_DB_NAME=blogdb wordpress:latest
2ca771d2241422bb4ed19060c157d4f5c07a077b59cd3e2c21515155ffd2a387
u334535@user-Precision-3460:~/docker-test$ docker ps
CONTAINER ID   IMAGE              COMMAND                  CREATED              STATUS              PORTS                                     NAMES
2ca771d22414   wordpress:latest   "docker-entrypoint.s…"   2 seconds ago        Up 2 seconds        0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   blog-app
43720d7cfe44   mysql:latest       "docker-entrypoint.s…"   About a minute ago   Up About a minute   3306/tcp, 33060/tcp                       blog-db
u334535@user-Precision-3460:~/docker-test$ docker ps
CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS          PORTS                                     NAMES
2ca771d22414   wordpress:latest   "docker-entrypoint.s…"   38 seconds ago   Up 38 seconds   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   blog-app
43720d7cfe44   mysql:latest       "docker-entrypoint.s…"   2 minutes ago    Up 2 minutes    3306/tcp, 33060/tcp                       blog-db
u334535@user-Precision-3460:~/docker-test$ docker ps -a
CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS                         PORTS                                     NAMES
2ca771d22414   wordpress:latest   "docker-entrypoint.s…"   40 seconds ago   Up 40 seconds                  0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   blog-app
43720d7cfe44   mysql:latest       "docker-entrypoint.s…"   2 minutes ago    Up 2 minutes                   3306/tcp, 33060/tcp                       blog-db
a230b8996909   alpine             "sh"                     2 hours ago      Exited (1) About an hour ago                                             serene_mclaren
611cefaaccae   alpine             "sh"                     2 hours ago      Exited (0) About an hour ago                                             kontener2
cc5567ee9cf9   alpine             "sh"                     2 hours ago      Exited (0) 2 hours ago                                                   kontener1
c3a0ff690e72   alpine             "sh"                     2 hours ago      Exited (0) 2 hours ago                                                   kind_matsumoto
2be2496cc9e5   ubuntu             "bash"                   2 hours ago      Exited (0) 2 hours ago                                                   peaceful_zhukovsky
8ec89171ca40   ubuntu             "bash"                   2 hours ago      Exited (0) 2 hours ago                                                   frosty_newton
115ca1734802   hello-world        "/hello"                 2 hours ago      Exited (0) 2 hours ago                                                   trusting_swartz
76d049775ae2   hello-world        "/hello"                 2 hours ago      Exited (0) 2 hours ago                                                   angry_sinoussi
u334535@user-Precision-3460:~/docker-test$ docker rm blog-app
Error response from daemon: cannot remove container "blog-app": container is running: stop the container before removing or force remove
u334535@user-Precision-3460:~/docker-test$ docker stop blog-app
blog-app
u334535@user-Precision-3460:~/docker-test$ docker rm blog-app
blog-app
u334535@user-Precision-3460:~/docker-test$ docker run -d --name blog-app --network blognet -p 8080:80 -e WORDPRESS_DB_HOST=blog-db -e WORDPRESS_DB_USER=blogger -e WORDPRESS_DB_PASSWORD=secret123 -e WORDPRESS_DB_NAME=blogdb wordpress:latest
918995e229ad2b1d0f7836ca19c3c0b2888faba777def49c3dac2b9b04349a03
u334535@user-Precision-3460:~/docker-test$ docekr image ls
Nie znaleziono polecenia 'docekr', czy chodziło o:
  polecenie 'docker' ze snapa docker (28.4.0)
  polecenie 'docker' ze snapa docker (28.1.1+1)
  polecenie 'docker' z pakietu deb docker.io (28.2.2-0ubuntu1~24.04.1)
  polecenie 'docker' z pakietu deb podman-docker (4.9.3+ds1-1ubuntu0.2)
Zobacz 'snap info <nazwasnapa>' dla dodatkowych wersji.
u334535@user-Precision-3460:~/docker-test$ docker image ls
REPOSITORY    TAG         IMAGE ID       CREATED        SIZE
nginx         alpine      d4918ca78576   6 days ago     52.8MB
nginx         latest      9d0e6f6199dc   6 days ago     152MB
mysql         latest      f6b0ca07d79d   13 days ago    934MB
mysql         8.0         34178dbaefd0   13 days ago    783MB
postgres      15-alpine   ba05c11fe977   2 weeks ago    273MB
alpine        latest      706db57fb206   3 weeks ago    8.32MB
ubuntu        latest      97bed23a3497   4 weeks ago    78.1MB
wordpress     latest      7332768c717f   4 weeks ago    734MB
hello-world   latest      1b44b5a3e06a   2 months ago   10.1kB
u334535@user-Precision-3460:~/docker-test$ docker image inspect wordpress:latest
[
    {
        "Id": "sha256:7332768c717ffdc11b604ae2b4cd782ae434fd429d7a9365eecf40634e768ea0",
        "RepoTags": [
            "wordpress:latest"
        ],
        "RepoDigests": [
            "wordpress@sha256:3b89ab18542e90b63e4c150e24d5b590a21c1200c6cebe626a6015e99f498721"
        ],
        "Parent": "",
        "Comment": "buildkit.dockerfile.v0",
        "Created": "2025-10-01T01:03:19Z",
        "DockerVersion": "",
        "Author": "",
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 733735491,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/e62876f75151f5c9423ac0e6b1fbab4e89d941cd5bfdd9e9c26b1ffb8c650e72/diff:/var/lib/docker/overlay2/817e9fed9b6e8b42c13e90f6e9b866fd1f9bb1d632e439af6b5731e2d3bc4648/diff:/var/lib/docker/overlay2/54d78ee2104f7f6a5d75b5dfb5000369c80cdeb96638cee6a07d38fe43bfd02a/diff:/var/lib/docker/overlay2/7a846a7c6ad01cad036047b6bdfb4c9299dc45f437b50124564463033b6d6a06/diff:/var/lib/docker/overlay2/2dffe40d97b9eb3b7315c98d9779abdb3e656caaafd00b8cf438ca24a846681f/diff:/var/lib/docker/overlay2/4f6fa033c5b447cf3ffb5fe8b797a739bbd5c18a116449a837d4b788b6129d05/diff:/var/lib/docker/overlay2/ed8f503970ffda0506e5572d54c08bd5c914f2861644ac2005317c2edf8f15e1/diff:/var/lib/docker/overlay2/de217e9c60d96f56e8f3103df5b771052932cd807db58d48b3cad14fbd57bb26/diff:/var/lib/docker/overlay2/5cf233f20a3b1ac94a8eacbd12320d70f4d4543a2dfc66a414183e295f9debaf/diff:/var/lib/docker/overlay2/8584cf3c05cf64ed935b28526cf106d8a5a10cc7faa58db06e6b5d8993e14d3a/diff:/var/lib/docker/overlay2/b92419d208afb7976ddf364271cc62e04aa80dc102226074f9237a124436ee7c/diff:/var/lib/docker/overlay2/5284b2ea8a77b839a5510716bc679177b392475f57b9eaa86ec7b409e1ea199a/diff:/var/lib/docker/overlay2/dc3bb2771fd75a9556f9a006cb3b7dbdcd65949616b76dde0f57dcb7acae51a3/diff:/var/lib/docker/overlay2/d17e4398e0b0e6212ca073a168f1e4d0ff8cf207ea1e3bd33695bb40c50e4c3a/diff:/var/lib/docker/overlay2/a4f5badbfab4002e4e273380518c2c8d31e647a0f99e43c4faf320aaff4c1a76/diff:/var/lib/docker/overlay2/fc406aa54a4af9f5b4c948030cb46d7cb423b06b627d0967f9287369ce251ab9/diff:/var/lib/docker/overlay2/19137ff1fb8418e81796fdefcc52d6c2bfe010470abe18eb6d7a60ad7f2f9286/diff:/var/lib/docker/overlay2/055c2aade01c9e4c23f2d537e0793268c42e878f8591694feb64f3bf5534a051/diff:/var/lib/docker/overlay2/179db95b54dff943e1fccc367d7575efa040b392e346062a211b525e63fae0fb/diff:/var/lib/docker/overlay2/147d72a3028d7c39f38ce1b68b8df461bdfcaca361eba89bb823be29a470f6a0/diff:/var/lib/docker/overlay2/adc8b279a139d0ecab8736d0d754149b88f7b227aa2673a6a90a5fce62a50df0/diff:/var/lib/docker/overlay2/4c633a42eb04904c8f166b534de0c59da276b7f44ccf92a6b0bb89083f25fbf2/diff:/var/lib/docker/overlay2/0a05e1456c64b87f24038305c6b57e21c5b45c3a0154e3e1b606861b0ea54887/diff",
                "MergedDir": "/var/lib/docker/overlay2/01a683085123bf26a4726d4a5634a909889c953c7290e040c11c35b6e7c27b88/merged",
                "UpperDir": "/var/lib/docker/overlay2/01a683085123bf26a4726d4a5634a909889c953c7290e040c11c35b6e7c27b88/diff",
                "WorkDir": "/var/lib/docker/overlay2/01a683085123bf26a4726d4a5634a909889c953c7290e040c11c35b6e7c27b88/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:d7c97cb6f1fe7cae982649e9f55efe201212e8acaa64bd668c083b204e4efd4c",
                "sha256:a70a53678e39f7b0ce3ee010b5f379169b5e6ae888da41c832baa05b0c836037",
                "sha256:ec1c6a2202b427269aee3628025afe6fa0e12170cf3915f647ee86a3f9c29c5f",
                "sha256:64013f07709c032338fb88d67e7982bca2f100b3a364a7895ddd3d99dfb70c6f",
                "sha256:a9cd4deb2ac49517838469c1d5ff011bdd29a8ac8d26d33e94b55f39d4b3563d",
                "sha256:5267a9f8a6b2364dd30bdbb928154a66ca68aa679ccbb105079d07700a920a36",
                "sha256:5e86fb8dd799b14a73149d6815ab064caaaaff922ec96d4b32d40bdb6692dacb",
                "sha256:5b90ee3c1b2c0f5ad02c8bdd09bbe7b9e3a80106a8ad632f4a31626fe0e59510",
                "sha256:cbf34dbfe55cdfdcfe6bcd17b6851795e7ec7bb7612c4460eee3de4da67e60e6",
                "sha256:bf8e40ac3c461d4e0536a57fdb1d853eb2d8037224cd25cf309a7e8959c37908",
                "sha256:eab84bfa29decff68d13a9c5e480f8bb2806bbcdae6294098ed3d44b4e919823",
                "sha256:b0b0c4c00ce3d0f5e2ed59246db618a6c75653242157fd4ce90cd84a222d322a",
                "sha256:e0be901b9885239938944a87b5960803610bf44a621c78bf0be697941541c058",
                "sha256:6da6ce241629b3c16e28d4cd2413e055caeb7d8dc9f8b6214c74b8f2ebf2d944",
                "sha256:5f70bf18a086007016e948b04aed3b82103a36bea41755b6cddfaf10ace3c6ef",
                "sha256:f16af4118bfd5096e31e13a168c2b26335e266cebc87dcda63ff44bc65fa7059",
                "sha256:11499b408d28b5602f3c694bcc1f046b6e7b2285e3fa8ff81ca8f06c725b80f5",
                "sha256:d4fb5745f7e2ee4e3849bc96b5b29b98ab7a70602c59c9d5c78278908c513cc2",
                "sha256:88727e4c7cd340aebaeea076c7b033eea6b088fa42572aabdb7acf60b41de3f2",
                "sha256:899301bc2a5efcc1e8bea4f2685ebf686376dbbe6dbdc739228c59a7c4bd3be6",
                "sha256:3c62cb52fd632b5fd5b357ceaf0de3fd12563a42fdfc2968f222553e85ab943a",
                "sha256:333f858516767cff4dd4cad333d31724aa0cb5ce61bf327228724f93b80bba3b",
                "sha256:7c0dccd76095884cd939e17fb710153efda1dcd81dd5ee995a6af876af2c6e0a",
                "sha256:e753d60318fa2ccaf4bb5189e087a3e1583e717d0b3f7508d57fd679fbf883bb"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        },
        "Config": {
            "Cmd": [
                "apache2-foreground"
            ],
            "Entrypoint": [
                "docker-entrypoint.sh"
            ],
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "PHPIZE_DEPS=autoconf \t\tdpkg-dev \t\tfile \t\tg++ \t\tgcc \t\tlibc-dev \t\tmake \t\tpkg-config \t\tre2c",
                "PHP_INI_DIR=/usr/local/etc/php",
                "APACHE_CONFDIR=/etc/apache2",
                "APACHE_ENVVARS=/etc/apache2/envvars",
                "PHP_CFLAGS=-fstack-protector-strong -fpic -fpie -O2 -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64",
                "PHP_CPPFLAGS=-fstack-protector-strong -fpic -fpie -O2 -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64",
                "PHP_LDFLAGS=-Wl,-O1 -pie",
                "GPG_KEYS=1198C0117593497A5EC5C199286AF1F9897469DC C28D937575603EB4ABB725861C0779DC5C0A9DE4 AFD8691FDAEDF03BDF6E460563F15A9B715376CA",
                "PHP_VERSION=8.3.27",
                "PHP_URL=https://www.php.net/distributions/php-8.3.27.tar.xz",
                "PHP_ASC_URL=https://www.php.net/distributions/php-8.3.27.tar.xz.asc",
                "PHP_SHA256=c15a09a9d199437144ecfef7d712ec4ca5c6820cf34acc24cc8489dd0cee41ba"
            ],
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Labels": null,
            "OnBuild": null,
            "StopSignal": "SIGWINCH",
            "User": "",
            "Volumes": {
                "/var/www/html": {}
            },
            "WorkingDir": "/var/www/html"
        }
    }
]
u334535@user-Precision-3460:~/docker-test$ docker run -d -P nginx:latest
6bc08ebf7f85a988ad7f596459b25b53f56f7123f228afbf5dde595a55437411
u334535@user-Precision-3460:~/docker-test$ docker ps
CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS          PORTS                                       NAMES
6bc08ebf7f85   nginx:latest       "/docker-entrypoint.…"   4 seconds ago    Up 3 seconds    0.0.0.0:32768->80/tcp, [::]:32768->80/tcp   wizardly_gagarin
918995e229ad   wordpress:latest   "docker-entrypoint.s…"   8 minutes ago    Up 8 minutes    0.0.0.0:8080->80/tcp, [::]:8080->80/tcp     blog-app
43720d7cfe44   mysql:latest       "docker-entrypoint.s…"   12 minutes ago   Up 12 minutes   3306/tcp, 33060/tcp                         blog-db
u334535@user-Precision-3460:~/docker-test$ docker run nginx:latest
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2025/11/04 11:28:25 [notice] 1#1: using the "epoll" event method
2025/11/04 11:28:25 [notice] 1#1: nginx/1.29.3
2025/11/04 11:28:25 [notice] 1#1: built by gcc 14.2.0 (Debian 14.2.0-19) 
2025/11/04 11:28:25 [notice] 1#1: OS: Linux 6.14.0-34-generic
2025/11/04 11:28:25 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2025/11/04 11:28:25 [notice] 1#1: start worker processes
2025/11/04 11:28:25 [notice] 1#1: start worker process 29
2025/11/04 11:28:25 [notice] 1#1: start worker process 30
2025/11/04 11:28:25 [notice] 1#1: start worker process 31
2025/11/04 11:28:25 [notice] 1#1: start worker process 32
2025/11/04 11:28:25 [notice] 1#1: start worker process 33
2025/11/04 11:28:25 [notice] 1#1: start worker process 34
2025/11/04 11:28:25 [notice] 1#1: start worker process 35
2025/11/04 11:28:25 [notice] 1#1: start worker process 36
2025/11/04 11:28:25 [notice] 1#1: start worker process 37
2025/11/04 11:28:25 [notice] 1#1: start worker process 38
2025/11/04 11:28:25 [notice] 1#1: start worker process 39
2025/11/04 11:28:25 [notice] 1#1: start worker process 40
^C2025/11/04 11:29:50 [notice] 1#1: signal 2 (SIGINT) received, exiting
2025/11/04 11:29:50 [notice] 30#30: exiting
2025/11/04 11:29:50 [notice] 32#32: exiting
2025/11/04 11:29:50 [notice] 29#29: exiting
2025/11/04 11:29:50 [notice] 33#33: exiting
2025/11/04 11:29:50 [notice] 31#31: exiting
2025/11/04 11:29:50 [notice] 35#35: exiting
2025/11/04 11:29:50 [notice] 34#34: exiting
2025/11/04 11:29:50 [notice] 36#36: exiting
2025/11/04 11:29:50 [notice] 37#37: exiting
2025/11/04 11:29:50 [notice] 38#38: exiting
2025/11/04 11:29:50 [notice] 39#39: exiting
2025/11/04 11:29:50 [notice] 35#35: exit
2025/11/04 11:29:50 [notice] 29#29: exit
2025/11/04 11:29:50 [notice] 36#36: exit
2025/11/04 11:29:50 [notice] 37#37: exit
2025/11/04 11:29:50 [notice] 32#32: exit
2025/11/04 11:29:50 [notice] 34#34: exit
2025/11/04 11:29:50 [notice] 38#38: exit
2025/11/04 11:29:50 [notice] 39#39: exit
2025/11/04 11:29:50 [notice] 31#31: exit
2025/11/04 11:29:50 [notice] 40#40: exiting
2025/11/04 11:29:50 [notice] 30#30: exit
2025/11/04 11:29:50 [notice] 40#40: exit
2025/11/04 11:29:50 [notice] 33#33: exit
2025/11/04 11:29:50 [notice] 1#1: signal 17 (SIGCHLD) received from 40
2025/11/04 11:29:50 [notice] 1#1: worker process 40 exited with code 0
2025/11/04 11:29:50 [notice] 1#1: signal 29 (SIGIO) received
2025/11/04 11:29:50 [notice] 1#1: signal 17 (SIGCHLD) received from 35
2025/11/04 11:29:50 [notice] 1#1: worker process 35 exited with code 0
2025/11/04 11:29:50 [notice] 1#1: signal 29 (SIGIO) received
2025/11/04 11:29:50 [notice] 1#1: signal 17 (SIGCHLD) received from 34
2025/11/04 11:29:50 [notice] 1#1: worker process 34 exited with code 0
2025/11/04 11:29:50 [notice] 1#1: signal 29 (SIGIO) received
2025/11/04 11:29:50 [notice] 1#1: signal 17 (SIGCHLD) received from 36
2025/11/04 11:29:50 [notice] 1#1: worker process 36 exited with code 0
2025/11/04 11:29:50 [notice] 1#1: worker process 37 exited with code 0
2025/11/04 11:29:50 [notice] 1#1: signal 29 (SIGIO) received
2025/11/04 11:29:50 [notice] 1#1: signal 17 (SIGCHLD) received from 38
2025/11/04 11:29:50 [notice] 1#1: worker process 38 exited with code 0
2025/11/04 11:29:50 [notice] 1#1: signal 29 (SIGIO) received
2025/11/04 11:29:50 [notice] 1#1: signal 17 (SIGCHLD) received from 29
2025/11/04 11:29:50 [notice] 1#1: worker process 29 exited with code 0
2025/11/04 11:29:50 [notice] 1#1: signal 29 (SIGIO) received
2025/11/04 11:29:50 [notice] 1#1: signal 17 (SIGCHLD) received from 31
2025/11/04 11:29:50 [notice] 1#1: worker process 31 exited with code 0
2025/11/04 11:29:50 [notice] 1#1: signal 29 (SIGIO) received
2025/11/04 11:29:50 [notice] 1#1: signal 17 (SIGCHLD) received from 39
2025/11/04 11:29:50 [notice] 1#1: worker process 39 exited with code 0
2025/11/04 11:29:50 [notice] 1#1: signal 29 (SIGIO) received
2025/11/04 11:29:50 [notice] 1#1: signal 17 (SIGCHLD) received from 30
2025/11/04 11:29:50 [notice] 1#1: worker process 30 exited with code 0
2025/11/04 11:29:50 [notice] 1#1: signal 29 (SIGIO) received
2025/11/04 11:29:50 [notice] 1#1: signal 17 (SIGCHLD) received from 32
2025/11/04 11:29:50 [notice] 1#1: worker process 32 exited with code 0
2025/11/04 11:29:50 [notice] 1#1: signal 29 (SIGIO) received
2025/11/04 11:29:50 [notice] 1#1: signal 17 (SIGCHLD) received from 33
2025/11/04 11:29:50 [notice] 1#1: worker process 33 exited with code 0
2025/11/04 11:29:50 [notice] 1#1: exit
u334535@user-Precision-3460:~/docker-test$ docker run -it alpine hs
docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: error during container init: exec: "hs": executable file not found in $PATH: unknown

Run 'docker run --help' for more information
u334535@user-Precision-3460:~/docker-test$ docker run -it alpine sh
/ # exit
u334535@user-Precision-3460:~/docker-test$ docker run -d -p 8001:80 nginx:latest
cebe92207ecd9073ab44702779e062ec94d96961de65f163946ef9dcca5e2a4d
u334535@user-Precision-3460:~/docker-test$ curl http://localhost:8001
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
u334535@user-Precision-3460:~/docker-test$ docker run -d -p 80 nginx:latest
5e7c50176c1866f7f4843a8b65cd318da0b686465165040f8ee3550740da4a3c
u334535@user-Precision-3460:~/docker-test$ docker ps
CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS          PORTS                                       NAMES
5e7c50176c18   nginx:latest       "/docker-entrypoint.…"   3 seconds ago    Up 3 seconds    0.0.0.0:32769->80/tcp, [::]:32769->80/tcp   elastic_kapitsa
cebe92207ecd   nginx:latest       "/docker-entrypoint.…"   52 seconds ago   Up 52 seconds   0.0.0.0:8001->80/tcp, [::]:8001->80/tcp     modest_shockley
6bc08ebf7f85   nginx:latest       "/docker-entrypoint.…"   4 minutes ago    Up 4 minutes    0.0.0.0:32768->80/tcp, [::]:32768->80/tcp   wizardly_gagarin
918995e229ad   wordpress:latest   "docker-entrypoint.s…"   13 minutes ago   Up 13 minutes   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp     blog-app
43720d7cfe44   mysql:latest       "docker-entrypoint.s…"   16 minutes ago   Up 16 minutes   3306/tcp, 33060/tcp                         blog-db
u334535@user-Precision-3460:~/docker-test$ docker exec blog-db env | grep MYSQL
MYSQL_ROOT_PASSWORD=rootpass
MYSQL_DATABASE=blogdb
MYSQL_USER=blogger
MYSQL_PASSWORD=secret123
MYSQL_MAJOR=innovation
MYSQL_VERSION=9.5.0-1.el9
MYSQL_SHELL_VERSION=9.5.0-1.el9
u334535@user-Precision-3460:~/docker-test$ docker exec -it blog-db -uroot -prootpass
OCI runtime exec failed: exec failed: unable to start container process: exec: "-uroot": executable file not found in $PATH: unknown
u334535@user-Precision-3460:~/docker-test$ docker exec -it blog-db -uroot -prootpass
OCI runtime exec failed: exec failed: unable to start container process: exec: "-uroot": executable file not found in $PATH: unknown
u334535@user-Precision-3460:~/docker-test$ docker exec -it blog-db -uroot -prootpass
OCI runtime exec failed: exec failed: unable to start container process: exec: "-uroot": executable file not found in $PATH: unknown
u334535@user-Precision-3460:~/docker-test$ nano app.env
u334535@user-Precision-3460:~/docker-test$ docker run -d \
> --name app-test \
> --env-file app.env \
> alpine sleep 3600
6f584e341a4d077c0ec227a8937735fbd4c8da8317983ce4e29f90e2dc15a569
u334535@user-Precision-3460:~/docker-test$ docker exec app-test env | grep APP
APP_ENV=production
APP_DEBUG=false
APP_PORT=3000
u334535@user-Precision-3460:~/docker-test$ docker run -d --name app-limit --memory="512m" --cpus="0.5" nginx:alpine
fd54acfb1ebcc0abdbf9ca9761aebc5e3af739823069179383352b4631d0605d
u334535@user-Precision-3460:~/docker-test$ docker inspect app-limit
[
    {
        "Id": "fd54acfb1ebcc0abdbf9ca9761aebc5e3af739823069179383352b4631d0605d",
        "Created": "2025-11-04T11:40:54.962050436Z",
        "Path": "/docker-entrypoint.sh",
        "Args": [
            "nginx",
            "-g",
            "daemon off;"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 44725,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2025-11-04T11:40:55.025895454Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:d4918ca78576a537caa7b0c043051c8efc1796de33fee8724ee0fff4a1cabed9",
        "ResolvConfPath": "/var/lib/docker/containers/fd54acfb1ebcc0abdbf9ca9761aebc5e3af739823069179383352b4631d0605d/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/fd54acfb1ebcc0abdbf9ca9761aebc5e3af739823069179383352b4631d0605d/hostname",
        "HostsPath": "/var/lib/docker/containers/fd54acfb1ebcc0abdbf9ca9761aebc5e3af739823069179383352b4631d0605d/hosts",
        "LogPath": "/var/lib/docker/containers/fd54acfb1ebcc0abdbf9ca9761aebc5e3af739823069179383352b4631d0605d/fd54acfb1ebcc0abdbf9ca9761aebc5e3af739823069179383352b4631d0605d-json.log",
        "Name": "/app-limit",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "docker-default",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "bridge",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                42,
                168
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 536870912,
            "NanoCpus": 500000000,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 0,
            "MemorySwap": 1073741824,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": [],
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/interrupts",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware",
                "/sys/devices/virtual/powercap",
                "/sys/devices/system/cpu/cpu0/thermal_throttle",
                "/sys/devices/system/cpu/cpu1/thermal_throttle",
                "/sys/devices/system/cpu/cpu2/thermal_throttle",
                "/sys/devices/system/cpu/cpu3/thermal_throttle",
                "/sys/devices/system/cpu/cpu4/thermal_throttle",
                "/sys/devices/system/cpu/cpu5/thermal_throttle",
                "/sys/devices/system/cpu/cpu6/thermal_throttle",
                "/sys/devices/system/cpu/cpu7/thermal_throttle",
                "/sys/devices/system/cpu/cpu8/thermal_throttle",
                "/sys/devices/system/cpu/cpu9/thermal_throttle",
                "/sys/devices/system/cpu/cpu10/thermal_throttle",
                "/sys/devices/system/cpu/cpu11/thermal_throttle"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "ID": "fd54acfb1ebcc0abdbf9ca9761aebc5e3af739823069179383352b4631d0605d",
                "LowerDir": "/var/lib/docker/overlay2/01cac1b3fb34b2c40ac7a826078e5c728842f14a72fd11af92dfad2efc790843-init/diff:/var/lib/docker/overlay2/0e1b71c2d39d23d809081b413faabe0e61f16ed947bca30f483e723680bc07db/diff:/var/lib/docker/overlay2/e1993339cc010e23d4b2411954e379997d94310854744bfc8e44c1bf4d022579/diff:/var/lib/docker/overlay2/c424d41445db40486afebfb47c159ced170ef32bc44fe0ab78ddccadf1b34750/diff:/var/lib/docker/overlay2/006ba43015a6b9579d7f592c4431df6cee0b8e7ca95a09d3ab9797b1bbfd3d69/diff:/var/lib/docker/overlay2/bf9da614e4414d49a6971af760646e092a097da9c5441a97d1b0acb0f30477f8/diff:/var/lib/docker/overlay2/12796360e71bf9905bd46a1d049c277d069ca139168bee1b085d72957bc546b1/diff:/var/lib/docker/overlay2/35e39f3880ed6b62607e71a54e002d395ae0fa7636f99d89dc1cb494614d8a37/diff:/var/lib/docker/overlay2/ce927deea9e92474a95c42a4a617ff366aca3dfe41d285e36ef652856c2b6c31/diff",
                "MergedDir": "/var/lib/docker/overlay2/01cac1b3fb34b2c40ac7a826078e5c728842f14a72fd11af92dfad2efc790843/merged",
                "UpperDir": "/var/lib/docker/overlay2/01cac1b3fb34b2c40ac7a826078e5c728842f14a72fd11af92dfad2efc790843/diff",
                "WorkDir": "/var/lib/docker/overlay2/01cac1b3fb34b2c40ac7a826078e5c728842f14a72fd11af92dfad2efc790843/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "fd54acfb1ebc",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.29.3",
                "PKG_RELEASE=1",
                "DYNPKG_RELEASE=1",
                "NJS_VERSION=0.9.4",
                "NJS_RELEASE=1"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "Image": "nginx:alpine",
            "Volumes": null,
            "WorkingDir": "/",
            "Entrypoint": [
                "/docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {
                "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
            },
            "StopSignal": "SIGQUIT"
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "adfeb38faed1e9194d085b35a729ca7b1bd083eec9686c7cc7820f100729f6e9",
            "SandboxKey": "/var/run/docker/netns/adfeb38faed1",
            "Ports": {
                "80/tcp": null
            },
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "21ac18b2243f47a64ddc6f222c49f869ff53b1486b52a30a9feb4cf1d069acd1",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.6",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "0e:f7:69:89:24:5d",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "MacAddress": "0e:f7:69:89:24:5d",
                    "DriverOpts": null,
                    "GwPriority": 0,
                    "NetworkID": "d8e7c20f8e0c4d573e4253b3af16014aac32d3bcb75d53e39a16c05f888e7468",
                    "EndpointID": "21ac18b2243f47a64ddc6f222c49f869ff53b1486b52a30a9feb4cf1d069acd1",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.6",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "DNSNames": null
                }
            }
        }
    }
]
u334535@user-Precision-3460:~/docker-test$ docker inspect app-limit | grep -A 5 "Memory"
            "Memory": 536870912,
            "NanoCpus": 500000000,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
--
            "MemoryReservation": 0,
            "MemorySwap": 1073741824,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": [],
            "CpuCount": 0,
            "CpuPercent": 0,
u334535@user-Precision-3460:~/docker-test$ docker stats app-limit --no-stream
CONTAINER ID   NAME        CPU %     MEM USAGE / LIMIT   MEM %     NET I/O         BLOCK I/O         PIDS
fd54acfb1ebc   app-limit   0.00%     10.07MiB / 512MiB   1.97%     3.73kB / 126B   77.8kB / 12.3kB   13
u334535@user-Precision-3460:~/docker-test$ docker run -d \
> --name stress-test \
> --memory="256m" \
> --cpus="1.0" \
> progrium/stress --cpu 2 --timeout 60s
Unable to find image 'progrium/stress:latest' locally
latest: Pulling from progrium/stress
docker: Docker Image Format v1 and Docker Image manifest version 2, schema 1 support has been removed. Suggest the author of docker.io/progrium/stress:latest to upgrade the image to the OCI Format or Docker Image manifest v2, schema 2. More information at https://docs.docker.com/go/deprecated-image-specs/

Run 'docker run --help' for more information
u334535@user-Precision-3460:~/docker-test$ docker stats stress-test
Error response from daemon: No such container: stress-test
u334535@user-Precision-3460:~/docker-test$ docker ps
CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS          PORTS                                       NAMES
fd54acfb1ebc   nginx:alpine       "/docker-entrypoint.…"   6 minutes ago    Up 6 minutes    80/tcp                                      app-limit
6f584e341a4d   alpine             "sleep 3600"             8 minutes ago    Up 8 minutes                                                app-test
5e7c50176c18   nginx:latest       "/docker-entrypoint.…"   14 minutes ago   Up 14 minutes   0.0.0.0:32769->80/tcp, [::]:32769->80/tcp   elastic_kapitsa
cebe92207ecd   nginx:latest       "/docker-entrypoint.…"   15 minutes ago   Up 15 minutes   0.0.0.0:8001->80/tcp, [::]:8001->80/tcp     modest_shockley
6bc08ebf7f85   nginx:latest       "/docker-entrypoint.…"   19 minutes ago   Up 19 minutes   0.0.0.0:32768->80/tcp, [::]:32768->80/tcp   wizardly_gagarin
918995e229ad   wordpress:latest   "docker-entrypoint.s…"   28 minutes ago   Up 28 minutes   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp     blog-app
43720d7cfe44   mysql:latest       "docker-entrypoint.s…"   31 minutes ago   Up 31 minutes   3306/tcp, 33060/tcp                         blog-db
u334535@user-Precision-3460:~/docker-test$ docker ps -a
CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS                      PORTS                                       NAMES
fd54acfb1ebc   nginx:alpine       "/docker-entrypoint.…"   6 minutes ago    Up 6 minutes                80/tcp                                      app-limit
6f584e341a4d   alpine             "sleep 3600"             8 minutes ago    Up 8 minutes                                                            app-test
5e7c50176c18   nginx:latest       "/docker-entrypoint.…"   14 minutes ago   Up 14 minutes               0.0.0.0:32769->80/tcp, [::]:32769->80/tcp   elastic_kapitsa
cebe92207ecd   nginx:latest       "/docker-entrypoint.…"   15 minutes ago   Up 15 minutes               0.0.0.0:8001->80/tcp, [::]:8001->80/tcp     modest_shockley
cba3d4b01694   alpine             "sh"                     16 minutes ago   Exited (0) 16 minutes ago                                               elated_aryabhata
a1134cdfc0b0   alpine             "hs"                     16 minutes ago   Created                                                                 youthful_blackwell
f1f02cfe87bd   nginx:latest       "/docker-entrypoint.…"   18 minutes ago   Exited (0) 17 minutes ago                                               boring_darwin
6bc08ebf7f85   nginx:latest       "/docker-entrypoint.…"   19 minutes ago   Up 19 minutes               0.0.0.0:32768->80/tcp, [::]:32768->80/tcp   wizardly_gagarin
918995e229ad   wordpress:latest   "docker-entrypoint.s…"   28 minutes ago   Up 28 minutes               0.0.0.0:8080->80/tcp, [::]:8080->80/tcp     blog-app
43720d7cfe44   mysql:latest       "docker-entrypoint.s…"   31 minutes ago   Up 31 minutes               3306/tcp, 33060/tcp                         blog-db
a230b8996909   alpine             "sh"                     2 hours ago      Exited (1) 2 hours ago                                                  serene_mclaren
611cefaaccae   alpine             "sh"                     2 hours ago      Exited (0) 2 hours ago                                                  kontener2
cc5567ee9cf9   alpine             "sh"                     2 hours ago      Exited (0) 2 hours ago                                                  kontener1
c3a0ff690e72   alpine             "sh"                     2 hours ago      Exited (0) 2 hours ago                                                  kind_matsumoto
2be2496cc9e5   ubuntu             "bash"                   2 hours ago      Exited (0) 2 hours ago                                                  peaceful_zhukovsky
8ec89171ca40   ubuntu             "bash"                   2 hours ago      Exited (0) 2 hours ago                                                  frosty_newton
115ca1734802   hello-world        "/hello"                 2 hours ago      Exited (0) 2 hours ago                                                  trusting_swartz
76d049775ae2   hello-world        "/hello"                 2 hours ago      Exited (0) 2 hours ago                                                  angry_sinoussi
u334535@user-Precision-3460:~/docker-test$ docker logs app-limit
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2025/11/04 11:40:55 [notice] 1#1: using the "epoll" event method
2025/11/04 11:40:55 [notice] 1#1: nginx/1.29.3
2025/11/04 11:40:55 [notice] 1#1: built by gcc 14.2.0 (Alpine 14.2.0) 
2025/11/04 11:40:55 [notice] 1#1: OS: Linux 6.14.0-34-generic
2025/11/04 11:40:55 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2025/11/04 11:40:55 [notice] 1#1: start worker processes
2025/11/04 11:40:55 [notice] 1#1: start worker process 31
2025/11/04 11:40:55 [notice] 1#1: start worker process 32
2025/11/04 11:40:55 [notice] 1#1: start worker process 33
2025/11/04 11:40:55 [notice] 1#1: start worker process 34
2025/11/04 11:40:55 [notice] 1#1: start worker process 35
2025/11/04 11:40:55 [notice] 1#1: start worker process 36
2025/11/04 11:40:55 [notice] 1#1: start worker process 37
2025/11/04 11:40:55 [notice] 1#1: start worker process 38
2025/11/04 11:40:55 [notice] 1#1: start worker process 39
2025/11/04 11:40:55 [notice] 1#1: start worker process 40
2025/11/04 11:40:55 [notice] 1#1: start worker process 41
2025/11/04 11:40:55 [notice] 1#1: start worker process 42
u334535@user-Precision-3460:~/docker-test$ docker -f logs app-limit
unknown shorthand flag: 'f' in -f

Usage:  docker [OPTIONS] COMMAND [ARG...]

Run 'docker --help' for more information
u334535@user-Precision-3460:~/docker-test$ docker logs -f app-limit
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2025/11/04 11:40:55 [notice] 1#1: using the "epoll" event method
2025/11/04 11:40:55 [notice] 1#1: nginx/1.29.3
2025/11/04 11:40:55 [notice] 1#1: built by gcc 14.2.0 (Alpine 14.2.0) 
2025/11/04 11:40:55 [notice] 1#1: OS: Linux 6.14.0-34-generic
2025/11/04 11:40:55 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2025/11/04 11:40:55 [notice] 1#1: start worker processes
2025/11/04 11:40:55 [notice] 1#1: start worker process 31
2025/11/04 11:40:55 [notice] 1#1: start worker process 32
2025/11/04 11:40:55 [notice] 1#1: start worker process 33
2025/11/04 11:40:55 [notice] 1#1: start worker process 34
2025/11/04 11:40:55 [notice] 1#1: start worker process 35
2025/11/04 11:40:55 [notice] 1#1: start worker process 36
2025/11/04 11:40:55 [notice] 1#1: start worker process 37
2025/11/04 11:40:55 [notice] 1#1: start worker process 38
2025/11/04 11:40:55 [notice] 1#1: start worker process 39
2025/11/04 11:40:55 [notice] 1#1: start worker process 40
2025/11/04 11:40:55 [notice] 1#1: start worker process 41
2025/11/04 11:40:55 [notice] 1#1: start worker process 42
^Cu334535@user-Precision-3460:~/docker-test$ docker logs -f app-limit
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2025/11/04 11:40:55 [notice] 1#1: using the "epoll" event method
2025/11/04 11:40:55 [notice] 1#1: nginx/1.29.3
2025/11/04 11:40:55 [notice] 1#1: built by gcc 14.2.0 (Alpine 14.2.0) 
2025/11/04 11:40:55 [notice] 1#1: OS: Linux 6.14.0-34-generic
2025/11/04 11:40:55 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2025/11/04 11:40:55 [notice] 1#1: start worker processes
2025/11/04 11:40:55 [notice] 1#1: start worker process 31
2025/11/04 11:40:55 [notice] 1#1: start worker process 32
2025/11/04 11:40:55 [notice] 1#1: start worker process 33
2025/11/04 11:40:55 [notice] 1#1: start worker process 34
2025/11/04 11:40:55 [notice] 1#1: start worker process 35
2025/11/04 11:40:55 [notice] 1#1: start worker process 36
2025/11/04 11:40:55 [notice] 1#1: start worker process 37
2025/11/04 11:40:55 [notice] 1#1: start worker process 38
2025/11/04 11:40:55 [notice] 1#1: start worker process 39
2025/11/04 11:40:55 [notice] 1#1: start worker process 40
2025/11/04 11:40:55 [notice] 1#1: start worker process 41
2025/11/04 11:40:55 [notice] 1#1: start worker process 42
^Cu334535@user-Precision-3460:~/docker-test$ ^C
u334535@user-Precision-3460:~/docker-test$ docker logs --tail 10 app-limit
2025/11/04 11:40:55 [notice] 1#1: start worker process 33
2025/11/04 11:40:55 [notice] 1#1: start worker process 34
2025/11/04 11:40:55 [notice] 1#1: start worker process 35
2025/11/04 11:40:55 [notice] 1#1: start worker process 36
2025/11/04 11:40:55 [notice] 1#1: start worker process 37
2025/11/04 11:40:55 [notice] 1#1: start worker process 38
2025/11/04 11:40:55 [notice] 1#1: start worker process 39
2025/11/04 11:40:55 [notice] 1#1: start worker process 40
2025/11/04 11:40:55 [notice] 1#1: start worker process 41
2025/11/04 11:40:55 [notice] 1#1: start worker process 42
u334535@user-Precision-3460:~/docker-test$ docker logs -t app-limit
2025-11-04T11:40:55.117687235Z /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
2025-11-04T11:40:55.117889092Z /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
2025-11-04T11:40:55.118099511Z /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
2025-11-04T11:40:55.126647209Z 10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
2025-11-04T11:40:55.137379539Z 10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
2025-11-04T11:40:55.137576938Z /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
2025-11-04T11:40:55.137681251Z /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
2025-11-04T11:40:55.140373864Z /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
2025-11-04T11:40:55.141971625Z /docker-entrypoint.sh: Configuration complete; ready for start up
2025-11-04T11:40:55.156629111Z 2025/11/04 11:40:55 [notice] 1#1: using the "epoll" event method
2025-11-04T11:40:55.156665450Z 2025/11/04 11:40:55 [notice] 1#1: nginx/1.29.3
2025-11-04T11:40:55.156674304Z 2025/11/04 11:40:55 [notice] 1#1: built by gcc 14.2.0 (Alpine 14.2.0) 
2025-11-04T11:40:55.156680822Z 2025/11/04 11:40:55 [notice] 1#1: OS: Linux 6.14.0-34-generic
2025-11-04T11:40:55.156685183Z 2025/11/04 11:40:55 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2025-11-04T11:40:55.158272904Z 2025/11/04 11:40:55 [notice] 1#1: start worker processes
2025-11-04T11:40:55.158534982Z 2025/11/04 11:40:55 [notice] 1#1: start worker process 31
2025-11-04T11:40:55.158714114Z 2025/11/04 11:40:55 [notice] 1#1: start worker process 32
2025-11-04T11:40:55.158946210Z 2025/11/04 11:40:55 [notice] 1#1: start worker process 33
2025-11-04T11:40:55.159215748Z 2025/11/04 11:40:55 [notice] 1#1: start worker process 34
2025-11-04T11:40:55.159489458Z 2025/11/04 11:40:55 [notice] 1#1: start worker process 35
2025-11-04T11:40:55.159809459Z 2025/11/04 11:40:55 [notice] 1#1: start worker process 36
2025-11-04T11:40:55.160394046Z 2025/11/04 11:40:55 [notice] 1#1: start worker process 37
2025-11-04T11:40:55.160744706Z 2025/11/04 11:40:55 [notice] 1#1: start worker process 38
2025-11-04T11:40:55.161043066Z 2025/11/04 11:40:55 [notice] 1#1: start worker process 39
2025-11-04T11:40:55.161377855Z 2025/11/04 11:40:55 [notice] 1#1: start worker process 40
2025-11-04T11:40:55.161670712Z 2025/11/04 11:40:55 [notice] 1#1: start worker process 41
2025-11-04T11:40:55.162009628Z 2025/11/04 11:40:55 [notice] 1#1: start worker process 42
u334535@user-Precision-3460:~/docker-test$ docker top app-limit
UID                 PID                 PPID                C                   STIME               TTY                 TIME                CMD
root                44725               44703               0                   11:40               ?                   00:00:00            nginx: master process nginx -g daemon off;
message+            44790               44725               0                   11:40               ?                   00:00:00            nginx: worker process
message+            44791               44725               0                   11:40               ?                   00:00:00            nginx: worker process
message+            44792               44725               0                   11:40               ?                   00:00:00            nginx: worker process
message+            44793               44725               0                   11:40               ?                   00:00:00            nginx: worker process
message+            44794               44725               0                   11:40               ?                   00:00:00            nginx: worker process
message+            44795               44725               0                   11:40               ?                   00:00:00            nginx: worker process
message+            44796               44725               0                   11:40               ?                   00:00:00            nginx: worker process
message+            44797               44725               0                   11:40               ?                   00:00:00            nginx: worker process
message+            44798               44725               0                   11:40               ?                   00:00:00            nginx: worker process
message+            44799               44725               0                   11:40               ?                   00:00:00            nginx: worker process
message+            44800               44725               0                   11:40               ?                   00:00:00            nginx: worker process
message+            44801               44725               0                   11:40               ?                   00:00:00            nginx: worker process
u334535@user-Precision-3460:~/docker-test$ docker exec -it app-limit sh
/ # ps aux
PID   USER     TIME  COMMAND
    1 root      0:00 nginx: master process nginx -g daemon off;
   31 nginx     0:00 nginx: worker process
   32 nginx     0:00 nginx: worker process
   33 nginx     0:00 nginx: worker process
   34 nginx     0:00 nginx: worker process
   35 nginx     0:00 nginx: worker process
   36 nginx     0:00 nginx: worker process
   37 nginx     0:00 nginx: worker process
   38 nginx     0:00 nginx: worker process
   39 nginx     0:00 nginx: worker process
   40 nginx     0:00 nginx: worker process
   41 nginx     0:00 nginx: worker process
   42 nginx     0:00 nginx: worker process
   43 root      0:00 sh
   49 root      0:00 ps aux
/ # netstat
Active Internet connections (w/o servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       
Active UNIX domain sockets (w/o servers)
Proto RefCnt Flags       Type       State         I-Node Path
unix  3      [ ]         STREAM     CONNECTED     146584 
unix  3      [ ]         STREAM     CONNECTED     146598 
unix  3      [ ]         STREAM     CONNECTED     146583 
unix  3      [ ]         STREAM     CONNECTED     146595 
unix  3      [ ]         STREAM     CONNECTED     146603 
unix  3      [ ]         STREAM     CONNECTED     146582 
unix  3      [ ]         STREAM     CONNECTED     146590 
unix  3      [ ]         STREAM     CONNECTED     146588 
unix  3      [ ]         STREAM     CONNECTED     146587 
unix  3      [ ]         STREAM     CONNECTED     146592 
unix  3      [ ]         STREAM     CONNECTED     146604 
unix  3      [ ]         STREAM     CONNECTED     146591 
unix  3      [ ]         STREAM     CONNECTED     146596 
unix  3      [ ]         STREAM     CONNECTED     146586 
unix  3      [ ]         STREAM     CONNECTED     146599 
unix  3      [ ]         STREAM     CONNECTED     146581 
unix  3      [ ]         STREAM     CONNECTED     146594 
unix  3      [ ]         STREAM     CONNECTED     146589 
unix  3      [ ]         STREAM     CONNECTED     146597 
unix  3      [ ]         STREAM     CONNECTED     146585 
unix  3      [ ]         STREAM     CONNECTED     146593 
unix  3      [ ]         STREAM     CONNECTED     146602 
unix  3      [ ]         STREAM     CONNECTED     146601 
unix  3      [ ]         STREAM     CONNECTED     146600 
/ # ls
bin                   docker-entrypoint.sh  lib                   opt                   run                   sys                   var
dev                   etc                   media                 proc                  sbin                  tmp
docker-entrypoint.d   home                  mnt                   root                  srv                   usr
/ # exit
u334535@user-Precision-3460:~/docker-test$ ls -ls
razem 8
4 -rw-rw-r-- 1 u334535 docker  85 lis  4 11:37 app.env
4 -rw-rw-r-- 1 u334535 u334535 51 lis  4 10:28 index.html
u334535@user-Precision-3460:~/docker-test$ docker cp app.env app-limit:/usr/share/nging/html/
no such directory
u334535@user-Precision-3460:~/docker-test$ docker ps
CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS          PORTS                                       NAMES
fd54acfb1ebc   nginx:alpine       "/docker-entrypoint.…"   13 minutes ago   Up 13 minutes   80/tcp                                      app-limit
6f584e341a4d   alpine             "sleep 3600"             15 minutes ago   Up 15 minutes                                               app-test
5e7c50176c18   nginx:latest       "/docker-entrypoint.…"   22 minutes ago   Up 22 minutes   0.0.0.0:32769->80/tcp, [::]:32769->80/tcp   elastic_kapitsa
cebe92207ecd   nginx:latest       "/docker-entrypoint.…"   22 minutes ago   Up 22 minutes   0.0.0.0:8001->80/tcp, [::]:8001->80/tcp     modest_shockley
6bc08ebf7f85   nginx:latest       "/docker-entrypoint.…"   26 minutes ago   Up 26 minutes   0.0.0.0:32768->80/tcp, [::]:32768->80/tcp   wizardly_gagarin
918995e229ad   wordpress:latest   "docker-entrypoint.s…"   35 minutes ago   Up 35 minutes   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp     blog-app
43720d7cfe44   mysql:latest       "docker-entrypoint.s…"   38 minutes ago   Up 38 minutes   3306/tcp, 33060/tcp                         blog-db
u334535@user-Precision-3460:~/docker-test$ docker ps -a
CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS                      PORTS                                       NAMES
fd54acfb1ebc   nginx:alpine       "/docker-entrypoint.…"   13 minutes ago   Up 13 minutes               80/tcp                                      app-limit
6f584e341a4d   alpine             "sleep 3600"             15 minutes ago   Up 15 minutes                                                           app-test
5e7c50176c18   nginx:latest       "/docker-entrypoint.…"   22 minutes ago   Up 22 minutes               0.0.0.0:32769->80/tcp, [::]:32769->80/tcp   elastic_kapitsa
cebe92207ecd   nginx:latest       "/docker-entrypoint.…"   22 minutes ago   Up 22 minutes               0.0.0.0:8001->80/tcp, [::]:8001->80/tcp     modest_shockley
cba3d4b01694   alpine             "sh"                     23 minutes ago   Exited (0) 23 minutes ago                                               elated_aryabhata
a1134cdfc0b0   alpine             "hs"                     23 minutes ago   Created                                                                 youthful_blackwell
f1f02cfe87bd   nginx:latest       "/docker-entrypoint.…"   25 minutes ago   Exited (0) 24 minutes ago                                               boring_darwin
6bc08ebf7f85   nginx:latest       "/docker-entrypoint.…"   26 minutes ago   Up 26 minutes               0.0.0.0:32768->80/tcp, [::]:32768->80/tcp   wizardly_gagarin
918995e229ad   wordpress:latest   "docker-entrypoint.s…"   35 minutes ago   Up 35 minutes               0.0.0.0:8080->80/tcp, [::]:8080->80/tcp     blog-app
43720d7cfe44   mysql:latest       "docker-entrypoint.s…"   38 minutes ago   Up 38 minutes               3306/tcp, 33060/tcp                         blog-db
a230b8996909   alpine             "sh"                     2 hours ago      Exited (1) 2 hours ago                                                  serene_mclaren
611cefaaccae   alpine             "sh"                     2 hours ago      Exited (0) 2 hours ago                                                  kontener2
cc5567ee9cf9   alpine             "sh"                     2 hours ago      Exited (0) 2 hours ago                                                  kontener1
c3a0ff690e72   alpine             "sh"                     2 hours ago      Exited (0) 2 hours ago                                                  kind_matsumoto
2be2496cc9e5   ubuntu             "bash"                   2 hours ago      Exited (0) 2 hours ago                                                  peaceful_zhukovsky
8ec89171ca40   ubuntu             "bash"                   2 hours ago      Exited (0) 2 hours ago                                                  frosty_newton
115ca1734802   hello-world        "/hello"                 2 hours ago      Exited (0) 2 hours ago                                                  trusting_swartz
76d049775ae2   hello-world        "/hello"                 2 hours ago      Exited (0) 2 hours ago                                                  angry_sinoussi
u334535@user-Precision-3460:~/docker-test$ docker system df
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          9         7         2.807GB   1.135GB (40%)
Containers      18        7         5.653kB   1.242kB (21%)
Local Volumes   8         2         575.7MB   278.4MB (48%)
Build Cache     0         0         0B        0B
u334535@user-Precision-3460:~/docker-test$ docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
cba3d4b01694212a568056193856bd3caeaa98ab8ec04bac5e235a45e1f517a3
a1134cdfc0b07dfc729a4eb1bc80055c6f700afd117d5da60be39e91b1dc0a5f
f1f02cfe87bdb03323ab60394216f5a2a02fbd1884cda4d464ac7fed409d2749
a230b89969091d4e4145f7059aeaec265a507e0b381568ba408c39555ad09ffc
611cefaaccae7a09c2e083a87fbb38d017bf0bf45236943edfb8dafb045ebc0f
cc5567ee9cf9d9add707e528411dbdc1bca2d45d5f50cca6dc4ed7fbd3fa132b
c3a0ff690e726c4ec61ed03f4e646e3da42ebec9e3152cde8f52e78ed98f17c4
2be2496cc9e5d6a6de4849a312e6b82b95ada8f76eccd4ed368e09d2810901c3
8ec89171ca40d5c6168d71c74328771de41c0c90f7e9751b5563bf5c9496c94d
115ca1734802001af80eafa6e2e56c14b0d71c02240537bbdd53c3b073b65639
76d049775ae2e4d19923e8e324de739ee0d53d05eed86c514a1f5687a3807798

Total reclaimed space: 1.242kB
u334535@user-Precision-3460:~/docker-test$ docker images
REPOSITORY    TAG         IMAGE ID       CREATED        SIZE
nginx         alpine      d4918ca78576   6 days ago     52.8MB
nginx         latest      9d0e6f6199dc   6 days ago     152MB
mysql         latest      f6b0ca07d79d   13 days ago    934MB
mysql         8.0         34178dbaefd0   13 days ago    783MB
postgres      15-alpine   ba05c11fe977   2 weeks ago    273MB
alpine        latest      706db57fb206   3 weeks ago    8.32MB
ubuntu        latest      97bed23a3497   4 weeks ago    78.1MB
wordpress     latest      7332768c717f   4 weeks ago    734MB
hello-world   latest      1b44b5a3e06a   2 months ago   10.1kB
u334535@user-Precision-3460:~/docker-test$ docker rmi nginx:alpine
Error response from daemon: conflict: unable to remove repository reference "nginx:alpine" (must force) - container fd54acfb1ebc is using its referenced image d4918ca78576
u334535@user-Precision-3460:~/docker-test$ docker rmi -f nginx:alpine
Untagged: nginx:alpine
Untagged: nginx@sha256:b3c656d55d7ad751196f21b7fd2e8d4da9cb430e32f646adcf92441b72f82b14
u334535@user-Precision-3460:~/docker-test$ docker image prune -a
WARNING! This will remove all images without at least one container associated to them.
Are you sure you want to continue? [y/N] y
Deleted Images:
untagged: hello-world:latest
untagged: hello-world@sha256:56433a6be3fda188089fb548eae3d91df3ed0d6589f7c2656121b911198df065
deleted: sha256:1b44b5a3e06a9aae883e7bf25e45c100be0bb81a0e01b32de604f3ac44711634
deleted: sha256:53d204b3dc5ddbc129df4ce71996b8168711e211274c785de5e0d4eb68ec3851
untagged: ubuntu:latest
untagged: ubuntu@sha256:66460d557b25769b102175144d538d88219c077c678a49af4afca6fbfc1b5252
deleted: sha256:97bed23a34971024aa8d254abbe67b7168772340d1f494034773bc464e8dd5b6
deleted: sha256:073ec47a8c22dcaa4d6e5758799ccefe2f9bde943685830b1bf6fd2395f5eabc
untagged: postgres:15-alpine
untagged: postgres@sha256:64583b3cb4f2010277bdd9749456de78e5c36f8956466ba14b0b96922e510950
deleted: sha256:ba05c11fe977ed520354d744e145736c881d4a4a581718dbcd6eec266f822549
deleted: sha256:1282e695225154a10f8392839983b9bedbc798ea720cb337f5bb4e3102b6d951
deleted: sha256:cbc8a5925f5cc0321e42f70bd64ab5649b2d53a121ffbb5fe7417a6a85936c85
deleted: sha256:83251c97e183177acc1db4e0f9d4301811ec2b4012771b472b2e4d06789dc1d0
deleted: sha256:effae3e105034bd03f6c3c4f6894354094e633a04da4d1f11a39a85abef3714a
deleted: sha256:a6e41e5b194cf159cd72105d5f1511f276658f2c9d510956620411d0743b897a
deleted: sha256:eb559bb8853ce47312c75ceb62b4994073ca14a7ac6c09be29980bdfdd9d5c63
deleted: sha256:dfcf6233bcc2394362dcbce17a0bd6909ede8347814dfcc3b33f5d125e6dff43
deleted: sha256:573c9aac9563f2b2f22b951feb68e452f97b12aac1670e531c2d3d39994fece8
deleted: sha256:d0276add30654f443d1cfec10d1881a420f729e46fceb4117123a131576c3609
deleted: sha256:c2ed485ae7f8080bd94c41cfde830768dafe886d295e678ec731bd21006e2e42
untagged: mysql:8.0
untagged: mysql@sha256:f37951fc3753a6a22d6c7bf6978c5e5fefcf6f31814d98c582524f98eae52b21
deleted: sha256:34178dbaefd067c5997133cbdef31f164aa899689394f70b065725afb7aa322a
deleted: sha256:fab78eceacfcebbb5bd484ceb21f8022a79fb772f0707b4d7fe67455abacc036
deleted: sha256:7ae921cf3c0f0da284d83348460de8766432bdabf3d894746963bd693ec383ab
deleted: sha256:dc8911c9dc2670c8ec7bbefbdf3b686204e176d3c24d36fd7a03ab2db9955924
deleted: sha256:47d0aca02b92cc2c9283a4271d25505a1e9e89ef280dfe746fa20a18b8bb5436
deleted: sha256:593af6ee05a82bc0db61d90c7cbb58614872497b180ab06e9dd3218493262bec
deleted: sha256:d52aa01dc5a87269bd1aa938d02cf36b7049e8e4442bacf4e55da11418f0d979
deleted: sha256:d8e73fb58f5dd547c7e610ca9b1d5d002d9e5126db61b832c6f39ea8af6a49ee
deleted: sha256:f748a496326a844036e7093759965acc76d46d6650fed0b559790f1621b016b7
deleted: sha256:9863f254df026b93d0179af62c863ec49ae91b1c6f13cb16317438f1a37d70b7
deleted: sha256:be3b8d46f5b3759f2b6ca5a7112d4877b83b52ab3b7ad624b55d087403c11c38

Total reclaimed space: 1.012GB
u334535@user-Precision-3460:~/docker-test$ docker volume prune
WARNING! This will remove anonymous local volumes not used by at least one container.
Are you sure you want to continue? [y/N] t
u334535@user-Precision-3460:~/docker-test$ docker volume prune
WARNING! This will remove anonymous local volumes not used by at least one container.
Are you sure you want to continue? [y/N] y
Deleted Volumes:
78ff3d2ae0c8649963fdb567d748811ef88a8cf18d42951e66a4efc42ff6b237
ac8838120d03f3e945c85702dfa7b8f439e23db1d8b062fed8e3a3117e779da4
3bdc22614ce9c45379eca6684cc9d8688a87cfbf8a7da7871d326b515a80595f
b5748940c413241c17098bbed95bd4a56fa04ccf9af092a875c1dcefc8493253
b1f05df826e0464ed55614a1731672ff66bce895420cf426220465c5699c22b6

Total reclaimed space: 230.6MB
u334535@user-Precision-3460:~/docker-test$ docker network prune
WARNING! This will remove all custom networks not used by at least one container.
Are you sure you want to continue? [y/N] y
u334535@user-Precision-3460:~/docker-test$ docker ps
CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS          PORTS                                       NAMES
fd54acfb1ebc   d4918ca78576       "/docker-entrypoint.…"   15 minutes ago   Up 15 minutes   80/tcp                                      app-limit
6f584e341a4d   alpine             "sleep 3600"             17 minutes ago   Up 17 minutes                                               app-test
5e7c50176c18   nginx:latest       "/docker-entrypoint.…"   23 minutes ago   Up 23 minutes   0.0.0.0:32769->80/tcp, [::]:32769->80/tcp   elastic_kapitsa
cebe92207ecd   nginx:latest       "/docker-entrypoint.…"   24 minutes ago   Up 24 minutes   0.0.0.0:8001->80/tcp, [::]:8001->80/tcp     modest_shockley
6bc08ebf7f85   nginx:latest       "/docker-entrypoint.…"   28 minutes ago   Up 28 minutes   0.0.0.0:32768->80/tcp, [::]:32768->80/tcp   wizardly_gagarin
918995e229ad   wordpress:latest   "docker-entrypoint.s…"   37 minutes ago   Up 37 minutes   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp     blog-app
43720d7cfe44   mysql:latest       "docker-entrypoint.s…"   40 minutes ago   Up 40 minutes   3306/tcp, 33060/tcp                         blog-db
u334535@user-Precision-3460:~/docker-test$ docker system prune --dry-run
unknown flag: --dry-run

Usage:  docker system prune [OPTIONS]

Run 'docker system prune --help' for more information
u334535@user-Precision-3460:~/docker-test$ docker system prune -a --volumes
WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all anonymous volumes not used by at least one container
  - all images without at least one container associated to them
  - all build cache

Are you sure you want to continue? [y/N] y
Total reclaimed space: 0B
u334535@user-Precision-3460:~/docker-test$ docker system df
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          5         5         1.794GB   86.94MB (4%)
Containers      7         7         4.411kB   0B (0%)
Local Volumes   3         2         345.2MB   47.82MB (13%)
Build Cache     0         0         0B        0B
u334535@user-Precision-3460:~/docker-test$ docker ps
CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS          PORTS                                       NAMES
fd54acfb1ebc   d4918ca78576       "/docker-entrypoint.…"   16 minutes ago   Up 16 minutes   80/tcp                                      app-limit
6f584e341a4d   alpine             "sleep 3600"             18 minutes ago   Up 18 minutes                                               app-test
5e7c50176c18   nginx:latest       "/docker-entrypoint.…"   25 minutes ago   Up 25 minutes   0.0.0.0:32769->80/tcp, [::]:32769->80/tcp   elastic_kapitsa
cebe92207ecd   nginx:latest       "/docker-entrypoint.…"   26 minutes ago   Up 26 minutes   0.0.0.0:8001->80/tcp, [::]:8001->80/tcp     modest_shockley
6bc08ebf7f85   nginx:latest       "/docker-entrypoint.…"   29 minutes ago   Up 29 minutes   0.0.0.0:32768->80/tcp, [::]:32768->80/tcp   wizardly_gagarin
918995e229ad   wordpress:latest   "docker-entrypoint.s…"   38 minutes ago   Up 38 minutes   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp     blog-app
43720d7cfe44   mysql:latest       "docker-entrypoint.s…"   41 minutes ago   Up 41 minutes   3306/tcp, 33060/tcp                         blog-db
u334535@user-Precision-3460:~/docker-test$ docker ps -a
CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS          PORTS                                       NAMES
fd54acfb1ebc   d4918ca78576       "/docker-entrypoint.…"   16 minutes ago   Up 16 minutes   80/tcp                                      app-limit
6f584e341a4d   alpine             "sleep 3600"             18 minutes ago   Up 18 minutes                                               app-test
5e7c50176c18   nginx:latest       "/docker-entrypoint.…"   25 minutes ago   Up 25 minutes   0.0.0.0:32769->80/tcp, [::]:32769->80/tcp   elastic_kapitsa
cebe92207ecd   nginx:latest       "/docker-entrypoint.…"   26 minutes ago   Up 26 minutes   0.0.0.0:8001->80/tcp, [::]:8001->80/tcp     modest_shockley
6bc08ebf7f85   nginx:latest       "/docker-entrypoint.…"   29 minutes ago   Up 29 minutes   0.0.0.0:32768->80/tcp, [::]:32768->80/tcp   wizardly_gagarin
918995e229ad   wordpress:latest   "docker-entrypoint.s…"   38 minutes ago   Up 38 minutes   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp     blog-app
43720d7cfe44   mysql:latest       "docker-entrypoint.s…"   42 minutes ago   Up 42 minutes   3306/tcp, 33060/tcp                         blog-db



































