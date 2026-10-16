from pathlib import Path

content = r'''# 📱 Complete Guide to Mobile Phone IMEI Identity and Changes

> **Last updated:** August 20, 2026  
> **Version:** 3.0  
> **Repository:** [IMEI-Complete-Guide](https://github.com/humayun-himu/imei-complete-guide)

---

## 📖 Table of Contents

- [What Is IMEI?](#-what-is-imei)
- [IMEI Structure](#-imei-structure)
- [How to Identify an IMEI](#-how-to-identify-an-imei)
- [Software and Tools](#-software-and-tools)
- [Code and Scripts](#-code-and-scripts)
- [Mobile Apps](#-mobile-apps)
- [APIs and Web Services](#-apis-and-web-services)
- [Forensic Techniques](#-forensic-techniques)
- [GitHub Repository List](#-github-repository-list-complete)
- [Resources and References](#-resources-and-references)
- [IMEI Change Methods (Educational Only)](#-imei-change-methods-educational-only)
- [Legal Warning](#-legal-warning)
- [Support and Contributions](#-support-and-contributions)
- [Credits](#-credits)
- [License](#-license)
- [Quick Reference Table](#-quick-reference-table)
- [Web App and Python Toolkit](#-complete-web-app-and-python-toolkit)

---

## 📌 What Is IMEI?

**IMEI** (International Mobile Equipment Identity) is a unique identification number associated with a mobile device, commonly represented as 15 digits. It is used to identify devices on GSM, UMTS, and LTE networks.

> **Note:** An IMEI is associated with a device, not a SIM card. Dual-SIM devices may have a separate IMEI for each SIM slot.

### Why IMEI matters
- 📱 **Device identification:** Identifies a device on a network.
- 🔒 **Security:** Stolen phones may be added to a blacklist.
- 🛡️ **Warranty verification:** Helps establish device authenticity.
- 🌐 **Network access:** Helps carriers identify devices connecting to their networks.

---

## 🧬 IMEI Structure

A complete IMEI is divided into the following parts:

```
TAC (8 digits) + SNR (6 digits) + CD (1 digit) = 15 digits
Example: 357561856136304
```

| Part | Description | Length |
|------|-------------|--------|
| **TAC** (Type Allocation Code) | Identifies the device model; allocated by GSMA | 8 digits |
| **SNR** (Serial Number) | Unique serial number assigned by the manufacturer | 6 digits |
| **CD** (Check Digit) | Digit validated using the Luhn algorithm | 1 digit |

### Reporting Body Identifier (RBI)

The first two digits of the TAC indicate an authority:

| Code | Authority | Country |
|------|-----------|---------|
| `01` | PTCRB | USA |
| `35` | BABT | United Kingdom |
| `44` | ICASA | South Africa |
| `49` | BNetzA | Germany |
| `86` | TAF | China |
| `99` | GCF | Global |

---

## 🔍 How to Identify an IMEI

### 1. USSD code (easiest method)
Dial `*#06#` on the phone dial pad to display the IMEI number.

<details>
<summary><b>Other USSD codes</b></summary>

| Code | Function |
|------|----------|
| `*#*#4636#*#*` | Device information and statistics |
| `*#*#197328640#*#*` | Service mode menu |
| `*#*#2846579#*#*` | Engineering mode (Huawei) |
| `*#*#3646633#*#*` | Engineering mode (MediaTek) |
</details>

### 2. Device settings
- **Android:** Settings → About Phone → Status → IMEI Information
- **iPhone:** Settings → General → About → IMEI

### 3. Back cover / battery compartment
On phones with removable batteries, the IMEI may be printed on a label inside the battery compartment.

### 4. ADB (Android Debug Bridge) commands
```bash
adb shell service call iphonesubinfo 1
adb shell dumpsys iphonesubinfo
adb shell getprop ro.ril.oem.imei
```

### 5. AT commands
```bash
AT+CGSN
AT+IMEINUM
AT+GSN
```

### 6. Forensic extraction
- Logical extraction: collect the IMEI from device system information.
- Physical extraction: hardware-level extraction through JTAG or chip-off forensics.

---

## 🛠️ Software and Tools

### 1. IMEI-Find

https://img.shields.io/github/stars/D3crypT0r/IMEI-Find

- **Description:** GUI-based tool for searching an Android device file system for IMEI-related data using ADB.
- **Features:**
  - Search for specific terms (for example, `IMEI`, `getImei`).
  - Display mounted partitions.
  - Export results in JSON format.
- **Requirements:** Python 3.x, ADB, PyQt5
- **Installation:**
```bash
git clone https://github.com/D3crypT0r/IMEI-Find.git
cd IMEI-Find
pip install PyQt5 pyqt5-tools
python3 IMEI-Find.py
```
- **License:** Open Source

### 2. IMEI_Lookup

https://img.shields.io/github/stars/itsKayWat/IMEI_Lookup

- **Description:** Modern IMEI lookup tool with PIN authentication, paid/free device checks, and an IMEI calculator.
- **Features:** Responsive UI, sound effects, multi-user support.
- **Built with:** Vanilla JS/CSS
- **License:** MIT

### 3. IMEI Validator

https://img.shields.io/github/stars/JonnyBytesMe/imei-validator

- **Description:** Python tool for IMEI validation and analysis.
- **Features:** Luhn validation, TAC database lookup, RBI code analysis, and batch processing.
- **Usage:**
```bash
python imei_validator.py --imei 357561856136304
python imei_validator.py --batch input_imeis.txt
```
- **Requirements:** Python 3.7+

### 4. IMEI Scraper & Validation Tool

https://img.shields.io/github/stars/altheasignals/imei_scrape

- **Description:** High-performance Python application for collecting, managing, and validating IMEIs.
- **Features:** High-performance scraping, carrier compatibility verification, CSV-based database management, and blacklist management.
- **Installation:**
```bash
pip install -r requirements-v1.txt
python -m playwright install chromium
```
- **Usage:**
```bash
python src/imei_manager.py scrape --count 50 --brand Samsung
python src/imei_manager.py validate --imei 351138316163206
```

### 5. IMEI Atlas

https://img.shields.io/github/stars/IMEI-Atlas/IMEI-Atlas

- **Description:** IMEI generator and validator. Supports AT commands for MikroTik and FiberHome routers.
- **Features:** Luhn-based IMEI generation, TAC database for popular devices, bulk generation, and AT command generation.
- **License:** GNU GPL v3.0

### 6. MTK IMEI Patcher

https://img.shields.io/github/stars/timjosten/mtk_imei

- **Description:** Script for rebuilding the NVRAM partition for Xiaomi Helio G-series phones.
- **Feature:** Creates TWRP-flashable files.

### 7. IMEI Changer (MTK)

https://img.shields.io/github/stars/alecsx/imei-changer-mtk

- **Description:** Command-line IMEI change tool for MediaTek devices.
- **Installation:** `pip install imei-changer-mtk`
- **Usage:**
```bash
imei-changer --imei1 357561856136304 --imei2 357561856136305
```

### 8. IMEI-Change

https://img.shields.io/github/stars/tomsawyer777/IMEI-Change

- **Description:** Simple IMEI change tool for Android phones (root required).
- **Features:** Backup/restore and dual-SIM support.
- **Requirements:** Root access, ADB.

---

## 💻 Code and Scripts

### 1. Luhn algorithm (Python)
```python
def validate_imei(imei):
    """Validate an IMEI using the Luhn algorithm"""
    # Keep digits only
    digits = [int(d) for d in str(imei) if d.isdigit()]
    
    # Remove the check digit
    check_digit = digits[-1]
    payload = digits[:-1]
    
    # Luhn algorithm
    total = 0
    for i, d in enumerate(reversed(payload)):
        if i % 2 == 0:  # Every second digit (from the right)
            d *= 2
            if d > 9:
                d -= 9
        total += d
    
    calculated = (10 - (total % 10)) % 10
    return calculated == check_digit
```
[Source: JonnyBytesMe/imei-validator]

### 2. IMEI generator (Python)
```python
import random

def generate_imei(tac, serial_length=6):
    """Generate an IMEI from a TAC and serial number"""
    # TAC (8 digits) + serial number (6 digits)
    serial = ''.join([str(random.randint(0,9)) for _ in range(serial_length)])
    base = str(tac) + serial
    
    # Calculate the Luhn check digit
    total = 0
    for i, d in enumerate(reversed(base)):
        d = int(d)
        if i % 2 == 0:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    
    check_digit = (10 - (total % 10)) % 10
    return base + str(check_digit)

# Usage
print(generate_imei(35756185))  # Example: 357561856136304
```
[Source: bstein/py-imei-generator]

### 3. Android (Java) — retrieve IMEI
```java
import android.telephony.TelephonyManager;
import android.content.Context;
import android.Manifest;
import android.content.pm.PackageManager;
import androidx.core.app.ActivityCompat;

public class IMEIFetcher {
    public static String getIMEI(Context context) {
        TelephonyManager telephonyManager = (TelephonyManager) 
            context.getSystemService(Context.TELEPHONY_SERVICE);
        
        if (ActivityCompat.checkSelfPermission(context, 
            Manifest.permission.READ_PHONE_STATE) == PackageManager.PERMISSION_GRANTED) {
            
            if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.Q) {
                return telephonyManager.getImei(); // Android 10+
            } else {
                return telephonyManager.getDeviceId(); // For Android 9
            }
        }
        return null;
    }
}
```
[Source: Quectel Forums]

### 4. PHP — Luhn validation
```php
<?php
class LuhnAlgorithm {
    public function isValid($number) {
        $digits = str_split(strrev(preg_replace('/\D/', '', $number)));
        $sum = 0;
        foreach ($digits as $i => $digit) {
            if ($i % 2 == 1) {
                $digit *= 2;
                if ($digit > 9) $digit -= 9;
            }
            $sum += $digit;
        }
        return $sum % 10 == 0;
    }
}

// Usage
$validator = new LuhnAlgorithm();
echo $validator->isValid("357561856136304") ? "Valid" : "Invalid";
```
[Source: TheWebSolver/luhn-algorithm]

### 5. JavaScript — IMEI validator
```javascript
function validateIMEI(imei) {
    const digits = imei.replace(/\D/g, '').split('').map(Number);
    if (digits.length !== 15) return false;
    
    let sum = 0;
    for (let i = digits.length - 2; i >= 0; i--) {
        let digit = digits[i];
        if ((digits.length - 1 - i) % 2 === 1) {
            digit *= 2;
            if (digit > 9) digit -= 9;
        }
        sum += digit;
    }
    const checkDigit = (10 - (sum % 10)) % 10;
    return checkDigit === digits[digits.length - 1];
}
```

### 6. Bash — retrieve IMEI using ADB
```bash
#!/bin/bash

echo "=== All IMEI retrieval methods ==="

# Method 1
echo -e "\n[Method 1] service call:"
adb shell service call iphonesubinfo 1

# Method 2
echo -e "\n[Method 2] dumpsys:"
adb shell dumpsys iphonesubinfo | grep -i imei

# Method 3
echo -e "\n[Method 3] getprop:"
adb shell getprop | grep -i imei

# Method 4 (rooted)
echo -e "\n[Method 4] file system:"
adb shell su -c "cat /proc/cmdline | grep -i imei"
adb shell su -c "cat /data/nvram/md/NVRAM/NVD_IMEI/IMEI"
```

### 7. Node.js — IMEI validator
```javascript
const validateIMEI = (imei) => {
    const digits = imei.replace(/\D/g, '').split('').map(Number);
    if (digits.length !== 15) return false;
    
    let sum = 0;
    for (let i = digits.length - 2; i >= 0; i--) {
        let digit = digits[i];
        if ((digits.length - 1 - i) % 2 === 1) {
            digit *= 2;
            if (digit > 9) digit -= 9;
        }
        sum += digit;
    }
    return (10 - (sum % 10)) % 10 === digits[digits.length - 1];
};

console.log(validateIMEI("357561856136304")); // true
```

### 8. Python — get device information from an IMEI
```python
import requests
import json

def get_device_info(imei):
    """Get device information from the IMEI.info API"""
    url = f"https://api.imei.info/v1/device/{imei}"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Usage
info = get_device_info("357561856136304")
if info:
    print(f"Brand: {info.get('brand')}")
    print(f"Model: {info.get('model')}")
    print(f"Manufacturer: {info.get('manufacturer')}")
```

---

## 📱 Mobile Apps

### 1. Flutter Device IMEI Plugin
https://img.shields.io/github/stars/pranilshah4024/flutter_device_imei

- **Description:** Flutter plugin for retrieving device IDs on Android and iOS.
- **Features:** Below Android 10, returns IMEI; Android 10+, returns ANDROID_ID; iOS returns UUID.
- **Usage:**
```dart
import 'package:flutter_device_imei/flutter_device_imei.dart';
String imei = await FlutterDeviceImei.instance.getIMEI();
```

### 2. IMEI Plugin (Flutter)
https://img.shields.io/github/stars/nqhhdev/imei_plugin

- **Description:** Flutter plugin for retrieving IMEI on Android and iOS.
- **Feature:** Dual/triple-SIM support.
- **Usage:**
```dart
String imei = await ImeiPlugin.getImei();
List<String> multiImei = await ImeiPlugin.getImeiMulti();
```

### 3. MTK IMEI Switcheroo App
https://img.shields.io/github/stars/flipphoneguy/mtk-imei-switcheroo-app

- **Description:** App for reading and rewriting IMEI, Bluetooth MAC, and Wi-Fi MAC on rooted MediaTek MT67xx phones.
- **Features:** Generate IMEI, randomize MAC addresses, save the last five values.
- **Requirement:** Root (Magisk).

### 4. Device Info (Android)
https://img.shields.io/badge/GitHub-opt05/deviceid-blue

- **Description:** Open-source Android app displaying IMEI/MEID, device model, Android ID, Wi-Fi MAC, Bluetooth MAC, and other details.
- **Availability:** Available on the Play Store.

### 5. SimInfo
https://img.shields.io/github/stars/tech1ee/SimInfo

- **Description:** Android app providing SIM information, network connectivity, and carrier-service details.
- **Features:** Displays IMEI, Android ID, and ICCID.

### 6. IMEI Analyzer (React Native)
https://img.shields.io/github/stars/mahmoudabdelmomen/imei-analyzer

- **Description:** IMEI analysis app built with React Native.
- **Features:** IMEI validation, device information, and blacklist checks.

---

## 🌐 APIs and Web Services

### 1. IMEI.info API
https://img.shields.io/github/stars/imei-info/imei-check-api-node

- **Description:** API for retrieving mobile device information using an IMEI.
- **Node.js client:** `npm install imei-info`
- **Usage:**
```javascript
const IMEI = require('imei-info');
const client = new IMEI('YOUR_API_KEY');
const info = await client.check('357561856136304');
```

### 2. IMEI Checker API (Django)
https://img.shields.io/github/stars/iurkinvalentin/IMEI_checker

- **Description:** Django REST API that checks IMEIs through an external API.
- **Endpoint:** `/api/v1/check-imei/`
- **Installation:**
```bash
git clone https://github.com/iurkinvalentin/IMEI_checker
pip install -r requirements.txt
python manage.py runserver
```

### 3. iFreeiCloud API
https://img.shields.io/github/stars/hopla/ifreeicloud

- **Description:** TypeScript client for IMEI, iCloud, and carrier checks.
- **Installation:** `npm install @hopla/ifreeicloud`
- **Usage:**
```typescript
import { iFreeiCloud } from '@hopla/ifreeicloud';
const client = new iFreeiCloud('API_KEY');
const result = await client.checkImei('357561856136304');
```

### 4. e-Devlet IMEI Check (Go)
https://img.shields.io/github/stars/KilimcininKorOglu/edevlet-imei-check

- **Description:** Go library for checking IMEI registration status on Türkiye's e-Devlet portal.
- **Usage:**
```go
import "github.com/KilimcininKorOglu/edevlet-imei-check"
status := imei.Check("357561856136304")
```

### 5. Open IMEI Database API
https://img.shields.io/github/stars/OpenIMEI/opendb

- **Description:** Open-source IMEI database API.
- **Features:** Free access, TAC database, and device information.
- **API:** https://api.openimei.com/v1/lookup/{imei}

---

## 🔬 Forensic Techniques

### 1. Logical extraction
Collect IMEI information from device settings or system information using mobile forensic tools.

Example tools:
- Cellebrite UFED
- Oxygen Forensics
- Andriller
- Autopsy (Android accessory)

### 2. Physical extraction
If a device is damaged or inaccessible, hardware-level extraction may be performed using JTAG or chip-off forensics.

Required equipment:
- JTAG interface (Raspberry Pi + OpenOCD)
- Chip-off station (hot-air rework)
- eMMC programmer (EasyJTAG, Octoplus)

### 3. MTK NVRAM reverse engineering
Reverse-engineering the IMEI storage format on MediaTek devices.

- **File location:** `/mnt/vendor/nvdata/md/NVRAM/NVD_IMEI/LD0B_001`
- **Encryption:** AES-128-ECB + MD5-XOR checksum
- **Decryption tool:** `mtk-imei-decrypt`

### 4. pyAndriller
https://img.shields.io/github/stars/vicgc/pyAndriller

- **Description:** Forensically sound, read-only data extraction tool for rooted Android devices.
- **Features:** IMEI, device information, installed apps, SMS, and call logs.
- **Usage:**
```bash
python pyandriller.py --target /dev/block/mmcblk0
```

### 5. Mobile-Diagnostics-Research
https://img.shields.io/github/stars/fsinnes/Mobile-Diagnostics-Research

- **Description:** Repository for mobile-device identification and diagnostics research.
- **AT commands:** `AT+IMEINUM`, `shell cat /csa/imei/serialno.dat`
- **Windows tool:** `adb shell wmic path Win32_BaseBoard get SerialNumber`

### 6. Forensic imaging
```bash
# Android eMMC dump
adb shell su -c "dd if=/dev/block/mmcblk0 of=/sdcard/emmc_dump.img"

# NVRAM dump (MTK)
adb shell su -c "dd if=/dev/block/platform/mtk-msdc.0/11230000.msdc0/by-name/nvram of=/sdcard/nvram_dump.bin"

# Extract IMEI
strings emmc_dump.img | grep -E '[0-9]{15}'
```

### 7. Forensic analysis tools
```bash
# Scalpel
scalpel -c scalpel.conf emmc_dump.img

# PhotoRec
photorec emmc_dump.img

# DD recovery
dd if=emmc_dump.img of=imei_sector.bin bs=512 count=1 skip=110100
```

---

## 📦 GitHub Repository List (Complete)

| # | Repository | Description | Language | License | ⭐ |
|---:|---|---|---|---|---:|
| 1 | D3crypT0r/IMEI-Find | ADB-based IMEI finder | Python | - | 15 |
| 2 | itsKayWat/IMEI_Lookup | IMEI lookup tool | HTML/CSS/JS | MIT | 20 |
| 3 | JonnyBytesMe/imei-validator | IMEI validator | Python | - | 25 |
| 4 | altheasignals/imei_scrape | IMEI scraper and validator | Python | - | 10 |
| 5 | IMEI-Atlas/IMEI-Atlas | IMEI generator and validator | Python | GPL v3.0 | 18 |
| 6 | Supa-mustea/IMEI-tracker | IMEI tracking for law enforcement | Python/Node.js | - | 12 |
| 7 | Nurumoney/IMEI-Tracker | Real-time tracking with Flask + SocketIO | Python | - | 8 |
| 8 | pranilshah4024/flutter_device_imei | Flutter IMEI plugin | Dart | - | 30 |
| 9 | nqhhdev/imei_plugin | Flutter IMEI plugin | Java/Dart | MIT | 22 |
| 10 | flipphoneguy/mtk-imei-switcheroo-app | MTK IMEI change app | Java | - | 45 |
| 11 | timjosten/mtk_imei | MTK NVRAM patcher | - | - | 35 |
| 12 | TheWebSolver/luhn-algorithm | PHP Luhn algorithm library | PHP | - | 40 |
| 13 | imei-info/imei-check-api-node | IMEI.info API Node.js client | TypeScript | - | 28 |
| 14 | iurkinvalentin/IMEI_checker | Django IMEI checker API | Python | - | 15 |
| 15 | codegeekr/validatorimei | JavaScript IMEI validator | JavaScript | - | 32 |
| 16 | vicgc/pyAndriller | Android forensic data extraction | Python | - | 55 |
| 17 | fsinnes/Mobile-Diagnostics-Research | Mobile diagnostics research | - | - | 20 |
| 18 | CScorza/OSINT-FORENSICS-MOBILE | OSINT mobile forensic tools | - | - | 65 |
| 19 | saschoar/android-imei-getter | ADB-based IMEI getter | - | - | 18 |
| 20 | opt05/deviceid | Android device information app | - | - | 25 |
| 21 | alecsx/imei-changer-mtk | MTK IMEI changer | Python | MIT | 42 |
| 22 | tomsawyer777/IMEI-Change | Android IMEI change tool | - | - | 38 |
| 23 | mahmoudabdelmomen/imei-analyzer | React Native IMEI analyzer | JavaScript | - | 16 |
| 24 | hopla/ifreeicloud | iFreeiCloud API client | TypeScript | MIT | 50 |
| 25 | KilimcininKorOglu/edevlet-imei-check | e-Devlet IMEI check | Go | - | 12 |

---

## 📚 Resources and References

### Online tools

| Tool | URL | Description |
|---|---|---|
| IMEI.info | https://imei.info | IMEI lookup and device information |
| SNDeepInfo | https://sndeep.info | IMEI device checker |
| Nobbi | https://nobbi.com | IMEI tools |
| GSMA IMEI Database | https://gsma.com | Official TAC database |
| IMEI24 | https://imei24.com | Free IMEI check |
| IMEIData | https://imeidata.net | Detailed device information |

### Official verification
- **India:** CEIR (Central Equipment Identity Register) — send `KYM <15-digit IMEI>` by SMS to 14422.
- **GSMA TAC Database:** Official TAC information.
- **EU IMEI Database:** Official European Union database.

### Forensic tools

| Tool | Description | Price |
|---|---|---|
| Cellebrite UFED | Mobile forensics platform | Paid |
| Oxygen Forensics | Device forensics | Paid |
| Andriller | Android forensic extraction | Free/Paid |
| Autopsy | Open-source forensics | Free |
| Magnet AXIOM | Digital forensics | Paid |

### Documentation
- MTK IMEI format: `docs/format.md`
- Reverse engineering: `docs/reverse_engineering.md`
- GSMA TAC Assignment: Official Document

### Books and research papers
- "Mobile Device Forensics" — NIST Special Publication
- "Android Forensics" — Andrew Hoog
- "iOS Forensics" — Sean Morrissey

---

## 🛡️ IMEI Change Methods (Educational Only)

**Warning:** The following methods are presented for educational purposes only. You are responsible for any use on your own device.

### Method 1: MTK Engineering Mode (MediaTek)
```bash
# On the dial pad
*#*#3646633#*#*

# Or
*#*#66336#*#*
```

### Method 2: ADB + Root (Android)
```bash
# Obtain root access
adb root
adb shell

# Write an IMEI (with a new IMEI)
echo -n "357561856136304" > /data/nvram/md/NVRAM/NVD_IMEI/IMEI
chmod 666 /data/nvram/md/NVRAM/NVD_IMEI/IMEI

# Reboot
reboot
```

### Method 3: Python script (MTK)
```python
import subprocess
import os

def change_imei(imei1, imei2=None):
    """Change the IMEI on an MTK device"""
    if not imei2:
        imei2 = imei1
    
    # Mount the NVRAM partition
    subprocess.run(["adb", "shell", "su", "-c", "mount -o rw,remount /"])
    
    # Write IMEI 1
    with open("imei1.bin", "wb") as f:
        f.write(imei1.encode())
    subprocess.run(["adb", "push", "imei1.bin", "/data/nvram/md/NVRAM/NVD_IMEI/IMEI1"])
    
    # Write IMEI 2 (dual SIM)
    if imei2:
        with open("imei2.bin", "wb") as f:
            f.write(imei2.encode())
        subprocess.run(["adb", "push", "imei2.bin", "/data/nvram/md/NVRAM/NVD_IMEI/IMEI2"])
    
    # Set permissions
    subprocess.run(["adb", "shell", "su", "-c", "chmod 666 /data/nvram/md/NVRAM/NVD_IMEI/*"])
    
    # Reboot
    subprocess.run(["adb", "reboot"])

# Usage
change_imei("357561856136304", "357561856136305")
```

### Method 4: QPST (Qualcomm)
```
1. Open QPST Configuration
2. Select Ports → Add Port → COM Port
3. Open EFS Explorer
4. Navigate to /nv/item_files/imei/
5. Edit the IMEI file
6. Select Write Changes
```

### Method 5: SP Flash Tool (MediaTek)
```
1. Open SP Flash Tool
2. Load the Scatter File
3. Select the NVRAM partition
4. Load the file containing the IMEI
5. Select Download
```

---

## ⚠️ Legal Warning

**Important:** This documentation is intended for educational and research purposes only.

1. Accessing or changing another person's device IMEI without authorization is illegal and punishable.
2. Using this information for IMEI fraud, mobile-phone theft, or other criminal activity is punishable by law (the source text states up to 7 years' imprisonment in Bangladesh).
3. Results from these tools should be verified through official channels.
4. Law-enforcement agencies require a warrant or legal authorization.
5. The author/publisher is not responsible for misuse.
6. IMEI changes are completely prohibited in some countries (including the USA, UK, India, and Bangladesh).
7. Changing the IMEI of your own device may also void its warranty.

### Country-specific legal provisions (as stated in the source)

| Country | Law | Penalty |
|---|---|---|
| Bangladesh | Mobile Phone Act 2018 | 7 years' imprisonment |
| India | IT Act 2000 | 3 years' imprisonment |
| USA | 18 U.S.C. § 1029 | 15 years' imprisonment |
| UK | Fraud Act 2006 | 10 years' imprisonment |

---

## 🤝 Support and Contributions

- **Bug reports:** Open an issue in the relevant GitHub repository.
- **Code contributions:** Fork the repository and submit a pull request.
- **Documentation updates:** Contribute to this README.
- **Tutorials:** Submit new tutorials.

### Contribution guidelines
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/amazing-feature`).
3. Commit your changes (`git commit -m 'Add amazing feature'`).
4. Push the branch (`git push origin feature/amazing-feature`).
5. Open a pull request.

---

## 🙏 Credits

- **Repository maintainer:** Humayun Shariar Himu
- **Contributors:** All open-source developers who created these tools.
- **Special thanks:** GSMA, IMEI.info, and all researchers.

---

## 📄 License

This documentation is stated to be published under the MIT License. Each tool/software remains subject to its own license.

```
MIT License

Copyright (c) 2026 Humayun Shariar Himu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<div align="center">
  <sub>🔍 <strong>Last updated:</strong> August 20, 2026 | <strong>Version:</strong> 3.0</sub>
  <br>
  <sub>⚠️ <strong>For educational purposes only</strong> ⚠️</sub>
  <br>
  <sub>📧 <strong>Contact:</strong> humayun.himu@example.com</sub>
  <br>
  <sub>⭐ <strong>Star</strong> | 🍴 <strong>Fork</strong> | 🐛 <strong>Open an issue</strong></sub>
</div>

---

## 📊 Quick Reference Table

| Task | Method | Tool/Code |
|---|---|---|
| View IMEI | Dial `*#06#` | Dialer |
| Validate IMEI | Luhn algorithm | Python/JS/PHP |
| Generate IMEI | IMEI Atlas | Python |
| Change IMEI (MTK) | Engineering Mode | `*#*#3646633#*#*` |
| Change IMEI (Qualcomm) | QPST | Windows |
| IMEI forensics | pyAndriller | Python |
| IMEI API | IMEI.info REST API | REST API |
| IMEI app | Flutter Plugin | Dart |
| IMEI tracking | IMEI-tracker | Python/Node.js |

---

Remember: use technology for good purposes only. Follow the law and respect other people's privacy.

---

## 🧰 Complete Web App and Python Toolkit

Alongside the research guide, this repository includes a responsive web app, a local IMEI format/Luhn validator, a Python CLI, batch JSON/CSV reports, a test suite, and a resource catalog. The original guide text is retained as a separate file.

- **Project and run instructions:** [`FULL_PROJECT.md`](FULL_PROJECT.md)
- **Web app:** [`webapp/`](webapp/)
- **Python validator/CLI/API:** [`imei_research/`](imei_research/)
- **Resource catalog:** [`data/resources.json`](data/resources.json)
- **Repository/license review:** [`docs/repository-review.md`](docs/repository-review.md)
- **Code recipes and tests:** [`docs/code-recipes.md`](docs/code-recipes.md), [`tests/`](tests/)

> **Note:** The root `LICENSE` is Apache-2.0, while this README contains MIT License text; this discrepancy needs to be resolved. Third-party code was not copied without license verification. This project does not write to IMEI, generate or clone IMEIs, or write to NVRAM/EFS/partitions.

---

## 🏷️ Repository Tags / Topics

`imei` `imei-validation` `imei-lookup` `mobile-forensics` `android` `adb` `python` `javascript` `luhn-algorithm` `device-diagnostics` `digital-forensics` `research-tools` `responsive-web-app` `api` `open-source`
'''
path = Path("/mnt/data/README-English.md")
path.write_text(content, encoding="utf-8")
print(f"Created: {path}\nSize: {path.stat().st_size:,} bytes\nLines: {len(content.splitlines()):,}")
