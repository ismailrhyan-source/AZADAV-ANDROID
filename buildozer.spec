[app]
title = AZADAV
package.name = azadav
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
# Hapus versi python spesifik di sini agar buildozer menggunakan versi dari sistem
requirements = python3,kivy==2.3.0,requests,urllib3,openssl

orientation = portrait
fullscreen = 0
android.permissions = INTERNET
# UBAH INI MENJADI 34 agar sinkron dengan server
android.api = 34
android.minapi = 21
# NDK 25b sudah cukup baik
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.wakelock = 1

[buildozer]
log_level = 2
display_log = 1
