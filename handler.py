import os
current_dir = os.getcwd()
class Main:
    title = input('What would you like your rickroll website title to be? ')
    link = input('What would you like your rickroll link to be? ')
    text = input('What would you like your rickroll text to be? ')
# Read the HTML file
HTML_File=open('index.html','r')
s = HTML_File.read().format(p=Main())
#print ('Copy the following code (exclude this text) to an html file and send the file to your friend!')
#print(s)

print("Type cd " + current_dir + " to your terminal, write 'sudo mv " + current_dir + " ~/Desktop', enter your password and open the 'html_files' folder on your desktop. A new html file called 'do_not_open_this_file' will be created. Send that file to your friend and enjoy! Note: When you send the file, delete the 'do_not_open_this_file' for further rickrolls.")

os.chdir("html_files")
with open("do_not_open_this_file.html", "w") as f:
    f.write(s)