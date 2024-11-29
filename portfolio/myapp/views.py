from django.shortcuts import render
from django.views.generic import View

#from django.views.generic import View(captal)

# Create your views here.

#url:localhost:8000/index/
# method:get
# response:index.html

class IndexView(View):
    def get(self,request,*args,**kwargs):

        person_data={
            "id":2,
            "name":"rifa",
            "age":21,
            "location":"calicut",
            "contact":9074417477
        }
        return render(request,"index.html",{"person":person_data})
 



        # return render(request,"index.html",{"name":name,"age":age,"location":location,"contact":contact})




class ProjectView(View):
    def get(self,request,*args,**kwargs):


        projects=[
            {"id":1,"title":"codehub",
             "description":"project decsription",
             "front_end":"react","back_end":"django"
             },
              {"id":2,"title":"ServiceHub",
             "description":"project decsription",
             "front_end":"Angular","back_end":"django"
             },
              {"id":3,"title":"linksphere",
             "description":"project decsription",
             "front_end":"react","back_end":"django"
             }
        ]

        return render(request,"project.html",{"projects":projects})










        # project_title="CODEHUB"
        # project_framework="django"
        # project_database="MYSQL"
        # project_mail="RIFAFAIZAL@gmail.com"
# return render(request,"project.html",{"title":project_title,"framework":project_framework,"database":project_database,"mail":project_mail})        







#locationhost:8000/contact-us/
# method:get
# response :contact.html display email,phone,address,place

class ContactView(View):
    def get(self,request,*args,**kwargs):
        email="rifafathimafaizal@gmail.com"
        phone=9074417477
        address="mafas(ho),kadaloor(po),nandi bazar"
        place="nandi"


        return render(request,"contact.html",{"email":email,"phone":phone,"address":address,"place":place})



# localhost:8000/skills/
# method:get
# response:skills.html dispaly PythonDjango,MYSQL,React


class SkillsView(View):
    def get(self,request,*args,**kwargs):
        skilla="pythondjango"
        skillb="mysql"
        skillc="react"


        return render(request,"skill.html",{"first":skilla,"second":skillb,"third":skillc})



# localhost:8000/services/
# method:get
# response:services.html   webapplication,api development,ui/ux


class ServicesView(View):
    def get(self,request,*args,**kwargs):
        services=["web application","api development","ui/ux"]

        return render(request,"services.html",{"services":services})


#departments:
class DepartmentView(View):
    def get(self,request,*args,**kwargs):


        department_data={
            "dept":"bca",
            "number":20,
            "addr":"mafas"
        }

        



        return render(request,"department.html",{"department":department_data})




      