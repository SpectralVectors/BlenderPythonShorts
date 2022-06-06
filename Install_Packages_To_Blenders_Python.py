# You MUST run Blender as Administrator for this script to work
# Right Click on Blender.exe, and choose Run > As Administrator
# Otherwise you will get a Permission Error and the script will fail

import bpy, subprocess, sys

string = bpy.app.version_string
blenderversion = string.rstrip(string[-2:])

packages = ["shapely", "Equation"]

subprocess.check_call([
    sys.executable, 
    "-m", "ensurepip"])

subprocess.check_call([
    sys.executable, 
    "-m", "pip", "install", "--upgrade", "pip"])

for package in packages:
    subprocess.check_call([
        sys.executable, 
        "-m", "pip", "install",
        f"--target=C:\\Program Files\\Blender Foundation\\Blender {blenderversion}\\{blenderversion}\\python\\lib", 
        package])
 
