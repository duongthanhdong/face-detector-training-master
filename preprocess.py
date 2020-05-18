import json
import argparse
from random import shuffle
object_map = {
	'truck': 0,
	'bus' : 1,
	'car' : 2,
	'motorbike' : 3
}parser = argparse.ArgumentParser()
parser.add_argument('--anno_file', type=str)
parser.add_argument('--root_folder', type=str)
args = parser.parse_args()# python main.py --anno_file ./anno.json --root_folder /home/nghi/97GB/
if __name__ == '__main__':
	root_folder = args.root_folder	parser = json.load(open(args.anno_file,'r'))
	shuffle(parser)	total_record = len(parser)	f_train = open('./train.txt','w')
	f_val = open('./val.txt','w')	for index, rec in enumerate(parser):
		image_path = ''		image_path = root_folder + rec['relpath'].replace('vehicle/','') # #!@#$
		# f = open(image_path.split('/')[-1].replace('.jpg','.txt'), 'w')
		f = open(image_path.replace('.jpg','.txt'), 'w')		for i in rec['data']:
			# Get bb
			object_type = i['name']
			bbox = i['attributes']['bbox']			if object_type in object_map.keys():
				write_str = str(object_map[object_type]) + ' ' + str(bbox[0]+bbox[2]/2) + ' ' + str(bbox[1]+bbox[3]/2) + ' ' + str(bbox[2]) + ' ' + str(bbox[3]) + '\n'
				f.write(write_str)
		f.close()		if index < 0.8 * total_record:
			f_train.write(image_path + '\n')
		else:
			f_val.write(image_path + '\n')