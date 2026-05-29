import sqlite3


def simulate_database(schema):

    try:

        conn = sqlite3.connect(":memory:")

        cursor = conn.cursor()

        tables = schema["database"]["tables"]

        for table in tables:

            table_name = table["name"]

            columns = []

            for column in table["columns"]:

                if isinstance(column, str):
                    column_name = column

                else:
                    column_name = column["name"]

                if column_name == "id":

                    columns.append(
                        f"{column_name} INTEGER PRIMARY KEY"
                    )

                else:

                    columns.append(
                        f"{column_name} TEXT"
                    )

            query = f"""
            CREATE TABLE {table_name}
            (
                {",".join(columns)}
            )
            """

            cursor.execute(query)

        conn.commit()

        return {
            "success": True,
            "tables_created": len(tables)
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }