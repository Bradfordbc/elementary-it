# create TemporaryFile
temp = "tempfile.json"
search_filelist = []

# Creating an output file in writing mode
output_file = open(temp, "w")
  
# Opening input file and scanning each line
# from input file and writing in output file with comparsion
# comparison looks for files in the linux file system 
with open("temp", "r", newline="\n") as scan:
for line in scan.readlines():
    if "d" in line[:4]:
        continue
    else:
        line_split= line.split(" ")
        filename= line_split[5]
        search_filelist.append(filename)
         
# sending list of file to splunk via API         
for file in search_filelist:
    api_request= "https://http-inputs-host.splunkcloud.com:443/services/collector/raw/" + file