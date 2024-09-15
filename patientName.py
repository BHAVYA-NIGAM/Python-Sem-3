#WAP to check in a patient name Adi is 30 years old and is  a new patient
patient_name = "Adi"
patient_age = 30
new_patient = True
existing_patient = False

if(new_patient == True and existing_patient == False) :
  print("Yes, " + patient_name + " is a new patient.")
else: 
  print("No, " + patient_name + " is a existing patient.")

new_patient = False
existing_patient = True

if(new_patient == True and existing_patient == False) :
  print("Yes, " + patient_name + " is a new patient.")
else: 
  print("No, " + patient_name + " is a existing patient.")