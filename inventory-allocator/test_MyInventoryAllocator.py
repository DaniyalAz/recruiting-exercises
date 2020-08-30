import unittest
from src.MyInventoryAllocator import *

class TestInventory(unittest.TestCase):

    #Test cases provided by the examiner
    def testGivenExamples(self):
        inputs = [({ 'apple': 1 }, [{ 'name': 'owd', 'inventory': { 'apple': 1 } }]),
                          ({ 'apple': 1 }, [{ 'name': 'owd', 'inventory': { 'apple': 0 } }]),
                          ({ 'apple': 10 }, [{ 'name': 'owd', 'inventory': { 'apple': 5 } }])]
        outputs = [[{ 'owd': { 'apple': 1 } }],[],[]]

        for i in range(len(inputs)):
            self.assertEqual(Inventory(inputs[i][0], inputs[i][1]).OrderShipment(), outputs[i])


    #Test contain empty warehouses and orders. Should return empty lists
    def testEmptyShipment(self):
        inputs = [({},[]),({ 'apple': 1, 'orange':2, 'berry': 4},[]),({},[{ 'name': 'owd', 'inventory': { 'apple': 1 } },{ 'name': 'dm', 'inventory': { 'orange':2 }},]),]
        outputs = [[],[],[]]

        for i in range(len(inputs)):
            self.assertEqual(Inventory(inputs[i][0],inputs[i][1]).OrderShipment(),outputs[i])
    
if __name__ == '__main__':
    unittest.main()
