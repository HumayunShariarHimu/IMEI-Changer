```markdown
# 📱 মোবাইল ফোনের আইএমইআই পরিচয় ও পরিবর্তনের সম্পূর্ণ গাইড

> **সর্বশেষ হালনাগাদ:** ২০ আগস্ট ২০২৬  
> **সংস্করণ:** ৩.০  
> **রিপোজিটরি:** [IMEI-Complete-Guide](https://github.com/humayun-himu/imei-complete-guide)

---

## 📖 সূচিপত্র

- [আইএমইআই কী?](#-আইএমইআই-কী)
- [আইএমইআই স্ট্রাকচার](#-আইএমইআই-স্ট্রাকচার)
- [আইএমইআই পরিচয় করার পদ্ধতি](#-আইএমইআই-পরিচয়-করার-পদ্ধতি)
- [সফটওয়্যার ও টুলস](#-সফটওয়্যার-ও-টুলস)
- [কোড ও স্ক্রিপ্ট](#-কোড-ও-স্ক্রিপ্ট)
- [মোবাইল অ্যাপ](#-মোবাইল-অ্যাপ)
- [API ও ওয়েব সার্ভিস](#-api-ও-ওয়েব-সার্ভিস)
- [ফরেনসিক টেকনিক](#-ফরেনসিক-টেকনিক)
- [গিটহাব রিপোজিটরি লিস্ট](#-গিটহাব-রিপোজিটরি-লিস্ট)
- [সম্পদ ও রেফারেন্স](#-সম্পদ-ও-রেফারেন্স)
- [আইনি সতর্কতা](#-আইনি-সতর্কতা)

---

## 📌 আইএমইআই কী?

**IMEI** (International Mobile Equipment Identity) হলো প্রতিটি মোবাইল ডিভাইসের জন্য একটি অনন্য ১৫-১৭ ডিজিটের শনাক্তকরণ নম্বর। এটি GSM, UMTS এবং LTE নেটওয়ার্কে ডিভাইস শনাক্ত করতে ব্যবহৃত হয়।

> **দ্রষ্টব্য:** আইএমইআই ডিভাইসের সাথে সম্পর্কিত, সিম কার্ডের সাথে নয়। প্রতিটি সিম স্লটের জন্য আলাদা আইএমইআই থাকতে পারে (ডুয়াল-সিম ডিভাইসে)।

### আইএমইআই-এর গুরুত্ব:
- 📱 **ডিভাইস শনাক্তকরণ:** নেটওয়ার্কে ডিভাইস চিহ্নিত করে
- 🔒 **নিরাপত্তা:** চুরি যাওয়া ফোন ব্ল্যাকলিস্টে যুক্ত করা যায়
- 🛡️ **ওয়ারেন্টি যাচাই:** ডিভাইসের প্রামাণিকতা নিশ্চিত করে
- 🌐 **নেটওয়ার্ক অ্যাক্সেস:** ক্যারিয়ার নেটওয়ার্কে সংযোগ স্থাপনে সহায়তা করে

---

## 🧬 আইএমইআই স্ট্রাকচার

একটি সম্পূর্ণ আইএমইআই নিম্নলিখিত অংশে বিভক্ত:

```

TAC (8 ডিজিট) + SNR (6 ডিজিট) + CD (1 ডিজিট) = ১৫ ডিজিট
উদাহরণ: 357561856136304

```

| অংশ | বিবরণ | দৈর্ঘ্য |
|------|---------|---------|
| **TAC** (Type Allocation Code) | ডিভাইসের মডেল শনাক্ত করে। GSMA দ্বারা নির্ধারিত | ৮ ডিজিট |
| **SNR** (Serial Number) | উৎপাদনকারী কর্তৃক নির্ধারিত অনন্য সিরিয়াল নম্বর | ৬ ডিজিট |
| **CD** (Check Digit) | Luhn অ্যালগরিদম দ্বারা যাচাইকৃত ডিজিট | ১ ডিজিট |

### Reporting Body Identifier (RBI):

TAC-এর প্রথম ২ ডিজিট কর্তৃপক্ষ নির্দেশ করে:

| কোড | কর্তৃপক্ষ | দেশ |
|-----|-----------|------|
| `01` | PTCRB | USA |
| `35` | BABT | United Kingdom |
| `44` | ICASA | South Africa |
| `49` | BNetzA | Germany |
| `86` | TAF | China |
| `99` | GCF | Global |

---

## 🔍 আইএমইআই পরিচয় করার পদ্ধতি

### ১. USSD কোড (সবচেয়ে সহজ পদ্ধতি)
ডায়াল প্যাডে `*#06#` ডায়াল করলে আইএমইআই নম্বর স্ক্রিনে প্রদর্শিত হয়।

<details>
<summary><b>অন্যান্য USSD কোড</b></summary>

| কোড | কাজ |
|-----|-----|
| `*#*#4636#*#*` | ডিভাইস তথ্য ও পরিসংখ্যান |
| `*#*#197328640#*#*` | সার্ভিস মোড মেনু |
| `*#*#2846579#*#*` | প্রকৌশল মোড (Huawei) |
| `*#*#3646633#*#*` | প্রকৌশল মোড (MediaTek) |
</details>

### ২. ডিভাইস সেটিংস
- **Android:** Settings → About Phone → Status → IMEI Information
- **iPhone:** Settings → General → About → IMEI

### ৩. ডিভাইসের ব্যাক কভার/ব্যাটারি স্লট
ব্যাটারি খুলে স্লটের ভিতরে লেবেলে আইএমইআই লেখা থাকে।

### ৪. ADB (Android Debug Bridge) কমান্ড
```bash
adb shell service call iphonesubinfo 1
adb shell dumpsys iphonesubinfo
adb shell getprop ro.ril.oem.imei
```

৫. AT কমান্ড

```bash
AT+CGSN
AT+IMEINUM
AT+GSN
```

৬. ফরেনসিক এক্সট্রাকশন

· লজিক্যাল এক্সট্রাকশন: ডিভাইসের সিস্টেম ইনফরমেশন থেকে আইএমইআই সংগ্রহ
· ফিজিক্যাল এক্সট্রাকশন: JTAG বা Chip-off ফরেনসিকের মাধ্যমে হার্ডওয়্যার থেকে আইএমইআই এক্সট্র্যাক্ট

---

🛠️ সফটওয়্যার ও টুলস

১. IMEI-Find

https://img.shields.io/github/stars/D3crypT0r/IMEI-Find

· বিবরণ: ADB ব্যবহার করে Android ডিভাইসের ফাইল সিস্টেমে IMEI অনুসন্ধানের জন্য GUI-ভিত্তিক টুল
· বৈশিষ্ট্য:
  · নির্দিষ্ট টার্ম (যেমন: IMEI, getImei) অনুসন্ধান
  · মাউন্টেড পার্টিশন প্রদর্শন
  · JSON ফরম্যাটে রেজাল্ট এক্সপোর্ট
· প্রয়োজনীয়তা: Python 3.x, ADB, PyQt5
· ইনস্টলেশন:

```bash
git clone https://github.com/D3crypT0r/IMEI-Find.git
cd IMEI-Find
pip install PyQt5 pyqt5-tools
python3 IMEI-Find.py
```

· লাইসেন্স: Open Source

২. IMEI_Lookup

https://img.shields.io/github/stars/itsKayWat/IMEI_Lookup

· বিবরণ: PIN অথেন্টিকেশন, পেইড/ফ্রি ডিভাইস চেক এবং IMEI ক্যালকুলেটর সম্বলিত আধুনিক IMEI লুকআপ টুল
· বৈশিষ্ট্য: রেসপন্সিভ UI, সাউন্ড ইফেক্ট, মাল্টি-ইউজার সাপোর্ট
· নির্মিত: Vanilla JS/CSS
· লাইসেন্স: MIT

৩. IMEI Validator

https://img.shields.io/github/stars/JonnyBytesMe/imei-validator

· বিবরণ: IMEI নম্বর ভ্যালিডেশন ও অ্যানালাইসিসের জন্য Python টুল
· বৈশিষ্ট্য:
  · Luhn অ্যালগরিদম ভ্যালিডেশন
  · TAC ডেটাবেস লুকআপ
  · RBI কোড অ্যানালাইসিস
  · ব্যাচ প্রসেসিং
· ব্যবহার:

```bash
python imei_validator.py --imei 357561856136304
python imei_validator.py --batch input_imeis.txt
```

· প্রয়োজনীয়তা: Python 3.7+

৪. IMEI Scraper & Validation Tool

https://img.shields.io/github/stars/altheasignals/imei_scrape

· বিবরণ: হাই-পারফরম্যান্স Python অ্যাপ্লিকেশন যা IMEI সংগ্রহ, ম্যানেজ ও ভ্যালিডেট করে
· বৈশিষ্ট্য:
  · হাই-পারফরম্যান্স স্ক্র্যাপিং
  · ক্যারিয়ার কম্প্যাটিবিলিটি ভেরিফিকেশন
  · CSV-ভিত্তিক ডেটাবেস ম্যানেজমেন্ট
  · ব্ল্যাকলিস্ট ম্যানেজমেন্ট
· ইনস্টলেশন:

```bash
pip install -r requirements-v1.txt
python -m playwright install chromium
```

· ব্যবহার:

```bash
python src/imei_manager.py scrape --count 50 --brand Samsung
python src/imei_manager.py validate --imei 351138316163206
```

৫. IMEI Atlas

https://img.shields.io/github/stars/IMEI-Atlas/IMEI-Atlas

· বিবরণ: IMEI জেনারেটর ও ভ্যালিডেটর টুল। MikroTik ও FiberHome রাউটারের AT কমান্ড সাপোর্ট করে
· বৈশিষ্ট্য:
  · Luhn অ্যালগরিদম ব্যবহার করে IMEI জেনারেট
  · জনপ্রিয় ডিভাইসের জন্য TAC ডেটাবেস
  · বাল্ক জেনারেশন
  · AT কমান্ড জেনারেশন
· লাইসেন্স: GNU GPL v3.0

৬. MTK IMEI Patcher

https://img.shields.io/github/stars/timjosten/mtk_imei

· বিবরণ: Xiaomi Helio G সিরিজের ফোনের জন্য NVRAM পার্টিশন পুনঃনির্মাণের স্ক্রিপ্ট
· বৈশিষ্ট্য: TWRP-ফ্ল্যাশেবল ফাইল তৈরি

৭. IMEI Changer (MTK)

https://img.shields.io/github/stars/alecsx/imei-changer-mtk

· বিবরণ: MediaTek ডিভাইসের জন্য IMEI পরিবর্তন টুল (কমান্ড লাইন)
· ইনস্টলেশন: pip install imei-changer-mtk
· ব্যবহার:

```bash
imei-changer --imei1 357561856136304 --imei2 357561856136305
```

৮. IMEI-Change

https://img.shields.io/github/stars/tomsawyer777/IMEI-Change

· বিবরণ: Android ফোনের IMEI পরিবর্তনের সহজ টুল (রুট প্রয়োজন)
· বৈশিষ্ট্য: ব্যাকআপ/রিস্টোর, ডুয়াল সিম সাপোর্ট
· প্রয়োজনীয়তা: রুট অ্যাক্সেস, ADB

---

💻 কোড ও স্ক্রিপ্ট

১. Luhn অ্যালগরিদম (Python)

```python
def validate_imei(imei):
    """Luhn অ্যালগরিদম দিয়ে IMEI ভ্যালিডেট করুন"""
    # শুধু ডিজিট নিন
    digits = [int(d) for d in str(imei) if d.isdigit()]
    
    # চেক ডিজিট বাদ দিন
    check_digit = digits[-1]
    payload = digits[:-1]
    
    # Luhn অ্যালগরিদম
    total = 0
    for i, d in enumerate(reversed(payload)):
        if i % 2 == 0:  # প্রতি দ্বিতীয় ডিজিট (ডান থেকে)
            d *= 2
            if d > 9:
                d -= 9
        total += d
    
    calculated = (10 - (total % 10)) % 10
    return calculated == check_digit
```

[সোর্স: JonnyBytesMe/imei-validator]

২. IMEI জেনারেটর (Python)

```python
import random

def generate_imei(tac, serial_length=6):
    """TAC এবং সিরিয়াল থেকে IMEI জেনারেট করুন"""
    # TAC (8 ডিজিট) + সিরিয়াল (6 ডিজিট)
    serial = ''.join([str(random.randint(0,9)) for _ in range(serial_length)])
    base = str(tac) + serial
    
    # Luhn চেক ডিজিট গণনা
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

# ব্যবহার
print(generate_imei(35756185))  # উদাহরণ: 357561856136304
```

[সোর্স: bstein/py-imei-generator]

৩. Android (Java) - IMEI সংগ্রহ

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
                return telephonyManager.getDeviceId(); // Android 9-এর জন্য
            }
        }
        return null;
    }
}
```

[সোর্স: Quectel Forums]

৪. PHP - Luhn ভ্যালিডেশন

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

// ব্যবহার
$validator = new LuhnAlgorithm();
echo $validator->isValid("357561856136304") ? "ভ্যালিড" : "ইনভ্যালিড";
```

[সোর্স: TheWebSolver/luhn-algorithm]

৫. JavaScript - IMEI ভ্যালিডেটর

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

৬. Bash - ADB দিয়ে IMEI সংগ্রহ

```bash
#!/bin/bash

echo "=== IMEI সংগ্রহের সব পদ্ধতি ==="

# পদ্ধতি ১
echo -e "\n[পদ্ধতি ১] service call:"
adb shell service call iphonesubinfo 1

# পদ্ধতি ২
echo -e "\n[পদ্ধতি ২] dumpsys:"
adb shell dumpsys iphonesubinfo | grep -i imei

# পদ্ধতি ৩
echo -e "\n[পদ্ধতি ৩] getprop:"
adb shell getprop | grep -i imei

# পদ্ধতি ৪ (রুটেড)
echo -e "\n[পদ্ধতি ৪] ফাইল সিস্টেম:"
adb shell su -c "cat /proc/cmdline | grep -i imei"
adb shell su -c "cat /data/nvram/md/NVRAM/NVD_IMEI/IMEI"
```

৭. Node.js - IMEI ভ্যালিডেটর

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

৮. Python - IMEI থেকে ডিভাইস তথ্য

```python
import requests
import json

def get_device_info(imei):
    """IMEI.info API থেকে ডিভাইস তথ্য নিন"""
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

# ব্যবহার
info = get_device_info("357561856136304")
if info:
    print(f"ব্র্যান্ড: {info.get('brand')}")
    print(f"মডেল: {info.get('model')}")
    print(f"নির্মাতা: {info.get('manufacturer')}")
```

---

📱 মোবাইল অ্যাপ

১. Flutter Device IMEI Plugin

https://img.shields.io/github/stars/pranilshah4024/flutter_device_imei

· বিবরণ: Android ও iOS-এ ডিভাইস আইডি সংগ্রহের জন্য Flutter প্লাগইন
· বৈশিষ্ট্য:
  · Android 10-এর নিচে: IMEI রিটার্ন করে
  · Android 10+: ANDROID_ID রিটার্ন করে
  · iOS: UUID রিটার্ন করে
· ব্যবহার:

```dart
import 'package:flutter_device_imei/flutter_device_imei.dart';
String imei = await FlutterDeviceImei.instance.getIMEI();
```

২. IMEI Plugin (Flutter)

https://img.shields.io/github/stars/nqhhdev/imei_plugin

· বিবরণ: Flutter-এ Android ও iOS-এর জন্য IMEI সংগ্রহের প্লাগইন
· বৈশিষ্ট্য: ডুয়াল/ট্রিপল সিম সাপোর্ট
· ব্যবহার:

```dart
String imei = await ImeiPlugin.getImei();
List<String> multiImei = await ImeiPlugin.getImeiMulti();
```

৩. MTK IMEI Switcheroo App

https://img.shields.io/github/stars/flipphoneguy/mtk-imei-switcheroo-app

· বিবরণ: রুটেড MediaTek MT67xx ফোনে IMEI, Bluetooth MAC ও WiFi MAC রিড ও রিরাইট করার অ্যাপ
· বৈশিষ্ট্য: IMEI জেনারেট, MAC র‍্যান্ডোমাইজ, লাস্ট ৫ ভ্যালু সেভ
· প্রয়োজনীয়তা: রুট (Magisk)

৪. Device Info (Android)

https://img.shields.io/badge/GitHub-opt05/deviceid-blue

· বিবরণ: ওপেন সোর্স Android অ্যাপ যা IMEI/MEID, ডিভাইস মডেল, Android ID, Wi-Fi MAC, Bluetooth MAC ইত্যাদি প্রদর্শন করে
· প্লে স্টোরে উপলব্ধ

৫. SimInfo

https://img.shields.io/github/stars/tech1ee/SimInfo

· বিবরণ: সিম কার্ডের তথ্য, নেটওয়ার্ক কানেক্টিভিটি ও ক্যারিয়ার সার্ভিস সম্পর্কে বিস্তারিত তথ্য প্রদানকারী Android অ্যাপ
· বৈশিষ্ট্য: IMEI, Android ID, ICCID প্রদর্শন

৬. IMEI Analyzer (React Native)

https://img.shields.io/github/stars/mahmoudabdelmomen/imei-analyzer

· বিবরণ: React Native-এ নির্মিত IMEI অ্যানালাইসিস অ্যাপ
· বৈশিষ্ট্য: IMEI ভ্যালিডেশন, ডিভাইস তথ্য, ব্ল্যাকলিস্ট চেক

---

🌐 API ও ওয়েব সার্ভিস

১. IMEI.info API

https://img.shields.io/github/stars/imei-info/imei-check-api-node

· বিবরণ: IMEI ব্যবহার করে মোবাইল ডিভাইসের তথ্য সংগ্রহের API
· Node.js ক্লায়েন্ট: npm install imei-info
· ব্যবহার:

```javascript
const IMEI = require('imei-info');
const client = new IMEI('YOUR_API_KEY');
const info = await client.check('357561856136304');
```

২. IMEI Checker API (Django)

https://img.shields.io/github/stars/iurkinvalentin/IMEI_checker

· বিবরণ: Django-ভিত্তিক REST API যা বাহ্যিক API-এর মাধ্যমে IMEI চেক করে
· এন্ডপয়েন্ট: /api/v1/check-imei/
· ইনস্টলেশন:

```bash
git clone https://github.com/iurkinvalentin/IMEI_checker
pip install -r requirements.txt
python manage.py runserver
```

৩. iFreeiCloud API

https://img.shields.io/github/stars/hopla/ifreeicloud

· বিবরণ: IMEI / iCloud / ক্যারিয়ার চেকের জন্য TypeScript ক্লায়েন্ট
· ইনস্টলেশন: npm install @hopla/ifreeicloud
· ব্যবহার:

```typescript
import { iFreeiCloud } from '@hopla/ifreeicloud';
const client = new iFreeiCloud('API_KEY');
const result = await client.checkImei('357561856136304');
```

৪. e-Devlet IMEI Check (Go)

https://img.shields.io/github/stars/KilimcininKorOglu/edevlet-imei-check

· বিবরণ: তুরস্কের e-Devlet পোর্টালে IMEI রেজিস্ট্রেশন স্ট্যাটাস চেকের জন্য Go লাইব্রেরি
· ব্যবহার:

```go
import "github.com/KilimcininKorOglu/edevlet-imei-check"
status := imei.Check("357561856136304")
```

৫. Open IMEI Database API

https://img.shields.io/github/stars/OpenIMEI/opendb

· বিবরণ: ওপেন সোর্স IMEI ডেটাবেস API
· বৈশিষ্ট্য: ফ্রি, TAC ডেটাবেস, ডিভাইস তথ্য
· API: https://api.openimei.com/v1/lookup/{imei}

---

🔬 ফরেনসিক টেকনিক

১. লজিক্যাল এক্সট্রাকশন

মোবাইল ফরেনসিক টুলস ব্যবহার করে ডিভাইসের সেটিংস বা সিস্টেম ইনফরমেশন থেকে IMEI সংগ্রহ

উদাহরণ টুলস:

· Cellebrite UFED
· Oxygen Forensics
· Andriller
· Autopsy (Android अॅक्सेसरी)

২. ফিজিক্যাল এক্সট্রাকশন

ডিভাইস ড্যামেজ বা অ্যাক্সেসযোগ্য না হলে JTAG বা Chip-off ফরেনসিকের মাধ্যমে হার্ডওয়্যার থেকে IMEI এক্সট্র্যাক্ট

প্রয়োজনীয় সরঞ্জাম:

· JTAG ইন্টারফেস (Raspberry Pi + OpenOCD)
· Chip-off স্টেশন (Hot Air Rework)
· EMMC প্রোগ্রামার (EasyJTAG, Octoplus)

৩. MTK NVRAM রিভার্স ইঞ্জিনিয়ারিং

MediaTek ডিভাইসের IMEI এনক্রিপশন ফরম্যাট রিভার্স ইঞ্জিনিয়ারিং

· ফাইল লোকেশন: /mnt/vendor/nvdata/md/NVRAM/NVD_IMEI/LD0B_001
· এনক্রিপশন: AES-128-ECB + MD5-XOR checksum
· ডিক্রিপশন টুল: mtk-imei-decrypt

৪. pyAndriller

https://img.shields.io/github/stars/vicgc/pyAndriller

· বিবরণ: রুটেড Android ডিভাইস থেকে রিড-অনলি, ফরেনসিকভাবে সাউন্ড ডেটা এক্সট্রাকশন টুল
· বৈশিষ্ট্য: IMEI, ডিভাইস তথ্য, ইনস্টলড অ্যাপ, SMS, কল লগ
· ব্যবহার:

```bash
python pyandriller.py --target /dev/block/mmcblk0
```

৫. Mobile-Diagnostics-Research

https://img.shields.io/github/stars/fsinnes/Mobile-Diagnostics-Research

· বিবরণ: মোবাইল ডিভাইস শনাক্তকরণ ও ডায়াগনোসিস গবেষণার জন্য রিপোজিটরি
· AT কমান্ড: AT+IMEINUM, shell cat /csa/imei/serialno.dat
· উইন্ডোজ টুল: adb shell wmic path Win32_BaseBoard get SerialNumber

৬. ফরেনসিক ইমেজিং

```bash
# Android EMMC ডাম্প
adb shell su -c "dd if=/dev/block/mmcblk0 of=/sdcard/emmc_dump.img"

# NVRAM ডাম্প (MTK)
adb shell su -c "dd if=/dev/block/platform/mtk-msdc.0/11230000.msdc0/by-name/nvram of=/sdcard/nvram_dump.bin"

# IMEI এক্সট্রাক্ট
strings emmc_dump.img | grep -E '[0-9]{15}'
```

৭. ফরেনসিক বিশ্লেষণ টুলস

```bash
# স্কেলেক্স
scalpel -c scalpel.conf emmc_dump.img

# ফটোরেক
photorec emmc_dump.img

# ডিডি পুনরুদ্ধার
dd if=emmc_dump.img of=imei_sector.bin bs=512 count=1 skip=110100
```

---

📦 গিটহাব রিপোজিটরি লিস্ট (সম্পূর্ণ)

# রিপোজিটরি বিবরণ ভাষা লাইসেন্স ⭐
1 D3crypT0r/IMEI-Find ADB-ভিত্তিক IMEI ফাইন্ডার Python - 15
2 itsKayWat/IMEI_Lookup IMEI লুকআপ টুল HTML/CSS/JS MIT 20
3 JonnyBytesMe/imei-validator IMEI ভ্যালিডেটর Python - 25
4 altheasignals/imei_scrape IMEI স্ক্র্যাপার ও ভ্যালিডেটর Python - 10
5 IMEI-Atlas/IMEI-Atlas IMEI জেনারেটর ও ভ্যালিডেটর Python GPL v3.0 18
6 Supa-mustea/IMEI-tracker আইন প্রয়োগের জন্য IMEI ট্র্যাকিং Python/Node.js - 12
7 Nurumoney/IMEI-Tracker Flask + SocketIO রিয়েল-টাইম ট্র্যাকিং Python - 8
8 pranilshah4024/flutter_device_imei Flutter IMEI প্লাগইন Dart - 30
9 nqhhdev/imei_plugin Flutter IMEI প্লাগইন Java/Dart MIT 22
10 flipphoneguy/mtk-imei-switcheroo-app MTK IMEI পরিবর্তন অ্যাপ Java - 45
11 timjosten/mtk_imei MTK NVRAM প্যাচার - - 35
12 TheWebSolver/luhn-algorithm PHP Luhn অ্যালগরিদম লাইব্রেরি PHP - 40
13 imei-info/imei-check-api-node IMEI.info API Node.js ক্লায়েন্ট TypeScript - 28
14 iurkinvalentin/IMEI_checker Django IMEI চেকার API Python - 15
15 codegeekr/validatorimei JavaScript IMEI ভ্যালিডেটর JavaScript - 32
16 vicgc/pyAndriller Android ফরেনসিক ডেটা এক্সট্রাকশন Python - 55
17 fsinnes/Mobile-Diagnostics-Research মোবাইল ডায়াগনস্টিক গবেষণা - - 20
18 CScorza/OSINT-FORENSICS-MOBILE OSINT মোবাইল ফরেনসিক টুলস - - 65
19 saschoar/android-imei-getter ADB-ভিত্তিক IMEI গেটার - - 18
20 opt05/deviceid Android ডিভাইস তথ্য অ্যাপ - - 25
21 alecsx/imei-changer-mtk MTK IMEI চেঞ্জার Python MIT 42
22 tomsawyer777/IMEI-Change Android IMEI পরিবর্তন টুল - - 38
23 mahmoudabdelmomen/imei-analyzer React Native IMEI অ্যানালাইসার JavaScript - 16
24 hopla/ifreeicloud iFreeiCloud API ক্লায়েন্ট TypeScript MIT 50
25 KilimcininKorOglu/edevlet-imei-check e-Devlet IMEI চেক (Go) Go - 12

---

📚 সম্পদ ও রেফারেন্স

অনলাইন টুলস

টুল URL বিবরণ
IMEI.info https://imei.info IMEI লুকআপ ও ডিভাইস তথ্য
SNDeepInfo https://sndeep.info IMEI ডিভাইস চেকার
Nobbi https://nobbi.com IMEI টুলস
GSMA IMEI Database https://gsma.com অফিসিয়াল TAC ডেটাবেস
IMEI24 https://imei24.com ফ্রি IMEI চেক
IMEIData https://imeidata.net ডিভাইস বিস্তারিত

অফিসিয়াল ভেরিফিকেশন

· ভারত: CEIR (Central Equipment Identity Register) - KYM<15 ডিজিট IMEI> SMS পাঠান 14422-এ
· GSMA TAC Database - অফিসিয়াল TAC তথ্য
· EU IMEI Database - ইউরোপিয়ান ইউনিয়নের অফিসিয়াল ডেটাবেস

ফরেনসিক টুলস

টুল বিবরণ মূল্য
Cellebrite UFED মোবাইল ফরেনসিক প্ল্যাটফর্ম পেইড
Oxygen Forensics ডিভাইস ফরেনসিক পেইড
Andriller Android ফরেনসিক এক্সট্রাকশন ফ্রি/পেইড
Autopsy ওপেন সোর্স ফরেনসিক ফ্রি
Magnet AXIOM ডিজিটাল ফরেনসিক পেইড

ডকুমেন্টেশন

· MTK IMEI ফরম্যাট: docs/format.md
· রিভার্স ইঞ্জিনিয়ারিং: docs/reverse_engineering.md
· GSMA TAC Assignment: Official Document

বই ও গবেষণাপত্র

· "Mobile Device Forensics" - NIST Special Publication
· "Android Forensics" - Andrew Hoog
· "iOS Forensics" - Sean Morrissey

---

🛡️ IMEI পরিবর্তনের পদ্ধতি (শুধুমাত্র শিক্ষামূলক)

সতর্কতা: নিচের পদ্ধতিগুলো শুধুমাত্র শিক্ষামূলক উদ্দেশ্যে। আপনার নিজস্ব ডিভাইসে ব্যবহারের জন্য দায়িত্ব আপনার।

পদ্ধতি ১: MTK Enginnering Mode (MediaTek)

```bash
# ডায়াল প্যাডে
*#*#3646633#*#*

# অথবা
*#*#66336#*#*
```

পদ্ধতি ২: ADB + Root (Android)

```bash
# রুট অ্যাক্সেস নিন
adb root
adb shell

# IMEI লেখা (নতুন IMEI সহ)
echo -n "357561856136304" > /data/nvram/md/NVRAM/NVD_IMEI/IMEI
chmod 666 /data/nvram/md/NVRAM/NVD_IMEI/IMEI

# রিবুট করুন
reboot
```

পদ্ধতি ৩: Python স্ক্রিপ্ট (MTK)

```python
import subprocess
import os

def change_imei(imei1, imei2=None):
    """MTK ডিভাইসের IMEI পরিবর্তন করুন"""
    if not imei2:
        imei2 = imei1
    
    # NVRAM পার্টিশন মাউন্ট করুন
    subprocess.run(["adb", "shell", "su", "-c", "mount -o rw,remount /"])
    
    # IMEI 1 লেখা
    with open("imei1.bin", "wb") as f:
        f.write(imei1.encode())
    subprocess.run(["adb", "push", "imei1.bin", "/data/nvram/md/NVRAM/NVD_IMEI/IMEI1"])
    
    # IMEI 2 লেখা (ডুয়াল সিম)
    if imei2:
        with open("imei2.bin", "wb") as f:
            f.write(imei2.encode())
        subprocess.run(["adb", "push", "imei2.bin", "/data/nvram/md/NVRAM/NVD_IMEI/IMEI2"])
    
    # পারমিশন সেট করুন
    subprocess.run(["adb", "shell", "su", "-c", "chmod 666 /data/nvram/md/NVRAM/NVD_IMEI/*"])
    
    # রিবুট
    subprocess.run(["adb", "reboot"])

# ব্যবহার
change_imei("357561856136304", "357561856136305")
```

পদ্ধতি ৪: QPST (Qualcomm)

```
1. QPST Configuration খুলুন
2. Ports → Add Port → COM Port সিলেক্ট করুন
3. EFS Explorer খুলুন
4. /nv/item_files/imei/ পাথে যান
5. IMEI ফাইলটি এডিট করুন
6. Write Changes করুন
```

পদ্ধতি ৫: SP Flash Tool (MediaTek)

```
1. SP Flash Tool খুলুন
2. Scatter File লোড করুন
3. NVRAM পার্টিশন সিলেক্ট করুন
4. IMEI সহ ফাইল লোড করুন
5. Download করুন
```

---

⚠️ আইনি সতর্কতা

গুরুত্বপূর্ণ: এই ডকুমেন্টেশনটি শুধুমাত্র শিক্ষামূলক ও গবেষণামূলক উদ্দেশ্যে তৈরি করা হয়েছে।

1. অনুমোদন ছাড়া অন্য কারও ডিভাইসের IMEI অ্যাক্সেস বা পরিবর্তন করা অবৈধ এবং শাস্তিযোগ্য অপরাধ
2. IMEI জালিয়াতি, মোবাইল চুরি, বা অন্যান্য অপরাধমূলক কাজে এই তথ্য ব্যবহার করা আইনত দণ্ডনীয় (বাংলাদেশে ৭ বছর পর্যন্ত কারাদণ্ড)
3. এই টুলসগুলোর ফলাফল অফিসিয়াল চ্যানেলের মাধ্যমে যাচাই করতে হবে
4. আইন প্রয়োগকারী সংস্থাগুলোর জন্য ওয়ারেন্ট বা আইনি অনুমোদন প্রয়োজন
5. এই ডকুমেন্টেশনের লেখক/প্রকাশক কোনও অপব্যবহারের জন্য দায়ী নন
6. কিছু দেশে IMEI পরিবর্তন সম্পূর্ণ নিষিদ্ধ (USA, UK, India, Bangladesh সহ)
7. আপনার নিজস্ব ডিভাইসের IMEI পরিবর্তন করলেও তা ওয়ারেন্টি বাতিল করে দিতে পারে

দেশভিত্তিক আইনি বিধান

দেশ আইন শাস্তি
বাংলাদেশ মোবাইল ফোন আইন ২০১৮ ৭ বছর কারাদণ্ড
ভারত IT Act 2000 ৩ বছর কারাদণ্ড
USA 18 U.S.C. § 1029 ১৫ বছর কারাদণ্ড
UK Fraud Act 2006 ১০ বছর কারাদণ্ড

---

🤝 সহায়তা ও অবদান

· বাগ রিপোর্ট: সংশ্লিষ্ট গিটহাব রিপোজিটরিতে ইস্যু খুলুন
· কোড কন্ট্রিবিউশন: ফর্ক করে পুল রিকোয়েস্ট পাঠান
· ডকুমেন্টেশন আপডেট: এই রিডমি ফাইলে কন্ট্রিবিউট করুন
· টিউটোরিয়াল: নতুন টিউটোরিয়াল জমা দিন

কন্ট্রিবিউশন গাইডলাইন

1. রিপোজিটরি ফর্ক করুন
2. ফিচার ব্রাঞ্চ তৈরি করুন (git checkout -b feature/amazing-feature)
3. চেঞ্জ কমিট করুন (git commit -m 'Add amazing feature')
4. পুশ করুন (git push origin feature/amazing-feature)
5. পুল রিকোয়েস্ট খুলুন

---

🙏 ক্রেডিট

· রিপোজিটরি মেইনটেইনার: Humayun Shariar Himu
· কন্ট্রিবিউটর: সমস্ত ওপেন সোর্স ডেভেলপার যারা এই টুলস তৈরি করেছেন
· স্পেশাল থ্যাঙ্কস: GSMA, IMEI.info, এবং সকল গবেষক

---

📄 লাইসেন্স

এই ডকুমেন্টেশনটি MIT License-এর অধীনে প্রকাশিত। প্রতিটি টুল/সফটওয়্যারের নিজস্ব লাইসেন্স প্রযোজ্য।

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
  <sub>🔍 <strong>সর্বশেষ হালনাগাদ:</strong> ২০ আগস্ট ২০২৬ | <strong>সংস্করণ:</strong> ৩.০</sub>
  <br>
  <sub>⚠️ <strong>শুধুমাত্র শিক্ষামূলক উদ্দেশ্যে</strong> ⚠️</sub>
  <br>
  <sub>📧 <strong>যোগাযোগ:</strong> humayun.himu@example.com</sub>
  <br>
  <sub>⭐ <strong>স্টার দিন</strong> | 🍴 <strong>ফর্ক করুন</strong> | 🐛 <strong>ইস্যু খুলুন</strong></sub>
</div>

---

📊 দ্রুত রেফারেন্স টেবিল

কাজ পদ্ধতি টুল/কোড
IMEI দেখুন *#06# ডায়ালার
IMEI ভ্যালিডেট Luhn Algorithm Python/JS/PHP
IMEI জেনারেট IMEI Atlas Python
IMEI পরিবর্তন (MTK) Engineering Mode *#*#3646633#*#*
IMEI পরিবর্তন (Qualcomm) QPST Windows
IMEI ফরেনসিক pyAndriller Python
IMEI API IMEI.info REST API
IMEI অ্যাপ Flutter Plugin Dart
IMEI ট্র্যাক IMEI-tracker Python/Node.js

---

মনে রাখবেন: প্রযুক্তি শুধুমাত্র ভালো কাজের জন্য ব্যবহার করুন। আইন মেনে চলুন এবং অন্যের গোপনীয়তা সম্মান করুন।
