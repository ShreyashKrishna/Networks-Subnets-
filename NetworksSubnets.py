def recieved(st1,j):
    j=j-1
    #decrement j by one
    ctr=0
    numberofblocks=len(st1)/16
    endst=''
    k=''
    for i in st1:
        ctr+=1
        #increment counter by one
        k=k+st1[ctr-1]#here get the position of string added
        if(ctr==16):
            b=int(k,2)
            endst+=chr(b)
            k=''#reinitialize k
            ctr=0
            st1=st1[16:]
    return (endst)
def acceptinput():
    finalstring=''
    inp=input('Enter your message:')
    for i in inp:
        k=''.join(format(ord(x), 'b') for x in i)
        ln=len(k)
        #print(ln)
        ln1=16-ln
        sta=''
        for o in range(0,ln1):
            sta=sta+'0'
        sta=sta+k
        finalstring=finalstring+sta
    st=''.join(format(ord(x), 'b') for x in inp)
    lenght=len(finalstring.encode('utf-8'))
    leng=len(st.encode('utf-8'))
    print(leng)
    list=[]
    list.append(st)
    list.append(lenght)
    list.append(inp)
    list.append(finalstring)
    return(list)
def h1():
    f = open("host1.txt", "a")  # open corresponding switch1 text to edit.
    lines = [line.rstrip('\n') for line in open('C:\\Users\\Sreyash krishna\\PycharmProjects\\untitled\\host1.txt')]
    #line1=int(lines[0])
    list=acceptinput()
    #print(list)
    inp=list[0]
    size=list[1]
    percent=0
    st=list[3]#so st stores list at first position-message in bytes
    numberofpackets=0
    send=input('Enter the destination host number:')
    leng1 = len(st)
    list1=[]
    list1.append('H1')
    list1.append(send)
    if (size > 1500):
        numberofpackets = int(size / 1500)
        percent = int(size % 1500)
    lastpacket=0
    if (percent != 0):
        numberofpackets += 1
        lastpacket=percent
    if(size<1500):
        numberofpackets=1
    print(numberofpackets)
    for i in range(0, numberofpackets):
        #in the ith packet, do:
        list1.append(i)#sequence number
        list1.append(i*1500)#load
        sendingst=''
        if (lastpacket != 0 and i == numberofpackets - 1):
            for u in range(0, lastpacket):
                sendingst = st[1500 * (numberofpackets - 1):]
        else:
            if(numberofpackets==1):
                for u in range(0,len(st)):
                    sendingst+=st[u]
            else:
                numberofel = int(1500 / 16)  # so number of el is around 250 elements
                # print(numberofel)
                numberofel = numberofel * 16  # these many blocks of elment is to be added in the message
                for u in range(0, numberofel):
                    sendingst += st[u]
                st = st[numberofel:]  # remove these elements
        list1.append(sendingst)
        #print(list1)
        switch1(list1)
        print(len(list1[4]))
        list1.pop()
        list1.pop()
        list1.pop()
def h2():
    f = open("host2.txt", "a")  # open corresponding switch1 text to edit.
    lines = [line.rstrip('\n') for line in open('C:\\Users\\Sreyash krishna\\PycharmProjects\\untitled\\host1.txt')]
    # line1=int(lines[0])
    list = acceptinput()
    # print(list)
    inp = list[0]
    size = list[1]
    percent = 0
    st = list[3]  # so st stores list at first position-message in bytes
    numberofpackets = 0
    send = input('Enter the destination host number:')
    leng1 = len(st)
    list1 = []
    list1.append('H2')
    list1.append(send)
    if (size > 1500):
        numberofpackets = int(size / 1500)
        percent = int(size % 1500)
    lastpacket = 0
    if (percent != 0):
        numberofpackets += 1
        lastpacket = percent
    if (size < 1500):
        numberofpackets = 1
    print(numberofpackets)
    for i in range(0, numberofpackets):
        # in the ith packet, do:
        list1.append(i)  # sequence number
        list1.append(i * 1500)  # load
        sendingst = ''
        if (lastpacket != 0 and i == numberofpackets - 1):
            for u in range(0, lastpacket):
                sendingst = st[1500 * (numberofpackets - 1):]
        else:
            if (numberofpackets == 1):
                for u in range(0, len(st)):
                    sendingst += st[u]
            else:
                numberofel = int(1500 / 16)  # so number of el is around 250 elements
                # print(numberofel)
                numberofel = numberofel * 16  # these many blocks of elment is to be added in the message
                for u in range(0, numberofel):
                    sendingst += st[u]
                st = st[numberofel:]  # remove these elements
        list1.append(sendingst)
        # print(list1)
        switch1(list1)
        print(len(list1[4]))
        list1.pop()
        list1.pop()
        list1.pop()
def h3():
    f = open("host3.txt", "a")  # open corresponding switch1 text to edit.
    lines = [line.rstrip('\n') for line in open('C:\\Users\\Sreyash krishna\\PycharmProjects\\untitled\\host1.txt')]
    # line1=int(lines[0])
    list = acceptinput()
    # print(list)
    inp = list[0]
    size = list[1]
    percent = 0
    st = list[3]  # so st stores list at first position-message in bytes
    numberofpackets = 0
    send = input('Enter the destination host number:')
    leng1 = len(st)
    list1 = []
    list1.append('H3')
    list1.append(send)
    if (size > 500):
        numberofpackets = int(size / 500)
        percent = int(size % 500)
    lastpacket = 0
    if (percent != 0):
        numberofpackets += 1
        lastpacket = percent
    if (size < 500):
        numberofpackets = 1
    print(numberofpackets)
    for i in range(0, numberofpackets):
        # in the ith packet, do:
        list1.append(i)  # sequence number
        list1.append(i * 500)  # load
        sendingst = ''
        if (lastpacket != 0 and i == numberofpackets - 1):
            for u in range(0, lastpacket):
                sendingst = st[500 * (numberofpackets - 1):]
        else:
            if (numberofpackets == 1):
                for u in range(0, len(st)):
                    sendingst += st[u]
            else:
                numberofel = int(500 / 16)  # so number of el is around 250 elements
                # print(numberofel)
                numberofel = numberofel * 16  # these many blocks of elment is to be added in the message
                for u in range(0, numberofel):
                    sendingst += st[u]
                st = st[numberofel:]  # remove these elements
        list1.append(sendingst)
        # print(list1)
        switch1(list1)
        print(len(list1[4]))
        list1.pop()
        list1.pop()
        list1.pop()
def h4():
    f = open("host4.txt", "a")  # open corresponding switch1 text to edit.
    lines = [line.rstrip('\n') for line in open('C:\\Users\\Sreyash krishna\\PycharmProjects\\untitled\\host1.txt')]
    # line1=int(lines[0])
    list = acceptinput()
    # print(list)
    inp = list[0]
    size = list[1]
    percent = 0
    st = list[3]  # so st stores list at first position-message in bytes
    numberofpackets = 0
    send = input('Enter the destination host number:')
    leng1 = len(st)
    list1 = []
    list1.append('H4')
    list1.append(send)
    if (size > 500):
        numberofpackets = int(size /500)
        percent = int(size % 500)
    lastpacket = 0
    if (percent != 0):
        numberofpackets += 1
        lastpacket = percent
    if (size < 500):
        numberofpackets = 1
    print(numberofpackets)
    for i in range(0, numberofpackets):
        # in the ith packet, do:
        list1.append(i)  # sequence number
        list1.append(i * 500)  # load
        sendingst = ''
        if (lastpacket != 0 and i == numberofpackets - 1):
            for u in range(0, lastpacket):
                sendingst = st[500 * (numberofpackets - 1):]
        else:
            if (numberofpackets == 1):
                for u in range(0, len(st)):
                    sendingst += st[u]
            else:
                numberofel = int(500 / 16)  # so number of el is around 250 elements
                # print(numberofel)
                numberofel = numberofel * 16  # these many blocks of elment is to be added in the message
                for u in range(0, numberofel):
                    sendingst += st[u]
                st = st[numberofel:]  # remove these elements
        list1.append(sendingst)
        # print(list1)
        switch1(list1)
        print(len(list1[4]))
        list1.pop()
        list1.pop()
        list1.pop()
def h5():
    f = open("host5.txt", "a")  # open corresponding switch1 text to edit.
    lines = [line.rstrip('\n') for line in open('C:\\Users\\Sreyash krishna\\PycharmProjects\\untitled\\host5.txt')]
    # line1=int(lines[0])
    list = acceptinput()
    # print(list)
    inp = list[0]
    size = list[1]
    percent = 0
    st = list[3]  # so st stores list at first position-message in bytes
    numberofpackets = 0
    send = input('Enter the destination host number:')
    leng1 = len(st)
    list1 = []
    list1.append('H5')
    list1.append(send)
    if (size > 500):
        numberofpackets = int(size / 500)
        percent = int(size % 500)
    lastpacket = 0
    if (percent != 0):
        numberofpackets += 1
        lastpacket = percent
    if (size < 500):
        numberofpackets = 1
    print(numberofpackets)
    for i in range(0, numberofpackets):
        # in the ith packet, do:
        list1.append(i)  # sequence number
        list1.append(i * 500)  # load
        sendingst = ''
        if (lastpacket != 0 and i == numberofpackets - 1):
            for u in range(0, lastpacket):
                sendingst = st[500 * (numberofpackets - 1):]
        else:
            if (numberofpackets == 1):
                for u in range(0, len(st)):
                    sendingst += st[u]
            else:
                numberofel = int(500 / 16)  # so number of el is around 250 elements
                # print(numberofel)
                numberofel = numberofel * 16  # these many blocks of elment is to be added in the message
                for u in range(0, numberofel):
                    sendingst += st[u]
                st = st[numberofel:]  # remove these elements
        list1.append(sendingst)
        # print(list1)
        switch1(list1)
        print(len(list1[4]))
        list1.pop()
        list1.pop()
        list1.pop()
def h6():
    f = open("host6.txt", "a")  # open corresponding switch1 text to edit.
    lines = [line.rstrip('\n') for line in open('C:\\Users\\Sreyash krishna\\PycharmProjects\\untitled\\host6.txt')]
    # line1=int(lines[0])
    list = acceptinput()
    # print(list)
    inp = list[0]
    size = list[1]
    percent = 0
    st = list[3]  # so st stores list at first position-message in bytes
    numberofpackets = 0
    send = input('Enter the destination host number:')
    leng1 = len(st)
    list1 = []
    list1.append('H6')
    list1.append(send)
    if (size > 500):
        numberofpackets = int(size / 500)
        percent = int(size % 500)
    lastpacket = 0
    if (percent != 0):
        numberofpackets += 1
        lastpacket = percent
    if (size < 500):
        numberofpackets = 1
    print(numberofpackets)
    for i in range(0, numberofpackets):
        # in the ith packet, do:
        list1.append(i)  # sequence number
        list1.append(i * 500)  # load
        sendingst = ''
        if (lastpacket != 0 and i == numberofpackets - 1):
            for u in range(0, lastpacket):
                sendingst = st[500 * (numberofpackets - 1):]
        else:
            if (numberofpackets == 1):
                for u in range(0, len(st)):
                    sendingst += st[u]
            else:
                numberofel = int(500 / 16)  # so number of el is around 250 elements
                # print(numberofel)
                numberofel = numberofel * 16  # these many blocks of elment is to be added in the message
                for u in range(0, numberofel):
                    sendingst += st[u]
                st = st[numberofel:]  # remove these elements
        list1.append(sendingst)
        # print(list1)
        switch1(list1)
        print(len(list1[4]))
        list1.pop()
        list1.pop()
        list1.pop()
def h7():
    f = open("host4.txt", "a")  # open corresponding switch1 text to edit.
    lines = [line.rstrip('\n') for line in open('C:\\Users\\Sreyash krishna\\PycharmProjects\\untitled\\host1.txt')]
    # line1=int(lines[0])
    list = acceptinput()
    # print(list)
    inp = list[0]
    size = list[1]
    percent = 0
    st = list[3]  # so st stores list at first position-message in bytes
    numberofpackets = 0
    send = input('Enter the destination host number:')
    leng1 = len(st)
    list1 = []
    list1.append('H7')
    list1.append(send)
    if (size > 1000):
        numberofpackets = int(size / 1000)
        percent = int(size % 1000)
    lastpacket = 0
    if (percent != 0):
        numberofpackets += 1
        lastpacket = percent
    if (size < 1000):
        numberofpackets = 1
    print(numberofpackets)
    for i in range(0, numberofpackets):
        # in the ith packet, do:
        list1.append(i)  # sequence number
        list1.append(i * 1000)  # load
        sendingst = ''
        if (lastpacket != 0 and i == numberofpackets - 1):
            for u in range(0, lastpacket):
                sendingst = st[1000 * (numberofpackets - 1):]
        else:
            if (numberofpackets == 1):
                for u in range(0, len(st)):
                    sendingst += st[u]
            else:
                numberofel = int(1000 / 16)  # so number of el is around 250 elements
                # print(numberofel)
                numberofel = numberofel * 16  # these many blocks of elment is to be added in the message
                for u in range(0, numberofel):
                    sendingst += st[u]
                st = st[numberofel:]  # remove these elements
        list1.append(sendingst)
        # print(list1)
        switch1(list1)
        print(len(list1[4]))
        list1.pop()
        list1.pop()
        list1.pop()
def h8():
    f = open("host8.txt", "a")  # open corresponding switch1 text to edit.
    lines = [line.rstrip('\n') for line in open('C:\\Users\\Sreyash krishna\\PycharmProjects\\untitled\\host8.txt')]
    # line1=int(lines[0])
    list = acceptinput()
    # print(list)
    inp = list[0]
    size = list[1]
    percent = 0
    st = list[3]  # so st stores list at first position-message in bytes
    numberofpackets = 0
    send = input('Enter the destination host number:')
    leng1 = len(st)
    list1 = []
    list1.append('H8')
    list1.append(send)
    if (size > 2000):
        numberofpackets = int(size / 2000)
        percent = int(size % 2000)
    lastpacket = 0
    if (percent != 0):
        numberofpackets += 1
        lastpacket = percent
    if (size < 2000):
        numberofpackets = 1
    print(numberofpackets)
    for i in range(0, numberofpackets):
        # in the ith packet, do:
        list1.append(i)  # sequence number
        list1.append(i * 2000)  # load
        sendingst = ''
        if (lastpacket != 0 and i == numberofpackets - 1):
            for u in range(0, lastpacket):
                sendingst = st[2000 * (numberofpackets - 1):]
        else:
            if (numberofpackets == 1):
                for u in range(0, len(st)):
                    sendingst += st[u]
            else:
                numberofel = int(2000 / 16)  # so number of el is around 250 elements
                # print(numberofel)
                numberofel = numberofel * 16  # these many blocks of elment is to be added in the message
                for u in range(0, numberofel):
                    sendingst += st[u]
                st = st[numberofel:]  # remove these elements
        list1.append(sendingst)
        # print(list1)
        switch1(list1)
        print(len(list1[4]))
        list1.pop()
        list1.pop()
        list1.pop()
def h9():
    f = open("host9.txt", "a")  # open corresponding switch1 text to edit.
    lines = [line.rstrip('\n') for line in open('C:\\Users\\Sreyash krishna\\PycharmProjects\\untitled\\host9.txt')]
    # line1=int(lines[0])
    list = acceptinput()
    # print(list)
    inp = list[0]
    size = list[1]
    percent = 0
    st = list[3]  # so st stores list at first position-message in bytes
    numberofpackets = 0
    send = input('Enter the destination host number:')
    leng1 = len(st)
    list1 = []
    list1.append('H9')
    list1.append(send)
    if (size > 2000):
        numberofpackets = int(size / 2000)
        percent = int(size % 2000)
    lastpacket = 0
    if (percent != 0):
        numberofpackets += 1
        lastpacket = percent
    if (size <2000):
        numberofpackets = 1
    print(numberofpackets)
    for i in range(0, numberofpackets):
        # in the ith packet, do:
        list1.append(i)  # sequence number
        list1.append(i * 2000)  # load
        sendingst = ''
        if (lastpacket != 0 and i == numberofpackets - 1):
            for u in range(0, lastpacket):
                sendingst = st[2000 * (numberofpackets - 1):]
        else:
            if (numberofpackets == 1):
                for u in range(0, len(st)):
                    sendingst += st[u]
            else:
                numberofel = int(2000 / 16)  # so number of el is around 250 elements
                # print(numberofel)
                numberofel = numberofel * 16  # these many blocks of elment is to be added in the message
                for u in range(0, numberofel):
                    sendingst += st[u]
                st = st[numberofel:]  # remove these elements
        list1.append(sendingst)
        # print(list1)
        switch1(list1)
        print(len(list1[4]))
        list1.pop()
        list1.pop()
        list1.pop()
def h10():
    f = open("host10.txt", "a")  # open corresponding switch1 text to edit.
    lines = [line.rstrip('\n') for line in open('C:\\Users\\Sreyash krishna\\PycharmProjects\\untitled\\host10.txt')]
    # line1=int(lines[0])
    list = acceptinput()
    # print(list)
    inp = list[0]
    size = list[1]
    percent = 0
    st = list[3]  # so st stores list at first position-message in bytes
    numberofpackets = 0
    send = input('Enter the destination host number:')
    leng1 = len(st)
    list1 = []
    list1.append('H10')
    list1.append(send)
    if (size > 500):
        numberofpackets = int(size / 500)
        percent = int(size % 500)
    lastpacket = 0
    if (percent != 0):
        numberofpackets += 1
        lastpacket = percent
    if (size < 500):
        numberofpackets = 1
    print(numberofpackets)
    for i in range(0, numberofpackets):
        # in the ith packet, do:
        list1.append(i)  # sequence number
        list1.append(i * 500)  # load
        sendingst = ''
        if (lastpacket != 0 and i == numberofpackets - 1):
            for u in range(0, lastpacket):
                sendingst = st[500 * (numberofpackets - 1):]
        else:
            if (numberofpackets == 1):
                for u in range(0, len(st)):
                    sendingst += st[u]
            else:
                numberofel = int(500 / 16)  # so number of el is around 250 elements
                # print(numberofel)
                numberofel = numberofel * 16  # these many blocks of elment is to be added in the message
                for u in range(0, numberofel):
                    sendingst += st[u]
                st = st[numberofel:]  # remove these elements
        list1.append(sendingst)
        # print(list1)
        switch1(list1)
        print(len(list1[4]))
        list1.pop()
        list1.pop()
        list1.pop()
def h11():
    f = open("host11.txt", "a")  # open corresponding switch1 text to edit.
    lines = [line.rstrip('\n') for line in open('C:\\Users\\Sreyash krishna\\PycharmProjects\\untitled\\host1.txt')]
    # line1=int(lines[0])
    list = acceptinput()
    # print(list)
    inp = list[0]
    size = list[1]
    percent = 0
    st = list[3]  # so st stores list at first position-message in bytes
    numberofpackets = 0
    send = input('Enter the destination host number:')
    leng1 = len(st)
    list1 = []
    list1.append('H11')
    list1.append(send)
    if (size > 1500):
        numberofpackets = int(size / 1500)
        percent = int(size % 1500)
    lastpacket = 0
    if (percent != 0):
        numberofpackets += 1
        lastpacket = percent
    if (size < 1500):
        numberofpackets = 1
    print(numberofpackets)
    for i in range(0, numberofpackets):
        # in the ith packet, do:
        list1.append(i)  # sequence number
        list1.append(i * 1500)  # load
        sendingst = ''
        if (lastpacket != 0 and i == numberofpackets - 1):
            for u in range(0, lastpacket):
                sendingst = st[1500 * (numberofpackets - 1):]
        else:
            if (numberofpackets == 1):
                for u in range(0, len(st)):
                    sendingst += st[u]
            else:
                numberofel = int(1500 / 16)  # so number of el is around 250 elements
                # print(numberofel)
                numberofel = numberofel * 16  # these many blocks of elment is to be added in the message
                for u in range(0, numberofel):
                    sendingst += st[u]
                st = st[numberofel:]  # remove these elements
        list1.append(sendingst)
        # print(list1)
        switch1(list1)
        print(len(list1[4]))
        list1.pop()
        list1.pop()
        list1.pop()
def h12():
    f = open("host12.txt", "a")  # open corresponding switch1 text to edit.
    lines = [line.rstrip('\n') for line in open('C:\\Users\\Sreyash krishna\\PycharmProjects\\untitled\\host12.txt')]
    # line1=int(lines[0])
    list = acceptinput()
    # print(list)
    inp = list[0]
    size = list[1]
    percent = 0
    st = list[3]  # so st stores list at first position-message in bytes
    numberofpackets = 0
    send = input('Enter the destination host number:')
    leng1 = len(st)
    list1 = []
    list1.append('H7')
    list1.append(send)
    if (size > 2000):
        numberofpackets = int(size / 2000)
        percent = int(size % 2000)
    lastpacket = 0
    if (percent != 0):
        numberofpackets += 1
        lastpacket = percent
    if (size < 2000):
        numberofpackets = 1
    print(numberofpackets)
    for i in range(0, numberofpackets):
        # in the ith packet, do:
        list1.append(i)  # sequence number
        list1.append(i * 2000)  # load
        sendingst = ''
        if (lastpacket != 0 and i == numberofpackets - 1):
            for u in range(0, lastpacket):
                sendingst = st[2000 * (numberofpackets - 1):]
        else:
            if (numberofpackets == 1):
                for u in range(0, len(st)):
                    sendingst += st[u]
            else:
                numberofel = int(2000 / 16)  # so number of el is around 250 elements
                # print(numberofel)
                numberofel = numberofel * 16  # these many blocks of elment is to be added in the message
                for u in range(0, numberofel):
                    sendingst += st[u]
                st = st[numberofel:]  # remove these elements
        list1.append(sendingst)
        # print(list1)
        list1.append(numberofpackets)
        switch1(list1)
        print(len(list1[4]))
        list1.pop()
        list1.pop()
        list1.pop()
def switch1(list1):
    print(list1)
    dest=list1[1]
    i=0
    if dest in S1:
        i+=1
        lists1.append(recieved(list1[4],i))#so here we have lists1 appended with element
        print(lists1)
    else:
        if(dest=='H7' or dest=='H6' or dest=='H10'or dest=='H5'):
            print('')

lists1=[]
listh1=[]
H=['H1','H2','H3','H4','H5','H6','H7','H8','H9']
S1=['H1','H11','H2','S4','S2']
S2=['H7','S1','S3']
S3=['H5','H10','H6']
S4=['H3','H4','S1','S5']
S5=['H8','H12','H9','S4']
i=0
ctr=0
ctr1=0
while ctr==0:
    i=int(input('Enter 1 if you want to send a message, else press 0 to exit program:'))
    if(i!=0):
        j = int(input('Enter the sender host number:'))
        if(j==1):
            h1();
        if (j == 2):
            h2();
        if (j == 3):
            h3();
        if (j == 4):
            h4();
        if (j == 5):
            h5();
        if (j == 6):
            h6();
        if (j == 7):
            h7();
        if (j == 8):
            h8();
        if (j == 9):
            h9();
        if ( j == 10):
            h10();
        if ( j == 11):
            h11();
        if ( j == 12):
            h12();
    else:
        ctr=ctr+1#increment counter by one.