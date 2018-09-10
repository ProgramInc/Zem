import os
import subprocess
import threading
import time
import csvreader
import FileHandler2 as FileHandler
import shutil
import MailSender

#This is the location of the log source folder
logSourceFolder = r'C:\\Users\\User\\Documents\\Orban Audio Loudness Meter\\'
#This is the location of the log destination folder
logDestinationFolder = r'C:\\Users\\User\\Desktop\\Loudness Log Backup\\'
#This is the location of the video source folder
videoSourceFolder = r'C:\\Users\\User\\Desktop\\video source\\'
#This is the location of the video destination folder
videoDestinationFolder = r'C:\\Users\\User\\Desktop\\video backup\\'

count = 0
badList = []
goodList = []
x = os.listdir(videoSourceFolder)


class ProgramRunner(threading.Thread):

    def run(self):
        a = subprocess.Popen(["C:\Program Files (x86)\Orban\Meter\Orban Loudness Meter.exe"])
        time.sleep(40)
        a.kill()


class fileRunner(threading.Thread):

    def run(self):
        for f in os.listdir(videoSourceFolder):
            subprocess.call(['C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe', videoSourceFolder+f, '--play-and-exit'])
            time.sleep(37)
        #b = subprocess.call("C:\\Users\\User\\Dropbox\\Def0.wav")
       # time.sleep(4)

       # time.sleep(3)



for files in x:
    count = count + 1

print(count, "File\s Found:")

for files in x:
    print(files)


#if count > 0:
for v in os.listdir(videoSourceFolder):
    if len(os.listdir(videoSourceFolder)) == 0:
        print('All Files Were Checked')
        break
    else:
        worker = FileHandler.FileMover()
        reader = csvreader.Reader()
        worker.move(logSourceFolder, logDestinationFolder)
        time.sleep(1)
        runProgram = ProgramRunner()
        runFile = fileRunner()
        runProgram.start()
        time.sleep(3)
        runFile.start()
        time.sleep(40)
        shutil.move(videoSourceFolder+v, videoDestinationFolder)
        reader.fileOpener()
        b = reader.final_check()
        if b is True:
            goodList.append(v)
        else:
            badList.append(v)

        time.sleep(1)
        print("loop was ended")

reader2 = csvreader.Reader()
# email_message = [reader2.total_tally(), 'Approved File/s:'+str(goodList), 'Rejected File/s'+str(badList)]
email2 = str(reader2.goodCount) + ' Approved File/s:\n' + str(goodList) + '\n' + str(reader2.badCount) + ' Rejected File/s\n'+ str(badList)
print(email2)

MailSender.TEXT = email2
MailSender.Mail.send_mail()

