#Writing to a file
f=open("python.txt","w")
f.write("Monty Python's Flying Circus")
f.close()

#writelines()-
lines=[" Beautiful is better than ugly.\n", "Explicit is better than implicit.\n",
  "Simple is better than complex.\n", "Complex is better than complicated.\n"]
f=open("python.txt","w")
f.writelines(lines)
f.close()
