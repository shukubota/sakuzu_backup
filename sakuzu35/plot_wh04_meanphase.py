#coding:utf-8
#決定版

import sys
sys.path.append('/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu09/')

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from function import *
import os.path
import matplotlib.cm as cm

from matplotlib import dates as mdates
from matplotlib import ticker
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.ticker import *
from pylab import *
from netCDF4 import *
##################
#####################
#fileのサイズ
#########################
lon1=70.
lon2=160.
lat1=-15.
lat2=30.
grid=0.1

##############################
#かきたいえのsize
#########################
#hov,pyとあわせる
#lon3=96.
#lon4=101.
#lat3=-5.


#ng east
#lon3=142.
#lon4=144.
#lat3=-3.
#local=9
#dire="ng"


#sm east
#lon3=100.
#lon4=103.
#lat3=0.
#local=7
#dire="smeast"


#sm west
#lon3=93.
#lon4=96.
#lat3=4.
#local=7
#dire="smwest"

#brwest
lon3=116.
lon4=118.
lat3=6.
local=8
dire="brwest"


#breast
#lon3=115.
#lon4=119.
#lat3=-1.
#local=8
#dire="breast"


#mean
#lon3=90.
#lon4=130.
#lat3=-2.
#lat4=2.
#local=7
#dire="mean"

length=lon4-lon3

lat4=lat3+length



#leveldata=Dataset("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu34/ETOPO1_Bed_g_gmt4.grd")
#leveldata.close
#standard=0.
#lat=leveldata.variables["y"][:]
#lon=leveldata.variables['x'][:]
#levelline=leveldata.variables["z"][:]
#levelline[levelline<0.]=0.
#cols=np.where(lat<-0.1)
#lat=np.delete(lat,cols,0)
#levelline=np.delete(levelline,cols,0)
#cols=np.where(lat>0.1)
#levelline=np.delete(levelline,cols,0)
#lat=np.delete(lat,cols,0)
#cols=np.where(lon<lon3)
#levelline=np.delete(levelline,cols,1)
#lon=np.delete(lon,cols,0)
#cols=np.where(lon>lon4)
#levelline=np.delete(levelline,cols,1)
#lon=np.delete(lon,cols,0)

#levelline=levelline.mean(axis=0)
#levellinenum=np.size(levelline)

#lon=np.reshape(lon,((1,-1)))
#lon=lon[0]




nstart=int((lon3-lon1)/grid)
nend=int((lon4-lon1)/grid)
mstart=int((lat3-lat1)/grid)
mend=int((lat4-lat1)/grid)




lonp=np.arange(lon3,lon4+grid,grid)
latp=np.arange(lat3,lat4+grid,grid)


mpsize,npsize=getsize(lonp,latp)



houraxis=np.arange(0,25)
#houraxis=np.hstack((houraxis,houraxis))
#tatejiku



#plotfin=np.zeros((len(houraxis),mpsize))


for time in range(1,2):
	if time==1:
		title="Easterly regimes"
		#phaselist=[1,2,3,4,8]
		phaselist=np.arange(1,9,1)

	if time==2:
		title="Westerly regimes"
		phaselist=[5,6,7]

	#plotdata=np.loadtxt("plotdata/wh04/"+dire+"/hovphase1.dat",delimiter=",")
	plotdata=np.loadtxt("plotdata/wh04/"+dire+"/meanphase.dat",delimiter=",")
	#sizem,sizen=np.shape(plotdata)
	#plotdata=np.zeros((sizem,sizen))
	#count=0
	#for phase in range(1,9):
		#count+=1
		#plotdata2=np.zeros((2*npsize,mpsize))
	#	filename="plotdata/wh04/"+dire+"/hovphase"+"%d"%phase+".dat"
	#	plotdata+=np.loadtxt(filename,delimiter=",")
	#	print "plotdata",np.shape(plotdata)
	

	#plotdata=plotdata/8.
	X,Y=np.meshgrid(lonp,houraxis)
	

	print "x,y",len(lonp),len(houraxis)


	fig=plt.figure(figsize=(5,12))


	#fig.text(0.1,0.92,"Time series of coastal rainfall [phase=%d][mm/hr]"%phase,fontsize=15)
	#fig.text(0.4,0.92,title,fontsize=15)
	#plt.xlabel("Longitude [deg E]")
	#plt.ylabel("Local Time (UTC+7)")
	fig.text(0.05,0.6,"Local Time (UTC+%d)"%local,rotation=90)
	#fig.text(0.35,0.07,"Longitude [deg E]",rotation=0)
	fig.text(0.2,0.08,"West")
	fig.text(0.8,0.08,"East")
	#fig.text(0.4,0.08,"Longitude [deg E]")
	plt.subplots_adjust(left=None, bottom=None, right=None, top=None, hspace=0.0)


	#################
	#max,range
	##############

	max=0.50001
	range=0.05

	#####################

	#fig,(ax1,ax2)=plt.subplots(2,1,sharex=True)
	#ax1.contourf(X,Y,plotdata,np.arange(0.,max,range))

	test1=plt.subplot(211)
	cf=plt.contourf(X,Y,plotdata,np.arange(0.,max,range),extend="max")
	
	
	ax1=plt.gca()
	ax1.yaxis.set_major_locator(MultipleLocator(3))
	ax1.invert_yaxis()
	ax1.set_xticklabels([])
	#ax.xaxis.set_major_locator(mdates.AutoDateLocator(maxticks=0))

	cax=fig.add_axes([0.94,0.1,0.04,0.8])
	plt.colorbar(cf,cax)
	


	#plt.colorbar()

	plt.subplot(212)
	plt.contourf(X,Y,plotdata,np.arange(0.,max,range),extend="max")
	#plt.colorbar()	

	#fig.colorbar()
	#plt.locator_params(axis="y",tight=True,nbins=4)
		
	ax2=plt.gca()
	plt.yticks(np.arange(3,25,3))
	#ax2.yaxis.set_major_locator(MultipleLocator(6))
	ax2.invert_yaxis()
	ax2.set_xticklabels([])
	#plt.colorbar()
	
	#plt.subplot(313)
	#plt.fill_between(lon,levelline,color="black")
	#ax3=plt.gca()
	#ax3.set_yticklabels([0,200,400,600,800,1000,1200])
	
	#axs1.tick_params(labelbottom='off')
	#cax=fig.add_axes([0.9,0.05,0.6,0,015])
	#plt.colorbar(t1,cax,orientation="vertical")
	plt.savefig("figure/wh04_"+dire+"/"+dire+".png",bbox_inches="tight")
	plt.clf()	

  


#os.system("convert -delay 80 -loop 0 figure/wh04/*.png figure/hov_wh04.gif")

	



