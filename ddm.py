import scipy as sp
import scipy.stats as stats
import matplotlib.pyplot as plt

'''
Estimates stock price based on n-period model.
Input: 	r = discount rate
		g = long term dividend growth rate
		d = dividend vector n + 1
Output: Stock price for n-period model
'''
def pvValueNperiodModel(r,g,d):
	# Gordon Growth Model
 	n = len(d) - 1
	pv = sp.npv(r, d[:-1]) * (1 + r)
	sellingPrice = d[n] / (r - g)
	pv += sp.pv(r,n,0,-sellingPrice)
 	return pv

'''
Histogram for normal distribution
Input:	m = specified mean
		std = standard deviation
		n = size of input
Output: Histogram for a set of random values drawn from a normal distribution
		with specified mean and standard deviation
'''
def generateNormalHistogram(m, std, n):
	sp.random.seed(12345)
	x = sp.random.normal(m,std,n)
	plt.hist(x, 15, normed=True)
	plt.title("Histogram for random numbers drawn from a normal distribution")
	plt.annotate("mean="+str(m),xy=(0.6,1.5))
	plt.annotate("std="+str(std),xy=(0.6,1.4))
	plt.show()

# Main Function
if __name__ == "__main__":
	# Example inputs:
	# r = 0.182
	# g = 0.03
	# d = [1.8,2.07,2.277,2.48193,2.68,2.7877]

	# mean = 0.1
	# std = 0.2
	# n = 1000
	
	print("\n1. Calculate the price of stock using Dividend Discount Model")
	print("2. Generate histogram for set of random values\n")
	option = raw_input("Select option: ")
	if option == '1':
		print("\n--Calculating the price of stock using the Dividend Discount Model--\n")
		r = float(raw_input("Enter the discount rate: "))
		g = float(raw_input("Enter the long term dividend growth rate: "))
		d = []

		while True:
			entry = raw_input("Enter a dividend (q to quit): ")
			if entry.lower() == 'q':
				break
			d.append(float(entry))

		print "\nEstimated stock price: {}\n".format(pvValueNperiodModel(r,g,d))

	else:
		print("\n--Generate the histogram--\n")
		mean = float(raw_input("Enter the mean: "))
		std = float(raw_input("Enter the standard deviation: "))
		n = int(raw_input("Enter the number of variables: "))

		generateNormalHistogram(mean, std, n)
