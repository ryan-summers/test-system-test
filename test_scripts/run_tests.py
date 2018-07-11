#!/usr/bin/python

from lxml import etree
import argparse
import glob


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('dir', type=str)

	args = parser.parse_args()

	file_list = glob.glob('build/{}/*'.format(args.dir))

	root = etree.Element('testsuite', tests='{}'.format(len(file_list)))

	for f in file_list:

		test_node = etree.Element('testcase', classname=args.dir, name=f)

		try:
			subprocess.check_output([f])
		except:
			failure_node = etree.Element('failure')
			failure_node.text = 'Generic failure text.'
			test_node.append(failure_node)

		root.append(test_node)


	print(etree.tostring(root, pretty_print=True))
