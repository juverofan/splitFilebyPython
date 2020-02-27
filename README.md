# splitFilebyPython
Split the multiple files from a folder (filter by wildcard) using Python
<br>
Using on Linux os:<br>
Split 1 file to 2 files:<br>
<b>python splitFile -f <file_name> -r <rate_for_split> -o <output_folder></b>
  
<br><b>Example:</b> rate = 0.1 => the line number of the first splitted file = 0.1 * the line number of the original file.

<br>Split the multiple files (from a folder):<br>
<b>python splitFileWildCard -d <folder_name> -w [wildcard] -r <rate_for_split> -o <output_folder></b>
  
 
