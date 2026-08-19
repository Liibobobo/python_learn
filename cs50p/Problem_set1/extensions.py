def main(): 
    file = input("File name: ").lower()

    # using function 'in' python to check sub_string in string or not, return true or false, so false --> move to the next statement
    if ('.gif' in file):
        print ('image/gif')
    elif ('.jpg' in file) or ('.jpeg' in file):
        print ('image/jpeg')
    elif ('.png' in file):
        print ('image/png')
    elif ('.pdf' in file):
        print ('application/pdf')
    elif ('.txt' in file):
        print ('text/plain')
    elif ('.zip' in file):
        print ('application/zip')
    else: 
        print ('application/octet-stream') 

main()