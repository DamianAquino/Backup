from datetime import datetime
import shutil
import os

def crear_backup(backup_path, backup_name, recursos):
    for recurso in recursos:
    
        if os.path.exists(recurso) and os.path.isdir(recurso):
            shutil.copytree(recurso, backup_path, dirs_exist_ok=True)

        elif os.path.exists(recurso) and os.path.isfile(recurso):
            shutil.copy(recurso, backup_path)

        # COMPRIMIR
        shutil.make_archive(backup_name, "zip", backup_path)

recursos = []

with open('RECURSOS.txt', 'r', encoding='utf-8') as file:
    for recurso in file:
        recursos.append(recurso.strip())

fecha_actual = datetime.now().strftime("%Y-%m-%d")
backup_name = f'Backup-{fecha_actual}'
backup_path = fr"C:\Users\aquinod\Desktop\Proyectos\Backup\{backup_name}"
os.makedirs(backup_path, exist_ok=True)

if __name__ == '__main__':
    crear_backup(backup_name, backup_path, recursos)
