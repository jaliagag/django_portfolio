from django.shortcuts import render
from django.http import HttpResponse

from MyFamily.models import *
from django.template import loader

import sqlite3

my_template = loader.get_template('family_index.html')

def dbview(table):
    #Connecting to sqlite
    conn = sqlite3.connect('db.sqlite3')
    
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    
    a = "SELECT * FROM " + table
    print(a)
    #Retrieving data
    cursor.execute(a)
    
    #Fetching 1st row from the table
#    result = cursor.fetchone();
#    print(result)
    
    #Fetching 1st row from the table
    result = cursor.fetchall();
    
    #Commit your changes in the database
    conn.commit()
    
    #Closing the connection
    conn.close()

    db = {'db': result}

    return db

def check_family_index(self):

    document = my_template.render()

    return HttpResponse(document)

def hi_family_member(self,name):
    mydict = { 'name': name }

    document = my_template.render(mydict)

    return HttpResponse(document)

def view_cousins(self):

    document = my_template.render(dbview('MyFamily_cousin'))

    return HttpResponse(document)

def view_members(self):

    document = my_template.render(dbview('MyFamily_family_member'))

    return HttpResponse(document)

def view_uncles(self):

    document = my_template.render(dbview('MyFamily_uncle'))

    return HttpResponse(document)

def add_member_cousin(self,vname,vlast_name,vage,vparents,vbirth):
    
    dbview('MyFamily_cousin')

    checking = 'Primos'

    mydict = {'name':vname,'last_name':vlast_name,'age':vage,'parents':vparents,'birth':vbirth,'checking':checking}
    # agregamos a la db

    member = Cousin(name=vname,last_name=vlast_name,age=vage,parents=vparents,birth=vbirth)
    member.save()

    # mostramos en html
    document = my_template.render(mydict)

    return HttpResponse(document)

def add_member_family_member(self,vname,vlast_name,vage,vbirth):

    dbview('MyFamily_family_member')

    checking = 'Miembros de familia directa'

    mydict = {'name':vname,'last_name':vlast_name,'age':vage,'birth':vbirth,'checking':checking}
    # agregamos a la db

    member = Family_member(name=vname,last_name=vlast_name,age=vage,birth=vbirth)
    member.save()

    # mostramos en html
    document = my_template.render(mydict)

    return HttpResponse(document)

def add_member_uncle(self,vname,vlast_name,vage,vbirth):

    dbview('MyFamily_uncle')

    checking = 'Tíos'

    mydict = {'name':vname,'last_name':vlast_name,'age':vage,'birth':vbirth,'checking':checking}
    # agregamos a la db

    member = Uncle(name=vname,last_name=vlast_name,age=vage,birth=vbirth)
    member.save()

    # mostramos en html
    document = my_template.render(mydict)

    return HttpResponse(document)

