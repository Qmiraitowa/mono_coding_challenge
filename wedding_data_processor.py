import psycopg2
import csv
from datetime import datetime, timedelta


# 连接到PostgreSQL数据库
def connect_to_db():
    conn = psycopg2.connect(
        dbname="wedding_db",
        user="postgres",
        password="190504",
        host="localhost",
        port="5432"
    )
    return conn


# 创建表结构
def create_tables(conn):
    with conn.cursor() as cur:
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id UUID PRIMARY KEY,
                username VARCHAR(50)
            );
        ''')

        cur.execute('''
            CREATE TABLE IF NOT EXISTS weddings (
                id SERIAL PRIMARY KEY,
                user_id UUID REFERENCES users(id),
                wedding_date DATE
            );
        ''')
    conn.commit()


# 导入CSV数据
def import_csv_data(conn):
    with conn.cursor() as cur:
        # 读取用户数据
        with open('C:/Users/F-miraitowa/Downloads/mono_coding_challenge-main/mono_coding_challenge-main/Users_Data.csv', 'r') as users_file:
            users_reader = csv.reader(users_file)
            next(users_reader)  # 跳过标题行
            for row in users_reader:
                cur.execute("INSERT INTO users (id, username) VALUES (%s, %s)", (row[0], row[1]))

        # 读取婚礼数据
        with open('C:/Users/F-miraitowa/Downloads/mono_coding_challenge-main/mono_coding_challenge-main/Weddings_Data.csv', 'r') as weddings_file:
            weddings_reader = csv.reader(weddings_file)
            next(weddings_reader)  # 跳过标题行
            for row in weddings_reader:
                cur.execute("INSERT INTO weddings (user_id, wedding_date) VALUES (%s, %s)", (row[0], row[1]))

    conn.commit()

# 查询2024年6月的婚礼用户
def get_june_2024_weddings(conn):
    with conn.cursor() as cur:
        cur.execute('''
            SELECT u.username 
            FROM weddings w
            JOIN users u ON w.user_id = u.id
            WHERE EXTRACT(YEAR FROM w.wedding_date) = 2024
            AND EXTRACT(MONTH FROM w.wedding_date) = 6;
        ''')
        return cur.fetchall()


# 查询两周内的婚礼用户
def get_upcoming_weddings(conn):
    today = datetime.today().date()
    two_weeks_later = today + timedelta(days=14)

    with conn.cursor() as cur:
        cur.execute('''
            SELECT u.username 
            FROM weddings w
            JOIN users u ON w.user_id = u.id
            WHERE w.wedding_date BETWEEN %s AND %s;
        ''', (today, two_weeks_later))
        return cur.fetchall()


# 将结果保存到文件
def save_results_to_file(results, filename):
    with open(filename, 'w') as f:
        for result in results:
            f.write(result[0] + '\n')


def main():
    conn = connect_to_db()
    create_tables(conn)
    import_csv_data(conn)

    june_weddings = get_june_2024_weddings(conn)
    save_results_to_file(june_weddings, 'june_2024_weddings.txt')

    upcoming_weddings = get_upcoming_weddings(conn)
    save_results_to_file(upcoming_weddings, 'upcoming_weddings.txt')

    conn.close()


if __name__ == "__main__":
    main()
