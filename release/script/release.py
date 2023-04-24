#-- coding: UTF-8 --

import os
import subprocess
import shutil

from local_settings import LocalSettings


def verify_file_exist(file_path):
    if os.path.isfile(file_path):
        return True
    else:
        print("Invalid file path: " + file_path)
        return False


def verify_directory_exist(dir_path):
    if os.path.isdir(dir_path):
        return True
    else:
        print("Invalid directory path: " + dir_path)
        return False


def create_directory_if_not_exist(dir_path):
    if os.path.isdir(dir_path):
        return True
    else:
        os.mkdir(dir_path)
        return os.path.isdir(dir_path)


def extract_file_to(zip_file_relpath, dir_relpath):
    zip_file_path = os.path.join(LocalSettings.repository_folder, zip_file_relpath)
    if verify_file_exist(zip_file_path) is False:
        return False
    
    dir_path = os.path.join(LocalSettings.output_folder, dir_relpath)
    if create_directory_if_not_exist(dir_path) is False:
        return False

    cmd_line = f"\"{LocalSettings.seven_zip_exe}\" x \"{zip_file_path}\" -o\"{dir_path}\\\""
    print(cmd_line)
    subprocess.call(cmd_line)
    return True


def copy_file_to(file_relpath, dir_relpath):
    file_path = os.path.join(LocalSettings.repository_folder, file_relpath)
    if verify_file_exist(file_path) is False:
        return False
    
    dir_path = os.path.join(LocalSettings.output_folder, dir_relpath)
    if create_directory_if_not_exist(dir_path) is False:
        return False

    dest_file_path = os.path.join(dir_path, os.path.basename(file_path))
    shutil.copyfile(file_path, dest_file_path)
    return verify_file_exist(dest_file_path)


verify_file_exist(LocalSettings.seven_zip_exe)
verify_directory_exist(LocalSettings.repository_folder)
create_directory_if_not_exist(LocalSettings.output_folder)

apps_folder = os.path.join(LocalSettings.output_folder, "apps")
create_directory_if_not_exist(apps_folder)

wad_folder = os.path.join(LocalSettings.output_folder, "wad")
create_directory_if_not_exist(wad_folder)


def step1():
    copy_file_to("hackmii-installer-v0.8\\boot.elf", "apps\\hackmii-installer-v0.8")
    copy_file_to("hackmii-installer-v1.0\\boot.elf", "apps\\hackmii-installer-v1.0")
    copy_file_to("hackmii-installer-v1.0\\boot.elf", ".")
    
    return extract_file_to("bannerbomb-v1\\aad1f_v108.zip", ".")

step1()


def step2():
    extract_file_to("some-yawmm-mod\\some-yawmm-mod-v1.0.zip", ".")
    extract_file_to("yawmME\\yawmME.zip", "apps")

    copy_file_to("cios-for-usb-loader\\cIOS222[38]-v5.1R.wad", "wad\\cIOS")
    copy_file_to("cios-for-usb-loader\\cIOS223[37]-v5.1R.wad", "wad\\cIOS")
    copy_file_to("cios-for-usb-loader\\cIOS224[57]-v5.1R.wad", "wad\\cIOS")
    copy_file_to("cios-for-usb-loader\\cIOS248[38]-d2x-v11-beta1.wad", "wad\\cIOS")
    copy_file_to("cios-for-usb-loader\\cIOS249[56]-d2x-v11-beta1.wad", "wad\\cIOS")
    copy_file_to("cios-for-usb-loader\\cIOS250[57]-d2x-v11-beta1.wad", "wad\\cIOS")
    copy_file_to("cios-for-usb-loader\\cIOS251[58]-d2x-v11-beta1.wad", "wad\\cIOS")
    return True

step2()


def step3():
    extract_file_to("mmm\\Multi-Mod-Manager-v13.4.zip", ".")

    copy_file_to("cios236\\cIOS236[36-v3351]-v65535.wad", "wad")
    copy_file_to("cios236\\IOS15-64-v257.wad", ".")
    copy_file_to("cios236\\IOS15-64-v1032.wad", ".")
    copy_file_to("cios236\\IOS36-64-v3608.wad", ".")
    return True

step3()


def step4():
    return copy_file_to("ios58\\IOS58-64-v6176.wad", "wad")

step4()


def step5():
    return extract_file_to("hackmii-installer-v1.2\\hackmii-installer-v1.2.zip", "apps")

step5()


def step6():
    copy_file_to("system-menu\\4.3j\\4.3J-SystemMenu-ZHTW-v512-4.wad", "wad\\4.3J-SystemMenu-ZHTW")
    copy_file_to("system-menu\\4.3j\\cIOS80-64-v16174.wad", "wad\\4.3J-SystemMenu-ZHTW")

    copy_file_to("system-menu\\4.3u\\4.3U-SystemMenu-TWN-v513-2011-2.wad", "wad\\4.3U-SystemMenu-TWN")
    copy_file_to("system-menu\\4.3u\\cIOS80-64-v16174.wad", "wad\\4.3U-SystemMenu-TWN")

    return extract_file_to("change-region\\ARCME.zip", "apps")

step6()


def step7():
    return extract_file_to("priiloader\\Priiloader-v0.9.1.zip", "apps")

step7()


def step8():
    extract_file_to("system-channel\\AnyTitleDeleterMOD.zip", "apps")
    return copy_file_to("system-channel\\MiiChannel-ZHTW-v4.wad", "wad")
    
step8()

extract_file_to("pc-tool\\FAT32-GUI-Formatter.zip", "pc-tool")
