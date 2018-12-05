import zipfile


def main():
	"""
	Zipfile password cracker using a brute-force dictionary attack
	"""
	zipfilename = 'test.zip'
	dictionary = 'dictionary.txt'

	zip_file = zipfile.ZipFile(zipfilename)
	with open(dictionary, 'r') as f:
		for line in f.readlines():
			password = line.strip('\n')
			try:
				print 'Trying password: %s' % password
				zip_file.extractall(pwd=password)
				print 'Password found >>> %s' % password
				break
			except:
				pass
	print 'No luck'

if __name__ == '__main__':
	main()
