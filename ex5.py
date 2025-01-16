wordlist = []
try:
    with open("ex5read.txt", "r") as file:
        for line in file:
            line = line.strip()
            wordlist.append(line)
except FileNotFoundError:
  print("File not found!")
except Exception as e: # Catches other potential errors
  print(f"An error occurred: {e}")

sorted_wordlist = sorted(wordlist, key = lambda x: (len(x),x))
print(sorted_wordlist)
try:
    with open("ex5write.txt","w") as file:
       for word in sorted_wordlist:
          file.write(f"{word}\n")
       
except Exception as e: # Catches other potential errors
  print(f"An error occurred: {e}")