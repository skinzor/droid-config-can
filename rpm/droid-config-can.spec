# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc

%define device can
%define vendor huawei

%define vendor_pretty Huawei
%define device_pretty Nova

%define dcd_path ./

# Adjust this for your device
%define pixel_ratio 1.8

# We assume most devices will
%define have_modem 1

Provides: ofono-configs

%include droid-configs-device/droid-configs.inc
