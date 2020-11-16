### MODULES
import unittest
import warnings
from RealtimeStock import sinaQuote, futuQuote, tigerQuote, xueqiuQuote, tencentQuote, getQuote

### TEST

class QuoteTest(unittest.TestCase):
	def setUp(self):
		warnings.simplefilter("ignore", ResourceWarning)

	def tearDown(self):
		warnings.simplefilter("default", ResourceWarning)

	def testSinaQuote(self):
		result2 = sinaQuote('hk','07200')
		result3 = sinaQuote('sh','600320')
		result4 = sinaQuote('sz','002122')

		self.assertEqual(result2['code'],'07200')
		self.assertEqual(result3['code'],'600320')
		self.assertEqual(result4['code'],'002122')

		self.assertEqual(result2['name'],'ＦＬ二南方恒指')
		self.assertEqual(result3['name'],'振华重工')
		self.assertEqual(result4['name'],'*ST天马')

		print('Sina quote with correct response')

	def testFutuQuote(self):
		result1 = futuQuote('us','VRSK')
		result2 = futuQuote('hk','07200')
		result3 = futuQuote('sh','600320')
		result4 = futuQuote('sz','002122')

		self.assertEqual(result1['code'],'VRSK')
		self.assertEqual(result2['code'],'07200')
		self.assertEqual(result3['code'],'600320')
		self.assertEqual(result4['code'],'002122')

		self.assertEqual(result1['name'],'Verisk Analytics')
		self.assertEqual(result2['name'],'南方两倍看多恒指')
		self.assertEqual(result3['name'],'振华重工')
		self.assertEqual(result4['name'],'*ST天马')

		print('Futu quote with correct response')

	def testTigerQuote(self):
		result1 = tigerQuote('us','VRSK')
		result2 = tigerQuote('hk','07200')
		result3 = tigerQuote('sh','600320')
		result4 = tigerQuote('sz','002122')

		self.assertEqual(result1['code'],'VRSK')
		self.assertEqual(result2['code'],'07200')
		self.assertEqual(result3['code'],'600320')
		self.assertEqual(result4['code'],'002122')

		self.assertEqual(result1['name'],'Verisk Analytics')
		self.assertEqual(result2['name'],'FL二南方恒指')
		self.assertEqual(result3['name'],'振华重工')
		self.assertEqual(result4['name'],'*ST天马')

		print('Tiger quote with correct response')

	def testXueqiuQuote(self):
		result1 = xueqiuQuote('us','VRSK')
		result2 = xueqiuQuote('hk','07200')
		result3 = xueqiuQuote('sh','600320')
		result4 = xueqiuQuote('sz','002122')

		self.assertEqual(result1['code'],'VRSK')
		self.assertEqual(result2['code'],'07200')
		self.assertEqual(result3['code'],'600320')
		self.assertEqual(result4['code'],'002122')

		self.assertEqual(result1['name'],'Verisk分析')
		self.assertEqual(result2['name'],'FL 二南方恒指')
		self.assertEqual(result3['name'],'振华重工')
		self.assertEqual(result4['name'],'*ST天马')

		print('Xueqiu quote with correct response')

	def  testTencentQuote(self):
		result1 = tencentQuote('us','VRSK')
		result2 = tencentQuote('hk','07200')
		result3 = tencentQuote('sh','600320')
		result4 = tencentQuote('sz','002122')

		self.assertEqual(result1['code'],'VRSK')
		self.assertEqual(result2['code'],'07200')
		self.assertEqual(result3['code'],'600320')
		self.assertEqual(result4['code'],'002122')

		self.assertEqual(result1['name'],'Verisk Analytics Inc')
		self.assertEqual(result2['name'],'FL二南方恒指')
		self.assertEqual(result3['name'],'振华重工')
		self.assertEqual(result4['name'],'*ST天马')

		print('Tencent quote with correct response')


	def testGetQuote(self):
		result1 = tencentQuote('us','VRSK')
		result2 = tencentQuote('hk','07200')
		result3 = tencentQuote('sh','600320')
		result4 = tencentQuote('sz','002122')

		self.assertEqual(result1['code'],'VRSK')
		self.assertEqual(result2['code'],'07200')
		self.assertEqual(result3['code'],'600320')
		self.assertEqual(result4['code'],'002122')

		print('Get quote with correct response')

### MAIN

if __name__ == '__main__':
	unittest.main()
