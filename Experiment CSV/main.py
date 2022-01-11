import csv
from datetime import date

def main():
    first_array = [] #Debug purposes
    with open("event_schedule.csv", mode="r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        row_count = 0
        for row in reader:
            #Ignore the first row
            if row_count == 0:
                first_array = row #Debug purposes
                pass
            else:
                #Count the first index in a row, always
                index_count = 0
                for item in row:
                    #Ignore the empty spaces
                    if item != "()": 
                        #Parse out the items, ex. (num1, num2) to [num1, num2] where num(1/2) are strings
                        disection_item = item.replace('(', "").replace(')', "").replace(')', "").split(",")
                        time_start = disection_item[0] #num1
                        time_end = disection_item[1] #num2

                        print("TIME START: " + time_start)
                        print("TIME END: " + time_end)
                        print()
                        continue
                        #Sunday
                        if index_count == 0:
                            sunday_event(local_appObj, local_fileObj, time_start, time_end)

                        #Monday
                        elif index_count == 1:
                            monday_event(local_appObj, local_fileObj, time_start, time_end)
                        
                        #Tuesday
                        elif index_count == 2:
                            tuesday_event(local_appObj, local_fileObj, time_start, time_end)

                        #Wednesday
                        elif index_count == 3:
                            wednesday_event(local_appObj, local_fileObj, time_start, time_end)
                        
                        #Thursday
                        elif index_count == 4: 
                            thursday_event(local_appObj, local_fileObj, time_start, time_end)

                        #Friday
                        elif index_count == 5:
                            friday_event(local_appObj, local_fileObj, time_start, time_end)

                        #Saturday
                        else:
                            saturday_event(local_appObj, local_fileObj, time_start, time_end)
                    
                    index_count += 1

            row_count += 1

if __name__ == "__main__":
    main()