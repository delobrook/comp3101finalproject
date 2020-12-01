def fifo():

    referenceString = input("Enter a string of more than 4 numbers (e.g. 1 2 3): ")   #Reference string of page numbers
    referencePages = list(map(int, referenceString.split()))                    #convert string to integer list of pages
    #frames = input("Enter the number of page frames: ")                         #space in main memory
   
    mainMemory = []             #Queue to perform FIFO  
    frames = 3
    pagefault = 0               #page is not in main memory
    pagehit = 0                 #page is in main memory

    "cpu demands page"
    "check if page is in main memory"
    "if not, get from sec memory and store in main memory"
    "if page is not in main memory it is a page fault"
    "if page is in main memory it is a page hit"

    for i in range(len(referencePages)):           #insert page and calculate pagefault/hit
                
        if len(mainMemory) < frames:
            if referencePages[i] not in mainMemory:
                mainMemory.append(referencePages[i])
                pagefault += 1
            else:
                pagehit += 1
        else:                                           #main memory full
            if referencePages[i] not in mainMemory:
                mainMemory.pop(0)                       #remove first page
                mainMemory.insert(0, referencePages[i])  #add next page
                pagefault += 1
            else:
                pagehit += 1

    return (pagefault, pagehit)
