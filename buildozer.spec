[app]
title = AZADAV
package.name = azadav
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3==3.11.8,kivy==2.3.0,requests,urllib3

orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.wakelock = 1

[buildozer]
log_level = 2
display_log = 1