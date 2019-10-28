print("Årstider")
print("Skriv inn en dato og du får vite hvilken årstid datoen hører til")

mnd = input("Måned: ").lower()
dag = int(input("Dag: "))

if ((mnd == "april" or mnd =="mai") or
    (mnd == "mars" and dag >= 20) or
    (mnd == "juni" and dag < 21)):
    print("Vår")
elif ((mnd == "juli" or mnd == "august") or
      (mnd == "juni" and dag >= 21) or
      (mnd == "september" and dag < 22)):
    print("Sommer")
elif ((mnd == "oktober" or mnd == "november") or
      (mnd == "september" and dag >= 22) or
      (mnd == "desember" and dag < 21)):
    print("Høst")
elif ((mnd == "januar" or mnd == "februar") or
      (mnd == "desember" and dag >= 21) or
      (mnd == "mars" and dag < 20)):
    print("Vinter")
