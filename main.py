class mulitipleFunctions():
    
    def Subfields():
        Sub = ['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print('Sub-fields in AI are:')
        for ai in Sub:
            print(ai)

    def OddEven(): 
        num = int(input('Enter a number:')) #declared as global var can access outside the fun
        if(num % 2 == 0):
            return f'{num} is Even number'
        else:
            return f'{num} is Odd number'
    
    def Elegible():
        gen = str(input('Your Gender:'))
        age = int(input('Your Age:'))
        if(gen == 'Male' and age > 21):
            return 'ELIGIBLE'
        elif(gen == 'Female' and age > 18):
            return 'ELIGIBLE'
        else:
            return 'NOT ELIGIBLE'

    def percentage():
        s1=int(input('Subject1='))
        s2=int(input('Subject2='))
        s3=int(input('Subject3='))
        s4=int(input('Subject4='))
        s5=int(input('Subject5='))
        add=s1+s2+s3+s4+s5
        result = add
        print('Total:',result)
        print('Percentage:',result/5)
        # return result       


    def triangle(*args):        
        area=(args[0]*args[1])/2
        perimeter=(args[2]+args[3]+args[4])
        print('Height:',args[0])
        print('Breadth:',args[1])
        print('Area of Triangle:',area)
        print('Height1:',args[2])
        print('Height2:',args[3])
        print('Breadth:',args[4])
        print('Area of perimeter:',perimeter)
        # return area,perimeter 
    



































    