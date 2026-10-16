#!/usr/bin/env bash
# Read-only Android device details; never queries IMEI or private partitions.
set -euo pipefail
command -v adb >/dev/null 2>&1 || { echo 'ADB not found; install Android Platform Tools.' >&2; exit 127; }
echo '== Connected devices =='; adb devices -l
echo '== Manufacturer / model / Android version =='; adb shell getprop ro.product.manufacturer; adb shell getprop ro.product.model; adb shell getprop ro.build.version.release
echo 'No IMEI, SIM, NVRAM, EFS or partition contents were read.'
