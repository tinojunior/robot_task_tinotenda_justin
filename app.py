# Importing sendpdf function 
# From pdf_mail Library 
from pdf_mail import sendpdf 


# Create an object of sendpdf function 
k = sendpdf("tinojunior1205@gmail.com", 
            "hitsumit@yopmail.com", 
            "triddaKid06", 
            "Tinotenda", 
            "Mupemhena", 
            "25/04/22 23:15", 
            "C:\Users\User\Desktop\Tino\MIT\robots\my_first_robot") 

# sending an email 
k.email_send()