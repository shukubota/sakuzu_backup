#coding:utf-8
import sys
sys.path.append('/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu09/')

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from function import *
import os.path
import matplotlib.cm as cm
from mpl_toolkits.basemap import maskoceans


#####################
#fileのサイズ
#########################
lon1=70.
lon2=160.
lat1=-15.
lat2=30.
grid=0.1

##################
grid2=0.75

##############################
#かきたいえのsize
#########################
#smatra
#lon3=94.
#lon4=107
#lat3=-7
#lat4=6

#maritime
#lon3=93.
#lon4=155.
#lat3=-12.
#lat4=8.

#lon3=70.
#lon4=160.
#lat3=-15.
#lat4=30.


#test
#lon3=90.
#lon4=160.
#lat3=1.5
#lat4=1.501

#peatman
#lon3=100.
#lon4=120.
#lat3=-7.
#lat4=10.
#savefile="peatman"
#t=1.96

#tian
lon3=100.
lon4=150.
lat3=-15.
lat4=10.
t=1.96
savefile="tian"

#sui
#lon3=119.
#lon4=121.
#lat3=-11.
#lat4=-9.
#t=1.98
#savefile="sui"


#kamimera
#lon3=99.
#lon4=102.
#lat3=-2.
#lat4=3
#t=1.96
#savefile="kamimera"

#iroiro
#lon3=98.
#lon4=100.
#lat3=-10.
#lat4=-8.
#t=1.96
#savefile="iroiro"

##############################
#c or phi(c:1 phiZ:2)
#####################
which=1
local=7
windlevel=20
#[100,125,150,175,200,225,250,300,350,400,450,500,550,600,650,700,750,775,800,825,850,875,900,925,950,975,1000]
#20:850hpa
##################


nstart=int((lon3-lon1)/grid)
nend=int((lon4-lon1)/grid)
mstart=int((lat3-lat1)/grid)
mend=int((lat4-lat1)/grid)

#grid2にあわせたlon1をこえる最小のlon,lon1<lon1min,lon2min<=lon2
#PRとECWMFは格子の作り方が異なるので注意
#latは90 to -90の順になっているので注意
#地図で見て格子の上と左端は含まれていない

lon1min=int(lon1/grid2)*grid2+grid2
lon2min=int(lon2/grid2)*grid2
#lon1min<lon2min

lat2min=90.-(int((90.-lat2)/grid2)*grid2+grid2)
lat1min=90.-int((90.-lat1)/grid2)*grid2
print "lat1min:",lat1min

lon3min=int(lon3/grid2)*grid2+grid2
lon4min=int(lon4/grid2)*grid2
#lon1min<lon2min

lat4min=90.-(int((90.-lat4)/grid2)*grid2+grid2)
lat3min=90.-int((90.-lat3)/grid2)*grid2


nstart2=int((lon3min-lon1min)/grid2)
nend2=int((lon4min-lon1min)/grid2)
mstart2=int((lat2min-lat4min)/grid2)
mend2=int((lat2min-lat3min)/grid2)


#print "mstart:",mstart,"mend:",mend,"nstart:",nstart,"nend:",nend
#print "mstart2:",mstart2,"mend2:",mend2,"nstart2:",nstart2,"nend2:",nend2
lon=np.arange(lon1,lon2+grid,grid)
lat=np.arange(lat1,lat2+grid,grid)
lonp=np.arange(lon3,lon4+grid,grid)
latp=np.arange(lat3,lat4+grid,grid)

lonp2=np.arange(lon3min,lon4min+grid2,grid2)
latp2=np.arange(lat3min,lat4min+grid2,grid2)
#print "lonp2",np.shape(lonp2)
#print "latp2",np.shape(latp2)

msize,nsize=getsize(lon,lat)
mpsize,npsize=getsize(lonp,latp)

mpsize2,npsize2=getsize(lonp2,latp2)

print "msize:",msize,"nsize:",nsize
print "mpsize:",mpsize,"npsize:",npsize
print "len(lonp):",len(lonp),"len(latp):",len(latp)
#print len(lon),len(lat)
#print lon


ocean=np.zeros(8)
land=np.zeros(8)
oceanerr=np.zeros(8)
landerr=np.zeros(8)
ocean2=np.zeros(8)
land2=np.zeros(8)
ocean2err=np.zeros(8)
land2err=np.zeros(8)
ocean3=np.zeros(8)
land3=np.zeros(8)
ocean3err=np.zeros(8)
land3err=np.zeros(8)
ocean4=np.zeros(8)
land4=np.zeros(8)
ocean4err=np.zeros(8)
land4err=np.zeros(8)

ocean5=np.zeros(8)
land5=np.zeros(8)
ocean5err=np.zeros(8)
land5err=np.zeros(8)

ocean6=np.zeros(8)
land6=np.zeros(8)
ocean6err=np.zeros(8)
land6err=np.zeros(8)


for i in range(1,9):

  
	plotcp=np.zeros((npsize,mpsize))
	plotcp2=np.zeros((npsize,mpsize))
	plotcp3=np.zeros((npsize,mpsize))
	plotcp4=np.zeros((npsize,mpsize))
	plotcp5=np.zeros((npsize,mpsize))
	plotcp6=np.zeros((npsize,mpsize))
	plotu=np.zeros((npsize2,mpsize2))
	plotv=np.zeros((npsize2,mpsize2))

	if which==1:
		#plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu21/p1test/00.dat")
		


		plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu21/plotdata_wh04/c_ratio"+"%02d"%i+".dat",delimiter=",")


		plotdata2=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu21/plotdata_wh04/c"+"%02d"%i+".dat",delimiter=",")
		plotdata3=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu24/plotdata_wh04/dailyp"+"%02d"%i+".dat",delimiter=",")
		plotdata4=np.load("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu39/plotdata_0228/plotdata%02d.npy"%i)

		plotdata5=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu24/plotdata_stra/dailyp"+"%02d"%i+".dat",delimiter=",")

		plotdata6=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu24/plotdata_stra2/dailyp"+"%02d"%i+".dat",delimiter=",")


	elif which==2:
		plotdata=np.loadtxt("/home/kubotashu/kubota/labo/sakuzu/sakuzu/sakuzu21/plotdata_wh04/phi"+"%02d"%i+".dat",delimiter=",")
	else:
		print "error"
	print np.shape(plotdata)
   
   



	#################
	#CUT
	################
	plotcp=plotdata[mstart:mend+1,nstart:nend+1]
	plotcp2=plotdata2[mstart:mend+1,nstart:nend+1]
	plotcp3=plotdata3[mstart:mend+1,nstart:nend+1]
	plotcp4=plotdata4[mstart:mend+1,nstart:nend+1]
	plotcp5=plotdata5[mstart:mend+1,nstart:nend+1]
	plotcp6=plotdata6[mstart:mend+1,nstart:nend+1]


	if which==2:
		plotcp+=local
		plotcp[plotcp>23]-=24
	
	m = Basemap(projection='merc', llcrnrlat=lat3, urcrnrlat=lat4,llcrnrlon=lon3, urcrnrlon=lon4, resolution='l')
	#resolution l m h
	m.drawcoastlines(linewidth=1.5,color='black')
	m.drawparallels(np.arange(lat3,lat4,2.),labels=[True,False,False,True])    #緯線
	m.drawmeridians(np.arange(lon3-3,lon4,10.),labels=[False,True,False,True])	#経線


	X, Y = np.meshgrid(lonp,latp)
	x, y = m(X, Y)	

	###########################################################

	#fig=plt.figure()

	if which==1:
		var1=maskoceans(X,Y,plotcp)
		var2=maskoceans(X,Y,plotcp)
		var2.mask = ~var2.mask
		var3=maskoceans(X,Y,plotcp2)
		var4=maskoceans(X,Y,plotcp2)
		var4.mask = ~var4.mask
		var5=maskoceans(X,Y,plotcp3)
		var6=maskoceans(X,Y,plotcp3)
		var6.mask = ~var6.mask
		var7=maskoceans(X,Y,plotcp4)
		var8=maskoceans(X,Y,plotcp4)
		var8.mask = ~var8.mask	



		var9=maskoceans(X,Y,plotcp5)
		var10=maskoceans(X,Y,plotcp5)
		var10.mask = ~var10.mask	
		var11=maskoceans(X,Y,plotcp6)
		var12=maskoceans(X,Y,plotcp6)
		var12.mask = ~var12.mask		
		#print plotcp
		#print var
		a=m.contourf(x, y, plotcp,np.arange(0,101,10.))
		#a=m.contourf(x, y, plotcp,np.arange(-0.35,0.36,0.1),cmap=cm.seismic,extend="both")
		np.save("cov/diurnal%02d.npy"%i,plotcp)
		#print "test\n"
		#b=plt.colorbar(a,orientation="horizontal",shrink=0.8)
		#b.set_label("mm/h")
		m.colorbar()
		#print plotcp.mean()


		countvar1=0
		countvar2=0
		countvar3=0
		countvar4=0
		countvar5=0
		countvar6=0
		countvar7=0
		countvar8=0
		for l in range(0,len(var1)):
			for n in range(0,len(var1[0])):
				if var1[l,n]>=0.:
					countvar1+=1
				if var2[l,n]>=0.:
					countvar2+=1
		print countvar1,countvar2


#		for l in range(0,len(var3)):
#			for n in range(0,len(var3[0])):
#				if var3[l,n]>=0.:
#					countvar3+=1
#				if var4[l,n]>=0.:
#					countvar4+=1
#		print countvar3,countvar4
#
#
#
#		for l in range(0,len(var5)):
#			for n in range(0,len(var5[0])):
#				if var5[l,n]>=0.:
#					countvar5+=1
#				if var6[l,n]>=0.:
#					countvar6+=1
#		print countvar5,countvar6
#
#
#		for l in range(0,len(var7)):
#			for n in range(0,len(var7[0])):
#				if var7[l,n]>=0.:
#					countvar7+=1
#				if var8[l,n]>=0.:
#					countvar8+=1
#		print countvar7,countvar8

		ocean[i-1]=var2.mean()
		oceanerr[i-1]=t*np.std(var2,ddof=1)/np.sqrt(countvar2)
		land[i-1]=var1.mean()
		landerr[i-1]=t*np.std(var1,ddof=1)/np.sqrt(countvar1)
		ocean2[i-1]=var4.mean()
		ocean2err[i-1]=t*np.std(var4,ddof=1)/np.sqrt(countvar2)
		land2[i-1]=var3.mean()
		land2err[i-1]=t*np.std(var3,ddof=1)/np.sqrt(countvar1)
		ocean3[i-1]=var6.mean()
		ocean3err[i-1]=t*np.std(var6,ddof=1)/np.sqrt(countvar2)
		land3[i-1]=var5.mean()
		land3err[i-1]=t*np.std(var5,ddof=1)/np.sqrt(countvar1)
		ocean4[i-1]=var8.mean()
		ocean4err[i-1]=t*np.std(var8,ddof=1)/np.sqrt(countvar2)
		land4[i-1]=var7.mean()
		land4err[i-1]=t*np.std(var7,ddof=1)/np.sqrt(countvar1)
	

		ocean5[i-1]=var10.mean()
		ocean5err[i-1]=t*np.std(var10,ddof=1)/np.sqrt(countvar2)
		land5[i-1]=var9.mean()
		land5err[i-1]=t*np.std(var9,ddof=1)/np.sqrt(countvar1)
		ocean6[i-1]=var12.mean()
		ocean6err[i-1]=t*np.std(var12,ddof=1)/np.sqrt(countvar2)
		land6[i-1]=var11.mean()
		land6err[i-1]=t*np.std(var11,ddof=1)/np.sqrt(countvar1)





	else:
		a=m.contourf(x, y, plotcp,np.arange(0,25,1),cmap=cm.hsv)

		
		b=plt.colorbar(a,orientation="horizontal",shrink=0.8)
		b.set_label("LT(UTC+7)")

	if which==1.:
		output="figure_wh04/c_ratio/c_ratio_wh04"+"%02d"%i+".png"
		plt.title("Phase%d"%i)
		#plt.title("Amplitude of Diurnal Precipitation anomaly[Phase="+"%02d"%i+"] [mm/h]")
	 
	if which==2:
		output="figure_wh04/phi/phi_wh04"+"%02d"%i+".png"
		#plt.title("Phase of Diurnal Precipitation [Phase="+"%02d"%i+"] LT(UTC+"+"%d"%local+")")
		plt.title("Phase%02d"%i)
	###########################################################
	#wind plot
	##########################
	

	X, Y = np.meshgrid(lonp2,latp2)
	x, y = m(X, Y)	
  
	if which==1:
		mabiki=3
		#q=m.quiver(x[::mabiki,::mabiki],y[::mabiki,::mabiki],plotu[::mabiki,::mabiki],plotv[::mabiki,::mabiki],scale=100,color="black",headwidth=5.)
		#qk = plt.quiverkey(q, 0.68, -0.26, 5, 'Wind 5 m/s', labelpos='W',color="black")
		#qk = plt.quiverkey(q, 1.09, -0.06, 5, '5 m/s', labelpos='W',color="black")
		#print "test\n"
	else:
		#q=m.quiver(x,y,plotu,plotv,scale=40)
		#qk = plt.quiverkey(q, 0.5, 0., 2, 'Wind Speed 2 m/s', labelpos='W',color="black")
		print "\n"

	
	plt.savefig(output,bbox_inches="tight")
	#print output
	#plt.show()
	


	plt.clf()
meandataaxis=[1,2,3,4,5,6,7,8]

fig,ax1=plt.subplots()
ax2=ax1.twinx()
#ax1.plot(meandataaxis,ocean,label="ratio on the ocean")
#ax1.errorbar(meandataaxis,ocean,yerr=oceanerr,capsize=10)
#ax1.plot(meandataaxis,land,label="ratio on the land")
#ax1.errorbar(meandataaxis,land,yerr=landerr,capsize=10)

ax1.plot(meandataaxis,ocean2,"r",label="diurnal on the ocean")
ax1.errorbar(meandataaxis,ocean2,yerr=ocean2err,ecolor="r",capsize=10)
ax1.plot(meandataaxis,land2,"b-",label="diurnal on the land")
ax1.errorbar(meandataaxis,land2,yerr=land2err,capsize=10)

ax1.plot(meandataaxis,ocean3,label="daily on the ocean")
ax1.errorbar(meandataaxis,ocean3,yerr=ocean3err,capsize=10)
ax1.plot(meandataaxis,land3,label="daily on the land")
ax1.errorbar(meandataaxis,land3,yerr=land3err,capsize=10)

ax2.plot(meandataaxis,ocean4,label="ir on the ocean")
ax2.errorbar(meandataaxis,ocean4,yerr=ocean4err,capsize=10)
ax2.plot(meandataaxis,land4,label="ir on the land")
ax2.errorbar(meandataaxis,land4,yerr=land4err,capsize=10)



#fig.xlabel("MJO phase")
#fig.ylabel("Ratio of diurnal precipitation to mean precipitation[%]")
#fig.legend(loc="right")
#ax1.ylim(30,50)
#file1=open("plotdata_wh04/"+savefile,"w")
#file1.write(ocean2)
#file1.write(ocean2err)
#file1.write(land2)
#file1.write(land2err)


#file1.close()



np.savetxt("plotdata_wh04/"+savefile+"/ocean.dat",ocean)
np.savetxt("plotdata_wh04/"+savefile+"/oceanerr.dat",oceanerr)
np.savetxt("plotdata_wh04/"+savefile+"/land.dat",land)
np.savetxt("plotdata_wh04/"+savefile+"/landerr.dat",landerr)


np.savetxt("plotdata_wh04/"+savefile+"/ocean2.dat",ocean2)
np.savetxt("plotdata_wh04/"+savefile+"/ocean2err.dat",ocean2err)
np.savetxt("plotdata_wh04/"+savefile+"/land2.dat",land2)
np.savetxt("plotdata_wh04/"+savefile+"/land2err.dat",land2err)

np.savetxt("plotdata_wh04/"+savefile+"/ocean3.dat",ocean3)
np.savetxt("plotdata_wh04/"+savefile+"/ocean3err.dat",ocean3err)
np.savetxt("plotdata_wh04/"+savefile+"/land3.dat",land3)
np.savetxt("plotdata_wh04/"+savefile+"/land3err.dat",land3err)

np.savetxt("plotdata_wh04/"+savefile+"/ocean4.dat",ocean4)
np.savetxt("plotdata_wh04/"+savefile+"/ocean4err.dat",ocean4err)
np.savetxt("plotdata_wh04/"+savefile+"/land4.dat",land4)
np.savetxt("plotdata_wh04/"+savefile+"/land4err.dat",land4err)


np.savetxt("plotdata_wh04/"+savefile+"/ocean5.dat",ocean5)
np.savetxt("plotdata_wh04/"+savefile+"/ocean5err.dat",ocean5err)
np.savetxt("plotdata_wh04/"+savefile+"/land5.dat",land5)
np.savetxt("plotdata_wh04/"+savefile+"/land5err.dat",land5err)

np.savetxt("plotdata_wh04/"+savefile+"/ocean6.dat",ocean6)
np.savetxt("plotdata_wh04/"+savefile+"/ocean6err.dat",ocean6err)
np.savetxt("plotdata_wh04/"+savefile+"/land6.dat",land6)
np.savetxt("plotdata_wh04/"+savefile+"/land6err.dat",land6err)



plt.savefig("figure_wh04/meandata.png",bbox_inches="tight")	
#os.system("convert -delay 80 -loop 0 figure_wh04/c/c*.png figure_wh04/c_wh04.gif")
#os.system("convert -delay 80 -loop 0 figure_wh04/phi/phi*.png figure_wh04/phi_wh04.gif")
