from django.shortcuts import render
from django.http import HttpResponse
import mimetypes
from django.core.files.storage import FileSystemStorage
import xlrd
import pandas as pd
import os
import pathlib
from scipy.stats import skew
import statistics as st
import matplotlib.pyplot as plt
import csv
import numpy as np



# Index Page
def index(request):
    return render (request, 'index.html')


def gotoAbout(request):
    return render (request,'#Second-section')


# DOWNLOAD OF TEMPLATES

def download_file(request):
    # fill these variables with real values
    fl_path = '/static/Download_content'
    filename = 'd_1.xlsx'

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def download_file_1(request):
    # fill these variables with real values
    fl_path = '/static/Download_content'
    filename = 'd_2.xlsx'

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response




# DOWNLOAD OF RESULT FILES

def download_file_result1(request):
    # fill these variables with real values
    fl_path = '/static/Result'
    filename = 'product1.csv'

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def download_file_result2(request):
    # fill these variables with real values
    fl_path = '/static/Result'
    filename = 'product2.csv'

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def download_file_result3(request):
    # fill these variables with real values
    fl_path = '/static/Result'
    filename = 'product3.csv'

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def download_file_result4(request):
    # fill these variables with real values
    fl_path = '/static/Result'
    filename = 'product4.csv'

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def download_file_result5(request):
    # fill these variables with real values
    fl_path = '/static/Result'
    filename = 'product5.csv'

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


def download_file_result_all(request):
    # fill these variables with real values
    fl_path = '/static/Result'
    filename = 'merged.xlsx'

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


# The result page
def result(request):

    if request.method == 'POST':
        products_file = request.FILES['myfile1']
        second_file = request.FILES['myfile2']


        #saving files to CodeFiles path on static        

       
        folder='static/CodeFiles' 
        
        fs = FileSystemStorage(location=folder) 
        fs.save(products_file.name, products_file)
        fs.save(second_file.name, second_file)

        # a = products_file.name
        # b = second_file.name

       

        # write your ML code here
        # assign your output (including your image name) to some variable name

        # read_file = pd.read_excel (r'static/CodeFiles/d_1.xlsx') 
        # read_file.to_csv ("static/CodeFiles/D_1.csv",  
        #                 index = None, 
        #                 header=True) 
        
        # plt.savefig('static/CodeFiles/Matplotlib Images/Product1.png',bbox_inches='tight')
        #  df.to_csv(r'static/CodeFiles', index=False)

      

        #read files and convert
        read_file = pd.read_excel (r'static/CodeFiles/'+ products_file.name) 
        read_file.to_csv ("D_1.csv",  
                        index = None, 
                        header=True) 
        df_1 = pd.read_csv("D_1.csv")
        #print(df_1)
        read_file = pd.read_excel (r'static/CodeFiles/'+ second_file.name) 
        read_file.to_csv ("D_2.csv",  
                        index = None, 
                        header=True) 
        df_2 = pd.read_csv("D_2.csv")
        #print(df_2)

        #splitting into respective product files
        csvfile = open(r'D_1.csv').readlines()
        filename = 1
        for i in range(len(csvfile)):
            if i % 14 == 0:
                open(str(filename) + '.csv', 'w+').writelines(csvfile[i:i+14])
                filename += 1

        #counting number of products
        count = -4
        for path in pathlib.Path(".").iterdir():
            if path.is_file():
                count += 1
        #print(count)
        x = count + 1

        #skew calculation
        p_val = []
        for i in range(1,x):
            df = pd.DataFrame(pd.read_csv(str(i)+'.csv'))
            val = df.values.tolist()
            #print(val)
            for j in range(1,13):
                for k in range(1,5):
                    p_val.append(val[j][k])
        #print(p_val)
        chunks = [p_val[x:x+4] for x in range(0, len(p_val), 4)]
        #print(chunks)
        s_val = []
        dummy = [1,2,3,4]
        for i in range(0,12*count):
            for j in range(0,4):
                dummy[j] = chunks[i][j]
            s_val.append(skew(dummy))
        #print(s_val)
        #print(len(s_val))



        # Graphical Representation of units consumed vs weeks of a month for all
        # the five different products.
            
        df_1t=df_1.transpose()
        #Plotting the graph of units consumed vs weeks for the first product
        X_one=df_1t.iloc[1:,0].values
        X_one=np.array(X_one).astype(np.int)
        lst=['January','February','March','April','May','June','July','August','September','October','November','December']
        for i in range(1,13):
            plt.figure()
            y_one=df_1t.iloc[1:,i].values
            y_one=np.array(y_one).astype(np.int)
            plt.plot(X_one,y_one, color = 'blue',linewidth=1,linestyle='-',marker='o',markerfacecolor='black',markersize=3)
            plt.xticks([1,2,3,4])
            plt.title('Week-Wise Consumption Of {}'.format(lst[i-1]),fontsize='xx-large',color='black')
            plt.xlabel('Weeks',fontsize='x-large',color='orange')
            plt.ylabel('No of units consumed',fontsize='x-large',color='orange')
            plt.savefig('static/Matplotlib Images/Product1/Month{}.png'.format(i))
    

        #Plotting the graph of units consumed vs weeks for the second product
        for i in range(15,27):
            plt.figure()
            y_two=df_1t.iloc[1:,i].values
            y_two=np.array(y_two).astype(np.int)
            plt.plot(X_one,y_two, color = 'blue',linewidth=1,linestyle='-',marker='o',markerfacecolor='black',markersize=3)
            plt.xticks([1,2,3,4])
            plt.title('Week-Wise Consumption Of {}'.format(lst[i-15]),fontsize='xx-large',color='black')
            plt.xlabel('Weeks',fontsize='x-large',color='orange')
            plt.ylabel('No of units consumed',fontsize='x-large',color='orange')
   
            plt.savefig('static/Matplotlib Images/Product2/Month{}.png'.format(i-14))
     

        #Plotting the graph of units consumed vs weeks for the third product
        for i in range(29,41):
            plt.figure()
            y_three=df_1t.iloc[1:,i].values
            y_three=np.array(y_three).astype(np.int)
            plt.plot(X_one,y_three, color = 'blue',linewidth=1,linestyle='-',marker='o',markerfacecolor='black',markersize=3)
            plt.xticks([1,2,3,4])
            plt.title('Week-Wise Consumption Of {}'.format(lst[i-29]),fontsize='xx-large',color='black')
            plt.xlabel('Weeks',fontsize='x-large',color='orange')
            plt.ylabel('No of units consumed',fontsize='x-large',color='orange')
          
            plt.savefig('static/Matplotlib Images/Product3/Month{}.png'.format(i-28))
          

        #Plotting the graph of units consumed vs weeks for the fourth product
        for i in range(43,55):
            plt.figure()
            y_four=df_1t.iloc[1:,i].values
            y_four=np.array(y_four).astype(np.int)
            plt.plot(X_one,y_four, color = 'blue',linewidth=1,linestyle='-',marker='o',markerfacecolor='black',markersize=3)
            plt.xticks([1,2,3,4])
            plt.title('Week-Wise Consumption Of {}'.format(lst[i-43]),fontsize='xx-large',color='black')
            plt.xlabel('Weeks',fontsize='x-large',color='orange')
            plt.ylabel('No of units consumed',fontsize='x-large',color='orange')
         
            plt.savefig('static/Matplotlib Images/Product4/Month{}.png'.format(i-42))
       

        #Plotting the graph of units consumed vs weeks for the fifth product
        for i in range(57,69):
            plt.figure()
            y_five=df_1t.iloc[1:,i].values
            y_five=np.array(y_five).astype(np.int)
            plt.plot(X_one,y_five, color = 'blue',linewidth=1,linestyle='-',marker='o',markerfacecolor='black',markersize=3)
            plt.xticks([1,2,3,4])
            plt.title('Week-Wise Consumption Of {}'.format(lst[i-57]),fontsize='xx-large',color='black')
            plt.xlabel('Weeks',fontsize='x-large',color='orange')
            plt.ylabel('No of units consumed',fontsize='x-large',color='orange')
            
            plt.savefig('static/Matplotlib Images/Product5/Month{}.png'.format(i-56))
            



        #calculate no.of products
        y = 0
        p_val.insert(0,y)
        z = (count*48)+1
        nop = []
        for i in range(1,z):
            if(i%4 == 0):
                nop.append(p_val[i]+p_val[i-1]+p_val[i-2]+p_val[i-3])
            else:
                continue
        #print(nop)
        #print(len(nop))

        #calculate order date

        od = []
        dda = df_2.iloc[:,1].values
        for i in range(0,count):
            for j in range(0,12*count):
                if(s_val[j]>=0):
                    if(dda[i] <= 7):
                        od.append('order between 25 to last day of previous month')
                    else:
                        od.append('order before 25 of previous month')
                else:
                    
                    if(dda[i] <= 7):
                        od.append('order before 2nd week of current month')
                    else:
                        od.append('order before last day of previous month')

            #print(od)
            break
        #print(od)

        c1 = [nop[x:x+12] for x in range(0, len(nop), 12)]
        c2 = [od[x:x+12] for x in range(0, len(od), 12)]
        #print(c1)
        #print(c2)

        #saving output in a specified location
        pr = []
        mo = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        for i in range(count):
            pr.append('Product_'+str(i+1))
            for j in range(12):
                dict = {'Product': pr[i], 'Month': mo, 'Units to order': c1[i][:], 'Order date': c2[i][:]}
                data = pd.DataFrame(dict)

            data.to_csv(r'static/Result/product'+str(i+1)+'.csv', index=False)

            data.to_csv(r'static/Result/P_'+str(i+1)+'.csv', index=False)

        
        # REMOVAL OF UPLOADED FILES:

        os.remove('static/CodeFiles/'+ products_file.name)
        os.remove('static/CodeFiles/'+ second_file.name)

        for i in range(5):
            read_file = pd.read_csv(r'static/Result/P_'+str(i+1)+'.csv')
            read_file.to_excel(r'static/Result/product'+str(i+1)+'.xlsx', index = None, header = True)

        f_names = []
        for i in range(1,x):
            f_names.append(r'static/Result/product'+str(i)+'.xlsx')

        excels = [pd.ExcelFile(name) for name in f_names]
        frames = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excels]
        frames[1:] = [df[1:] for df in frames[1:]]
        combined = pd.concat(frames)
        combined.to_excel(r'static/Result/merged.xlsx', header=False, index=False)


        

      

        context = {
            # Assigh ML output to some variable name to pass to front end 
            'a': products_file.name,
           
            'nop':nop,
            'od': od,
            'a1':nop[0],
            'b1':od[0],
            'a2':nop[1],
            'b2':od[1],
            'a3':nop[2],
            'b3':od[2],
            'a4':nop[3],
            'b4':od[3],
            'a5':nop[4],
            'b5':od[4],
            'a6':nop[5],
            'b6':od[5],
            'a7':nop[6],
            'b7':od[6],
            'a8':nop[7],
            'b8':od[7],
            'a9':nop[8],
            'b9':od[8],
            'a10':nop[9],
            'b10':od[9],
            'a11':nop[10],
            'b11':od[10],
            'a12':nop[11],
            'b12':od[11],
            'a13':nop[12],
            'b13':od[12],
            'a14':nop[13],
            'b14':od[13],
            'a15':nop[14],
            'b15':od[14],
            'a16':nop[15],
            'b16':od[15],
            'a17':nop[16],
            'b17':od[16],
            'a18':nop[17],
            'b18':od[17],
            'a19':nop[18],
            'b19':od[18],
            'a20':nop[19],
            'b20':od[19],
            'a21':nop[20],
            'b21':od[20],
            'a22':nop[21],
            'b22':od[21],
            'a23':nop[22],
            'b23':od[22],
            'a24':nop[23],
            'b24':od[23],
            'a25':nop[24],
            'b25':od[24],
            'a26':nop[25],
            'b26':od[25],
            'a27':nop[26],
            'b27':od[26],
            'a28':nop[27],
            'b28':od[27],
            'a29':nop[28],
            'b29':od[28],
            'a30':nop[29],
            'b30':od[29],
            'a31':nop[30],
            'b31':od[30],
            'a32':nop[31],
            'b32':od[31],
            'a33':nop[32],
            'b33':od[32],
            'a34':nop[33],
            'b34':od[33],
            'a35':nop[34],
            'b35':od[34],
            'a36':nop[35],
            'b36':od[35],
            'a37':nop[36],
            'b37':od[36],
            'a38':nop[37],
            'b38':od[37],
            'a39':nop[38],
            'b39':od[38],
            'a40':nop[39],
            'b40':od[39],
            'a41':nop[40],
            'b41':od[40],
            'a42':nop[41],
            'b42':od[41],
            'a43':nop[42],
            'b43':od[42],
            'a44':nop[43],
            'b44':od[43],
            'a45':nop[44],
            'b45':od[44],
            'a46':nop[45],
            'b46':od[45],
            'a47':nop[46],
            'b47':od[46],
            'a48':nop[47],
            'b48':od[47],
            'a49':nop[48],
            'b49':od[48],
            'a50':nop[49],
            'b50':od[49],
            'a51':nop[50],
            'b51':od[50],
            'a52':nop[51],
            'b52':od[51],
            'a53':nop[52],
            'b53':od[52],
            'a54':nop[53],
            'b54':od[53],
            'a55':nop[54],
            'b55':od[54],
            'a56':nop[55],
            'b56':od[55],
            'a57':nop[56],
            'b57':od[56],
            'a58':nop[57],
            'b58':od[57],
            'a59':nop[58],
            'b59':od[58],
            'a60':nop[59],
            'b60':od[59]
        }
        

        






        
        return render (request, 'result.html', context)
    
    else:
        return HttpResponse ("Unauthorised access")

