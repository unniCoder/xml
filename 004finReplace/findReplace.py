import xml.etree.ElementTree as ET
import csv, time
 
start_time = time.time()
 
xml_filename_original = "original_file.xml"
xml_filename_new = xml_filename_original.replace(".xml", "_new.xml")
find_and_replace_filename = "find_replace.csv"
xml_file_original = open(xml_filename_original, "r")
xml_file_new = open(xml_filename_new, "w")
 
counter = 0
 
with open(find_and_replace_filename, "r") as f:
    for line in xml_file_original:
        f.seek(0)
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            line_old = line
            line_new = line.replace(row[0], row[1])
            if line_new != line_old:
                line = line_new
                counter += 1
                print("Counter: " + str(counter))
        xml_file_new.write(line)
 
xml_file_original.close()
xml_file_new.close()
 
elapsed_time = time.time() - start_time
 
print("Script ended, replaced " + str(counter) + " strings")
print("Elapsed time: " + str(elapsed_time) + " seconds")