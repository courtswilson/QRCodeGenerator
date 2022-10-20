# Necessary importing of libraries
import qrcode

# Define function to generate a QR Code
def GenerateCode():
    code = qrcode.QRCode(version = None, error_correction = qrcode.constants.ERROR_CORRECT_Q, box_size = 20, border = 4)
    code.add_data(website)
    code.make(fit = True)

    qr_code = code.make_image(fill_color = custom_colour, back_color = custom_background)
    qr_code.save('')

# USER SPECIFICATIONS AND INPUT
website = input('\033[1m' + 'What website would you like to generate a QR Code for? ' + '\033]0m')

customise = input('\033[1m' + 'Would you like to customise the QR Code? (Y/N) ' + '\033[0m')

if customise == "Y" or customise == "y":
    custom_colour = input('\033[1m' + 'What colour would you like the code to be? ' + '\033[0m')
    custom_background = input('\033[1m' + 'What background colour would you like for the code? ' + '\033[0m')

GenerateCode()