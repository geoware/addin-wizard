import os
import zipfile

current_path = os.path.dirname(os.path.abspath(__file__))

out_zip_name = os.path.join(current_path, 
                            os.path.basename(current_path) + ".esriaddin")

zip_file = zipfile.ZipFile(out_zip_name, 'w')
for filename in ('config.xml', 'README.txt', 'makeaddin.py'):
    zip_file.write(os.path.join(current_path, filename), filename)
dirs_to_add = ['Images', 'Install']
for directory in dirs_to_add:
    for (path, dirs, files) in os.walk(os.path.join(current_path, directory)):
        archive_path = os.path.relpath(path, current_path)
        found_file = False
        for file in (f for f in files if not f.lower().endswith('_backup.py')):
            archive_file = os.path.join(archive_path, file)
            print archive_file
            zip_file.write(os.path.join(path, file), archive_file)
            found_file = True
        if not found_file:
            zip_file.writestr(os.path.join(archive_path, 'placeholder.txt'), 
                              "(Empty directory)")
zip_file.close()
