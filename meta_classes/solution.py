
# Metaclasses are used to generate SQL statements for CRUD operations
class ORMModelMeta(type):
    def __new__(cls, name, bases, attrs):
        # Perform necessary processing to generate SQL statements
        # based on the class attributes
        # Perform necessary processing to generate SQL statements
        table_name = name.lower()
        columns = []

        for attr_name, attr_value in attrs.items():
            if isinstance(attr_value, type):
                column_name = attr_name.lower()
                column_type = attr_value.__name__.lower()
                columns.append(f"{column_name}")

        # Create methods for SQL statement generation
        def generate_create_sql(self):
            return f"insert into {table_name} ({', '.join(columns)}) values (?, ?)"

        def generate_read_sql(self):
            return f"select * from {table_name} where id = ?"

        def generate_update_sql(self):
            return f"update {table_name} set {', '.join(columns)} where id = ?"

        def generate_delete_sql(self):
            return f"delete from {table_name} where id = ?"

        # Add the methods to the class
        attrs['generate_create_sql'] = generate_create_sql
        attrs['generate_read_sql'] = generate_read_sql
        attrs['generate_update_sql'] = generate_update_sql
        attrs['generate_delete_sql'] = generate_delete_sql

        return super().__new__(cls, name, bases, attrs)


class ORMModel(metaclass=ORMModelMeta):
    def __init__(self, **kwargs):
        for attr_name, attr_value in kwargs.items():
            setattr(self, attr_name, attr_value)

    def save(self):
        # Implement the logic to save the object to the database
        sql = self.generate_create_sql()  # Assuming the method is defined by the metaclass
        print(f"Executing SQL: {sql}")
        # Execute the SQL statement to save the object to the database

    def delete(self):
        # Implement the logic to delete the object from the database
        sql = self.generate_delete_sql()  # Assuming the method is defined by the metaclass
        print(f"Executing SQL: {sql}")
        # Execute the SQL statement to delete the object from the database

    def __str__(self):
        # Implement the string representation of the object
        return f"<{self.__class__.__name__}: {self.__dict__}>"