import sys
import os
def matcher(l):
    index=0
    first=l[0]
    last=l[len(l)-1]
    for each in range(len(last)):
        if first.startswith(last[:each]) and not str.isdigit(last[each]):
            index+=1
    return index


if __name__=="__main__":

    if len(sys.argv)<2:
        print ("""This script is used to check the sequence of files in a folder\n
               can be used to check the existence of every file in a sequence\n

               use the -d command to check a directory""")
    else :
        try:
            os.chdir(sys.argv[1])
        except :
            print ("Make sure you have entered a valid DIR")
            print ('exiting')
            exit()
        filesList=os.listdir()
        filesList.sort() #will sort the array alphabetically
        sliceIndex=matcher(filesList)
        # print(filesList[0])
        pre=filesList[0][:sliceIndex]
        # print(pre)
        for index in range (len(filesList)):
            filesList[index]=(filesList[index][sliceIndex:]).split('.')[0]
        first=int(filesList[0])
        last=int(filesList[len(filesList)-1])
        for i in range (first,last+1):
            try :
                filesList.index(str(i))
            except:
                print('missing file in sequence :'+pre + str(i))
        print ("end of execution")











