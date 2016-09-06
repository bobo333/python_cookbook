# check if .txt file
file_name = "steve.txt"
print(file_name.endswith('.txt'))

# check multiple options
protocols = ('http://', 'https://', 'ftp://')   # must be a tuple!
possible_sites = ['http://google.com', 'hahaha', 'ftz://nope.com', 'https://espn.com']

sites = [x for x in possible_sites if x.startswith(protocols)]
print(sites)
