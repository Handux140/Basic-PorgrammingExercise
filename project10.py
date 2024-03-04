# Input the email address
email = input("bradleyyaman416@gmail.com: ")

# Extract the domain name
domain = email.split('@')[-1]

# Print the domain name
print("Domain name:", domain)