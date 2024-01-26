import subprocess


def android_get_desired_capabilities():
    return {
        "autoGrantPermissions": True,
        "automationName": "uiautomator2",
        "newCommandTimeout": 500,
        "noSign": True,
        "platformName": "Android",
        "platformVersion": "11",
        "resetKeyboard": True,
        "systemPort": 8301,
        "takesScreenshot": True,
        "udid": None,
        "appPackage": "com.ajaxsystems",
        "appActivity": "com.ajaxsystems.ui.activity.LauncherActivity",
    }


def get_udid_of_connected_device():
    result = subprocess.run(
        ["adb", "devices"], capture_output=True, text=True, check=True
    )
    output_lines = result.stdout.strip().split("\n")[1:]

    connected_devices = [
        line.split("\t")[0] for line in output_lines if "device" in line
    ]
    return connected_devices[0]


if __name__ == "__main__":
    print(get_udid_of_connected_device())
