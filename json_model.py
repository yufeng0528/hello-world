#!/usr/bin/python
#-*- coding:utf-8 -*-
import json

JSON_FILE='/Users/trymore/Downloads/x.txt'
JSON_DIR='/Users/trymore/Downloads/x_'

def getJson():
    try:
        data = open(JSON_FILE, 'r')
        return data.read()
    except IOError as err:
        print('File error:' + str(err))
    finally:
        if data in locals():
            data.close()
            
def toFile(file_name,file_str):
    try:
        data = open(JSON_DIR+ file_name +'.txt', 'w')
        data.write(file_str)
    except IOError as err:
        print('File error:' + str(err))
    finally:
        if data in locals():
            data.close()

def toModel():
    jsonData = getJson()
    print jsonData
    
    jsonObject = json.loads(jsonData)
    
    for key in jsonObject:
        print key,jsonObject[key]
        if key != 'status' and key != 'reason':
            toClass(key, jsonObject[key])
            
def toModelFromXcode():
    jsonData = getJson()
    
    jsonObject = json.loads(jsonData)
    
    print jsonObject
            
            
def toClass(name, model):
    field_list = []
    
    if isinstance(model, list):
        print '>>>>this is list'
        
        if len(model) > 0:
            for key in model[0]:
                value = model[0][key]
                
                field_list.append((key,value))    
                
        toIosClass(name, field_list)       
            
    else:
        for key in model:
            value = model[key]
            field_list.append((key,value))   
            
        toIosClass(name, field_list) 
            
def toIosClass(name, field_list):  
    class_str_list = []
           
    class_str_list.append("@interface ")
    class_str_list.append(name)
    class_str_list.append(" : NSObject")
    class_str_list.append("\n\n")
            
    for field,value in field_list:
        print '>>>>>>>>', field, value  
                                                        
        # 字符串
        if isinstance(value, (unicode, str)):
            print '>>>>>>>> ++++', value
            class_str_list.append("@property (strong,nonatomic) NSString *")
            class_str_list.append(field)
            class_str_list.append(";\n")
        elif isinstance(value, dict):
            print '>>>>>>>> ++++ dict', value
            class_str_list.append("@property (strong,nonatomic) id ")
            class_str_list.append(field)
            class_str_list.append(";\n")
            
            toClass(field, value)
        
        elif isinstance(value, list):
            print '>>>>>>>> ++++ list', value
            class_str_list.append("@property (strong,nonatomic) NSArray *")
            class_str_list.append(field)
            class_str_list.append(";\n")
            
            toClass(field, value)
            
        else:
            class_str_list.append("@property (strong,nonatomic) NSNumber *")
            class_str_list.append(field)
            class_str_list.append(";\n")
            
    class_str_list.append('- (instancetype)initWithDict:(NSDictionary *)dict;\n\n@end')
            
    #.m文件
    class_str_list.append('\n\n')
    class_str_list.append("@implementation ")
    class_str_list.append(name) 
    class_str_list.append('\n')
    
    class_str_list.append('@synthesize ')  
    
    for field,value in field_list: 
        class_str_list.append(field)
        class_str_list.append(",")
    class_str_list.pop()
    class_str_list.append(';\n')
    
    class_str_list.append("\n")
    class_str_list.append("- (id)initWithDict:(NSDictionary *)dict {\n")
    class_str_list.append("    self = [super init];\n")
    class_str_list.append("    if (self) {\n")
    class_str_list.append("        if (![Tool isEmpty:dict]) {\n\n")
    
    for field,value in field_list:
        class_str_list.append("            self.")
        class_str_list.append(field)
        class_str_list.append('= [dict objectForKey:@"')
        class_str_list.append(field)
        class_str_list.append('"];\n')
                    
    class_str_list.append('\n        }\n\n')
    class_str_list.append('    }\n')
    class_str_list.append('    return self;\n')
    class_str_list.append('}\n')
    class_str_list.append('\n\n@end\n')
        
    class_str = ''.join(class_str_list)
    
    toFile(name, class_str) 
    
    
if __name__ == "__main__":
    toModel()
