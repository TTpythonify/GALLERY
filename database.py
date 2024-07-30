import psycopg2

# CONNECT TO THE DATABASE
def connect():
    return psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='12345',
        host='localhost',
        port='5432'
    )

# CREATE TABLE IF IT DOESN'T EXIST
def create_table():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS my_gallery (
                    id SERIAL PRIMARY KEY,
                    media_type TEXT NOT NULL,
                    file_path TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

# ADD TO GALLERY
def add_to_gallery(media_type, file_path, created_at):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                    INSERT INTO my_gallery (media_type, file_path, created_at)
                    VALUES (%s, %s, %s)
                """, (media_type, file_path, created_at))
            conn.commit()


# RETRIEVE FILE_PATH FROM THE DATABASE BASED ON MEDIA_TYPE
def retrieve_from_database(category):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT file_path FROM my_gallery
                WHERE media_type = %s
                ORDER BY created_at
            """, (category,))
                
            # Fetch all results
            results = cur.fetchall()
                
            # Return the file paths
            return [row[0] for row in results]
        

        