# TODO #

	Data = Data.astype(float)
	Data = Data[3:17,:].T
	lengSample = 200
	numberChanels = Data.shape[1]
	lengSignal = lengSample	
	ox = [x for x in range(lengSignal)]

	listAx = []
	listLine = []
	fig, (ax1, ax2, ax3) = plt.subplots(numberChanels//4,1)
	listAx = [ax1, ax2, ax3]
	for ch, ax in enumerate(listAx):
		line, = ax.plot(ox, Data.T[ch][:200], lw=2)
		ax.axes.xaxis.set_visible(False)
		ax.axes.yaxis.set_visible(False)
		# ax.axes.set_autoscale_on(True)
		# ax.axes.autoscale_view(True,True,True)
		listLine.append(line)

	# for x in range(leng):
	# 	plt.clf()
	# 	newData = np.copy(Data)
	# 	newData = newData[x : x+lengSample,:]
	# 	ims = getImg(newData)
	writergif = animation.PillowWriter(fps=30) 
	anim = FuncAnimation(fig, animate,
	                               frames=1000, interval=20, blit=True)

	anim.save("test.gif", writer=writergif)
