import os
import subprocess

# A script fájl helye (nem a futtatás helye!)
script_dir = os.path.dirname(os.path.abspath(__file__))
custom_nodes_path = os.path.join(script_dir, "custom_nodes")

# Bejárás a custom_nodes mappán belül
for foldername in os.listdir(custom_nodes_path):
    folder_path = os.path.join(custom_nodes_path, foldername)
    requirements_path = os.path.join(folder_path, "requirements.txt")

    if os.path.isdir(folder_path) and os.path.isfile(requirements_path):
        print(f"\n[✓] Követelmények telepítése: {foldername}")
        try:
            # pip install --upgrade
            subprocess.run(
                ["pip", "install", "--upgrade", "-r", requirements_path],
                check=True
            )
            # sima pip install
            subprocess.run(
                ["pip", "install", "-r", requirements_path],
                check=True
            )
        except subprocess.CalledProcessError as e:
            print(f"[!] Hiba történt a(z) {foldername} telepítése közben: {e}")
    else:
        print(f"[~] Nincs requirements.txt: {foldername}, átugrás.")
