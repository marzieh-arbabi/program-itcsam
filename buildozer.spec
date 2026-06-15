[app]

title = My Application
package.name = myapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 34
android.minapi = 24
android.ndk = 27c
android.ndk_api = 24
android.accept_sdk_license = True

android.archs = arm64-v8a

[buildozer]

log_level = 2
warn_on_root = 0
