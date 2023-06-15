# Problem: We want to create a custom ORM (Object-Relational Mapping) 
# framework for a specific database. We need a way to define model classes 
# with attributes representing the table columns, 
# and automatically generate SQL statements for CRUD operations.

import unittest
from solution import ORMModel

class ORMModelTests(unittest.TestCase):
    
    def test_model_creation(self):
        class MyModel(ORMModel):
            name = str
            age = int

        self.assertTrue(hasattr(MyModel, 'name'))
        self.assertTrue(hasattr(MyModel, 'age'))

    def test_sql_generation(self):
        class MyModel(ORMModel):
            name = str
            age = int

        my_model = MyModel()
        create_sql = my_model.generate_create_sql()
        read_sql = my_model.generate_read_sql()
        update_sql = my_model.generate_update_sql()
        delete_sql = my_model.generate_delete_sql()
        
        self.assertEqual(create_sql, 'insert into mymodel (name, age) values (?, ?)')
        self.assertEqual(read_sql, 'select * from mymodel where id = ?')
        self.assertEqual(update_sql, 'update mymodel set name, age where id = ?')
        self.assertEqual(delete_sql, 'delete from mymodel where id = ?')
        

if __name__ == '__main__':
    unittest.main()