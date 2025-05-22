"""
SQLite 資料庫範例程式

此程式示範如何使用 SQLite 資料庫進行基本的 CRUD 操作，
並展示多對多關係的處理方式。

資料庫結構：
- students: 儲存學生資料
- courses: 儲存課程資料
- student_courses: 學生與課程的關聯表（多對多關係）
"""

import sqlite3
from pathlib import Path

def setup_database():
    """
    初始化資料庫連接並建立表格
    
    Returns:
        tuple: 包含 (connection, cursor) 的元組
    """
    # 確保 sample 資料夾存在
    db_dir = Path(__file__).parent / 'sample'
    db_dir.mkdir(parents=True, exist_ok=True)
    
    # 連接到資料庫
    db_path = db_dir / 'school.db'
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    
    # 啟用外鍵約束
    cursor.execute("PRAGMA foreign_keys = ON")
    
    # 建立表格
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS student_courses (
        student_id INTEGER,
        course_id INTEGER,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
        FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
    )
    ''')
    
    return conn, cursor

def insert_sample_data(cursor):
    """
    插入範例資料到資料庫
    
    Args:
        cursor: 資料庫游標
    """
    cursor.executescript('''
    INSERT OR IGNORE INTO students (name) VALUES ('Alice');
    INSERT OR IGNORE INTO students (name) VALUES ('Bob');
    INSERT OR IGNORE INTO courses (course_name) VALUES ('Math');
    INSERT OR IGNORE INTO courses (course_name) VALUES ('Science');
    INSERT OR IGNORE INTO student_courses (student_id, course_id) VALUES (1, 1);
    INSERT OR IGNORE INTO student_courses (student_id, course_id) VALUES (1, 2);
    INSERT OR IGNORE INTO student_courses (student_id, course_id) VALUES (2, 1);
    ''')

def query_student_courses(cursor, student_name):
    """
    查詢指定學生的所有課程
    
    Args:
        cursor: 資料庫游標
        student_name: 學生姓名
        
    Returns:
        list: 包含課程名稱的列表
    """
    cursor.execute('''
    SELECT c.course_name
    FROM students s
    JOIN student_courses sc ON s.student_id = sc.student_id
    JOIN courses c ON sc.course_id = c.course_id
    WHERE s.name = ?
    ''', (student_name,))
    return [row[0] for row in cursor.fetchall()]

def main():
    """主程式入口"""
    try:
        # 初始化資料庫
        conn, cursor = setup_database()
        
        # 插入範例資料
        insert_sample_data(cursor)
        
        # 查詢 Alice 的課程
        alice_courses = query_student_courses(cursor, 'Alice')
        print(f"Alice 的課程: {', '.join(alice_courses)}")
        
        # 查詢 Bob 的課程
        bob_courses = query_student_courses(cursor, 'Bob')
        print(f"Bob 的課程: {', '.join(bob_courses) if bob_courses else '無'}")
        
    except sqlite3.Error as e:
        print(f"資料庫錯誤: {e}")
    finally:
        # 確保連接被正確關閉
        if 'conn' in locals():
            conn.commit()
            conn.close()

if __name__ == "__main__":
    main()
