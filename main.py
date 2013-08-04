#!/bin/python

import re

class Length(object):
    

    def __init__(self,input_file_name):
        
        self._mail = 'fuxiang90@gmail.com'
        self._input_file_name = input_file_name
        self._legth_dict ={}
        self._unit_dict = { "miles":"mile" ,"feet":"foot","inches":"inch","yards":"yard","faths":"fath","furlong":"furlong" }
    def run(self):
        fin = open(self._input_file_name)
        fout = open('output.txt','w')
        fout.write(self._mail + '\n\n')
        for each in fin:
            if each.strip() == '':
                continue
            
            if each.find('=') == -1:
                result = self.compute(each.strip())
                fout.write("%.2f m\n" %result)

            else :
                l1 = each.strip().split('=')
                unit = l1[0].strip().split(' ')[1]
                num  = l1[1].strip().split(' ')[0]
            
                self._legth_dict[unit] = self._legth_dict.get(unit ,0.0) + float(num)

        fin.close()
        fout.close()
    def compute(self,eval_str):
        eval_list = eval_str.split(' ')
        new_eval_str = ""
        
        #temp_list = []
        for pos in range(len(eval_list) ) :
            
            s = eval_list[pos]
            _len = len(s)
            

            if s.isalpha(): 

                unit_name = self._unit_dict.get(s,s)
                eval_list[pos -1] = str(float(eval_list[pos - 1]) * self._legth_dict[unit_name]  )

                eval_list[pos] = 'm'
        eval_str = ' '.join(eval_list)             
        eval_str = eval_str.replace('m' ,' ')
        return  eval(eval_str)

            

if __name__ == '__main__':

    test = Length('input.txt')
    test.run()
    
    
     
    print "done it"

