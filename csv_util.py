import inspect
from operator import attrgetter

class Csv_Column:
    def __init__(self,priority,name,format=None):
        self.name=name
        self.priority=priority
        self.format=format
        self.value=''
        
        
        
    def __get__(self,instance,owner):
        return self.value    
    def __set__(self,instance,value):
        self.value=value
        instance.__dict__[self.attr_name]=self
    def __set_name__(self,owner,name):
        self.attr_name=name
      
           

 
        
class Csv_FA_Cusoty:
    Fund1=Csv_Column(1,'Test1')
    Fund2=Csv_Column(1,'Test2')
    Fund3=Csv_Column(1,'Test3')
    Fund4=Csv_Column(1,'Test4')
    def __init__(self):
        self.Fund1=''
        self.Fund2=''
        self.Fund3=''
        self.Fund4=''
   
def is_uniform_type(lst):
    if not lst:
        return True
    first_type=type(lst[0])
    return all(isinstance(item,first_type) for item in lst)



xx=is_uniform_type([1,2,3])
print(xx)

def csv_dumps(csv_entities,seperator=','):
    final=''
    heads=[]
    rows=[]
    
    if is_uniform_type(csv_entities):
        dict=get_csv_columns(csv_entities[0])
        for key,value in dict.items():
            if not value.name:
                heads.append(key)
            else:
                heads.append(value.name)    
                
        
        
        for csv_entity in csv_entities:
            row=[]
            dict=get_csv_columns(csv_entity)
            row=[i.value for i in dict.values()]
            rows.append(row)
 
            
    heads=','.join(heads)
    final+=f'{heads}\n'
    for row in rows:
       columns=seperator.join(row)
       final+=f'{columns}\n'
       
    return final   
            
            
            
            
    
    



def get_csv_columns(csv_entity:Csv_Column):
    

    csv_dict=csv_entity.__csv
    csv_atts_dict={key:value for key, value in atts if not key.startswith("__") and isinstance(value,Csv_Column)}
    if csv_atts_dict:
        #sort_value=attrgetter('priority')
        sorted(csv_atts_dict.items(),key=lambda item:item[1].priority)
        return csv_atts_dict
    else:
        return None
    
    
    
f1=Csv_FA_Cusoty()
f1.Fund1='f1Fund1'
print(f1.Fund1)
# f1.Fund2='f1Fund2'
# f1.Fund3='f1Fund3'
# f1.Fund4='f1Fund4'
f2=Csv_FA_Cusoty()
f2.Fund1.value='f2Fund1'
f2.Fund2.value='f2Fund2'
f2.Fund3.value='f2Fund3'
f2.Fund4.value='f2Fund4'
f3=Csv_FA_Cusoty()
f3.Fund1.value='f3Fund1'
f3.Fund2.value='f3Fund2'
f3.Fund3.value='f3Fund3'
f3.Fund4.value='f3Fund4'
f4=Csv_FA_Cusoty()
f4.Fund1.value='f4Fund1'
f4.Fund2.value='f4Fund2'
f4.Fund3.value='f4Fund3'
f4.Fund4.value='f4Fund4'
f5=Csv_FA_Cusoty()
f5.Fund1.value='f5Fund1'
f5.Fund2.value='f5Fund2'
f5.Fund3.value='f5Fund3'
f5.Fund4.value='f5Fund4'

ff=csv_dumps([f1,f2,f3,f4])
print(ff)
