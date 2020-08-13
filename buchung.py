import sys
import pandas as pd
import re

if len(sys.argv) != 3: #check if exactly two file names have been submitted
    #usage information: if more or less files have been submitted
    print("usage: python buchung.py <bank account bookings csv> <participants csv>") 
    print("results will be written to local directory")
    sys.exit() #exit program


Konto = pd.read_csv(sys.argv[1], skiprows=4, sep=',', encoding="utf8") #read csv files in utf8
Teilnehmer = pd.read_csv(sys.argv[2], encoding="utf8")
Rest = Konto.iloc[0:0]
Rest["Fehler"] = 0 # Creation of a file for booking-mistakes
Teilnehmer["Datum"] = ""



sus_nummer = "[sS][0-9][0-9][0-9][0-9]" #structure of student ID (example: S7867)



p = re.compile(sus_nummer)


for index, row in Konto.iterrows(): #look through all the rows of "Konto"
    found_numbers = p.findall(row["Verwendungszweck"]) # search in row "Verwendugszweck" for student IDs
    if len(found_numbers) == 1: #make sure, only one student ID has been submitted
        schueler = found_numbers[0].upper() #creating the variable "schueler" (student)
        tr = Teilnehmer.loc[Teilnehmer['Nummer'] == schueler] #assign student ID to respective student ("schueler")
                
        if len(tr.index) == 1:
            if Teilnehmer['SBF-J'][tr.index[0]] != "ja": #check whether they have already been marked as paid
                Teilnehmer['SBF-J'][tr.index[0]] = "ja" #mark them as paid
                Teilnehmer['Einzahlung'][tr.index[0]] = row["Haben"] #add the amount paid and,
                Teilnehmer['Datum'][tr.index[0]] = row["Buchungstag"] #add the date on wich the payment happened

            else:
                row["Fehler"] = "Bereits bezahlt" #if the person had already paid, add an error message and,
                Rest = Rest.append(row) #add the student to the "Rest"-file wich will be the "error"-file later
          
        else:
            row["Fehler"] = "Falsche Sus-Nr" #if no student with the submitted student ID exists, add an error message and,
            Rest = Rest.append(row) #add the student to the "Rest"-file wich will be the "error"-file later
            
    else:
        row["Fehler"] = "Keine oder mehrere SuS-Nr" #if multiple student IDs or none at all have been submitted, add an error message and,
        Rest = Rest.append(row, ignore_index = True) #add the student to the "Rest"-file wich will be the "error"-file later
     
            
            

Teilnehmer.to_csv(r"result.csv", encoding="ANSI") #create output files
Rest.to_csv(r"errors.csv", encoding="ANSI")

print("Success, wrote updated participantslist to result.csv and a list of unprocessed payments to errors.csv.")







