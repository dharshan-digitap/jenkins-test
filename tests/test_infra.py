import redis
import mysql.connector
import time


def test_redis_connection():
    r = redis.Redis(host="redis", port=6379)

    # retry (containers can be slightly slow)
    for _ in range(5):
        try:
            if r.ping():
                assert True
                return
        except Exception:
            time.sleep(1)

    assert False, "Redis connection failed"


def test_mysql_connection():
    for _ in range(5):
        try:
            conn = mysql.connector.connect(
                host="mysql",
                user="root",
                password="mysql_root_password",
                database="testdb"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT 1")
            result = cursor.fetchone()

            assert result[0] == 1
            return

        except Exception:
            time.sleep(2)

    assert False, "MySQL connection failed"