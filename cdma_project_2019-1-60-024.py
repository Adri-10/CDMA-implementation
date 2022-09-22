import numpy as np

no_of_stations=8 #no_of_stations= 2^n = 2^3=8
print('Number of stations:',no_of_stations)
seed=1
n=3 
seq_mat=[[seed]]

#using walsh code to generate chip sequence
#generating walsh matrix
i=1
while(i<=n):
    mat_dim=2**i
    rows, cols = (mat_dim, mat_dim)
    mat = [[0 for i1 in range(cols)] for i2 in range(rows)]

    #top left
    r=0 #on top left starts from row=0
    rt=0
    while(r<mat_dim//2): #loop for filling top left 4 row slots
        c=0 ##on top left starts from col=0
        ct=0
        while(c<mat_dim//2):  #loop for filling top left 4 col slot
            mat[r][c]=seq_mat[rt][ct]
            ct+=1
            c+=1
        rt+=1
        r+=1

    #top Right 
    r=0
    rt=0
    while(r<mat_dim//2): #for top right, row same but col change
        c=((mat_dim-1)//2)+1
        ct=0
        while(c<mat_dim):
            mat[r][c]=seq_mat[rt][ct]
            ct+=1
            c+=1
        rt+=1
        r+=1
    
    #Bottom left
    r=((mat_dim-1)//2)+1 #for bottom left, row increases but col starts from 0
    rt=0
    while(r<mat_dim):
        c=0
        ct=0
        while(c<mat_dim//2):
            mat[r][c]=seq_mat[rt][ct]
            ct+=1
            c+=1
        rt+=1
        r+=1
    
    #bottom right
    r=((mat_dim-1)//2)+1 #for bottom right, row same and col starts from next division part
    rt=0
    while(r<mat_dim):
        c=((mat_dim-1)//2)+1
        ct=0
        while(c<mat_dim):
            mat[r][c]=-1*seq_mat[rt][ct] #negate part
            ct+=1
            c+=1
        rt+=1
        r+=1

    seq_mat=mat.copy() #filling walsh matrix by copping one by one
    i+=1

#printing chip sequence code
i=1
for item in seq_mat:
    print('Station '+str(i)+'-> '+str(item))
    i+=1
print('\n')

#data bits
_1bit=1
_0bit=-1
Silent=0
#station_data_bits=[_1bit, _1bit, _1bit, Silent, _1bit, _0bit, _1bit, Silent]
#station_data_bits=[1, 1, 1, 0, 1, -1, 1, 0]
rows, cols = (no_of_stations, no_of_stations)

data_bits = []
for i in range(0, 8):
	bit = int(input('Enter data bits: '))
	data_bits.append(bit) 
print('Station data bits are: ',data_bits)

#Multiplexing (c1*d1....)
mux = [[0 for i1 in range(cols)] for i2 in range(rows)] #defining list of list
i=0
for data in data_bits:
    j=0
    for code in seq_mat[i]:
        mux[i][j]=np.multiply(code,data)
        j+=1
    i+=1

print('After Multiplexing, Resultant Code:')
i=1
for item in mux:
    print('Station '+str(i)+'-> '+str(item))
    i+=1
print('\n')

channel=[0,0,0,0,0,0,0,0]
i=0
while i<no_of_stations:
    j=0
    while j<no_of_stations:
        channel[i]=channel[i]+mux[j][i] #adding by column elements
        j+=1
    i+=1
print('After Multiplexing, we get data on channel: '+str(channel))
print('\n')

#Demultiplexing
demux=[]
print('Demultiplexed value for:')
st_no=1 #to define string numbering
result = []
print('After demultiplexed bits are: ')
for station in seq_mat:
    i=0
    add=0
    while i<no_of_stations:
        add=add+station[i]*channel[i]
        i+=1
    res=add/8
    result.append(res)
    
    if res==1:
        val='1 bit'
    elif res==-1:
        val='0 bit'
    elif res==0:
        val='Silent'
    else:
        val='Error'
    demux.append(val)
    print('Station '+str(st_no)+'-> '+val)
    st_no+=1

#verify part
bit_transfer=0
for i in range(0, 8):
    if(result[i]==data_bits[i]):
        bit_transfer=1    
if(bit_transfer==1):
    print('Successfully sent correct bits!')
else:
    print('Error in transfering bits!')
print('\n')





