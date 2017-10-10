my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
new_dict = []
for key,value in my_dict.items():
    temp = (key,value)
    new_dict.append(temp)
print new_dict