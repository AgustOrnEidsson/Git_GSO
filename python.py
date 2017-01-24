#Git gagnasafna
text_file=open("texti.txt", "w")

text_file.write("Eru ekki allir i studi eda???")
text_file.close()

text_file=open("texti.txt", "a")
text_file.write("\n" + "Eru ekki allir i studi eda???")
text_file.write("\n" + "Eru ekki allir i studi eda???")
text_file.write("\n" + "Eru ekki allir i studi eda???")