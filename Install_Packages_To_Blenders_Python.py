# You MUST run Blender as Administrator for this script to work
# Right Click on Blender.exe, and choose Run > As Administrator
# Otherwise you will get a Permission Error and the script will fail

import bpy, subprocess, sys

versionnumber = str(bpy.data.version)
versionstring = versionnumber.replace(',','.').replace(' ','').replace('(','')
version = versionstring.rstrip(versionstring[-3:])

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
        "--target=C:\\Program Files\\Blender Foundation\\Blender " + version + "\\" + version + "\\python\\lib", 
        package])
 