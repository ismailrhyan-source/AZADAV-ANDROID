[app]
title = AZADAV
package.name = azadav
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
# Pastikan openssl ada untuk mencegah crash pada requests
requirements = python3,kivy==2.3.0,requests,urllib3,openssl

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# Konfigurasi sinkron dengan build.yml
android.api = 34
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.wakelock = 1

# PENTING: Paksa buildozer menggunakan SDK yang kita buat di build.yml
android.sdk_path = /home/runner/android-sdk

[buildozer]
log_level = 2
display_log = 1
