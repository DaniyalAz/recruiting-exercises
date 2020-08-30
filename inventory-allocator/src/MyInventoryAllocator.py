import copy

#Inventory class has all the components that compute the cheapest order available (via first warehouse in the list/input).
class Inventory(object):
    def __init__(self, order, inventory):

        # This is the constructor for the allocator, in this we set the self inventory and self order to the given order of user (inputs provided)
        # if the inventory details or order is empty/not provided, it will return an empty list. 
        self.inventory=inventory
        self.order=order
        
        #if not self.order or not self.inventory:
        #    return []

    def OrderShipment(self):
        
        #OrderShipment: This member function/function checks if the order is available in warehouses or not.
        #--The conditions that this function fullfills are:
        #----1. If the order and inventory details are provided correctly or not. If not, then it returns an empty list. 
        #----2. In case if the order is not available in any warehouse, it returns an empty list
        #----3. Since we are considering that warehouses are orderd in less to most expensive basis, so if the order can be fulfilled by the first warehouse that comes in the list, all the order is sent from that warehouse.
        #----4. If order is not fulfilled by single warehouse, whatever is available in that warehouse, it is sent from there, the rest is sent from the next least expensive warehouse in the list.
        #----5. Once the order has been checked, a counter checked is made to check if all the ordered iteams are selected or not. If not it returns an empty list.

        # if the inventory details or order is empty/not provided, it will return an empty list.
        if not self.order or not self.inventory:
            return []    
        
        #if inventory and order details are provided correctly, further calculations are done.
        else:
        
        #copies the order placed and invetory details provided by the user/input
            warehouses= copy.copy(self.inventory)
            checkorder= copy.copy(self.order)
            
        #a list to hold the shipment details when they are confirmed (if availabe)     
            confirmshipment=[]

        #iterating through each warehouse
            for warehouse in warehouses:

                #dictionary that stores the items that can be shiped from a warehouse
                availablestock={}

                #iterating through users order list/input
                for key in checkorder.keys():
                    #if the item is needed/in the order list
                    if checkorder[key]>0 :
                        #check if the item checkorder[key] is available in this warehouse
                        if key in warehouse['inventory'].keys():

                            #check if the warehouse has enough of this item to fulfill the demand or not
                            if warehouse['inventory'][key]>checkorder[key]:

                                #availability of item = true
                                availablestock[key]= checkorder[key]

                                #subtract the amount of item needed from the amount of item available in that warehouse/inventory.
                                warehouse['inventory'][key]= warehouse['inventory'][key]-checkorder[key]

                                #it is set to zero so that the next item can be searched/checked
                                checkorder[key]=0
                            else:

                                #if the warehouse doesnt have the complete stock that is required in order, we take whatever it can fulfill and search in next warehouse to complete the order
                                availablestock[key]=warehouse['inventory'][key]

                                #subtract from what's required so that what's left can be searched in next warehouse
                                checkorder[key]=checkorder[key] - warehouse['inventory'][key]

                                #set the amount of item in that warehouse=0 because we'll take what it can fulfill.
                                warehouse['inventory'][key]=0
                #comfirm the order once all the warehouses are searched
                confirmshipment.append({warehouse['name']:availablestock})
            #counter check if still anything is left in the order list, if yes it returns an empty list.   
            for key in checkorder.keys():
                if checkorder[key]>0:
                    return []  
            #All clear, return the order along with name of warehouse/inventory and items that are ordered      
            return confirmshipment

if __name__ == '__main__':
    Myorder=Inventory({ 'apple': 2 }, [{ 'name': 'owd', 'inventory': { 'apple': 5 } }])
    print ("Order Details:", Myorder.OrderShipment())

    SecondOrder=Inventory({ 'apple': 1 }, [{ 'name': 'owd', 'inventory': { 'apple': 0 } }])
    print ("Second Order Details: ", SecondOrder.OrderShipment())

    ThirdOrder=Inventory({ 'apple': 1 }, [{ 'name': 'owd', 'inventory': { 'apple': 1 } }])
    print ("Third Order Details: ", ThirdOrder.OrderShipment())

    Forthorder=Inventory({ 'apple': 2, 'berry': 5, 'banana': 15 }, [{ 'name': 'owd', 'inventory': { 'apple': 15, 'berry': 25, 'banana': 30, 'Mangoes': 50 } }])
    print ("Forth Order Details:", Forthorder.OrderShipment())                  

