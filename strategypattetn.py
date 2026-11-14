class ExportType :
    def type(self,vtype) :
        print("Product export processing type!")
        
class ship(ExportType) :
    def type(self,vtype) :
        print(f"Product export with{vtype} ship! ")
        
class car(ExportType) :
    def type(self,vtype) :
        print(f"Product export with {vtype} car! ")
        
class airplane(ExportType) :
        def type(self,vtype) :
            print(f"Product export with {vtype} airplane! ")
            
            
class Exportvehicle_type :
    def __init__(self,strategy) :
        self.strategy = strategy
        
    def exportvehicke(self,vtype) :
        self.strategy.type(vtype)
        
        
Ship=ship()
Car=car()
Airplane=airplane()



export=Exportvehicle_type(Ship)
export.exportvehicke("MSC container")


export=Exportvehicle_type(Car)
export.exportvehicke("Box Truck type")

export=Exportvehicle_type(Airplane)
export.exportvehicke("Air_Cargo")        
            
        
        