'''
Created on 2017年8月29日

@author: Francis
'''

import time
start = time.clock()
import pandas as pd;
import numpy as np;
#数据导入
print ('开始导入数据');
yunwei = pd.read_table('serv_net_cz_201707.txt',delimiter='|',encoding='gb2312');
UE_P_DEC = pd.read_excel('D://12月2G终端和网络用户占比.xlsx','分省');
UE_C_DEC = pd.read_excel('D://12月2G终端和网络用户占比.xlsx','分地市');
print (type(yunwei));
end_1 = time.clock()
print ('数据导入成功，开始运行,本次数据导入时长为：',end_1-start,'s');
#联通234G终端占比
CUUE_P = yunwei.pivot_table(index='省分',columns='联通终端',values='出账用户数',aggfunc=np.sum);
CUUE_C = yunwei.pivot_table(index='本地网',columns='联通终端',values='出账用户数',aggfunc=np.sum);
CUUE_P.loc['全国']=CUUE_P.sum();#对全国求和
CUUE_P['合计']=CUUE_P.sum(axis=1);
CUUE_C['合计']=CUUE_C.sum(axis=1);
for c in CUUE_P.columns:         
    CUUE_P[''.join([c,'占比'])]=CUUE_P[c]/CUUE_P['合计'];
cof_P = CUUE_P['无法区分终端占比'];
CUUE_P.drop(labels=['合计占比','无法区分终端占比'], axis=1,inplace = True);
CUUE_P.insert(len(CUUE_P.columns), '无法区分终端占比', cof_P);
for c in CUUE_C.columns:         
    CUUE_C[''.join([c,'占比'])]=CUUE_C[c]/CUUE_C['合计'];  
cof_C = CUUE_C['无法区分终端占比'];
CUUE_C.drop(labels=['合计占比','无法区分终端占比'], axis=1,inplace = True);
CUUE_C.insert(len(CUUE_C.columns), '无法区分终端占比', cof_C);
print ('完成‘联通234G终端占比’，1/18');
#234G网络用户占比
NETUE_P = yunwei.pivot_table(index='省分',columns='网络类型',values='出账用户数',aggfunc=np.sum);
NETUE_C = yunwei.pivot_table(index='本地网',columns='网络类型',values='出账用户数',aggfunc=np.sum);
NETUE_P.loc['全国']=NETUE_P.sum();
NETUE_P['合计']=NETUE_P.sum(axis=1);
NETUE_C['合计']=NETUE_C.sum(axis=1);
for c in NETUE_P.columns:         
    NETUE_P[''.join([c,'用户占比'])]=NETUE_P[c]/NETUE_P['合计'];
NETUE_P.drop(labels=['合计用户占比'], axis=1,inplace = True);
for c in NETUE_C.columns:         
    NETUE_C[''.join([c,'用户占比'])]=NETUE_C[c]/NETUE_C['合计'];
NETUE_C.drop(labels=['合计用户占比'], axis=1,inplace = True);
print ('完成‘234G网络用户占比’，2/18');
#2G网络用户分析
TWGUE_CLASSIFY_P = yunwei[yunwei['网络类型']=='使用2G网络'].pivot_table(index='省分',columns='定制终端',values='出账用户数',aggfunc=np.sum);
TWGUE_CLASSIFY_C = yunwei[yunwei['网络类型']=='使用2G网络'].pivot_table(index='本地网',columns='定制终端',values='出账用户数',aggfunc=np.sum);
TWGUE_CLASSIFY_P.loc['全国']=TWGUE_CLASSIFY_P.sum();
TWGUE_CLASSIFY_P['合计']=TWGUE_CLASSIFY_P.sum(axis=1);
TWGUE_CLASSIFY_C['合计']=TWGUE_CLASSIFY_C.sum(axis=1);
for c in TWGUE_CLASSIFY_P.columns:         
    TWGUE_CLASSIFY_P[''.join([c,'占比'])]=TWGUE_CLASSIFY_P[c]/TWGUE_CLASSIFY_P['合计'];
TWGUE_CLASSIFY_P.drop(labels=['合计占比'], axis=1,inplace = True);
for c in TWGUE_CLASSIFY_C.columns:         
    TWGUE_CLASSIFY_C[''.join([c,'占比'])]=TWGUE_CLASSIFY_C[c]/TWGUE_CLASSIFY_C['合计']; 
TWGUE_CLASSIFY_C.drop(labels=['合计占比'], axis=1,inplace = True);
print ('完成‘2G网络用户分析’，3/18');
#3G网络用户分析
THGUE_CLASSIFY_P = yunwei[yunwei['网络类型']=='使用3G网络'].pivot_table(index='省分',columns='定制终端',values='出账用户数',aggfunc=np.sum);
THGUE_CLASSIFY_C = yunwei[yunwei['网络类型']=='使用3G网络'].pivot_table(index='本地网',columns='定制终端',values='出账用户数',aggfunc=np.sum);
THGUE_CLASSIFY_P.loc['全国']=THGUE_CLASSIFY_P.sum();
THGUE_CLASSIFY_P['合计']=THGUE_CLASSIFY_P.sum(axis=1);
THGUE_CLASSIFY_C['合计']=THGUE_CLASSIFY_C.sum(axis=1);
for c in THGUE_CLASSIFY_P.columns:         
    THGUE_CLASSIFY_P[''.join([c,'占比'])]=THGUE_CLASSIFY_P[c]/THGUE_CLASSIFY_P['合计'];
THGUE_CLASSIFY_P.drop(labels=['合计占比'], axis=1,inplace = True);
for c in THGUE_CLASSIFY_C.columns:         
    THGUE_CLASSIFY_C[''.join([c,'占比'])]=THGUE_CLASSIFY_C[c]/THGUE_CLASSIFY_C['合计'];
THGUE_CLASSIFY_C.drop(labels=['合计占比'], axis=1,inplace = True);
print ('完成‘3G网络用户分析’，4/18');
#234G网络收入占比
NETUE_REV_P = yunwei.pivot_table(index='省分',columns='网络类型',values='出账收入',aggfunc=np.sum);
NETUE_REV_C = yunwei.pivot_table(index='本地网',columns='网络类型',values='出账收入',aggfunc=np.sum);
NETUE_REV_P.loc['全国']=NETUE_REV_P.sum();
NETUE_REV_P['合计']=NETUE_REV_P.sum(axis=1);
NETUE_REV_C['合计']=NETUE_REV_C.sum(axis=1);
for c in NETUE_REV_P.columns:         
    NETUE_REV_P[''.join([c,'收入占比'])]=NETUE_REV_P[c]/NETUE_REV_P['合计'];    
NETUE_REV_P.drop(labels=['合计收入占比'], axis=1,inplace = True);
for c in NETUE_REV_C.columns:         
    NETUE_REV_C[''.join([c,'收入占比'])]=NETUE_REV_C[c]/NETUE_REV_C['合计'];
NETUE_REV_C.drop(labels=['合计收入占比'], axis=1,inplace = True);
print ('完成‘234G网络收入占比’，5/18');
#234G网络用户ARPU值
NETUE_ARPU_P = pd.DataFrame();
NETUE_ARPU_C = pd.DataFrame();
NETUE_ARPU_P['省分']=NETUE_REV_P.index;
NETUE_ARPU_P=NETUE_ARPU_P.set_index(['省分']);
NETUE_ARPU_C['本地网']=NETUE_REV_C.index;
NETUE_ARPU_C=NETUE_ARPU_C.set_index(['本地网']);
NETUE_ARPU_P['2G网络用户ARPU值']=NETUE_REV_P['使用2G网络']/NETUE_P['使用2G网络'];
NETUE_ARPU_C['2G网络用户ARPU值']=NETUE_REV_C['使用2G网络']/NETUE_C['使用2G网络'];
NETUE_ARPU_P['3G网络用户ARPU值']=NETUE_REV_P['使用3G网络']/NETUE_P['使用3G网络'];
NETUE_ARPU_C['3G网络用户ARPU值']=NETUE_REV_C['使用3G网络']/NETUE_C['使用3G网络'];
NETUE_ARPU_P['4G网络用户ARPU值']=NETUE_REV_P['使用4G网络']/NETUE_P['使用4G网络'];
NETUE_ARPU_C['4G网络用户ARPU值']=NETUE_REV_C['使用4G网络']/NETUE_C['使用4G网络'];
NETUE_ARPU_P['无法区分网络用户ARPU值']=NETUE_REV_P['无法区分网络']/NETUE_P['无法区分网络'];
NETUE_ARPU_C['无法区分网络用户ARPU值']=NETUE_REV_C['无法区分网络']/NETUE_C['无法区分网络'];
NETUE_ARPU_P['总体ARPU值']=NETUE_REV_P['合计']/NETUE_P['合计'];
NETUE_ARPU_C['总体ARPU值']=NETUE_REV_C['合计']/NETUE_C['合计'];
print ('完成‘234G网络用户ARPU值’，6/18');
#2G网络用户高ARPU值占比
TWGUE_ARPU_INTERVAL_P = yunwei[yunwei['网络类型']=='使用2G网络'].pivot_table(index='省分',columns='收入区间',values='出账用户数',aggfunc=np.sum);
TWGUE_ARPU_INTERVAL_C = yunwei[yunwei['网络类型']=='使用2G网络'].pivot_table(index='本地网',columns='收入区间',values='出账用户数',aggfunc=np.sum);
TWGUE_ARPU_INTERVAL_P.loc['全国']=TWGUE_ARPU_INTERVAL_P.sum();
TWGUE_ARPU_INTERVAL_P['合计']=TWGUE_ARPU_INTERVAL_P.sum(axis=1);
TWGUE_ARPU_INTERVAL_C['合计']=TWGUE_ARPU_INTERVAL_C.sum(axis=1);
for c in TWGUE_ARPU_INTERVAL_P.columns:         
    TWGUE_ARPU_INTERVAL_P[''.join([c,'占比'])]=TWGUE_ARPU_INTERVAL_P[c]/TWGUE_ARPU_INTERVAL_P['合计'];
TWGUE_ARPU_INTERVAL_P.drop(labels=['合计占比'], axis=1,inplace = True);
for c in TWGUE_ARPU_INTERVAL_C.columns:         
    TWGUE_ARPU_INTERVAL_C[''.join([c,'占比'])]=TWGUE_ARPU_INTERVAL_C[c]/TWGUE_ARPU_INTERVAL_C['合计'];
TWGUE_ARPU_INTERVAL_C.drop(labels=['合计占比'], axis=1,inplace = True);
TWGUE_ARPU_INTERVAL_P['高ARPU值2G网络用户占比（大于30元）']=TWGUE_ARPU_INTERVAL_P[['[30,35)元占比','[35,40)元占比','[40,45)元占比',\
'[45,50)元占比','[50,60)元占比','[60,70)元占比','[70,80)元占比','[80,90)元占比','[90,100)元占比','100元以上占比']].sum(axis=1);
TWGUE_ARPU_INTERVAL_C['高ARPU值2G网络用户占比（大于30元）']=TWGUE_ARPU_INTERVAL_C[['[30,35)元占比','[35,40)元占比','[40,45)元占比',\
'[45,50)元占比','[50,60)元占比','[60,70)元占比','[70,80)元占比','[80,90)元占比','[90,100)元占比','100元以上占比']].sum(axis=1);
print ('完成‘2G网络用户高ARPU值占比’，7/18');
#234G网络用户MOU值
NETUE_TALKLEN_P = yunwei.pivot_table(index='省分',columns='网络类型',values='计费时长',aggfunc=np.sum);
NETUE_TALKLEN_C = yunwei.pivot_table(index='本地网',columns='网络类型',values='计费时长',aggfunc=np.sum);
NETUE_TALKLEN_P.loc['全国']=NETUE_TALKLEN_P.sum();
NETUE_TALKLEN_P['合计']=NETUE_TALKLEN_P.sum(axis=1);
NETUE_TALKLEN_C['合计']=NETUE_TALKLEN_C.sum(axis=1);
for c in NETUE_TALKLEN_P.columns:         
    NETUE_TALKLEN_P[''.join([c,'通话时长占比'])]=NETUE_TALKLEN_P[c]/NETUE_TALKLEN_P['合计'];
NETUE_TALKLEN_P.drop(labels=['合计通话时长占比'], axis=1,inplace = True);
for c in NETUE_TALKLEN_C.columns:         
    NETUE_TALKLEN_C[''.join([c,'通话时长占比'])]=NETUE_TALKLEN_C[c]/NETUE_TALKLEN_C['合计'];
NETUE_TALKLEN_C.drop(labels=['合计通话时长占比'], axis=1,inplace = True);
NETUE_MOU_P = pd.DataFrame();
NETUE_MOU_C = pd.DataFrame();
NETUE_MOU_P['省分']=NETUE_P.index;
NETUE_MOU_P=NETUE_MOU_P.set_index(['省分']);
NETUE_MOU_C['本地网']=NETUE_REV_C.index;
NETUE_MOU_C=NETUE_MOU_C.set_index(['本地网']);
NETUE_MOU_P['2G网络用户MOU值']=NETUE_TALKLEN_P['使用2G网络']/NETUE_P['使用2G网络'];
NETUE_MOU_C['2G网络用户MOU值']=NETUE_TALKLEN_C['使用2G网络']/NETUE_C['使用2G网络'];
NETUE_MOU_P['3G网络用户MOU值']=NETUE_TALKLEN_P['使用3G网络']/NETUE_P['使用3G网络'];
NETUE_MOU_C['3G网络用户MOU值']=NETUE_TALKLEN_C['使用3G网络']/NETUE_C['使用3G网络'];
NETUE_MOU_P['4G网络用户MOU值']=NETUE_TALKLEN_P['使用4G网络']/NETUE_P['使用4G网络'];
NETUE_MOU_C['4G网络用户MOU值']=NETUE_TALKLEN_C['使用4G网络']/NETUE_C['使用4G网络'];
NETUE_MOU_P['无法区分网络用户MOU值']=NETUE_TALKLEN_P['无法区分网络']/NETUE_P['无法区分网络'];
NETUE_MOU_C['无法区分网络用户MOU值']=NETUE_TALKLEN_C['无法区分网络']/NETUE_C['无法区分网络'];
NETUE_MOU_P['总体MOU值']=NETUE_TALKLEN_P['合计']/NETUE_P['合计'];
NETUE_MOU_C['总体MOU值']=NETUE_TALKLEN_C['合计']/NETUE_C['合计'];
print ('完成‘234G网络用户MOU值’，8/18');
#2G网络用户高MOU值占比
TWGUE_MOU_INTERVAL_P = yunwei[yunwei['网络类型']=='使用2G网络'].pivot_table(index='省分',columns='当月累计通话时长区间',values='出账用户数',aggfunc=np.sum)
TWGUE_MOU_INTERVAL_C = yunwei[yunwei['网络类型']=='使用2G网络'].pivot_table(index='本地网',columns='当月累计通话时长区间',values='出账用户数',aggfunc=np.sum)
TWGUE_MOU_INTERVAL_P.loc['全国']=TWGUE_MOU_INTERVAL_P.sum();
TWGUE_MOU_INTERVAL_P['合计']=TWGUE_MOU_INTERVAL_P.sum(axis=1);
TWGUE_MOU_INTERVAL_C['合计']=TWGUE_MOU_INTERVAL_C.sum(axis=1);
for c in TWGUE_MOU_INTERVAL_P.columns:         
    TWGUE_MOU_INTERVAL_P[''.join([c,'占比'])]=TWGUE_MOU_INTERVAL_P[c]/TWGUE_MOU_INTERVAL_P['合计'];
TWGUE_MOU_INTERVAL_P.drop(labels=['合计占比'], axis=1,inplace = True);
for c in TWGUE_MOU_INTERVAL_C.columns:         
    TWGUE_MOU_INTERVAL_C[''.join([c,'占比'])]=TWGUE_MOU_INTERVAL_C[c]/TWGUE_MOU_INTERVAL_C['合计'];
TWGUE_MOU_INTERVAL_C.drop(labels=['合计占比'], axis=1,inplace = True);
TWGUE_MOU_INTERVAL_P['高MOU值2G网络用户占比（大于250分钟）']=TWGUE_MOU_INTERVAL_P[['[250,300)分钟占比', '[300,400)分钟占比','[400,500)分钟占比'\
,'500分钟以上占比']].sum(axis=1);
TWGUE_MOU_INTERVAL_C['高MOU值2G网络用户占比（大于250分钟）']=TWGUE_MOU_INTERVAL_C[['[250,300)分钟占比', '[300,400)分钟占比','[400,500)分钟占比'\
,'500分钟以上占比']].sum(axis=1);
print ('完成‘2G网络用户高MOU值占比’，9/18');
#234G网络数据业务流量占比
NETWORK_DATA_P = yunwei.pivot_table(index='省分',values=['LTE网络上使用总流量','WCDMA网络上使用总流量',\
'GSM网络上使用总流量', '无法区分的流量'],aggfunc=np.sum);
NETWORK_DATA_C = yunwei.pivot_table(index='本地网',values=['LTE网络上使用总流量','WCDMA网络上使用总流量',\
'GSM网络上使用总流量', '无法区分的流量'],aggfunc=np.sum);
NETWORK_DATA_P.loc['全国']=NETWORK_DATA_P.sum();
NETWORK_DATA_P['合计']=NETWORK_DATA_P.sum(axis=1);
NETWORK_DATA_C['合计']=NETWORK_DATA_C.sum(axis=1);
for c in NETWORK_DATA_P.columns:         
    NETWORK_DATA_P[''.join([c,'占比'])]=NETWORK_DATA_P[c]/NETWORK_DATA_P['合计'];    
NETWORK_DATA_P.drop(labels=['合计占比'], axis=1,inplace = True);
for c in NETWORK_DATA_C.columns:         
    NETWORK_DATA_C[''.join([c,'占比'])]=NETWORK_DATA_C[c]/NETWORK_DATA_C['合计'];    
NETWORK_DATA_C.drop(labels=['合计占比'], axis=1,inplace = True);
print ('完成‘234G网络数据业务流量占比’，10/18');
#234G网络用户DOU值分布
NETUE_DATA_P = yunwei.pivot_table(index='省分',columns='网络类型',values='计费流量',aggfunc=np.sum);
NETUE_DATA_C = yunwei.pivot_table(index='本地网',columns='网络类型',values='计费流量',aggfunc=np.sum);
NETUE_DATA_P.loc['全国']=NETUE_DATA_P.sum();
NETUE_DATA_P['合计']=NETUE_DATA_P.sum(axis=1);
NETUE_DATA_C['合计']=NETUE_DATA_C.sum(axis=1);
for c in NETUE_DATA_P.columns:         
    NETUE_DATA_P[''.join([c,'流量占比'])]=NETUE_DATA_P[c]/NETUE_DATA_P['合计'];    
NETUE_DATA_P.drop(labels=['合计流量占比'], axis=1,inplace = True);
for c in NETUE_DATA_C.columns:         
    NETUE_DATA_C[''.join([c,'流量占比'])]=NETUE_DATA_C[c]/NETUE_DATA_C['合计'];    
NETUE_DATA_C.drop(labels=['合计流量占比'], axis=1,inplace = True);
NETUE_DOU_P = pd.DataFrame();
NETUE_DOU_C = pd.DataFrame();
NETUE_DOU_P['省分']=NETUE_P.index;
NETUE_DOU_P=NETUE_DOU_P.set_index(['省分']);
NETUE_DOU_C['本地网']=NETUE_REV_C.index;
NETUE_DOU_C=NETUE_DOU_C.set_index(['本地网']);
NETUE_DOU_P['2G网络用户DOU值']=NETUE_DATA_P['使用2G网络']/NETUE_P['使用2G网络'];
NETUE_DOU_C['2G网络用户DOU值']=NETUE_DATA_C['使用2G网络']/NETUE_C['使用2G网络'];
NETUE_DOU_P['3G网络用户DOU值']=NETUE_DATA_P['使用3G网络']/NETUE_P['使用3G网络'];
NETUE_DOU_C['3G网络用户DOU值']=NETUE_DATA_C['使用3G网络']/NETUE_C['使用3G网络'];
NETUE_DOU_P['4G网络用户DOU值']=NETUE_DATA_P['使用4G网络']/NETUE_P['使用4G网络'];
NETUE_DOU_C['4G网络用户DOU值']=NETUE_DATA_C['使用4G网络']/NETUE_C['使用4G网络'];
NETUE_DOU_P['无法区分网络用户DOU值']=NETUE_DATA_P['无法区分网络']/NETUE_P['无法区分网络'];
NETUE_DOU_C['无法区分网络用户DOU值']=NETUE_DATA_C['无法区分网络']/NETUE_C['无法区分网络'];
NETUE_DOU_P['总体DOU值']=NETUE_DATA_P['合计']/NETUE_P['合计'];
NETUE_DOU_C['总体DOU值']=NETUE_DATA_C['合计']/NETUE_C['合计'];
print ('完成‘234G网络用户DOU值分布’，11/18');
#2G网络用户高DOU值分布
TWGUE_DOU_INTERVAL_P = yunwei[yunwei['网络类型']=='使用2G网络'].pivot_table(index='省分',columns='流量区间',values='出账用户数',aggfunc=np.sum);
TWGUE_DOU_INTERVAL_C = yunwei[yunwei['网络类型']=='使用2G网络'].pivot_table(index='本地网',columns='流量区间',values='出账用户数',aggfunc=np.sum);
TWGUE_DOU_INTERVAL_P.loc['全国']=TWGUE_DOU_INTERVAL_P.sum();
TWGUE_DOU_INTERVAL_P['合计']=TWGUE_DOU_INTERVAL_P.sum(axis=1);
TWGUE_DOU_INTERVAL_C['合计']=TWGUE_DOU_INTERVAL_C.sum(axis=1);
for c in TWGUE_DOU_INTERVAL_P.columns:         
    TWGUE_DOU_INTERVAL_P[''.join([c,'占比'])]=TWGUE_DOU_INTERVAL_P[c]/TWGUE_DOU_INTERVAL_P['合计'];    
TWGUE_DOU_INTERVAL_P.drop(labels=['合计占比'], axis=1,inplace = True);
for c in TWGUE_DOU_INTERVAL_C.columns:         
    TWGUE_DOU_INTERVAL_C[''.join([c,'占比'])]=TWGUE_DOU_INTERVAL_C[c]/TWGUE_DOU_INTERVAL_C['合计']    ;
TWGUE_DOU_INTERVAL_C.drop(labels=['合计占比'], axis=1,inplace = True);
TWGUE_DOU_INTERVAL_P['高DOU值2G网络用户占比（大于100M）']=TWGUE_DOU_INTERVAL_P[['[100,500)M占比','[500,1024)M占比']].sum(axis=1);
TWGUE_DOU_INTERVAL_C['高DOU值2G网络用户占比（大于100M）']=TWGUE_DOU_INTERVAL_C[['[100,500)M占比','[500,1024)M占比']].sum(axis=1);
print ('完成‘2G网络用户高DOU值分布’，12/18');
#4G网络用户在各网产生的流量占比
NETWORK_DATA_LTEUE_P = yunwei[yunwei['网络类型']=='使用4G网络'].pivot_table(index='省分',values=['LTE网络上使用总流量','WCDMA网络上使用总流量',\
'GSM网络上使用总流量', '无法区分的流量'],aggfunc=np.sum);
NETWORK_DATA_LTEUE_C = yunwei[yunwei['网络类型']=='使用4G网络'].pivot_table(index='本地网',values=['LTE网络上使用总流量','WCDMA网络上使用总流量',\
'GSM网络上使用总流量', '无法区分的流量'],aggfunc=np.sum);
NETWORK_DATA_LTEUE_P.loc['全国']=NETWORK_DATA_LTEUE_P.sum();
NETWORK_DATA_LTEUE_P['合计']=NETWORK_DATA_LTEUE_P.sum(axis=1);
NETWORK_DATA_LTEUE_C['合计']=NETWORK_DATA_LTEUE_C.sum(axis=1);
for c in NETWORK_DATA_LTEUE_P.columns:         
    NETWORK_DATA_LTEUE_P[''.join([c,'占比'])]=NETWORK_DATA_LTEUE_P[c]/NETWORK_DATA_LTEUE_P['合计'];    
NETWORK_DATA_LTEUE_P.drop(labels=['合计占比'], axis=1,inplace = True);
for c in NETWORK_DATA_LTEUE_C.columns:         
    NETWORK_DATA_LTEUE_C[''.join([c,'占比'])]=NETWORK_DATA_LTEUE_C[c]/NETWORK_DATA_LTEUE_C['合计'];    
NETWORK_DATA_LTEUE_C.drop(labels=['合计占比'], axis=1,inplace = True);
print ('完成‘4G网络用户在各网产生的流量占比’，13/18');
#3G网络用户在各网产生的流量占比
NETWORK_DATA_WCDMAUE_P = yunwei[yunwei['网络类型']=='使用3G网络'].pivot_table(index='省分',values=['LTE网络上使用总流量','WCDMA网络上使用总流量',\
'GSM网络上使用总流量', '无法区分的流量'],aggfunc=np.sum);
NETWORK_DATA_WCDMAUE_C = yunwei[yunwei['网络类型']=='使用3G网络'].pivot_table(index='本地网',values=['LTE网络上使用总流量','WCDMA网络上使用总流量',\
'GSM网络上使用总流量', '无法区分的流量'],aggfunc=np.sum);
NETWORK_DATA_WCDMAUE_P.loc['全国']=NETWORK_DATA_WCDMAUE_P.sum();
NETWORK_DATA_WCDMAUE_P['合计']=NETWORK_DATA_WCDMAUE_P.sum(axis=1);
NETWORK_DATA_WCDMAUE_C['合计']=NETWORK_DATA_WCDMAUE_C.sum(axis=1);
for c in NETWORK_DATA_WCDMAUE_P.columns:         
    NETWORK_DATA_WCDMAUE_P[''.join([c,'占比'])]=NETWORK_DATA_WCDMAUE_P[c]/NETWORK_DATA_WCDMAUE_P['合计'];    
NETWORK_DATA_WCDMAUE_P.drop(labels=['合计占比'], axis=1,inplace = True)
for c in NETWORK_DATA_WCDMAUE_C.columns:         
    NETWORK_DATA_WCDMAUE_C[''.join([c,'占比'])]=NETWORK_DATA_WCDMAUE_C[c]/NETWORK_DATA_WCDMAUE_C['合计'];    
NETWORK_DATA_WCDMAUE_C.drop(labels=['合计占比'], axis=1,inplace = True);
print ('完成‘3G网络用户在各网产生的流量占比’，14/18');
#234G网络数据业务通话时长占比
NETWORK_TALK_P = yunwei.pivot_table(index='省分',values=['WCDMA网络上使用总时长','GSM网络上使用总时长','无法区分的时长'],aggfunc=np.sum);
NETWORK_TALK_C = yunwei.pivot_table(index='本地网',values=['WCDMA网络上使用总时长','GSM网络上使用总时长','无法区分的时长'],aggfunc=np.sum);
NETWORK_TALK_P.loc['全国']=NETWORK_TALK_P.sum();
NETWORK_TALK_P['合计']=NETWORK_TALK_P.sum(axis=1);
NETWORK_TALK_C['合计']=NETWORK_TALK_C.sum(axis=1);
for c in NETWORK_TALK_P.columns:         
    NETWORK_TALK_P[''.join([c,'占比'])]=NETWORK_TALK_P[c]/NETWORK_TALK_P['合计'];    
NETWORK_TALK_P.drop(labels=['合计占比'], axis=1,inplace = True);
for c in NETWORK_TALK_C.columns:         
    NETWORK_TALK_C[''.join([c,'占比'])]=NETWORK_TALK_C[c]/NETWORK_TALK_C['合计'];    
NETWORK_TALK_C.drop(labels=['合计占比'], axis=1,inplace = True);
print ('完成‘23G网络通话时长占比’，15/18');
#4G网络用户在各网产生的通话时长占比
NETWORK_TALK_LTEUE_P = yunwei[yunwei['网络类型']=='使用4G网络'].pivot_table(index='省分',values=['WCDMA网络上使用总时长','GSM网络上使用总时长','无法区分的时长'],aggfunc=np.sum);
NETWORK_TALK_LTEUE_C = yunwei[yunwei['网络类型']=='使用4G网络'].pivot_table(index='本地网',values=['WCDMA网络上使用总时长','GSM网络上使用总时长','无法区分的时长'],aggfunc=np.sum);
NETWORK_TALK_LTEUE_P.loc['全国']=NETWORK_TALK_LTEUE_P.sum();
NETWORK_TALK_LTEUE_P['合计']=NETWORK_TALK_LTEUE_P.sum(axis=1);
NETWORK_TALK_LTEUE_C['合计']=NETWORK_TALK_LTEUE_C.sum(axis=1);
for c in NETWORK_TALK_LTEUE_P.columns:         
    NETWORK_TALK_LTEUE_P[''.join([c,'占比'])]=NETWORK_TALK_LTEUE_P[c]/NETWORK_TALK_LTEUE_P['合计'];    
NETWORK_TALK_LTEUE_P.drop(labels=['合计占比'], axis=1,inplace = True);
for c in NETWORK_TALK_LTEUE_C.columns:         
    NETWORK_TALK_LTEUE_C[''.join([c,'占比'])]=NETWORK_TALK_LTEUE_C[c]/NETWORK_TALK_LTEUE_C['合计'];    
NETWORK_TALK_LTEUE_C.drop(labels=['合计占比'], axis=1,inplace = True);
print ('完成‘4G网络用户在各网产生的时长占比’，16/18');
#3G网络用户在各网产生的通话时长占比
NETWORK_TALK_WCDMAUE_P = yunwei[yunwei['网络类型']=='使用3G网络'].pivot_table(index='省分',values=['WCDMA网络上使用总时长','GSM网络上使用总时长', '无法区分的时长'],aggfunc=np.sum);
NETWORK_TALK_WCDMAUE_C = yunwei[yunwei['网络类型']=='使用3G网络'].pivot_table(index='本地网',values=['WCDMA网络上使用总时长','GSM网络上使用总时长', '无法区分的时长'],aggfunc=np.sum);
NETWORK_TALK_WCDMAUE_P.loc['全国']=NETWORK_TALK_WCDMAUE_P.sum();
NETWORK_TALK_WCDMAUE_P['合计']=NETWORK_TALK_WCDMAUE_P.sum(axis=1);
NETWORK_TALK_WCDMAUE_C['合计']=NETWORK_TALK_WCDMAUE_C.sum(axis=1);
for c in NETWORK_TALK_WCDMAUE_P.columns:         
    NETWORK_TALK_WCDMAUE_P[''.join([c,'占比'])]=NETWORK_TALK_WCDMAUE_P[c]/NETWORK_TALK_WCDMAUE_P['合计'];    
NETWORK_TALK_WCDMAUE_P.drop(labels=['合计占比'], axis=1,inplace = True)
for c in NETWORK_TALK_WCDMAUE_C.columns:         
    NETWORK_TALK_WCDMAUE_C[''.join([c,'占比'])]=NETWORK_TALK_WCDMAUE_C[c]/NETWORK_TALK_WCDMAUE_C['合计'];    
NETWORK_TALK_WCDMAUE_C.drop(labels=['合计占比'], axis=1,inplace = True);
print ('完成‘3G网络用户在各网产生的时长占比’，17/18');
#开始计算优比
#先把多张表进行合并
YBUE_P = UE_P_DEC.merge(CUUE_P,left_on='省分',right_on='省分',right_index=True,how='left')[['省分','12月联通2G终端占比','联通2G终端占比']];
YBUE_C = UE_C_DEC.merge(CUUE_C,left_on='本地网',right_on='本地网',right_index=True,how='left')[['本地网','省分','是否省会和计划单列市','12月联通2G终端占比','联通2G终端占比']];
YBNET_P = UE_P_DEC.merge(NETUE_P,left_on='省分',right_on='省分',right_index=True,how='left')[['省分','12月2G网络用户占比','使用2G网络用户占比']];
YBNET_C = UE_C_DEC.merge(NETUE_C,left_on='本地网',right_on='本地网',right_index=True,how='left')[['本地网','省分','是否省会和计划单列市','12月2G网络用户占比','使用2G网络用户占比']];
YBUE_P.sort_values('12月联通2G终端占比',inplace = True);
YBUE_C.sort_values('12月联通2G终端占比',inplace = True);
YBNET_P.sort_values('12月2G网络用户占比',inplace = True);
YBNET_C.sort_values('12月2G网络用户占比',inplace = True);
YBUE_P=YBUE_P[YBUE_P['省分']!='全国'];
YBNET_P=YBNET_P[YBNET_P['省分']!='全国'];
print('开始计算优比');
#计算YBUE_P的优比
YBUE_P['自改善值']=YBUE_P['12月联通2G终端占比']-YBUE_P['联通2G终端占比'];
YBUE_P['12月禀赋群均值']='';
YBUE_P['当月禀赋群均值']='';
YBUE_P['优比']='';
for c in np.arange(len(YBUE_P)):
    if ((c==0) or (c==1)):
        YBUE_P['12月禀赋群均值'].iloc[c] = YBUE_P['12月联通2G终端占比'].iloc[0];
        YBUE_P['当月禀赋群均值'].iloc[c] = YBUE_P['联通2G终端占比'].iloc[0];
        YBUE_P['优比'].iloc[c] = ((YBUE_P['当月禀赋群均值'].iloc[c]-YBUE_P['联通2G终端占比'].iloc[c]-\
                                     YBUE_P['12月禀赋群均值'].iloc[c]+YBUE_P['12月联通2G终端占比'].iloc[c])+\
                                    YBUE_P['自改善值'].iloc[c])/2;
    elif (c>1 and c<=4):
        YBUE_P['12月禀赋群均值'].iloc[c] = \
        (YBUE_P['12月联通2G终端占比'].iloc[c-1]*(6-c)+YBUE_P['12月联通2G终端占比'].iloc[0:(c-2+1)].sum(axis=0))/5;#iloc[m:n]指的是m行到（n-1）行
        YBUE_P['当月禀赋群均值'].iloc[c] = \
        (YBUE_P['联通2G终端占比'].iloc[c-1]*(6-c)+YBUE_P['联通2G终端占比'].iloc[0:(c-2+1)].sum(axis=0))/5;
        YBUE_P['优比'].iloc[c] = ((YBUE_P['当月禀赋群均值'].iloc[c]-YBUE_P['联通2G终端占比'].iloc[c]-\
                                    YBUE_P['12月禀赋群均值'].iloc[c]+YBUE_P['12月联通2G终端占比'].iloc[c])+YBUE_P['自改善值'].iloc[c])/2;
    else:
        YBUE_P['12月禀赋群均值'].iloc[c] = YBUE_P['12月联通2G终端占比'].iloc[(c-5):(c-1+1)].sum(axis=0)/5;
        YBUE_P['当月禀赋群均值'].iloc[c] = YBUE_P['联通2G终端占比'].iloc[(c-5):(c-1+1)].sum(axis=0)/5;
        YBUE_P['优比'].iloc[c] = YBUE_P['当月禀赋群均值'].iloc[c]-YBUE_P['联通2G终端占比'].iloc[c]-\
                                    YBUE_P['12月禀赋群均值'].iloc[c]+YBUE_P['12月联通2G终端占比'].iloc[c];
#计算YBUE_C的优比
YBUE_C['自改善值']=YBUE_C['12月联通2G终端占比']-YBUE_C['联通2G终端占比'];
YBUE_C['12月禀赋群均值']='';
YBUE_C['当月禀赋群均值']='';
YBUE_C['优比']='';
for c in np.arange(len(YBUE_C)):
    if ((c==0) or (c==1)):
        YBUE_C['12月禀赋群均值'].iloc[c] = YBUE_C['12月联通2G终端占比'].iloc[0];
        YBUE_C['当月禀赋群均值'].iloc[c] = YBUE_C['联通2G终端占比'].iloc[0];
        YBUE_C['优比'].iloc[c] = ((YBUE_C['当月禀赋群均值'].iloc[c]-YBUE_C['联通2G终端占比'].iloc[c]-\
                                     YBUE_C['12月禀赋群均值'].iloc[c]+YBUE_C['12月联通2G终端占比'].iloc[c])+\
                                    YBUE_C['自改善值'].iloc[c])/2;
    elif (c>1 and c<=4):
        YBUE_C['12月禀赋群均值'].iloc[c] = \
        (YBUE_C['12月联通2G终端占比'].iloc[c-1]*(6-c)+YBUE_C['12月联通2G终端占比'].iloc[0:(c-2+1)].sum(axis=0))/5;#iloc[m:n]指的是m行到（n-1）行
        YBUE_C['当月禀赋群均值'].iloc[c] = \
        (YBUE_C['联通2G终端占比'].iloc[c-1]*(6-c)+YBUE_C['联通2G终端占比'].iloc[0:(c-2+1)].sum(axis=0))/5;
        YBUE_C['优比'].iloc[c] = ((YBUE_C['当月禀赋群均值'].iloc[c]-YBUE_C['联通2G终端占比'].iloc[c]-\
                                    YBUE_C['12月禀赋群均值'].iloc[c]+YBUE_C['12月联通2G终端占比'].iloc[c])+YBUE_C['自改善值'].iloc[c])/2;
    else:
        YBUE_C['12月禀赋群均值'].iloc[c] = YBUE_C['12月联通2G终端占比'].iloc[(c-5):(c-1+1)].sum(axis=0)/5;
        YBUE_C['当月禀赋群均值'].iloc[c] = YBUE_C['联通2G终端占比'].iloc[(c-5):(c-1+1)].sum(axis=0)/5;
        YBUE_C['优比'].iloc[c] = YBUE_C['当月禀赋群均值'].iloc[c]-YBUE_C['联通2G终端占比'].iloc[c]-\
                                    YBUE_C['12月禀赋群均值'].iloc[c]+YBUE_C['12月联通2G终端占比'].iloc[c];
#计算YBNET_P的优比
YBNET_P['自改善值']=YBNET_P['12月2G网络用户占比']-YBNET_P['使用2G网络用户占比'];
YBNET_P['12月禀赋群均值']='';
YBNET_P['当月禀赋群均值']='';
YBNET_P['优比']='';
for c in np.arange(len(YBNET_P)):
    if ((c==0) or (c==1)):
        YBNET_P['12月禀赋群均值'].iloc[c] = YBNET_P['12月2G网络用户占比'].iloc[0];
        YBNET_P['当月禀赋群均值'].iloc[c] = YBNET_P['使用2G网络用户占比'].iloc[0];
        YBNET_P['优比'].iloc[c] = ((YBNET_P['当月禀赋群均值'].iloc[c]-YBNET_P['使用2G网络用户占比'].iloc[c]-\
                                     YBNET_P['12月禀赋群均值'].iloc[c]+YBNET_P['12月2G网络用户占比'].iloc[c])+\
                                    YBNET_P['自改善值'].iloc[c])/2;
    elif (c>1 and c<=4):
        YBNET_P['12月禀赋群均值'].iloc[c] = \
        (YBNET_P['12月2G网络用户占比'].iloc[c-1]*(6-c)+YBNET_P['12月2G网络用户占比'].iloc[0:(c-2+1)].sum(axis=0))/5;#iloc[m:n]指的是m行到（n-1）行
        YBNET_P['当月禀赋群均值'].iloc[c] = \
        (YBNET_P['使用2G网络用户占比'].iloc[c-1]*(6-c)+YBNET_P['使用2G网络用户占比'].iloc[0:(c-2+1)].sum(axis=0))/5;
        YBNET_P['优比'].iloc[c] = ((YBNET_P['当月禀赋群均值'].iloc[c]-YBNET_P['使用2G网络用户占比'].iloc[c]-\
                                    YBNET_P['12月禀赋群均值'].iloc[c]+YBNET_P['12月2G网络用户占比'].iloc[c])+YBNET_P['自改善值'].iloc[c])/2;
    else:
        YBNET_P['12月禀赋群均值'].iloc[c] = YBNET_P['12月2G网络用户占比'].iloc[(c-5):(c-1+1)].sum(axis=0)/5;
        YBNET_P['当月禀赋群均值'].iloc[c] = YBNET_P['使用2G网络用户占比'].iloc[(c-5):(c-1+1)].sum(axis=0)/5;
        YBNET_P['优比'].iloc[c] = YBNET_P['当月禀赋群均值'].iloc[c]-YBNET_P['使用2G网络用户占比'].iloc[c]-\
                                    YBNET_P['12月禀赋群均值'].iloc[c]+YBNET_P['12月2G网络用户占比'].iloc[c];
#计算YBNET_C的优比
YBNET_C['自改善值']=YBNET_C['12月2G网络用户占比']-YBNET_C['使用2G网络用户占比'];
YBNET_C['12月禀赋群均值']='';
YBNET_C['当月禀赋群均值']='';
YBNET_C['优比']='';
for c in np.arange(len(YBNET_C)):
    if ((c==0) or (c==1)):
        YBNET_C['12月禀赋群均值'].iloc[c] = YBNET_C['12月2G网络用户占比'].iloc[0];
        YBNET_C['当月禀赋群均值'].iloc[c] = YBNET_C['使用2G网络用户占比'].iloc[0];
        YBNET_C['优比'].iloc[c] = ((YBNET_C['当月禀赋群均值'].iloc[c]-YBNET_C['使用2G网络用户占比'].iloc[c]-\
                                     YBNET_C['12月禀赋群均值'].iloc[c]+YBNET_C['12月2G网络用户占比'].iloc[c])+\
                                    YBNET_C['自改善值'].iloc[c])/2;
    elif (c>1 and c<=4):
        YBNET_C['12月禀赋群均值'].iloc[c] = \
        (YBNET_C['12月2G网络用户占比'].iloc[c-1]*(6-c)+YBNET_C['12月2G网络用户占比'].iloc[0:(c-2+1)].sum(axis=0))/5;#iloc[m:n]指的是m行到（n-1）行
        YBNET_C['当月禀赋群均值'].iloc[c] = \
        (YBNET_C['使用2G网络用户占比'].iloc[c-1]*(6-c)+YBNET_C['使用2G网络用户占比'].iloc[0:(c-2+1)].sum(axis=0))/5;
        YBNET_C['优比'].iloc[c] = ((YBNET_C['当月禀赋群均值'].iloc[c]-YBNET_C['使用2G网络用户占比'].iloc[c]-\
                                    YBNET_C['12月禀赋群均值'].iloc[c]+YBNET_C['12月2G网络用户占比'].iloc[c])+YBNET_C['自改善值'].iloc[c])/2;
    else:
        YBNET_C['12月禀赋群均值'].iloc[c] = YBNET_C['12月2G网络用户占比'].iloc[(c-5):(c-1+1)].sum(axis=0)/5;
        YBNET_C['当月禀赋群均值'].iloc[c] = YBNET_C['使用2G网络用户占比'].iloc[(c-5):(c-1+1)].sum(axis=0)/5;
        YBNET_C['优比'].iloc[c] = YBNET_C['当月禀赋群均值'].iloc[c]-YBNET_C['使用2G网络用户占比'].iloc[c]-\
                                    YBNET_C['12月禀赋群均值'].iloc[c]+YBNET_C['12月2G网络用户占比'].iloc[c];
print ('优比计算完成！,18/18');
end_2 = time.clock()
#打印和输出
print('所有数据运行完成，开始保存数据,本次程序运行时长为：',end_2-end_1,'s');
# print(CUUE_P)
# print(CUUE_C)
# print(NETUE_P)
# print(NETUE_C)
# print(TWGUE_CLASSIFY_P)
# print(TWGUE_CLASSIFY_C)
# print(THGUE_CLASSIFY_P)
# print(THGUE_CLASSIFY_C)
# print(NETUE_REV_P)
# print(NETUE_REV_C)
# print(NETUE_ARPU_P)
# print(NETUE_ARPU_C)
# print(TWGUE_ARPU_INTERVAL_P)
# print(TWGUE_ARPU_INTERVAL_C)
# print(NETUE_MOU_P)
# print(NETUE_MOU_C)
# print(TWGUE_MOU_INTERVAL_P)
# print(TWGUE_MOU_INTERVAL_C)
# print(NETWORK_DATA_P)
# print(NETWORK_DATA_C)
# print(NETUE_DOU_P)
# print(NETUE_DOU_C)
# print(TWGUE_DOU_INTERVAL_P)
# print(TWGUE_DOU_INTERVAL_C)
# print(NETWORK_DATA_LTEUE_P)
# print(NETWORK_DATA_LTEUE_C)
# print(NETWORK_DATA_WCDMAUE_P)
# print(NETWORK_DATA_WCDMAUE_C)
# print(NETWORK_TALK_P)
# print(NETWORK_TALK_C)
# print(NETWORK_TALK_LTEUE_P)
# print(NETWORK_TALK_LTEUE_C)
# print(NETWORK_TALK_WCDMAUE_P)
# print(NETWORK_TALK_WCDMAUE_C)
# print (YBUE_P.head(10));
# print (YBUE_C.head(10));
# print (YBNET_P.head(10));
# print (YBNET_C.head(10));
#建立excel文件
writer_P = pd.ExcelWriter('D:/7月详表-分省.xlsx');
writer_C = pd.ExcelWriter('D:/7月详表-分地市.xlsx');
writer_YB_P = pd.ExcelWriter('D:/7月优比-分省.xlsx');
writer_YB_C = pd.ExcelWriter('D:/7月优比-分地市.xlsx');
#保存详表
CUUE_P.to_excel(writer_P,'联通234G终端数量占比');
CUUE_C.to_excel(writer_C,'联通234G终端数量占比');
NETUE_P.to_excel(writer_P,'234G网络用户数量占比');
NETUE_C.to_excel(writer_C,'234G网络用户数量占比');
TWGUE_CLASSIFY_P.to_excel(writer_P,'2G网络用户分析');
TWGUE_CLASSIFY_C.to_excel(writer_C,'2G网络用户分析');
THGUE_CLASSIFY_P.to_excel(writer_P,'3G网络用户分析');
THGUE_CLASSIFY_C.to_excel(writer_C,'3G网络用户分析');
NETUE_REV_P.to_excel(writer_P,'234G网络用户收入占比');
NETUE_REV_C.to_excel(writer_C,'234G网络用户收入占比');
NETUE_ARPU_P.to_excel(writer_P,'234G网络用户ARPU值');
NETUE_ARPU_C.to_excel(writer_C,'234G网络用户ARPU值');
TWGUE_ARPU_INTERVAL_P.to_excel(writer_P,'2G网络用户高ARPU值占比');
TWGUE_ARPU_INTERVAL_C.to_excel(writer_C,'2G网络用户高ARPU值占比');
NETUE_MOU_P.to_excel(writer_P,'234G网络用户MOU值');
NETUE_MOU_C.to_excel(writer_C,'234G网络用户MOU值');
TWGUE_MOU_INTERVAL_P.to_excel(writer_P,'2G网络用户高MOU值占比');
TWGUE_MOU_INTERVAL_C.to_excel(writer_C,'2G网络用户高MOU值占比');
NETWORK_DATA_P.to_excel(writer_P,'234G网络数据业务流量占比');
NETWORK_DATA_C.to_excel(writer_C,'234G网络数据业务流量占比');
NETUE_DOU_P.to_excel(writer_P,'234G网络用户DOU值');
NETUE_DOU_C.to_excel(writer_C,'234G网络用户DOU值');
TWGUE_DOU_INTERVAL_P.to_excel(writer_P,'2G网络用户高DOU值占比');
TWGUE_DOU_INTERVAL_C.to_excel(writer_C,'2G网络用户高DOU值占比');
NETWORK_DATA_LTEUE_P.to_excel(writer_P,'4G网络用户在各网产生的流量占比');
NETWORK_DATA_LTEUE_C.to_excel(writer_C,'4G网络用户在各网产生的流量占比');
NETWORK_DATA_WCDMAUE_P.to_excel(writer_P,'3G网络用户在各网产生的流量占比');
NETWORK_DATA_WCDMAUE_C.to_excel(writer_C,'3G网络用户在各网产生的流量占比');
NETWORK_TALK_P.to_excel(writer_P,'23G网络通话时长占比');
NETWORK_TALK_C.to_excel(writer_C,'23G网络通话时长占比');
NETWORK_TALK_LTEUE_P.to_excel(writer_P,'4G网络用户在各网产生的通话时长占比');
NETWORK_TALK_LTEUE_C.to_excel(writer_C,'4G网络用户在各网产生的通话时长占比');
NETWORK_TALK_WCDMAUE_P.to_excel(writer_P,'3G网络用户在各网产生的通话时长占比');
NETWORK_TALK_WCDMAUE_C.to_excel(writer_C,'3G网络用户在各网产生的通话时长占比');
#优比保存
YBUE_P.to_excel(writer_YB_P,'2G终端优比');
YBUE_C.to_excel(writer_YB_C,'2G终端优比');
YBNET_P.to_excel(writer_YB_P,'2G网络用户优比');
YBNET_C.to_excel(writer_YB_C,'2G网络用户优比');
writer_P.save();
writer_C.save();
writer_YB_P.save();
writer_YB_C.save();
print('保存完成！');
end_3=time.clock()
print('本次任务执行总时长为：',end_3-start,'s');