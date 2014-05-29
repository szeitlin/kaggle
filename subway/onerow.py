import csv

def update(filenames):

    f = open (filenames, 'r')  #if you use with, you don't have to add a close statement
    old_name = csv.reader(f)       #have to create a file object because csv.reader doesn't use a path
    #listf = open("updated_" + filenames, 'w')
    #writer = csv.writer(listf, quoting = csv.QUOTE_NONE)


    for row in old_name:
        if len(row) > 0:
            print len(row)
            prefix = []
            prefix.extend(row[0:3])
        #writer.writerow(newlist)
            print "prefix contains" + str(prefix)
            del row[0:3]
            #print "remaining in row" + str(row)
            #print "row is now" + str(len(row))
            while len(row) >= 5:
                unit = []
                unit.extend(row[0:5])
                compunit = prefix + unit
                print "new complete unit is" + str(compunit)
                del row[0:5]
                #print "remaining in row" + str(row)
                print "row is now" + str(len(row))

            else:
                continue
        else:
            continue

    f.close()

update("mini_testfile.txt")


