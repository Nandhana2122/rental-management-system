import pywhatkit
import time

print("Starting WhatsApp test...")

# small delay before opening browser
time.sleep(2)

phone = "+918838412908"   
message = "Welcome to RentEase 🎉 You logged in successfully ✅"

pywhatkit.sendwhatmsg_instantly(
    phone_no=phone,
    message=message,
    wait_time=25,
    tab_close=False
)

print("Message process finished.")


