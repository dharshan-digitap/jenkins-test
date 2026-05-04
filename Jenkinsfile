node('asg-workers') {
    stage('Process Webhook and Post Status to GitHub') {
        try {
runTest {

    echo "Running on node:"
    sh 'hostname -i'

    sh '''
        echo "===== NETWORK DEBUG ====="
        ip addr || true

        echo "===== DNS CHECK ====="
        getent hosts mysql || true
        getent hosts redis || true

        echo "===== MYSQL TEST ====="
        python - <<EOF
import pymysql
import time

for i in range(5):
    try:
        conn = pymysql.connect(
            host="mysql",
            user="root",
            password="mysql_root_password",
            database="testdb"
        )
        print("MySQL Connected ✅")
        conn.close()
        break
    except Exception as e:
        print("Retrying MySQL...", e)
        time.sleep(2)
else:
    raise Exception("MySQL connection failed ❌")
EOF

        echo "===== REDIS TEST ====="
        python - <<EOF
import redis
import time

for i in range(5):
    try:
        r = redis.Redis(host="redis", port=6379)
        r.ping()
        print("Redis Connected ✅")
        break
    except Exception as e:
        print("Retrying Redis...", e)
        time.sleep(2)
else:
    raise Exception("Redis connection failed ❌")
EOF
    '''
}
        } catch (Exception e) {
            status = 'failure'
            echo "Error occurred: ${e.message}"
        }
    }
}