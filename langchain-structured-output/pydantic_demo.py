from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    
    # name :str 
    # new_student = {'name':32} This is the basic Pydantic model this will through an error message
    # student = Student(**new_student)
    # print(student)     
    
    # name :str = 'nitish' This is the default pydantic value for the name or for the model
    # new_student :{}
    #student = student(**new_student)
    #print(student) # this is the default value for the name
    #print(student.name) # this is the default value for the model
    
    
    
    # age: int = 18 This is the default pydantic value for the age
    # email: EmailStr = '
    # age: Optional[int] = None This is the optional value for the age
    # email: EmailStr = 'abc@gmail.com' This is the validation for the email
    
    name: str = 'nitish'
    age: Optional[int] = None # Here this is the age is optional value for the attribute of the model instance.
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10 , default=5, description='A decimal value representing the cgpa of the student')
                        # Yeha per ab ye hum na constraint lagay hoi hai hum na like jo gt=0, lt=10 yeha per hum na lagay hoi hai
                        # yeha per hum na default value bhi lagay hoi hai 5 ka or hum na description bhi lagay hoi hai 

new_student = {'age':'32', 'email':'abc@gmail.com'} # corce ho raha hai yeha per 
# Pydantic kha ander automatically each and every thing hoti hai mmeans that wo hr chese to autmoatically samag lata hai bina kasi perameter ke

student = Student(**new_student)

student_dict = dict(student)

print(student_dict['age'])

student_json = student.model_dump_json() # This is the structured format in json format

# print(student_json)
