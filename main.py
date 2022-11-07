import yaml
import json

class exercise:
    def __init__(self) -> None:
         with open("dep.json" ,'r' ) as depens:
            try:
                self.dep = json.load(depens)
            except Exception as e:
                print(e)
            
         self.out = []
    
    def build(self): # main build function
        for k,v in self.dep.items():
            self.flatten(v,self.out) 
            if k in self.out:
                print("Found Cycle Fixing ...")
                self.out.remove(k)
            self.out.append(k)
        print(self.run_build())


    def run_build(self): # run the build process without building the same service twice
        finish_build = []
        for i in self.out:
            if i in finish_build:
                continue
            finish_build.append(i)
        return finish_build

    def flatten(self,obje,out): # recursive function to create the flat dependices list
        if type(obje) is dict:
            for a in obje:
                self.flatten(obje[a],out)
                out.append(a)
        else:
            out += obje
        return list(dict.fromkeys(out))

exercise().build()

