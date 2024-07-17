from django.test import TestCase

# Create your tests here.
 department_name=request.POST['departmentname']
            department_type=request.POST['department']
        
           create(name,dbname)
    


def create(name,dbname):
            db_name = name
            table_name = f'{dbname}_{'department_type'}'

            # Configure the database settings dynamically
            settings.DATABASES[db_name] = {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(settings.BASE_DIR, f'{db_name}.sqlite3'),
            }

            # Create a new model dynamically
            model_code = f"""
# Format the date and time to the specified format
    # formatted_dt = dt.strftime("%d/%m/%Y %I.%M %p")
    # print(formatted_dt)
    
    print()

class {table_name}(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'attence'
"""

            # Write the model code to a file
            model_file_path = f'attence/models.py'
            with open(model_file_path, 'a') as f:
                f.write(model_code)

            # Update __init__.py to include the new model
            # with open('attence/models/__init__.py', 'a') as init_file:
            #     init_file.write(f'\nfrom .{table_name.lower()} import {table_name}')

            # Generate and apply the migration
            # call_command('makemigrations', 'attence')
            # call_command('migrate', 'attence')
            print('if')
            return HttpResponse(f'Table {table_name} created in database {db_name}')
 

            db_name = 'departments'
            table_name = f'{department_name}_{department_type}'

            # Configure the database settings dynamically
            settings.DATABASES[db_name] = {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(settings.BASE_DIR, f'{db_name}.sqlite3'),
            }

            # Create a new model dynamically
            model_code = f"""
from django.db import models

class {table_name}(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'attence'
"""

            # Write the model code to a file
            model_file_path = f'attence/models.py'
            with open(model_file_path, 'w') as f:
                f.write(model_code)

            # Update __init__.py to include the new model
            # with open('attence/models/__init__.py', 'a') as init_file:
            #     init_file.write(f'\nfrom .{table_name.lower()} import {table_name}')

            # Generate and apply the migration
            call_command('makemigrations', 'attence')
            call_command('migrate', 'attence')
            print('if')
            return HttpResponse(f'Table {table_name} created in database {db_name}')

    else:
        form = CreateDepartmentForm()
        print('else')




from django.db import models

class course_ug(models.Model):
    department = models.CharField(max_length=100)
    year1 = models.CharField(max_length=100)
    year2 = models.CharField(max_length=100)
    year3 = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.department
    
    
class course_pg(models.Model):
    department = models.CharField(max_length=100)
    year1 = models.CharField(max_length=100)
    year2 = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.department
    



      
    datechek1='day'+ str(day+1)
    b=0 
    c=''
    e=[]
    z=0
    for i in student:
        a=0 
        c=''
        z+=1
        datechek='i.day'+ str(z)
        #student_details.objects.filter(regnumber=i.regnumber).update(**{datechek1: ''})
        for ia in eval(datechek):
            #print(eval(datechek))
            c+=ia
            print(ia,"the level",a)
            a+=1
        b=a
        e.append(c)
    print(b,c)
    d=c
    print(d)
    print(type(e))
    print(e)
    xt=[]
    for i in e[0]:
        xt+=i
    my_list = ["['0', '1', '0', '1', '0']", "['1', '1', '0', '0', '1']", "['0', '1', '0', '1', '0']"]
# clean_list = [ast.literal_eval(item) for item in my_list]
    data = student_details.objects.get(regnumber='21UIT001')
    days = [data.day1, data.day2, ..., data.day90]
  data={
        'ug':course_ug.objects.all(),
        'pg':course_pg.objects.all(),
        'data':[ast.literal_eval(item) for item in e],
        'student' : student_details.objects.get(regnumber='21UIT001'),
        #'days' : days
    }