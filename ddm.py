import scipy as sp
import scipy.stats as stats
import matplotlib.pyplot as plt

'''
Estimates stock price based on n-period model.
Input: 	r = discount rate
		g = long term dividend growth rate
		d = dividend per share
Output: Stock price for n-period model
'''
def nPeriodDDM(r,g,d):
	n = len(d) - 1
	pv = sp.npv(r, d[:-1]) * (1 + r)
	sellingPrice = d[n] / (r - g)
	pv += sp.pv(r,n,0,-sellingPrice)
	return pv

'''
Estimates stock price using Donaldson-Kamstra Gordon Growth Model
Input: 	d = dividend per share
		n = number of periods
Output: Stock price for n-period model
'''
def nPeriodGGM(d,n):
	list_growth_rate = sp.random.standard_normal(n)
	list_discount_rate = sp.random.standard_normal(n)
	print(list_discount_rate)
	print(list_growth_rate)
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
	
	print("\n1. Estimate the price of stock using Dividend Discount Model")
	print("2. Estimate the price of stock using Donaldson-Kamstra Gordon Growth Model")
	print("3. Generate histogram for set of random values\n")
	option = input("Select option: ")

	# Dividend Discount Model
	if option == '1':
		print("\n--Dividend Discount Model--\n")
		r = float(input("Enter the discount rate: "))
		g = float(input("Enter the long term dividend growth rate: "))
		d = []

		while True:
			entry = input("Enter a dividend (q to quit): ")
			if entry.lower() == 'q':
				break
			d.append(float(entry))

		print ("\nEstimated stock price: {}\n".format(nPeriodDDM(r,g,d)))

	# Donaldson-Kamstra Gordon Growth Model
	elif option == '2':
		print("\n--Donaldson-Kamstra Gordon Growth Model--\n")
		d = float(input("Enter the initial dividend per share: "))
		n = int(input("Enter the number of periods: "))
		nPeriodGGM(d,n)

	# Histogram
	else:
		print("\n--Generate the histogram--\n")
		mean = float(input("Enter the mean: "))
		std = float(input("Enter the standard deviation: "))
		n = int(input("Enter the number of variables: "))

		generateNormalHistogram(mean, std, n)
