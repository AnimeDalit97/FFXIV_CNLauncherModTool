import os, zipfile

def backupLauncher(ffxivRootDir, outputDir):
    outputPath = os.path.join(outputDir, 'FFXIVLauncherbackup.zip')
    ffxivLauncherDir = os.path.join(ffxivRootDir, 'sdo/sdologin/')
    zipDir1 = os.path.join(ffxivLauncherDir, 'skin')
    zipDir2 = os.path.join(ffxivLauncherDir, 'dengluweb')
    zip = zipfile.ZipFile(outputPath, 'w', zipfile.ZIP_DEFLATED)
    filesList = []
    findFile(zipDir1, filesList)
    findFile(zipDir2, filesList)
    for file in filesList:
        zip.write(file, file.replace(ffxivLauncherDir,''))
    zip.close()

def backupLauncherAll(ffxivRootDir, outputDir):
    outputPath = os.path.join(outputDir, 'FFXIVLauncherbackup.zip')
    ffxivLauncherDir = os.path.join(ffxivRootDir, 'sdo/sdologin/')
    zip = zipfile.ZipFile(outputPath, 'w', zipfile.ZIP_DEFLATED)
    filesList = []
    findFile(ffxivLauncherDir, filesList)
    for file in filesList:
        zip.write(file, file.replace(ffxivLauncherDir,''))
    zip.close()


def findFile(inputDir, res):
    files = os.listdir(inputDir)
    for file in files:
        fpath = os.path.join(inputDir, file)
        if os.path.isdir(fpath):
            findFile(fpath, res)
        else:
            res.append(fpath)

def replaceFile(ffxivRootDir, modFilePath):
    ffxivLauncherDir = os.path.join(ffxivRootDir, 'sdo/sdologin/')
    modFile = zipfile.ZipFile(modFilePath)
    for file in modFile.namelist():
        modFile.extract(file, ffxivLauncherDir)


if __name__=='__main__':
    path = 'F:/Program Files (x86)/上海数龙科技有限公司/最终幻想XIV/'
    backupLauncher(path, 'F:/')