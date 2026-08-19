📱 মোবাইল ফোমের আইএমইআই চেইঞ্জ করার সম্পূর্ণ গাইড


📖 সূচিপত্র

1. আইএমইআই কী?
2. আইএমইআই স্ট্রাকচার
3. আইএমইআই পরিচয় করার পদ্ধতি
4. সফটওয়্যার ও টুলস
5. কোড ও স্ক্রিপ্ট
6. মোবাইল অ্যাপ
7. API ও ওয়েব সার্ভিস
8. ফরেনসিক টেকনিক
9. গিটহাব রিপোজিটরি লিস্ট
10. সম্পদ ও রেফারেন্স
11. আইনি সতর্কতা

---

📌 আইএমইআই কী?

IMEI (International Mobile Equipment Identity) হলো প্রতিটি মোবাইল ডিভাইসের জন্য একটি অনন্য ১৫-১৭ ডিজিটের শনাক্তকরণ নম্বর। এটি GSM, UMTS এবং LTE নেটওয়ার্কে ডিভাইস শনাক্ত করতে ব্যবহৃত হয়।

দ্রষ্টব্য: আইএমইআই ডিভাইসের সাথে সম্পর্কিত, সিম কার্ডের সাথে নয়। প্রতিটি সিম স্লটের জন্য আলাদা আইএমইআই থাকতে পারে (ডুয়াল-সিম ডিভাইসে)।

---

🧬 আইএমইআই স্ট্রাকচার

একটি সম্পূর্ণ আইএমইআই নিম্নলিখিত অংশে বিভক্ত:

```
TAC (8 ডিজিট) + SNR (6 ডিজিট) + CD (1 ডিজিট) = ১৫ ডিজিট
উদাহরণ: 357561856136304
```

অংশ বিবরণ দৈর্ঘ্য
TAC (Type Allocation Code) ডিভাইসের মডেল শনাক্ত করে। GSMA দ্বারা নির্ধারিত ৮ ডিজিট
SNR (Serial Number) উৎপাদনকারী কর্তৃক নির্ধারিত অনন্য সিরিয়াল নম্বর ৬ ডিজিট
CD (Check Digit) Luhn অ্যালগরিদম দ্বারা যাচাইকৃত ডিজিট ১ ডিজিট

Reporting Body Identifier (RBI): TAC-এর প্রথম ২ ডিজিট কর্তৃপক্ষ নির্দেশ করে:

· 01 – PTCRB (USA)
· 35 – BABT (United Kingdom)
· 44 – ICASA (South Africa)
· 49 – BNetzA (Germany)
· 86 – TAF (China)
· 99 – GCF (Global)

---

🔍 আইএমইআই পরিচয় করার পদ্ধতি

১. USSD কোড (সবচেয়ে সহজ পদ্ধতি)

ডায়াল প্যাডে *#06# ডায়াল করলে আইএমইআই নম্বর স্ক্রিনে প্রদর্শিত হয়।

২. ডিভাইস সেটিংস

· Android: Settings → About Phone → Status → IMEI Information
· iPhone: Settings → General → About → IMEI

৩. ডিভাইসের ব্যাক কভার/ব্যাটারি স্লট

ব্যাটারি খুলে স্লটের ভিতরে লেবেলে আইএমইআই লেখা থাকে।

৪. ADB (Android Debug Bridge) কমান্ড

```bash
adb shell service call iphonesubinfo 1
```

৫. AT কমান্ড

```bash
AT+CGSN
```

এই কমান্ডটি আইএমইআই রিটার্ন করে।

৬. ফরেনসিক এক্সট্রাকশন

· লজিক্যাল এক্সট্রাকশন: ডিভাইসের সিস্টেম ইনফরমেশন থেকে আইএমইআই সংগ্রহ
· ফিজিক্যাল এক্সট্রাকশন: JTAG বা Chip-off ফরেনসিকের মাধ্যমে হার্ডওয়্যার থেকে আইএমইআই এক্সট্র্যাক্ট

---

🛠️ সফটওয়্যার ও টুলস

১. IMEI-Find https://img.shields.io/github/stars/D3crypT0r/IMEI-Find

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

২. IMEI_Lookup https://img.shields.io/github/stars/itsKayWat/IMEI_Lookup

· বিবরণ: PIN অথেন্টিকেশন, পেইড/ফ্রি ডিভাইস চেক এবং IMEI ক্যালকুলেটর সম্বলিত আধুনিক IMEI লুকআপ টুল
· বৈশিষ্ট্য: রেসপন্সিভ UI, সাউন্ড ইফেক্ট, মাল্টি-ইউজার সাপোর্ট
· নির্মিত: Vanilla JS/CSS
· লাইসেন্স: MIT

৩. IMEI Validator https://img.shields.io/github/stars/JonnyBytesMe/imei-validator

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

৪. IMEI Scraper & Validation Tool https://img.shields.io/github/stars/altheasignals/imei_scrape

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

৫. IMEI Atlas https://img.shields.io/github/stars/IMEI-Atlas/IMEI-Atlas

· বিবরণ: IMEI জেনারেটর ও ভ্যালিডেটর টুল। MikroTik ও FiberHome রাউটারের AT কমান্ড সাপোর্ট করে
· বৈশিষ্ট্য:
  · Luhn অ্যালগরিদম ব্যবহার করে IMEI জেনারেট
  · জনপ্রিয় ডিভাইসের জন্য TAC ডেটাবেস
  · বাল্ক জেনারেশন
  · AT কমান্ড জেনারেশন
· লাইসেন্স: GNU GPL v3.0

৬. MTK IMEI Patcher https://img.shields.io/github/stars/timjosten/mtk_imei

· বিবরণ: Xiaomi Helio G সিরিজের ফোনের জন্য NVRAM পার্টিশন পুনঃনির্মাণের স্ক্রিপ্ট
· বৈশিষ্ট্য: TWRP-ফ্ল্যাশেবল ফাইল তৈরি

---

💻 কোড ও স্ক্রিপ্ট

১. Luhn অ্যালগরিদম (Python)

```python
def validate_imei(imei):
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
```

[সোর্স: bstein/py-imei-generator]

৩. Android (Java) - IMEI সংগ্রহ

```java
TelephonyManager telephonyManager = (TelephonyManager) 
    context.getSystemService(Context.TELEPHONY_SERVICE);

if (ActivityCompat.checkSelfPermission(context, 
    Manifest.permission.READ_PHONE_STATE) == PackageManager.PERMISSION_GRANTED) {
    String imei = telephonyManager.getImei(); // Android 10+
    // অথবা telephonyManager.getDeviceId() // Android 9-এর জন্য
}
```

[সোর্স: Quectel Forums]

৪. PHP - Luhn ভ্যালিডেশন

```php
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
```

[সোর্স: TheWebSolver/luhn-algorithm]

৫. ADB কমান্ডের মাধ্যমে IMEI

```bash
# পদ্ধতি ১
adb shell service call iphonesubinfo 1

# পদ্ধতি ২
adb shell dumpsys iphonesubinfo

# পদ্ধতি ৩ (রুটেড ডিভাইস)
adb shell cat /proc/cmdline
```

---

📱 মোবাইল অ্যাপ

১. Flutter Device IMEI Plugin https://img.shields.io/github/stars/pranilshah4024/flutter_device_imei

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

২. IMEI Plugin (Flutter) https://img.shields.io/github/stars/nqhhdev/imei_plugin

· বিবরণ: Flutter-এ Android ও iOS-এর জন্য IMEI সংগ্রহের প্লাগইন
· বৈশিষ্ট্য: ডুয়াল/ট্রিপল সিম সাপোর্ট
· ব্যবহার:

```dart
String imei = await ImeiPlugin.getImei();
List<String> multiImei = await ImeiPlugin.getImeiMulti();
```

৩. MTK IMEI Switcheroo App https://img.shields.io/github/stars/flipphoneguy/mtk-imei-switcheroo-app

· বিবরণ: রুটেড MediaTek MT67xx ফোনে IMEI, Bluetooth MAC ও WiFi MAC রিড ও রিরাইট করার অ্যাপ
· বৈশিষ্ট্য: IMEI জেনারেট, MAC র‍্যান্ডোমাইজ, লাস্ট ৫ ভ্যালু সেভ
· প্রয়োজনীয়তা: রুট (Magisk)

৪. Device Info (Android) https://img.shields.io/badge/GitHub-opt05/deviceid-blue

· বিবরণ: ওপেন সোর্স Android অ্যাপ যা IMEI/MEID, ডিভাইস মডেল, Android ID, Wi-Fi MAC, Bluetooth MAC ইত্যাদি প্রদর্শন করে
· প্লে স্টোরে উপলব্ধ

৫. SimInfo https://img.shields.io/github/stars/tech1ee/SimInfo

· বিবরণ: সিম কার্ডের তথ্য, নেটওয়ার্ক কানেক্টিভিটি ও ক্যারিয়ার সার্ভিস সম্পর্কে বিস্তারিত তথ্য প্রদানকারী Android অ্যাপ
· বৈশিষ্ট্য: IMEI, Android ID, ICCID প্রদর্শন

---

🌐 API ও ওয়েব সার্ভিস

১. IMEI.info API

· বিবরণ: IMEI ব্যবহার করে মোবাইল ডিভাইসের তথ্য সংগ্রহের API
· Node.js ক্লায়েন্ট: imei-info/imei-check-api-node
· Rust ক্রেট: imei-info

২. IMEI Checker API (Django)

· বিবরণ: Django-ভিত্তিক REST API যা বাহ্যিক API-এর মাধ্যমে IMEI চেক করে
· রিপোজিটরি: iurkinvalentin/IMEI_checker

৩. iFreeiCloud API

· বিবরণ: IMEI / iCloud / ক্যারিয়ার চেকের জন্য TypeScript ক্লায়েন্ট
· ইনস্টলেশন: npm install @hopla/ifreeicloud

৪. e-Devlet IMEI Check (Go)

· বিবরণ: তুরস্কের e-Devlet পোর্টালে IMEI রেজিস্ট্রেশন স্ট্যাটাস চেকের জন্য Go লাইব্রেরি
· রিপোজিটরি: KilimcininKorOglu/edevlet-imei-check

---

🔬 ফরেনসিক টেকনিক

১. লজিক্যাল এক্সট্রাকশন

মোবাইল ফরেনসিক টুলস ব্যবহার করে ডিভাইসের সেটিংস বা সিস্টেম ইনফরমেশন থেকে IMEI সংগ্রহ

২. ফিজিক্যাল এক্সট্রাকশন

ডিভাইস ড্যামেজ বা অ্যাক্সেসযোগ্য না হলে JTAG বা Chip-off ফরেনসিকের মাধ্যমে হার্ডওয়্যার থেকে IMEI এক্সট্র্যাক্ট

৩. MTK NVRAM রিভার্স ইঞ্জিনিয়ারিং

MediaTek ডিভাইসের IMEI এনক্রিপশন ফরম্যাট রিভার্স ইঞ্জিনিয়ারিং

· ফাইল লোকেশন: /mnt/vendor/nvdata/md/NVRAM/NVD_IMEI/LD0B_001
· এনক্রিপশন: AES-128-ECB + MD5-XOR checksum

৪. pyAndriller https://img.shields.io/github/stars/vicgc/pyAndriller

· বিবরণ: রুটেড Android ডিভাইস থেকে রিড-অনলি, ফরেনসিকভাবে সাউন্ড ডেটা এক্সট্রাকশন টুল

৫. Mobile-Diagnostics-Research https://img.shields.io/github/stars/fsinnes/Mobile-Diagnostics-Research

· বিবরণ: মোবাইল ডিভাইস শনাক্তকরণ ও ডায়াগনোসিস গবেষণার জন্য রিপোজিটরি
· AT কমান্ড: AT+IMEINUM, shell cat /csa/imei/serialno.dat

---

📦 গিটহাব রিপোজিটরি লিস্ট (সম্পূর্ণ)

# রিপোজিটরি বিবরণ ভাষা লাইসেন্স
1 D3crypT0r/IMEI-Find ADB-ভিত্তিক IMEI ফাইন্ডার Python -
2 itsKayWat/IMEI_Lookup IMEI লুকআপ টুল HTML/CSS/JS MIT
3 JonnyBytesMe/imei-validator IMEI ভ্যালিডেটর Python -
4 altheasignals/imei_scrape IMEI স্ক্র্যাপার ও ভ্যালিডেটর Python -
5 IMEI-Atlas/IMEI-Atlas IMEI জেনারেটর ও ভ্যালিডেটর Python GPL v3.0
6 Supa-mustea/IMEI-tracker আইন প্রয়োগের জন্য IMEI ট্র্যাকিং Python/Node.js -
7 Nurumoney/IMEI-Tracker Flask + SocketIO রিয়েল-টাইম ট্র্যাকিং Python -
8 pranilshah4024/flutter_device_imei Flutter IMEI প্লাগইন Dart -
9 nqhhdev/imei_plugin Flutter IMEI প্লাগইন Java/Dart MIT
10 flipphoneguy/mtk-imei-switcheroo-app MTK IMEI পরিবর্তন অ্যাপ Java -
11 timjosten/mtk_imei MTK NVRAM প্যাচার - -
12 TheWebSolver/luhn-algorithm PHP Luhn অ্যালগরিদম লাইব্রেরি PHP -
13 imei-info/imei-check-api-node IMEI.info API Node.js ক্লায়েন্ট TypeScript -
14 iurkinvalentin/IMEI_checker Django IMEI চেকার API Python -
15 codegeekr/validatorimei JavaScript IMEI ভ্যালিডেটর JavaScript -
16 vicgc/pyAndriller Android ফরেনসিক ডেটা এক্সট্রাকশন Python -
17 fsinnes/Mobile-Diagnostics-Research মোবাইল ডায়াগনস্টিক গবেষণা - -
18 CScorza/OSINT-FORENSICS-MOBILE OSINT মোবাইল ফরেনসিক টুলস - -
19 saschoar/android-imei-getter ADB-ভিত্তিক IMEI গেটার - -
20 opt05/deviceid Android ডিভাইস তথ্য অ্যাপ - -

---

📚 সম্পদ ও রেফারেন্স

অনলাইন টুলস

· IMEI.info - https://imei.info - IMEI লুকআপ ও ডিভাইস তথ্য
· SNDeepInfo - IMEI ডিভাইস চেকার
· Nobbi - IMEI টুলস
· GSMA IMEI Database - অফিসিয়াল TAC ডেটাবেস

অফিসিয়াল ভেরিফিকেশন

· ভারত: CEIR (Central Equipment Identity Register) - KYM<15 ডিজিট IMEI> SMS পাঠান 14422-এ
· GSMA TAC Database - অফিসিয়াল TAC তথ্য

ফরেনসিক টুলস

· Cellebrite - মোবাইল ফরেনসিক প্ল্যাটফর্ম
· Andriller - Android ফরেনসিক এক্সট্রাকশন টুল

ডকুমেন্টেশন

· MTK IMEI ফরম্যাট: docs/format.md
· রিভার্স ইঞ্জিনিয়ারিং: docs/reverse_engineering.md

---

⚠️ আইনি সতর্কতা

গুরুত্বপূর্ণ: এই ডকুমেন্টেশনটি শুধুমাত্র শিক্ষামূলক ও গবেষণামূলক উদ্দেশ্যে তৈরি করা হয়েছে।

1. অনুমোদন ছাড়া অন্য কারও ডিভাইসের IMEI অ্যাক্সেস বা পরিবর্তন করা অবৈধ
2. IMEI জালিয়াতি, মোবাইল চুরি, বা অন্যান্য অপরাধমূলক কাজে এই তথ্য ব্যবহার করা আইনত দণ্ডনীয়
3. এই টুলসগুলোর ফলাফল অফিসিয়াল চ্যানেলের মাধ্যমে যাচাই করতে হবে
4. আইন প্রয়োগকারী সংস্থাগুলোর জন্য ওয়ারেন্ট বা আইনি অনুমোদন প্রয়োজন
5. এই ডকুমেন্টেশনের লেখক/প্রকাশক কোনও অপব্যবহারের জন্য দায়ী নন

---

📝 সহায়তা ও অবদান

· বাগ রিপোর্ট: সংশ্লিষ্ট গিটহাব রিপোজিটরিতে ইস্যু খুলুন
· কোড কন্ট্রিবিউশন: ফর্ক করে পুল রিকোয়েস্ট পাঠান
· ডকুমেন্টেশন আপডেট: এই রিডমি ফাইলে কন্ট্রিবিউট করুন

---

📄 লাইসেন্স

এই ডকুমেন্টেশনটি MIT License-এর অধীনে প্রকাশিত। প্রতিটি টুল/সফটওয়্যারের নিজস্ব লাইসেন্স প্রযোজ্য।
Repo Copyright : Humayun Shariar Himu 

---

<div align="center">
  <sub>🔍 <strong>সর্বশেষ হালনাগাদ:</strong> ২০ আগস্ট ২০২৬ | <strong>সংস্করণ:</strong> ১.০</sub>
  <br>
  <sub>⚠️ <strong>শুধুমাত্র শিক্ষামূলক উদ্দেশ্যে</strong> ⚠️</sub>
</div>
