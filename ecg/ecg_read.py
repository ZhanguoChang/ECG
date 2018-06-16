import codecs
import os
import scipy.io as sio
#os.listdir(r'F:\ecg_data')
ecg=sio.loadmat(r'G:\ecg\ECG数据\2013\2013.mat')
ecg_name=ecg['name_list']
ecg_name_str=[]
for i in ecg_name[0]:
    ecg_name_str.append(''.join(i))
patient_file=open(r'C:\Users\Dell\Desktop\patient\2017.txt','w')
for current_path, subfolders, filesname in os.walk(r'G:\ecg\ECG数据\2013'):
    for file in filesname:
        pdf=file+'.pdf'
        if pdf in filesname:
            if file in ecg_name_str:
                print(pdf,file)
                f=open(os.path.join(current_path,file),'rb')
                data=f.readlines()
                try:
                    declare=data[-2].decode('gb2312')
                except:
                    continue
                    #n
                    # declare = data[-1].decode('gb2312')
                file_d=file+'  诊断说明：'+declare
                patient_file.write(file_d)
                patient_file.write('\r\n')
                f.close()
patient_file.close()

    #print(subfolders,filesname)

'''
#f=open(r'F:\ecg\860956_1.7','rb')
f=open(r'G:\ecg\ECG数据\2013\1\6058_5972.7','rb')
data=f.readlines()
#u=f.read().decode('gb2312')
declare=data[-1].decode('gb2312')
print(declare)
f.close()
'''






