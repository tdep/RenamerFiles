#! python3
# renameFiles.py - Renames filenames in numerical sequence based on folder size and date modified

import shutil, os, re, sys
import pyinputplus as pyip

def main():
    # Some possible regex might go here
    getDirectoryAndRun()


def getDirectoryAndRun():

    while True:
        # 1. Ask for directory
        print('Enter directory containing files to be renamed:')
        directory = input()

        # 2. Confirm directory with summary of contents
        path = directory
        os.chdir(path)
        filteredFiles = filter(os.path.isfile, os.listdir('.'))
        filteredFileList = list(filteredFiles)
        numberOfFiles = len(filteredFileList)

        print(f'The directory containing the files to be renamed is: {path}')
        prompt = f'There are {numberOfFiles} files in this directory. Do you want to proceed(yes/no)?\n'
        response = pyip.inputYesNo(prompt)

        if response == "yes":
            print("Running program...")
            return renameFiles()
        elif response == "no":
            exitPrompt = "Do you wish to exit?"
            exitResponse = pyip.inputYesNo(exitPrompt)

            if exitResponse == "yes":
                return exitProgram()

def renameFiles():

    currentFileNum = 0
    fileList = filter(os.path.isfile, os.listdir('.'))
    sortedFiles = sorted(fileList, key=os.path.getmtime)
    numFiles = len(sortedFiles)
    numDigits = len(str(numFiles))


    # Loop over the files in the working directory.
    for filename in sortedFiles:
        # Condition for the regex if we use it
        currentFileNum += 1

        originalName, ext = os.path.splitext(filename)
        absWorkingDir = os.path.abspath('.')
        oldFilename = os.path.join(absWorkingDir, filename)
        newFilename = os.path.join(absWorkingDir, f'{str(currentFileNum).rjust(numDigits, "0")}{ext}')
        newFilename = f'{str(currentFileNum).rjust(numDigits, "0")}{ext}'

        print(f'Renaming "{oldFilename}" to "{newFilename}"...')
        shutil.move(oldFilename, newFilename)

    print('')
    print(f'Job done. Renamed {currentFileNum} files.')

def exitProgram():
    print("Exiting...")
    sys.exit()

if __name__ == "__main__":
    main()
