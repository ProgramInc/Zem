import os
import shutil



class FileMover:

    def move(self, source, destination):
        for f in os.listdir(source):
            if os.path.exists(destination+f):
                os.remove(source+f)
                print(f+'file already exists in destination folder... Deleting...')
            else:
                print(source+f, 'Was Moved To Backup')
                shutil.move(source+f, destination)


if __name__ == '__main__':
    pass

