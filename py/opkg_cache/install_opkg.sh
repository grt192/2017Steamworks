set -e
PACKAGES=()
DO_INSTALL=0
if ! opkg list-installed | grep -F 'python36 - 3.6.0-r1'; then
    PACKAGES+=("opkg_cache/python36_3.6.0-r1_cortexa9-vfpv3.ipk")
    DO_INSTALL=1
else
    echo "python36 already installed"
fi
if ! opkg list-installed | grep -F 'libgfortran3 - 4.8.2-r0'; then
    PACKAGES+=("opkg_cache/libgfortran3_4.8.2-r0_cortexa9-vfpv3.ipk")
    DO_INSTALL=1
else
    echo "libgfortran3 already installed"
fi
if ! opkg list-installed | grep -F 'libgcc1 - 4.9.2-r0.73'; then
    PACKAGES+=("opkg_cache/libgcc1_4.9.2-r0.73_cortexa9-vfpv3.ipk")
    DO_INSTALL=1
else
    echo "libgcc1 already installed"
fi
if ! opkg list-installed | grep -F 'libstdc++6 - 4.9.2-r0.71'; then
    PACKAGES+=("opkg_cache/libstdc++6_4.9.2-r0.71_cortexa9-vfpv3.ipk")
    DO_INSTALL=1
else
    echo "libstdc++6 already installed"
fi
if ! opkg list-installed | grep -F 'ATLAS - 3.10.2'; then
    PACKAGES+=("opkg_cache/ATLAS_3.10.2_cortexa9-vfpv3.ipk")
    DO_INSTALL=1
else
    echo "ATLAS already installed"
fi
if ! opkg list-installed | grep -F 'python36-numpy - 1.12.0'; then
    PACKAGES+=("opkg_cache/python36-numpy_1.12.0_cortexa9-vfpv3.ipk")
    DO_INSTALL=1
else
    echo "python36-numpy already installed"
fi
if ! opkg list-installed | grep -F 'opencv3 - 3.2.0'; then
    PACKAGES+=("opkg_cache/opencv3_3.2.0_cortexa9-vfpv3.ipk")
    DO_INSTALL=1
else
    echo "opencv3 already installed"
fi
if ! opkg list-installed | grep -F 'python36-opencv3 - 3.2.0'; then
    PACKAGES+=("opkg_cache/python36-opencv3_3.2.0_cortexa9-vfpv3.ipk")
    DO_INSTALL=1
else
    echo "python36-opencv3 already installed"
fi
if ! opkg list-installed | grep -F 'python36-robotpy-cscore - 2017.0.0rc3'; then
    PACKAGES+=("opkg_cache/python36-robotpy-cscore_2017.0.0rc3_cortexa9-vfpv3.ipk")
    DO_INSTALL=1
else
    echo "python36-robotpy-cscore already installed"
fi
if [ "${DO_INSTALL}" == "0" ]; then
    echo "No packages to install."
else
    opkg install  ${PACKAGES[@]}
fi