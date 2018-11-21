import json
import sys
import argparse

parser = argparse.ArgumentParser( description='A utility that reads a JSON file for the 2018 SIGSPATIAL CUP competition, decodes it,  and prints out a subset of its contents and creates a file for visualization using the plotter.py program.')
parser.add_argument('filename', help='the name of the JSON file to decode')
parser.add_argument( '-v', '--verbose', type=int, default=0, help='turns on verbose output.  Prints a formatted version of the JSON file and some other info.')
parser.add_argument( '-o', '--outputfilename', default='zzzout.txt', help='Specify the name of the output file.')

if len(sys.argv) < 2:
    parser.print_help()
    exit()

args = parser.parse_args()

infile = open( args.filename, 'r' )

stuff = json.load( infile )


if args.verbose > 0: print json.dumps( stuff, indent=4 )

#get the controllers
controllers = []
for item in stuff['controllers']:
    controllers.append( (item['assetGroupName'], item['globalId'], item['geometry']['x'], item['geometry']['y']) )

if args.verbose > 0:
    print 'controllers:'
    for x in controllers: print x

# get the graph edges
paths = []
for row in stuff['rows']:
    edges =  row['viaGeometry']
    edges = edges.get('paths')
    if edges != None:
        edges = edges[0]
        edges = [ (x[0],x[1] ) for x in edges ]
    paths.append(  {'frompointid':row['fromGlobalId'], 'topointid':row['toGlobalId'], 'edgeid':row['viaGlobalId'], 'path':edges } )

if args.verbose > 0:
    for path in paths: print path

#print all paths to a file
print 'writing to the output file: ', args.outputfilename
fout = open(args.outputfilename,'w')
for p in paths:
    if p['path']!= None:
        for i in range(1, len(p['path'])):
            fout.write( str(p['path'][i-1][0]) + ' '+  str( p['path'][i-1][1]) + ' ' + str( p['path'][i][0]) + ' ' + str( p['path'][i][1]) + '\n' )

