def cause_a_to_do_something():
  import code as x 

  x.create("Aakash",25)    #to create a key with key_name,value given and with no time-to-live property
  x.create("src",50,120)  #to create a key with key_name,value given and with time-to-live property value given(number of seconds)
  x.read("Aakash")         #it returns the value of the respective key in Jasonobject format 'key_name:value'
  x.read("src")            #it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR

  x.create("Aakash",50)    
                          
  x.delete("Aakash")       #it deletes the respective key and its value from the database(memory is also freed)
#we can access these using multiple threads like
  t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
  t1.start()
  t1.sleep()
  t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
  t2.start()
  t2.sleep()
  x.do_something()
