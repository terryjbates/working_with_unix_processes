p ARGV
ARGV.include?('--help')
# get the value of the -c option
ARGV.include?('-c') && ARGV[ARGV.index('-c') + 1]