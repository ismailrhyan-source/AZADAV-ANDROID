[app]
title = AZADAV
package.name = azadav
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0,requests,urllib3,openssl

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# PENTING: Konfigurasi sinkron dengan build.yml
android.api = 34
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.wakelock = 1

# PENTING: Paksa buildozer menggunakan SDK yang sudah kita buat di GitHub
android.sdk_path = /home/runner/android-sdk

[buildozer]
log_level = 2
display_log = 1