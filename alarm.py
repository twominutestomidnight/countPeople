import re


startEnterValue = 10

flag = False
i = 0



#rint(dataSplit[1])
str1 = "<eventState>active</eventState>"
str2 = "<eventDescription>IO alarm</eventDescription>"
srt3 = "<eventType>PeopleCounting</eventType>"
#startEnterValue = 112
#print(dataSplit[3][:-78])

#while(True):
f = open("test.log", "r")
dataFull = f.read()
# print(dataFull)
#print("=--=-=-=-=-")
dataSplit = dataFull.split('\n\n')
for block in dataSplit:
    small_block = block.split('\n')
    for row in small_block:
        if row == str2:
            flag = True
            #print("IO alarm :", row)

        if row == srt3 and flag == True:
            print("===========", i)
            enterValue = (int)(re.findall(r'<enter>(.*?)</enter>', block, re.DOTALL)[0])
            print("enterValue", enterValue)
            print("startEnterValue", startEnterValue)
            if enterValue > startEnterValue:

                if (enterValue - startEnterValue) > 1:
                    #file.write("people enter: "+ enterValue - startEnterValue+"alarm!!!")
                    print("people enter: ", enterValue - startEnterValue)
                    print("alarm!!!")
                    flag = False
                startEnterValue = enterValue
            print("===========")
            i += 1
