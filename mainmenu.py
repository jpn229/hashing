#The hashlib module provide an interface to algoriths to provide secure hashes 
#has SHA1, SHA224, SHA256, SHA384, and SHA512
import hashlib

#Defines the variable ans	
ans=True

#Sets up the while loop which prompts the user to select either a 
#string or a file to hash
while ans:
	print("""
	1. Enter a string to hash
	2. Enter a file to hash

	Press enter to quit
	""")
	
	ans=input("Make a selection?")
	
	if ans=="1":
			#Prompts the user to input a string and assisgnes the input
			#to the variable inputted_string
			inputted_string=input("Enter String to hash:  ")
				
			print("""
			1. Hash with SHA-1
			2. Hash with SHA-256
			3. Hash with SHA-512
			4. Hash with SHA-3
			5. All Hashes (SHA1, SHA-256, SHA-512 & SHA-3)
			
			""")
			
			#Prompts the user to select a hash to use such as SHA1, SHA-256, SHA-512 and SHA3
			#and assignes the input to the variable ans
			ans=input("Make a selection?")
			if ans=="1":
					#This calculates the SHA1 digest for string held in the inputted_string variable 
					#after it is encoded by the method encode() by calling the sha1 method from 
					#the library hasshlib. encode() is used to encode the user input string in 
					#a sequence of bytes
					#It then stores the result as a variable hash_object
					hash_object = hashlib.sha1(inputted_string.encode())
					
					#This returns the digest of the string which is returned as a string of double length
					#which only containing hexadecimal digits which allows it to exchanged by 
					#non-binary environments (email etc). This is held in the variable
					#hex_digest
					hex_digest = hash_object.hexdigest()
					
					#This prints out the user input held in the variable inputted_string 
					#and also prints out the variable hex_digest
					print("\n",inputted_string, "  Hashed with SHA-1 is   ",hex_digest )
			elif ans=="2":
					hash_object = hashlib.sha256(inputted_string.encode())
					hex_digest = hash_object.hexdigest()
					print("\n",inputted_string, "  Hashed with SHA-256 is   ",hex_digest )
			elif ans=="3":
					hash_object = hashlib.sha512(inputted_string.encode())
					hex_digest = hash_object.hexdigest()
					print("\n",inputted_string, "  Hashed with SHA-512 is   ",hex_digest )
			elif ans=="4":
					hash_object = hashlib.sha3_512(inputted_string.encode())
					hex_digest = hash_object.hexdigest()
					print("\n",inputted_string, "  Hashed with SHA-3 is   ",hex_digest )
			elif ans=="5":
					
					hash_object1 = hashlib.sha1(inputted_string.encode())
					hash_object2 = hashlib.sha256(inputted_string.encode())
					hash_object3 = hashlib.sha512(inputted_string.encode())
					hash_object4 = hashlib.sha3_512(inputted_string.encode())
					hex_digest1 = hash_object1.hexdigest()
					hex_digest2 = hash_object2.hexdigest()
					hex_digest3 = hash_object3.hexdigest()
					hex_digest4 = hash_object4.hexdigest()
					print("\n",inputted_string, "  Hashed with SHA-1 is   ",hex_digest1 )
					print("\n",inputted_string, "  Hashed with SHA-256 is   ",hex_digest2 )
					print("\n",inputted_string, "  Hashed with SHA-512 is   ",hex_digest3 )
					print("\n",inputted_string, "  Hashed with SHA-3 is   ",hex_digest4 )
			elif ans=="":
					print("\nThis is not a valid choice")
					


	
	
	elif ans=="2":
	
			#Prompts the user to input a file name with ot with its path 
			#and assisgnes the input to the variable full_path
			full_path=input("Enter file name:  ")
				
			print("""
			1. Hash with SHA-1
			2. Hash with SHA-256
			3. Hash with SHA-512
			4. Hash with SHA-3
			5. All Hashes (SHA1, SHA-256, SHA-512 & SHA-3)

			""")
			
			#Prompts the user to select a hash to use such as SHA1, SHA-256, SHA-512 and SHA3
			#and assignes the input to the variable ans
			ans=input("Make a selection?")
			if ans=="1":
			
					#The file or file / path held in the inputted_string variable is opened and 
					#read by the read() method in brinary read mode as stipulated 'rb'. 
					#The method hexdigest() then returns the digest of the read file as a 
					#string of double length which only containing hexadecimal digits which 
					#allows it to exchanged by non-binary environments (email etc).
					#After that is done it then calculates the SHA1 digest for the file and 
					#stores it in a variable file_string.	
					file_string = hashlib.sha1(open(full_path, 'rb').read()).hexdigest()
					
					#This prints out the variable inputted_string 
					print("\n","  Hashed with SHA-1   " ,file_string)
			elif ans=="2":
					file_string = hashlib.sha256(open(full_path, 'rb').read()).hexdigest()
					print("\n","  Hashed with SHA-256   " ,file_string)
			elif ans=="3":
					file_string = hashlib.sha512(open(full_path, 'rb').read()).hexdigest()
					print("\n","  Hashed with SHA-512   " ,file_string)
			elif ans=="4":
					file_string = hashlib.sha3_512(open(full_path, 'rb').read()).hexdigest()
					print("\n","  Hashed with SHA3   " ,file_string)
			elif ans=="5":
					file_string1 = hashlib.sha1(open(full_path, 'rb').read()).hexdigest()
					file_string2 = hashlib.sha256(open(full_path, 'rb').read()).hexdigest()
					file_string3 = hashlib.sha512(open(full_path, 'rb').read()).hexdigest()
					file_string4 = hashlib.sha3_512(open(full_path, 'rb').read()).hexdigest()
					print("\n","  Hashed with SHA-1   " ,file_string1)
					print("\n","  Hashed with SHA-256   " ,file_string2)
					print("\n","  Hashed with SHA-512   " ,file_string3)
					print("\n","  Hashed with SHA3   " ,file_string4)
					
			elif ans=="":
					print("\nThis is not a valid choice")
					

	elif ans=="":
		
		print("\nGood Bye1")  
		
